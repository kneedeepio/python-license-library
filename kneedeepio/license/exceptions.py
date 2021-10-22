#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class KneeDeepIOLicenseException(Exception):
    pass

# License Exceptions
class InvalidAssigneeException(KneeDeepIOLicenseException):
    pass

class InvalidContentException(KneeDeepIOLicenseException):
    pass

class InvalidExpiryDateException(KneeDeepIOLicenseException):
    pass

class InvalidSignatureException(KneeDeepIOLicenseException):
    pass

# Cache Exceptions
