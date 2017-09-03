Mortgage
====================

[![PyPI][pypi_logo]][pypi_link] [![CircleCI][circleci_logo]][circleci_link] [![Codecov][codecov_logo]][codecov_link] [![Pyup][pyup_logo]][pyup_link]

[pypi_logo]: https://img.shields.io/pypi/v/mortgage.svg
[pypi_link]: https://pypi.python.org/pypi/mortgage
[circleci_logo]: https://circleci.com/gh/austinmcconnell/mortgage.svg?style=shield
[circleci_link]: https://circleci.com/gh/austinmcconnell/mortgage
[codecov_logo]: https://codecov.io/gh/austinmcconnell/mortgage/branch/master/graph/badge.svg
[codecov_link]: https://codecov.io/gh/austinmcconnell/mortgage
[pyup_logo]: https://pyup.io/repos/github/austinmcconnell/mortgage/shield.svg
[pyup_link]: https://pyup.io/repos/github/austinmcconnell/mortgage/

Simple mortgage calculator tool


Installation
--------------------

To install mortgage, simply:

```commandline
pip install mortgage
```

How To Use
--------------------

This package is intended to help understand the true cost of a mortgage. It also can help you easily compare between different mortgages.

Begin by importing the loan class

```python
from mortgage import Loan

```

Create a simple mortgage

```python
from mortgage import Loan

loan = Loan(principal=200000, interest=.06, term=30)
```

View a summary of pertinent mortgage information by calling the summarize property.

```python
from mortgage import Loan

loan = Loan(principal=200000, interest=.06, term=30)
loan.summarize

>>> Original Balance:         $    200,000
>>> Interest Rate:                    0.06 %
>>> APY:                              6.17 %
>>> APR:                              6.00 %
>>> Term:                               30 years
>>> Monthly Payment:          $    1199.10

>>> Total principal payments: $ 200,000.00
>>> Total interest payments:  $ 231,676.38
>>> Total payments:           $ 431,676.38
>>> Interest to principal:           115.8 %
>>> Years to pay:                     30.0
```

Particularly telling is the Interest to Principal ratio. With the mortgage terms above, you will pay **115%** of the original balance in interest! Compare that to the same loan with a 15 year term below


```python
from mortgage import Loan

loan = Loan(principal=200000, interest=.06, term=15)
loan.summarize

>>> Original Balance:         $    200,000
>>> Interest Rate:                    0.06 %
>>> APY:                              6.17 %
>>> APR:                              6.00 %
>>> Term:                               15 years
>>> Monthly Payment:          $    1687.71

>>> Total principal payments: $ 200,000.00
>>> Total interest payments:  $ 103,788.46
>>> Total payments:           $ 303,788.46
>>> Interest to principal:            51.9 %
>>> Years to pay:                     15.0
```
In this case, you only pay **52%** of the original loan balance in interest. Obviously, the shorter the term with all else equal, the less interest you'll pay. But it helps to know exactly how much more/less you'll pay.

Run The Test Cases
--------------------
From the top level directory, run the following command:

```
pytest
```

Thank You
--------------------

Thanks for checking out the package! I hope you find it useful.

Feel free to open an issue with suggestions, imporovements, ideas, etc.
