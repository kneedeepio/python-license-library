#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import kneedeepio.license

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestContentDict(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_creation(self):
        self.logger.debug("%s creation", type(self).__name__)
        dut_cd = kneedeepio.license.ContentDict()
        self.assertIsInstance(dut_cd, kneedeepio.license.ContentDict)

    def test_get_set_content(self):
        self.logger.debug("%s get_set_content", type(self).__name__)
        dut_cd = kneedeepio.license.ContentDict()
        data_dict = {"key1": "value1", "key2": "value2"}
        dut_cd.content = data_dict
        self.assertDictEqual(dut_cd.content, data_dict)

    def test_get_empty_content(self):
        self.logger.debug("%s get_empty_content", type(self).__name__)
        dut_cd = kneedeepio.license.ContentDict()
        self.assertDictEqual(dut_cd.content, {})

    def test_set_bad_content(self):
        self.logger.debug("%s set_bad_content", type(self).__name__)
        dut_cd = kneedeepio.license.ContentDict()
        with self.assertRaises(TypeError):
            dut_cd.content = "bad value"
        with self.assertRaises(TypeError):
            dut_cd.content = 1234

    def test_get_set_content_for_license(self):
        self.logger.debug("%s get_set_content_for_license", type(self).__name__)
        dut_cd = kneedeepio.license.ContentDict()
        data_dict = {"key1": "value1", "key2": "value2"}
        dut_cd.set_content_from_license(data_dict)
        self.assertDictEqual(dut_cd.get_content_for_license(), data_dict)

    def test_equal_comparison(self):
        self.logger.debug("%s equal_comparison", type(self).__name__)
        dut_cd1 = kneedeepio.license.ContentDict()
        dut_cd2 = kneedeepio.license.ContentDict()
        dut_cd3 = kneedeepio.license.ContentDict()
        dut_cd1.content = {"key1": "value1", "key2": "value2"}
        dut_cd2.content = {"key1": "value1", "key2": "value2"}
        dut_cd3.content = {"key3": "value3", "key4": "value4"}
        self.assertEqual(dut_cd1, dut_cd2)
        self.assertNotEqual(dut_cd1, dut_cd3)
