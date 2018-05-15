Introduction
----------------

This package is intended to help understand the true cost of a mortgage. It also can help you
easily compare between different mortgages.

Begin by importing the loan class

    >>> from mortgage import Loan

.. testsetup:: *

    from mortgage import Loan
    loan = Loan(principal=200000, interest=.06, term=30)

Create a simple loan

.. doctest::

    >>> loan = Loan(principal=200000, interest=.06, term=30)
    >>> loan
    <Loan principal=200000, interest=0.06, term=30>

Get info about the first payemnt.

.. doctest::

    >>> loan.schedule(1)
    Installment(number=1, payment=Decimal('1199.101050305504789182922487'), interest=Decimal('1E+3'), principal=Decimal('199.101050305504789182922487'), total_interest=Decimal('1000'), balance=Decimal('199800.8989496944952108170775'))

Get info about the last payemnt.

.. doctest::

    >>> loan.schedule(360)
    Installment(number=360, payment=Decimal('1199.101050305504789182922487'), interest=Decimal('5.965676867191566115337922814'), principal=Decimal('1193.135373438313223067584564'), total_interest=Decimal('231676.3781099817241058520950'), balance=Decimal('-6.60E-22'))

View a summary of pertinent mortgage information by calling the summarize property.

.. doctest::

    >>> loan.summarize
    Original Balance:         $    200,000
    Interest Rate:                    0.06 %
    APY:                              6.17 %
    APR:                              6.00 %
    Term:                               30 years
    Monthly Payment:          $    1199.10
    <BLANKLINE>
    Total principal payments: $ 200,000.00
    Total interest payments:  $ 231,676.38
    Total payments:           $ 431,676.38
    Interest to principal:           115.8 %
    Years to pay:                     30.0
