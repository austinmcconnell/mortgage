from decimal import Decimal
import pytest

from mortgage.loan import Loan


def convert(value):
    return Decimal(value).quantize(Decimal('0.01'))

class TestLoan:

    loan = Loan(principal=200000, interest=.06, term=30, start_date=(2017, 3, 1))

    def test_monthly_payment(self):
        assert convert(self.loan.monthly_payment) == convert(1199.10)

    nth_principal = [
        (1, 199.10),
        (5, 203.11),
        (10, 208.24),
        (360, 1193.14)
    ]

    @pytest.mark.parametrize('nth_payment, principal', nth_principal)
    def test_nth_principal_payment(self, nth_payment, principal):
        assert convert(self.loan.schedule(nth_payment)['principal']) == convert(principal)

    nth_interest = [
        (1, 1000.00),
        (5, 995.99),
        (10, 990.86),
        (360, 5.97)
    ]

    @pytest.mark.parametrize('nth_payment, interest', nth_interest)
    def test_nth_interest_payment(self, nth_payment, interest):
        assert convert(self.loan.schedule(nth_payment)['interest']) == convert(interest)

    nth_total_interest = [
        (1, 1000.00),
        (5, 4990.00),
        (10, 9954.60),
        (360, 231676.38)
    ]

    @pytest.mark.parametrize('nth_payment, total_interest', nth_total_interest)
    def test_nth_total_interest_payment(self, nth_payment, total_interest):
        assert convert(self.loan.schedule(nth_payment)['total_interest']) == convert(total_interest)

    nth_balance = [
        (1, 199800.90),
        (5, 198994.49),
        (10, 197963.59),
        (360, 0)
    ]

    @pytest.mark.parametrize('nth_payment, balance', nth_balance)
    def test_nth_balance(self, nth_payment, balance):
        assert convert(self.loan.schedule(nth_payment)['balance']) == convert(balance)

    def test_original_balance(self):
        assert self.loan.principal == convert(200000.00)

    def test_interest_rate(self):
        assert self.loan.interest == convert(.06)

    def test_apy(self):
        assert self.loan.apy == convert(6.17)

    def test_apr(self):
        assert self.loan.apr == convert(6.00)

    def test_term(self):
        assert self.loan.term == 30

    def test_total_principal(self):
        assert self.loan.total_principal == convert(200000.00)

    def test_total_interest(self):
        assert self.loan.total_interest == convert(231676.38)

    def test_total_paid(self):
        assert self.loan.total_paid == convert(431676.38)

    def test_interest_to_principle(self):
        assert self.loan.interest_to_principle == convert(115.8)

    def test_years_to_pay(self):
        assert self.loan.years_to_pay == 30
