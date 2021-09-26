#!/usr/bin/env python3

### IMPORTS ###

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class CacheBase:
    def insert_license(self, assignee, value):
        # Insert a license into the cache mechanism keyed on assignee for rapid use later.
        # NOTE: This MUST be overridden by the cache class that implements this interface.
        raise NotImplementedError

    def check_for_licenses(self, assignee):
        # Check to see if assignee has any license in the cache.
        # NOTE: This MUST be overridden by the cache class that implements this interface.
        raise NotImplementedError
