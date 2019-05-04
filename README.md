Mortgage
====================

[![PyPI](https://img.shields.io/pypi/v/mortgage.svg)](https://pypi.python.org/pypi/mortgage)
[![CircleCI](https://circleci.com/gh/austinmcconnell/mortgage.svg?style=shield)](https://circleci.com/gh/austinmcconnell/mortgage)
[![CodeClimate Maintainability](https://api.codeclimate.com/v1/badges/ee719e510c795ebcc401/maintainability)](https://codeclimate.com/github/austinmcconnell/mortgage/maintainability)
[![CodeClimate Test Coverage](https://api.codeclimate.com/v1/badges/ee719e510c795ebcc401/test_coverage)](https://codeclimate.com/github/austinmcconnell/mortgage/test_coverage)
[![Pyup](https://pyup.io/repos/github/austinmcconnell/mortgage/shield.svg)](https://pyup.io/repos/github/austinmcconnell/mortgage/)
[![ReadTheDocs](https://readthedocs.org/projects/mortgage/badge/?version=latest)](http://mortgage.readthedocs.io/en/latest/?badge=latest)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/austinmcconnell)

![Logo](docs/_static/mortgage-logo.jpg)

Mortgage is a simple calculator intended to aid comprehension of the true cost of a mortgage.


Installation
--------------------

To install mortgage, simply:

```commandline
pip install mortgage
```


Documentation
-------------------

Documentation is available at [https://mortgage.readthedocs.io](https://mortgage.readthedocs.io)


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
