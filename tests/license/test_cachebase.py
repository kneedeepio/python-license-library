#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import kneedeepio.license

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestCacheBase(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_insert_license_not_implemented(self):
        self.logger.debug("test_insert_license_not_implemented")
        dut_cb = kneedeepio.license.CacheBase()
        with self.assertRaises(NotImplementedError):
            dut_cb.insert_license("assignee", {})

    def test_check_for_licenses_not_implemented(self):
        self.logger.debug("test_check_for_licenses_not_implemented")
        dut_cb = kneedeepio.license.CacheBase()
        with self.assertRaises(NotImplementedError):
            dut_cb.check_for_licenses("assignee")
