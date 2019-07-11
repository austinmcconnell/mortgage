"""The  Loan object used to create and calculate various mortgage statistics."""
from collections import namedtuple
from decimal import Decimal
from typing import Tuple

Installment = namedtuple('Installment', 'number payment interest principal total_interest balance')


class Loan(object):
    """
    :class:`Loan <Loan>` object used to create a loan.

    This object can calculate amortization schedule and show summary statistics for the loan.

    :param principal: The original sum of money borrowed.
    :param interest: The amount charged by lender for use of the assets.
    :param term: The lifespan of the loan.
    :param term_unit: Unit for the lifespan of the loan.
    :param compounded: Frequency that interest is compounded
    :param currency: Set the currency symbol for use with summarize

    Usage:
        >>> from mortgage import Loan
        >>> Loan(principal=200000, interest=.04125, term=15)
        <Loan principal=200000, interest=0.04125, term=15>
    """

    def __init__(self, principal, interest, term, term_unit='years', compounded='monthly', currency='$'):

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
        self._currency = currency

    def __repr__(self):
        return '<Loan principal={}, interest={}, term={}>'.format(self.principal, self.interest, self.term)

    @staticmethod
    def _quantize(value):
        return Decimal(value).quantize(Decimal('0.01'))

    def schedule(self, nth_payment=None):
        """
        Retrieve payment information for the nth payment.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=30)
            >>> loan.schedule(1)
            Installment(number=1, payment=Decimal('1199.101050305504789182922487'), interest=Decimal('1E+3'), principal=Decimal('199.101050305504789182922487'), total_interest=Decimal('1000'), balance=Decimal('199800.8989496944952108170775'))
        """
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
        """
        Return the total monthly payment (principal and interest) for the loan.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=30)
            >>> loan.monthly_payment
            Decimal('1199.10')
        """
        return self._quantize(self._monthly_payment)

    def _simple_interest(self, term):
        amt = self.principal * self.interest * term
        return self._quantize(amt)

    @property
    def apr(self) -> Decimal:
        """
        Return the annual percentage rate (APR).

        APR is the amount of interest on your total loan amount that
        you'll pay annually (averaged over the full term of the loan)

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.apr
            Decimal('6.00')
        """
        new_payment = self._simple_interest(term=1)
        apr = new_payment / self.principal
        return self._quantize(apr * 100)

    @property
    def apy(self) -> Decimal:
        """
        Return the annual percentage yield (APY).

        APY is the effective annual rate of return taking into
        account the effect of compounding interest.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.apy
            Decimal('6.17')
        """
        apy = (1 + self.interest / self.n_periods) ** self.n_periods - 1
        return self._quantize(apy * 100)

    @property
    def total_principal(self) -> Decimal:
        """
        Return the total principal paid over the life of the loan.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.total_principal
            Decimal('200000.00')
        """
        return self._quantize(self.principal)

    @property
    def total_interest(self) -> Decimal:
        """
        Return the total interest paid over the life of the loan.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.total_interest
            Decimal('103788.46')
        """
        return self._quantize(self.schedule(self.term * self.n_periods).total_interest)

    @property
    def total_paid(self) -> Decimal:
        """
        Return the total amount paid (both principal and interest) over the life of the loan.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.total_paid
            Decimal('303788.46')
        """
        return self.total_principal + self.total_interest

    @property
    def interest_to_principle(self) -> float:
        """
        Return the percentage of the principal that is payed in interest over the life of the loan.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.interest_to_principle
            51.9
        """
        return float(round(self.total_interest / self.total_principal * 100, 1))

    @property
    def years_to_pay(self) -> float:
        """
        Return the number of years it will take to pay off this loan given the payment schedule.

        Usage:
            >>> from mortgage import Loan
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.years_to_pay
            15.0
        """
        return round(self.term * self.n_periods / 12, 1)

    @property
    def summarize(self):
        print('Original Balance:         {}{:>11,}'.format(self._currency,self.principal))
        print('Interest Rate:             {:>11} %'.format(self.interest))
        print('APY:                       {:>11} %'.format(self.apy))
        print('APR:                       {:>11} %'.format(self.apr))
        print('Term:                      {:>11} {}'.format(self.term, self.term_unit))
        print('Monthly Payment:          {}{:>11}'.format(self._currency,self.monthly_payment))
        print('')
        print('Total principal payments: {}{:>11,}'.format(self._currency,self.total_principal))
        print('Total interest payments:  {}{:>11,}'.format(self._currency,self.total_interest))
        print('Total payments:           {}{:>11,}'.format(self._currency,self.total_paid))
        print('Interest to principal:     {:>11} %'.format(self.interest_to_principle))
        print('Years to pay:              {:>11}'.format(self.years_to_pay))

    def split_payment(self, number: int, amount: Decimal) -> Tuple[Decimal, Decimal]:
        """
        Split payment amount into principal and interest.

        :param number: the payment number (e.g. nth payment)
        :param amount: the total payment amount to be split

        Usage:
            >>> from mortgage import Loan
            >>> from decimal import Decimal
            >>> loan = Loan(principal=200000, interest=.06, term=15)
            >>> loan.split_payment(number=180, amount=Decimal(1199.10))
            (Decimal('8.396585353715933437157525763'), Decimal('1190.703414646283975613372297'))
        """
        def compute_interest_portion(payment_number):
            _int = self.interest / 12
            _intp1 = _int + 1

            numerator = self.principal * _int * (_intp1 ** (self.n_periods * self.term + 1)
                                                 - _intp1 ** payment_number)
            denominator = _intp1 * (_intp1 ** (self.n_periods * self.term) - 1)
            return numerator / denominator

        interest_payment = compute_interest_portion(number)
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
