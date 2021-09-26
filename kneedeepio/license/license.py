#!/usr/bin/env python3

### IMPORTS ###
import datetime

from kneedeepio.license.contentbase import ContentBase

from kneedeepio.license.exceptions import NoContentException, InvalidContentException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class License:
    def __init__(self):
        self._content = None
        self._creation_date = datetime.Datetime.utcnow()
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
            raise InvalidContentException
        self._content = value

    @property
    def creation_date(self):
        # FIXME: Should this and other values be validated here?
        #        Should a creation date newer than expiry be allowed?
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        # FIXME: This should check for datetime, and if not datetime, try to convert
        if not isinstance(value, datetime.Datetime):
            raise ValueError # FIXME: This should try to convert to datetime
        self._creation_date = value

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        if not isinstance(value, datetime.Datetime):
            raise ValueError # FIXME: This should try to convert to datetime
        if value < self.creation_date:
            # Don't allow the expiry date to be older than the creation_date
            raise ValueError # FIXME: Make a better exception for this
        self._expiry_date = value

    @property
    def validation_url(self):
        return self._validation_url

    @validation_url.setter
    def validation_url(self, value):
        # FIXME: Should do what's needed to make sure the URL is safe/encoded correctly.
        self._validation_url = value

    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        # FIXME: Does anything need to be done here?
        #        Should the signature be a "signature" object?
        self._signature = value

    def get_data_for_signing(self):
        # FIXME: This should serialize all of the data from the other values in preparation for signing
        raise NotImplementedError

    def is_license_valid(self):
        # FIXME: This should check the signature (and all of the other values) for validity and return True or False
        raise NotImplementedError

    def import_data(self, license_data):
        # FIXME: This should deserialize the license data into the component fields
        raise NotImplementedError

    def export_data(self):
        # FIXME: This should serialize all of the data from all of the values for exporting to an external transport
        #        mechanism.
        raise NotImplementedError
