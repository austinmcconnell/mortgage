from collections import namedtuple
from decimal import Decimal

Installment = namedtuple('Installment', 'number payment interest principal total_interest balance')


class Loan(object):
    def __init__(self, principal, interest, term, term_unit='years', compounded='monthly'):

        term_units = {'days', 'months', 'years'}
        compound = {'daily', 'monthly', 'annually'}

        assert principal > 0, 'Principal must be positive value'
        assert 0 <= interest <= 1, 'Interest rate must be between zero and one'
        assert term > 0, 'Term must be a positive number'
        assert term_unit in term_units, 'term_unit can be either  days, months, or years'
        assert compounded in compound, 'Compounding can occur daily, monthly, or annually'

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
        self.n_periods = periods[compounded]
        self._schedule = self._amortize()

    @staticmethod
    def _quantize(value):
        return Decimal(value).quantize(Decimal('0.01'))

    def schedule(self, nth_payment=None):
        if nth_payment:
            data = self._schedule[nth_payment]
        else:
            data = self._schedule
        return data

    @property
    def _monthly_payment(self):
        principal = self.principal
        _int = self.interest
        num = self.n_periods
        term = self.term
        payment = principal * _int / num / (1 - (1 + _int / num) ** (- num * term))
        return payment

    @property
    def monthly_payment(self):
        return self._quantize(self._monthly_payment)

    def _simple_interest(self, term):
        amt = self.principal * self.interest * term
        return self._quantize(amt)

    @property
    def apr(self):
        new_payment = self._simple_interest(term=1)
        apr = new_payment / self.principal
        return self._quantize(apr * 100)

    @property
    def apy(self):
        apy = (1 + self.interest / self.n_periods) ** self.n_periods - 1
        return self._quantize(apy * 100)

    @property
    def total_principal(self):
        return self._quantize(self.principal)

    @property
    def total_interest(self):
        return self._quantize(self.schedule(self.term * 12).total_interest)

    @property
    def total_paid(self):
        return self.total_principal + self.total_interest

    @property
    def interest_to_principle(self):
        return round(self.total_interest / self.total_principal * 100, 1)

    @property
    def years_to_pay(self):
        return round(self.term * self.n_periods / 12, 1)

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

    def compute_interest_portion(self, payment_number):
        _int = self.interest / 12
        _intp1 = _int + 1

        numerator = self.principal * _int * (_intp1 ** (self.n_periods * self.term + 1)
                                             - _intp1 ** payment_number)
        denominator = _intp1 * (_intp1 ** (self.n_periods * self.term) - 1)
        return numerator / denominator

    def split_payment(self, number, amount):
        interest_payment = self.compute_interest_portion(number)
        principal_payment = amount - interest_payment
        return interest_payment, principal_payment

    def _amortize(self):
        initialize = Installment(number=0,
                                 payment=0,
                                 interest=0,
                                 principal=0,
                                 total_interest=0,
                                 balance=self.principal)
        schedule = [initialize]
        total_interest = 0
        balance = self.principal
        for payment_number in range(1, self.term * self.n_periods + 1):

            split = self.split_payment(payment_number, self._monthly_payment)
            interest_payment, principal_payment = split

            total_interest += interest_payment
            balance -= principal_payment
            installment = Installment(number=payment_number,
                                      payment=self._monthly_payment,
                                      interest=interest_payment,
                                      principal=principal_payment,
                                      total_interest=total_interest,
                                      balance=balance)

            schedule.append(installment)

        return schedule
