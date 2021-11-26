#!/usr/bin/env python3

### IMPORTS ###
from kneedeepio.license.signaturebase import SignatureBase
from kneedeepio.license.exceptions import InvalidSignatureException

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class SignatureSHA256(SignatureBase):
    # An example of the dictionary that this should get passed or return to the license class:
    #    {
    #      'method': 'HMAC-SHA256',
    #      'value': '0123456789ABCDEF'
    #    }
    # This is to be defined with the signature, signor, and license handler implementations.
    _value: str

    def __init__(self):
        self._value = ""

    def __eq__(self, other):
        if not isinstance(other, SignatureSHA256):
            return NotImplemented
        return self.value == other.value

    @property
    def value(self):
        # FIXME: Should this raise an error if value is not set?
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not len(value) == 64:
            raise ValueError
        self._value = value

    def set_signature_from_license(self, value):
        # The value is supplied as a dict from the license object to this object to instantiate (aka load) the contents
        # of the license into this class.
        if not value["method"] == "SHA256":
            raise InvalidSignatureException
        self.value = value["value"]

    def get_signature_for_license(self):
        # The config is returned as a dict from this method to the license object to be included in the license.
        return {"method": "SHA256", "value": self.value}