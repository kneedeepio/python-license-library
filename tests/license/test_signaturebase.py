#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import kneedeepio.license

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestSignatureBase(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_set_signature_from_license_not_implemented(self):
        self.logger.debug("test_set_signature_from_license_not_implemented")
        dut_sb = kneedeepio.license.SignatureBase()
        with self.assertRaises(NotImplementedError):
            dut_sb.set_signature_from_license({})

    def test_get_signature_for_license_not_implemented(self):
        self.logger.debug("test_get_signature_for_license_not_implemented")
        dut_sb = kneedeepio.license.SignatureBase()
        with self.assertRaises(NotImplementedError):
            dut_sb.get_signature_for_license()
