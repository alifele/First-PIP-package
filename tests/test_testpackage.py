#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_testpackage
----------------------------------

Tests for `testpackage` module.
"""

import unittest

import testpackage


class TestTestpackage(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(testpackage.__version__)

    def tearDown(self):
        pass
