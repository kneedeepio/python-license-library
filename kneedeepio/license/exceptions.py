#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class KneeDeepIOLicenseException(Exception):
    pass

# Content Exceptions
class NoContentException(KneeDeepIOLicenseException):
    pass

class InvalidContentException(KneeDeepIOLicenseException):
    pass

# Signature Exceptions
class InvalidSignatureException(KneeDeepIOLicenseException):
    pass

# Cache Exceptions
