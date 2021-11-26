#!/usr/bin/env python3

### IMPORTS ###
import json
import logging
import random
import string
import unittest
import uuid

from datetime import datetime

import kneedeepio.license

from kneedeepio.license.exceptions import \
    InvalidAssigneeException, \
    InvalidContentException, \
    InvalidExpiryDateException, \
    InvalidSignatureException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestLicense(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_creation(self):
        self.logger.debug("%s creation", type(self).__name__)
        # NOTE: Don't need to test default values as those will be handled in their getter & setter tests
        dut_l = kneedeepio.license.License()

    def test_creation_content_class(self):
        self.logger.debug("%s creation_content_class", type(self).__name__)
        # NOTE: Don't need to test default values as those will be handled in their getter & setter tests
        dut_l = kneedeepio.license.License(content_class = kneedeepio.license.ContentDict)

    def test_creation_signature_class(self):
        self.logger.debug("%s creation_signature_class", type(self).__name__)
        # NOTE: Don't need to test default values as those will be handled in their getter & setter tests
        dut_l = kneedeepio.license.License(signature_class = kneedeepio.license.SignatureSHA256)

    def test_creation_bad_content_class(self):
        self.logger.debug("%s creation_bad_content_class", type(self).__name__)
        with self.assertRaises(TypeError):
            dut_l = kneedeepio.license.License(content_class = str)

    def test_creation_bad_signature_class(self):
        self.logger.debug("%s creation_bad_signature_class", type(self).__name__)
        with self.assertRaises(TypeError):
            dut_l = kneedeepio.license.License(signature_class = dict)

    def test_get_set_identifier(self):
        self.logger.debug("%s get_set_identifier", type(self).__name__)
        dut_l = kneedeepio.license.License()
        data_license_id = dut_l.identifier
        self.assertIsInstance(data_license_id, uuid.UUID)
        data_new_id = uuid.uuid4()
        dut_l.identifier = data_new_id
        self.assertEqual(dut_l.identifier, data_new_id)

    def test_set_bad_identifier(self):
        self.logger.debug("%s set_bad_identifier", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.identifier = "bad value"
        with self.assertRaises(TypeError):
            dut_l.identifier = 1234

    def test_get_set_assignee(self):
        self.logger.debug("%s get_set_assignee", type(self).__name__)
        dut_l = kneedeepio.license.License()
        data_assignee = "assignee@example.com"
        dut_l.assignee = data_assignee
        self.assertEqual(dut_l.assignee, data_assignee)

    def test_set_bad_assignee(self):
        self.logger.debug("%s set_bad_assignee", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.assignee = 1234
        with self.assertRaises(InvalidAssigneeException):
            dut_l.assignee = "12"
        with self.assertRaises(InvalidAssigneeException):
            # From this answer: https://stackoverflow.com/a/2257449
            dut_l.assignee = ''.join(random.choices(string.ascii_uppercase + string.digits, k=261))

    def test_get_set_content(self):
        self.logger.debug("%s get_set_content", type(self).__name__)
        # Create License
        dut_l = kneedeepio.license.License()
        # Check for InvalidContentException
        with self.assertRaises(InvalidContentException):
            self.assertIsNotNone(dut_l.content) # This should fail if the exception is not raised for some reason.
        # Create ContentBase
        dut_cb = kneedeepio.license.ContentBase()
        # Set Content with ContentBase
        dut_l.content = dut_cb
        # Get Content with ContentBase
        test_cb = dut_l.content
        # Verify of type ContentBase
        self.assertIsInstance(test_cb, kneedeepio.license.ContentBase)

    def test_set_bad_content(self):
        self.logger.debug("%s set_bad_content", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.content = "bad value"
        with self.assertRaises(TypeError):
            dut_l.content = 1234

    def test_get_set_content_with_data(self):
        self.logger.debug("%s get_set_content_with_data", type(self).__name__)
        # Create License with ContentDict as content_class
        dut_l = kneedeepio.license.License(content_class = kneedeepio.license.ContentDict)
        # Check for InvalidContentException
        with self.assertRaises(InvalidContentException):
            self.assertIsNotNone(dut_l.content) # This should fail if the exception is not raised for some reason.
        # Create ContentDict
        dut_cd = kneedeepio.license.ContentDict()
        dut_cd.content = {"key5": "value5", "key6": "value6", "key7": "value7"}
        # Set Content with ContentDict
        dut_l.content = dut_cd
        # Get Content with ContentDict
        test_cd = dut_l.content
        # Verify of type ContentDict
        self.assertIsInstance(test_cd, kneedeepio.license.ContentDict)
        # Verify contents of ContentDict
        self.assertEqual(test_cd, dut_cd)

    def test_get_set_creation_date(self):
        self.logger.debug("%s get_set_creation_date", type(self).__name__)
        # Create License
        dut_l = kneedeepio.license.License()
        # Check for valid datetime
        test_dt1 = dut_l.creation_date
        self.assertIsInstance(test_dt1, datetime)
        # Update datetime
        dut_l.creation_date = datetime.fromtimestamp(3)
        # Check again for valid datetime
        test_dt2 = dut_l.creation_date
        self.assertIsInstance(test_dt2, datetime)
        # Verify not same datetimes
        self.assertNotEqual(test_dt1, test_dt2)

    def test_set_bad_creation_date(self):
        self.logger.debug("%s set_bad_creation_date", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.creation_date = "bad value"
        with self.assertRaises(TypeError):
            dut_l.creation_date = 1234

    def test_get_set_creation_date_iso(self):
        self.logger.debug("%s get_set_creation_date_iso", type(self).__name__)
        # Create License
        dut_l = kneedeepio.license.License()
        # Check for valid datetime
        test_dt1 = dut_l.creation_date
        test_dti1 = dut_l.creation_date_iso
        self.assertIsInstance(test_dt1, datetime)
        self.assertIsInstance(test_dti1, str)
        self.assertEqual(test_dti1, test_dt1.isoformat())
        # Update datetime
        test_dt2 = datetime.fromtimestamp(3)
        dut_l.creation_date_iso = test_dt2.isoformat()
        # Check again for valid datetime
        test_dti2 = dut_l.creation_date_iso
        self.assertIsInstance(test_dt2, datetime)
        self.assertIsInstance(test_dti2, str)
        self.assertEqual(test_dti2, test_dt2.isoformat())
        # Verify not same datetimes
        self.assertNotEqual(test_dti1, test_dti2)

    def test_set_bad_creation_date_iso(self):
        self.logger.debug("%s set_bad_creation_date_iso", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.creation_date_iso = datetime.utcnow()
        with self.assertRaises(TypeError):
            dut_l.creation_date_iso = 1234

    def test_set_invalid_creation_date_iso(self):
        self.logger.debug("%s set_bad_creation_date_iso", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(ValueError):
            dut_l.creation_date_iso = "not an ISO8601 string"

    def test_get_set_expiry_date(self):
        self.logger.debug("%s get_set_expiry_date", type(self).__name__)
        # Create License
        dut_l = kneedeepio.license.License()
        # Check for None since not yet set
        self.assertIsNone(dut_l.expiry_date)
        # Update datetime
        data_dt = datetime.utcnow()
        dut_l.expiry_date = data_dt
        # Check again for valid datetime
        test_dt = dut_l.expiry_date
        self.assertIsInstance(test_dt, datetime)
        # Verify set correctly
        self.assertEqual(test_dt, data_dt)

    def test_set_bad_expiry_date(self):
        self.logger.debug("%s set_bad_expiry_date", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.expiry_date = "bad value"
        with self.assertRaises(TypeError):
            dut_l.expiry_date = 1234

    def test_set_too_old_expiry_date(self):
        self.logger.debug("%s set_too_old_expiry_date", type(self).__name__)
        dut_l = kneedeepio.license.License()
        data_dt = datetime.fromtimestamp(3)
        with self.assertRaises(InvalidExpiryDateException):
            dut_l.expiry_date = data_dt

    def test_get_set_expiry_date_iso(self):
        self.logger.debug("%s get_set_expiry_date_iso", type(self).__name__)
        # Create License
        dut_l = kneedeepio.license.License()
        # Update datetime
        test_dt2 = datetime.utcnow()
        dut_l.expiry_date_iso = test_dt2.isoformat()
        # Check again for valid datetime
        test_dti2 = dut_l.expiry_date_iso
        self.assertIsInstance(test_dt2, datetime)
        self.assertIsInstance(test_dti2, str)
        self.assertEqual(test_dti2, test_dt2.isoformat())

    def test_set_bad_expiry_date_iso(self):
        self.logger.debug("%s set_bad_expiry_date_iso", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.expiry_date_iso = datetime.utcnow()
        with self.assertRaises(TypeError):
            dut_l.expiry_date_iso = 1234

    def test_set_invalid_expiry_date_iso(self):
        self.logger.debug("%s set_bad_expiry_date_iso", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(ValueError):
            dut_l.expiry_date_iso = "not an ISO8601 string"

    def test_get_set_validation_url(self):
        self.logger.debug("%s get_set_validation_url", type(self).__name__)
        dut_l = kneedeepio.license.License()
        data_vurl = "https://example.com/validate"
        dut_l.validation_url = data_vurl
        self.assertEqual(dut_l.validation_url, data_vurl)

    def test_set_bad_validation_url(self):
        self.logger.debug("%s set_bad_validation_url", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.validation_url = 1234
        with self.assertRaises(ValueError):
            dut_l.validation_url = "12"
        with self.assertRaises(ValueError):
            # From this answer: https://stackoverflow.com/a/2257449
            dut_l.validation_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=261))

    def test_get_set_signature(self):
        self.logger.debug("%s get_set_signature", type(self).__name__)
        # Create License
        dut_l = kneedeepio.license.License()
        # Check for InvalidContentException
        with self.assertRaises(InvalidSignatureException):
            self.assertIsNotNone(dut_l.signature) # This should fail if the exception is not raised for some reason.
        # Create ContentBase
        dut_sb = kneedeepio.license.SignatureBase()
        # Set Content with ContentBase
        dut_l.signature = dut_sb
        # Get Content with ContentBase
        test_sb = dut_l.signature
        # Verify of type ContentBase
        self.assertIsInstance(test_sb, kneedeepio.license.SignatureBase)

    def test_set_bad_signature(self):
        self.logger.debug("%s set_bad_signature", type(self).__name__)
        dut_l = kneedeepio.license.License()
        with self.assertRaises(TypeError):
            dut_l.signature = "bad value"
        with self.assertRaises(TypeError):
            dut_l.signature = 1234

    def test_get_set_signature_with_data(self):
        self.logger.debug("%s get_set_signature_with_data", type(self).__name__)
        # Create License with SignatureSHA256 as signature_class
        dut_l = kneedeepio.license.License(signature_class = kneedeepio.license.SignatureSHA256)
        # Check for InvalidContentException
        with self.assertRaises(InvalidSignatureException):
            self.assertIsNotNone(dut_l.signature) # This should fail if the exception is not raised for some reason.
        # Create SignatureSHA256
        dut_ssha = kneedeepio.license.SignatureSHA256()
        dut_ssha.value = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        # Set Signature with SignatureSHA256
        dut_l.signature = dut_ssha
        # Get Signature with SignatureSHA256
        test_ssha = dut_l.signature
        # Verify of type SignatureSHA256
        self.assertIsInstance(test_ssha, kneedeepio.license.SignatureSHA256)

    def test_get_data_for_signing(self):
        self.logger.debug("%s get_data_for_signing", type(self).__name__)
        # Create License with ContentDict and SignatureSHA256
        dut_l = kneedeepio.license.License(
            content_class = kneedeepio.license.ContentDict,
            signature_class = kneedeepio.license.SignatureSHA256
        )
        # Set values
        dut_l.identifier = uuid.UUID("12345678-1234-5678-1234-567812345678")
        dut_l.assignee = "name@example.com"
        dut_cd = kneedeepio.license.ContentDict()
        dut_cd.content = {"key1": "value2", "key3": "value5"}
        dut_l.content = dut_cd
        dut_l.creation_date = datetime.fromtimestamp(3)
        # Not setting expiry_date yet
        dut_l.validation_url = "https://example.com/validate"
        # Get data string and compare to example
        test_dfs1 = dut_l.get_data_for_signing()
        data_dfs1 = '{"assignee":"name@example.com","content":{"key1":"value2","key3":"value5"},"creation_date":"1969-12-31T17:00:03","expiry_date":"","identifier":"12345678-1234-5678-1234-567812345678","validation_url":"https://example.com/validate"}'
        self.assertEqual(test_dfs1, data_dfs1)
        # Set expiry_date and compare again
        dut_l.expiry_date = datetime.fromtimestamp(7)
        test_dfs2 = dut_l.get_data_for_signing()
        data_dfs2 = '{"assignee":"name@example.com","content":{"key1":"value2","key3":"value5"},"creation_date":"1969-12-31T17:00:03","expiry_date":"1969-12-31T17:00:07","identifier":"12345678-1234-5678-1234-567812345678","validation_url":"https://example.com/validate"}'
        self.assertEqual(test_dfs2, data_dfs2)

    def test_export_data(self):
        self.logger.debug("%s export_data", type(self).__name__)
        # Create License with ContentDict and SignatureSHA256
        dut_l = kneedeepio.license.License(
            content_class = kneedeepio.license.ContentDict,
            signature_class = kneedeepio.license.SignatureSHA256
        )
        # Set values
        dut_l.identifier = uuid.UUID("12345678-1234-5678-1234-567812345678")
        dut_l.assignee = "name@example.com"
        dut_cd = kneedeepio.license.ContentDict()
        dut_cd.content = {"key1": "value2", "key3": "value5"}
        dut_l.content = dut_cd
        dut_l.creation_date = datetime.fromtimestamp(3)
        # Not setting expiry_date yet
        dut_l.validation_url = "https://example.com/validate"
        dut_ssha = kneedeepio.license.SignatureSHA256()
        dut_ssha.value = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        dut_l.signature = dut_ssha
        # Get data string and compare to example
        test_ed1 = dut_l.export_data()
        data_ed1 = '''{
  "assignee": "name@example.com",
  "content": {
    "key1": "value2",
    "key3": "value5"
  },
  "creation_date": "1969-12-31T17:00:03",
  "expiry_date": "",
  "identifier": "12345678-1234-5678-1234-567812345678",
  "signature": {
    "method": "SHA256",
    "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
  },
  "validation_url": "https://example.com/validate"
}'''
        self.assertEqual(test_ed1, data_ed1)
        # Set expiry_date and compare again
        dut_l.expiry_date = datetime.fromtimestamp(7)
        test_ed2 = dut_l.export_data()
        data_ed2 = '''{
  "assignee": "name@example.com",
  "content": {
    "key1": "value2",
    "key3": "value5"
  },
  "creation_date": "1969-12-31T17:00:03",
  "expiry_date": "1969-12-31T17:00:07",
  "identifier": "12345678-1234-5678-1234-567812345678",
  "signature": {
    "method": "SHA256",
    "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
  },
  "validation_url": "https://example.com/validate"
}'''
        self.assertEqual(test_ed2, data_ed2)

    def test_import_data(self):
        self.logger.debug("%s import_data", type(self).__name__)
        dut_l = kneedeepio.license.License(
            content_class = kneedeepio.license.ContentDict,
            signature_class = kneedeepio.license.SignatureSHA256
        )
        data_id1 = '''{
  "assignee": "name@example.com",
  "content": {
    "key1": "value2",
    "key3": "value5"
  },
  "creation_date": "1969-12-31T17:00:03",
  "expiry_date": "",
  "identifier": "12345678-1234-5678-1234-567812345678",
  "signature": {
    "method": "SHA256",
    "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
  },
  "validation_url": "https://example.com/validate"
}'''
        dut_l.import_data(data_id1)
        self.assertEqual(dut_l.identifier, uuid.UUID("12345678-1234-5678-1234-567812345678"))
        self.assertEqual(dut_l.assignee, "name@example.com")
        self.assertDictEqual(dut_l.content.get_content_for_license(), {"key1": "value2", "key3": "value5"})
        self.assertEqual(dut_l.creation_date, datetime.fromtimestamp(3))
        self.assertIsNone(dut_l.expiry_date)
        self.assertEqual(dut_l.validation_url, "https://example.com/validate")
        self.assertDictEqual(dut_l.signature.get_signature_for_license(), {
            "method": "SHA256",
            "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        })
        data_id2 = '''{
  "assignee": "name@example.com",
  "content": {
    "key1": "value2",
    "key3": "value5"
  },
  "creation_date": "1969-12-31T17:00:03",
  "expiry_date": "1969-12-31T17:00:07",
  "identifier": "12345678-1234-5678-1234-567812345678",
  "signature": {
    "method": "SHA256",
    "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
  },
  "validation_url": "https://example.com/validate"
}'''
        dut_l.import_data(data_id2)
        self.assertEqual(dut_l.identifier, uuid.UUID("12345678-1234-5678-1234-567812345678"))
        self.assertEqual(dut_l.assignee, "name@example.com")
        self.assertDictEqual(dut_l.content.get_content_for_license(), {"key1": "value2", "key3": "value5"})
        self.assertEqual(dut_l.creation_date, datetime.fromtimestamp(3))
        self.assertEqual(dut_l.expiry_date, datetime.fromtimestamp(7))
        self.assertEqual(dut_l.validation_url, "https://example.com/validate")
        self.assertDictEqual(dut_l.signature.get_signature_for_license(), {
            "method": "SHA256",
            "value": "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"
        })

    def test_import_data_bad_data(self):
        self.assertEqual(True, False, "FIXME: Implement this test")
