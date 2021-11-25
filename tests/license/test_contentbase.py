#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import kneedeepio.license

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestContentBase(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_set_content_from_license_not_implemented(self):
        self.logger.debug("test_set_content_from_license_not_implemented")
        dut_cb = kneedeepio.license.ContentBase()
        with self.assertRaises(NotImplementedError):
            dut_cb.set_content_from_license({})

    def test_get_content_for_license_not_implemented(self):
        self.logger.debug("test_get_content_for_license_not_implemented")
        dut_cb = kneedeepio.license.ContentBase()
        with self.assertRaises(NotImplementedError):
            dut_cb.get_content_for_license()
