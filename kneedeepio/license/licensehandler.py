#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class LicenseHandler:
    def __init__(self, license_library_object, license_signor_object):
        self.library = license_library_object
        self.signor = license_signor_object

    def import_license(self, license_data):
        # Use to import a license from an external transport mechanism, such as a file.
        pass

    def export_license(self):
        pass

    def generate_license(self):
        pass

    def validate_license(self):
        # FIXME: This should check the signature (and all of the other values) for validity and return True or False
        pass

    def deactivate_license(self):
        pass

    def enumerate_license(self):
        pass

# The validity should be checked by a handler, not internal to the license, so removing this from the license class
# def is_license_valid(self):
#     # FIXME: This should check the signature (and all of the other values) for validity and return True or False
#     raise NotImplementedError

