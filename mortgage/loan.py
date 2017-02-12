from datetime import date
from decimal import Decimal

from dateutil.relativedelta import relativedelta


class Loan(object):
    def __init__(self, principal, interest, term, term_unit='years', compounded='monthly', start_date=None):

        assert principal > 0, 'Principal must be positive value'
        assert 0 <= interest <= 1, 'Interest rate must be between zero and one'
        assert term > 0, 'Term must be a positive number'
        assert term_unit in ['days', 'months', 'years'], 'term_unit can be either  days, months, or years'
        assert compounded in ['daily', 'monthly', 'annually'], 'Compounding can occur daily, monthly, or annually'

        periods = {
            'daily': 365,
            'monthly': 12,
            'annually': 1
        }

        self.principal = Decimal(principal)
        self.interest = Decimal(interest * 100) / 100
        self.term = term
        self.term_unit = term_unit
        self.compounded = compounded
        self.start_date = date(*start_date)
        self.n_periods = periods[compounded]
        self.interest_rate_month = self.interest / 12
        self.payment_range = range(1, self.term * self.n_periods + 1)

        self._schedule = self._amortize()

    @staticmethod
    def convert(value):
        return Decimal(value).quantize(Decimal('0.01'))

    def schedule(self, nth_payment=None):

        if nth_payment:
            return self._schedule[nth_payment]
        else:
            return self._schedule

    @property
    def _monthly_payment(self):
        p = self.principal
        i = self.interest
        n = self.n_periods
        t = self.term
        payment = p * i / n / (1 - (1 + i / n) ** (- n * t))
        return payment

    @property
    def monthly_payment(self):
        return self.convert(self._monthly_payment)

    def _simple_interest(self, p, i, n):
        amt = p * i * n
        return self.convert(amt)

    @property
    def apr(self):
        new_payment = self._simple_interest(self.principal, self.interest, 1)
        apr = new_payment / self.principal
        return self.convert(apr * 100)

    @property
    def apy(self):
        apy = (1 + self.interest / self.n_periods) ** self.n_periods - 1
        return self.convert(apy * 100)

    @property
    def total_principal(self):
        return self.convert(self.principal)

    @property
    def total_interest(self):
        return self.convert(self.schedule(self.term * 12)['total_interest'])

    @property
    def total_paid(self):
        return self.total_principal + self.total_interest

    @property
    def interest_to_principle(self):
        return round(self.total_interest / self.total_principal * 100, 1)

    @property
    def years_to_pay(self):
        return round(self.payment_range[-1] / 12, 1)

    @property
    def summarize(self):
        print('Original Balance:         ${:>11,}'.format(self.principal))
        print('Interest Rate:             {:>11} %'.format(self.interest))
        print('APY:                       {:>11} %'.format(self.apy))
        print('APR:                       {:>11} %'.format(self.apr))
        print('Term:                      {:>11} {}'.format(self.term, self.term_unit))
        print('Monthly Payment:          ${:>11}'.format(self.monthly_payment))
        print('')
        print('Total principal payments: ${:>11,}'.format(self.total_principal))
        print('Total interest payments:  ${:>11,}'.format(self.total_interest))
        print('Total payments:           ${:>11,}'.format(self.total_paid))
        print('Interest to principal:     {:>11} %'.format(self.interest_to_principle))
        print('Years to pay:              {:>11}'.format(self.years_to_pay))

    def _interest_portion(self, payment_number):
        i = self.interest_rate_month
        i1 = i + 1

        numerator = self.principal * i * (i1 ** (self.n_periods * self.term + 1) - i1 ** payment_number)
        denominator = i1 * (i1 ** (self.n_periods * self.term) - 1)
        return numerator / denominator

    def _amortize(self):

        schedule = {
            0: {'date': self.start_date,
                'payment': 0,
                'interest': 0,
                'principal': 0,
                'total_interest': 0,
                'balance': self.principal

               }
            }

        for payment_number in self.payment_range:

            interest_payment = self._interest_portion(payment_number)
            principal_payment = self._monthly_payment - interest_payment

            row = {'date': schedule[payment_number-1]['date'] + relativedelta(months=1),
                   'payment': self._monthly_payment,
                   'interest': interest_payment,
                   'principal': principal_payment,
                   'total_interest': schedule[payment_number-1]['total_interest'] + interest_payment,
                   'balance': schedule[payment_number-1]['balance'] - principal_payment
                  }

            record = {payment_number: row}

            schedule = {**schedule, **record}

        return schedule
