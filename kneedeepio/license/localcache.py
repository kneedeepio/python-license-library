#!/usr/bin/env python3

### IMPORTS ###
from kneedeepio.license.cachebase import CacheBase

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class LocalCache(CacheBase):
    def __init__(self, num_assignees = 300, num_license_per_assignee = 30):
        self._num_assignees = num_assignees
        self._num_license_per_assignee = num_license_per_assignee
        self._cache = {}

    def insert_license(self, assignee, value):
        # FIXME: Do the following:
        #        - Check if assignee is in dict.  If not:
        #          - Check if assignee dict is full.  If so, remove the assignee with the oldest last use time.
        #          - Create assignee with license list and last use time.
        #        - Insert license into assignee license list and update last use time.
        raise NotImplementedError

    def check_for_licenses(self, assignee):
        # FIXME: Do the following:
        #        - Check if assignee is in dict. If not, return empty list.
        #        - Return list of licenses for the assignee.
        raise NotImplementedError
