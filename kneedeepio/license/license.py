#!/usr/bin/env python3

### IMPORTS ###
import json
import uuid

from datetime import datetime

from kneedeepio.license.contentbase import ContentBase
from kneedeepio.license.signaturebase import SignatureBase

from kneedeepio.license.exceptions import \
    InvalidAssigneeException, \
    InvalidContentException, \
    InvalidExpiryDateException, \
    InvalidSignatureException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class License:
    def __init__(self, content_class = ContentBase, signature_class = SignatureBase):
        if not issubclass(content_class, ContentBase):
            raise TypeError('content_class must be a subclass of ContentBase')
        if not issubclass(signature_class, SignatureBase):
            raise TypeError('signature_class must be a subclass of SignatureBase')
        self._identifier = uuid.uuid4()
        self._assignee = None
        self._content_class = content_class
        self._content = None
        self._creation_date = datetime.utcnow()
        self._expiry_date = None
        self._validation_url = None # FIXME: Should this be a "server" object that contains the URLs?
        self._signature_class = signature_class
        self._signature = None

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        if not isinstance(value, uuid.UUID):
            raise TypeError('Expecting object of type UUID')
        self._identifier = value

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        if not isinstance(value, str):
            raise TypeError('Expecting object of type str')
        if (len(value) < 3) or (len(value) > 255): # Arbitrary limits that seem reasonable based on an *SQL VARCHAR
            raise InvalidAssigneeException
        self._assignee = value

    @property
    def content(self):
        if self._content is None:
            raise InvalidContentException
        return self._content

    @content.setter
    def content(self, value):
        # FIXME: Should this be able to check for the implemented ContentBase Class?
        if not isinstance(value, self._content_class):
            raise TypeError('Expecting object of type {}'.format(type(self._content_class).__name__))
        self._content = value

    @property
    def creation_date(self):
        # FIXME: Should this and other values be validated here?
        #        Should a creation date newer than expiry be allowed?
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        if not isinstance(value, datetime):
            raise TypeError('Expecting object of type datetime')
        self._creation_date = value

    @property
    def creation_date_iso(self):
        return self.creation_date.isoformat()

    @creation_date_iso.setter
    def creation_date_iso(self, value):
        if not isinstance(value, str):
            raise TypeError('Expecting object of type str') # FIXME: Should this handle bytes objects?
        self.creation_date = datetime.fromisoformat(value)

    @property
    def expiry_date(self):
        # NOTE: Returning None if the expiry date is not set
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        if not isinstance(value, datetime):
            raise TypeError('Expecting object of type datetime')
        if value < self.creation_date:
            raise InvalidExpiryDateException('Expiry Date older than Creation Date')
        self._expiry_date = value

    @property
    def expiry_date_iso(self):
        # NOTE: Returning an empty string if the expiry date is not set
        return self.expiry_date.isoformat() if self.expiry_date is not None else ""

    @expiry_date_iso.setter
    def expiry_date_iso(self, value):
        if not isinstance(value, str):
            raise TypeError('Expecting object of type str') # FIXME: Should this handle bytes objects?
        self.expiry_date = datetime.fromisoformat(value)

    @property
    def validation_url(self):
        return self._validation_url

    @validation_url.setter
    def validation_url(self, value):
        # FIXME: Should do what's needed to make sure the URL is safe/encoded correctly.
        # FIXME: Should this be an object that contains information about the issuing server?
        #        Could include hostname/URL, validation path,
        if not isinstance(value, str):
            raise TypeError('Expecting object of type str')
        if (len(value) < 11) or (len(value) > 255): # Arbitrary limits that seem reasonable based on an *SQL VARCHAR
            raise ValueError
        self._validation_url = value

    @property
    def signature(self):
        if self._signature is None:
            raise InvalidSignatureException
        return self._signature

    @signature.setter
    def signature(self, value):
        if not isinstance(value, self._signature_class):
            raise TypeError('Expecting object of type {}'.format(type(self._signature_class).__name__))
        self._signature = value

    def get_data_for_signing(self):
        # This method is to be called to get the JSON data string for signing.
        # NOTE: This JSON data string is sorted and compact.
        value = {}
        value['identifier'] = str(self.identifier)
        value['assignee'] = self.assignee
        value['content'] = self.content.get_content_for_license()
        value['creation_date'] = self.creation_date_iso
        value['expiry_date'] = self.expiry_date_iso
        value['validation_url'] = self.validation_url
        return json.dumps(value, sort_keys = True, separators = (',', ':'))

    def export_data(self):
        # This method is to be called to get the JSON data string containing the entire license.
        # NOTE: This JSON data string is sorted and pretty printed.
        value = {}
        value['identifier'] = str(self.identifier)
        value['assignee'] = self.assignee
        value['content'] = self.content.get_content_for_license()
        value['creation_date'] = self.creation_date_iso
        value['expiry_date'] = self.expiry_date_iso
        value['validation_url'] = self.validation_url
        value['signature'] = self.signature.get_signature_for_license()
        return json.dumps(value, sort_keys = True, indent = 2)

    def import_data(self, license_data):
        # This method is to be called to set the data values for the entire license from a JSON data string
        if not isinstance(license_data, str):
            raise TypeError('Expecting object of type str') # FIXME: Should this handle bytes objects?
        value = json.loads(license_data)
        self.identifier = uuid.UUID(value['identifier'])
        self.assignee = value['assignee']
        self.content = self._content_class()
        self.content.set_content_from_license(value['content'])
        self.creation_date_iso = value['creation_date']
        if not value['expiry_date'] == '':
            self.expiry_date_iso = value['expiry_date']
        self.validation_url = value['validation_url']
        self.signature = self._signature_class()
        self.signature.set_signature_from_license(value['signature'])
