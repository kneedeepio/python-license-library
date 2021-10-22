#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class SignatureBase:
    # An example of the dictionary that this should get passed or return to the license class:
    #    {
    #      'method': 'HMAC-SHA256',
    #      'value': '0123456789ABCDEF'
    #    }
    # This is to be defined with the signature, signor, and license handler implementations.
    def set_signature_from_license(self, value):
        # The value is supplied as a dict from the license object to this object to instantiate (aka load) the contents
        # of the license into this class.
        # NOTE: This MUST be overridden by the signature class that implements this interface.
        raise NotImplementedError

    def get_signature_for_license(self):
        # The config is returned as a dict from this method to the license object to be included in the license.
        # NOTE: This MUST be overridden by the signature class that implements this interface.
        raise NotImplementedError
