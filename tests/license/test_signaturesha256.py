#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import kneedeepio.license

from kneedeepio.license.exceptions import InvalidSignatureException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestSignatureSHA256(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_creation(self):
        self.logger.debug("%s creation", type(self).__name__)
        dut_ssha = kneedeepio.license.SignatureSHA256()

    def test_get_set_value(self):
        self.logger.debug("%s get_set_content", type(self).__name__)
        dut_ssha = kneedeepio.license.SignatureSHA256()
        data_str = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        dut_ssha.value = data_str
        self.assertEqual(dut_ssha.value, data_str)

    def test_get_empty_value(self):
        self.logger.debug("%s get_empty_value", type(self).__name__)
        dut_ssha = kneedeepio.license.SignatureSHA256()
        # FIXME: Should this raise an error if value is not set?
        self.assertEqual(dut_ssha.value, "")

    def test_set_bad_value(self):
        self.logger.debug("%s set_bad_value", type(self).__name__)
        dut_ssha = kneedeepio.license.SignatureSHA256()
        with self.assertRaises(TypeError):
            dut_ssha.value = 1234
        with self.assertRaises(ValueError):
            dut_ssha.value = "bad value"

    def test_get_set_signature_for_license(self):
        self.logger.debug("%s get_set_signature_for_license", type(self).__name__)
        dut_ssha = kneedeepio.license.SignatureSHA256()
        data_dict = {"method": "SHA256", "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"}
        dut_ssha.set_signature_from_license(data_dict)
        self.assertDictEqual(dut_ssha.get_signature_for_license(), data_dict)

    def test_set_bad_signature_for_license(self):
        self.logger.debug("%s get_set_signature_for_license", type(self).__name__)
        dut_ssha = kneedeepio.license.SignatureSHA256()
        data_dict1 = {"method": "moo", "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"}
        with self.assertRaises(InvalidSignatureException):
            dut_ssha.set_signature_from_license(data_dict1)
        data_dict2 = {"method": "SHA256", "value": "0123"}
        with self.assertRaises(ValueError):
            dut_ssha.set_signature_from_license(data_dict2)

    def test_equal_comparison(self):
        self.logger.debug("%s equal_comparison", type(self).__name__)
        dut_ssha1 = kneedeepio.license.SignatureSHA256()
        dut_ssha2 = kneedeepio.license.SignatureSHA256()
        dut_ssha3 = kneedeepio.license.SignatureSHA256()
        dut_ssha1.value = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        dut_ssha2.value = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        dut_ssha3.value = "0123456789012345678901234567890123456789012345678901234567890123"
        self.assertEqual(dut_ssha1, dut_ssha2)
        self.assertNotEqual(dut_ssha1, dut_ssha3)
