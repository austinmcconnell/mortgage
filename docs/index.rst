Mortgage Library
====================

Mortgage is a library for calculating mortgage details and aids in comparing different loans.

.. image:: https://img.shields.io/pypi/l/mortgage.svg
    :target: https://pypi.org/project/mortgage/

.. image:: https://img.shields.io/pypi/pyversions/mortgage.svg
    :target: https://pypi.org/project/mortgage/

.. image:: https://circleci.com/gh/austinmcconnell/mortgage.svg?style=shield
    :target: https://circleci.com/gh/austinmcconnell/mortgage

.. image:: https://codecov.io/gh/austinmcconnell/mortgage/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/austinmcconnell/mortgage

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/austinmcconnell


How To Use
----------

This package is intended to help understand the true cost of a mortgage.
It also can help you easily compare between different mortgages.

Begin by importing the loan class

.. code:: python

   >>> from mortgage import Loan

Create a simple mortgage

.. code:: python

   >>> loan = Loan(principal=200000, interest=.06, term=30)

View a summary of pertinent mortgage information by calling the
summarize property.

.. code:: python

   >>> loan.summarize

   Original Balance:         $    200,000
   Interest Rate:                    0.06 %
   APY:                              6.17 %
   APR:                              6.00 %
   Term:                               30 years
   Monthly Payment:          $    1199.10

   Total principal payments: $ 200,000.00
   Total interest payments:  $ 231,676.38
   Total payments:           $ 431,676.38
   Interest to principal:           115.8 %
   Years to pay:                     30.0

Particularly telling is the Interest to Principal ratio. With the
mortgage terms above, you will pay **115%** of the original balance in
interest! Compare that to the same loan with a 15 year term below


Introduction
--------------------

.. toctree::
   :maxdepth: 2

   introduction

API Documentation
--------------------

Looking for information on a specific function, class, or method? Find what you're looking for below.

.. toctree::
   :maxdepth: 2

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
