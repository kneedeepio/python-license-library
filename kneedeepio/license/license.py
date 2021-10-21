#!/usr/bin/env python3

### IMPORTS ###
import json

from datetime import datetime

from kneedeepio.license.contentbase import ContentBase
from kneedeepio.license.signaturebase import SignatureBase

from kneedeepio.license.exceptions import NoContentException, InvalidSignatureException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class License:
    def __init__(self):
        self._content = None
        self._creation_date = datetime.utcnow()
        self._expiry_date = None
        self._validation_url = None # FIXME: Should this be a "server" object that contains the URLs?
        self._signature = None

    @property
    def content(self):
        if self._content is None:
            raise NoContentException
        return self._content

    @content.setter
    def content(self, value):
        # FIXME: Should this be able to check for the implemented ContentBase Class?
        if not isinstance(value, ContentBase):
            raise TypeError('Expecting object of type ContentBase')
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
            raise TypeError('Expecting object of type str')
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
            # Don't allow the expiry date to be older than the creation_date
            raise ValueError # FIXME: Make a better exception for this
        self._expiry_date = value

    @property
    def expiry_date_iso(self):
        # NOTE: Returning an empty string if the expiry date is not set
        return self.expiry_date.isoformat() if self.expiry_date is not None else ""

    @expiry_date_iso.setter
    def expiry_date_iso(self, value):
        if not isinstance(value, str):
            raise TypeError('Expecting object of type str')
        self.expiry_date = datetime.fromisoformat(value)

    @property
    def validation_url(self):
        return self._validation_url

    @validation_url.setter
    def validation_url(self, value):
        # FIXME: Should do what's needed to make sure the URL is safe/encoded correctly.
        self._validation_url = value

    @property
    def signature(self):
        if self._signature is None:
            raise InvalidSignatureException
        return self._signature

    @signature.setter
    def signature(self, value):
        # FIXME: Does anything need to be done here?
        #        Should the signature be a "signature" object?
        if not isinstance(value, SignatureBase):
            raise TypeError('Expecting object of type SignatureBase')
        self._signature = value

    def get_data_for_signing(self):
        # This method is to be called to get the JSON data string for signing.
        # NOTE: This JSON data string is sorted and compact.
        # FIXME: This should JSON serialize all of the data values except the signature in preparation for signing
        value = {}
        value['content'] = self.content.get_content_for_license()
        value['creation_date'] = self.creation_date_iso
        value['expiry_date'] = self.expiry_date_iso
        value['validation_url'] = self.validation_url
        return json.dumps(value, sort_keys = True, separators = (',', ':'))

    # The validity should be checked by a handler, not internal to the license, so removing this from the license class
    # def is_license_valid(self):
    #     # FIXME: This should check the signature (and all of the other values) for validity and return True or False
    #     raise NotImplementedError

    def import_data(self, license_data):
        if not isinstance(license_data, str):
            raise TypeError('Expecting object of type str')
        value = json.loads(license_data)
        # FIXME: How to figure out what the Content class should be?
        self.creation_date_iso = value['creation_date']
        self.expiry_date_iso = value['expiry_date']
        self.validation_url = value['validation_url']
        # FIXME: How to figure out what the Signature class should be?
        # FIXME: Should this import method be in the license handler instead?
        #        If so, the export method should probably be moved the license handler also.
        raise NotImplementedError

    def export_data(self):
        # This method is to be called to get the JSON data string containing the entire license.
        # NOTE: This JSON data string is sorted and pretty printed.
        value = {}
        value['content'] = self.content.get_content_for_license()
        value['creation_date'] = self.creation_date_iso
        value['expiry_date'] = self.expiry_date_iso
        value['validation_url'] = self.validation_url
        value['signature'] = self.signature.get_signature_for_license()
        return json.dumps(value, sort_keys = True, indent = 2)
