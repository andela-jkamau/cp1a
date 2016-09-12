[![Build Status](https://travis-ci.org/andela-jkamau/cp1a.svg?branch=develop)](https://travis-ci.org/andela-jkamau/cp1a)     [![Coverage Status](https://coveralls.io/repos/github/andela-jkamau/cp1a/badge.svg?branch=master)](https://coveralls.io/github/andela-jkamau/cp1a?branch=master)   [![Codacy Badge](https://api.codacy.com/project/badge/Grade/a03eccef1776494c8c590c5879e5790a)](https://www.codacy.com/app/jimmy-kamau/cp1a?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-jkamau/cp1a&amp;utm_campaign=Badge_Grade)

Amity has rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

# Installation

Clone this repo:
```
git clone https://github.com/andela-jkamau/cp1a.git
```


Navigate to the `cp1a` directory:
```
cd cp1a
```


Install dependancies:
```
pip install -r requirements.txt
```


Run tests to ensure everything is working as expected:
```
python tests.py
```


# To do

* Fix `print_allocations` and `print_unallocated` tests failing if called after index 7
* Find a better way to order tests
