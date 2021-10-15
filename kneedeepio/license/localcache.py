#!/usr/bin/env python3

### IMPORTS ###
import datetime

from kneedeepio.license.license import License
from kneedeepio.license.cachebase import CacheBase

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class LocalCache(CacheBase):
    def __init__(self, num_assignees = 300, num_license_per_assignee = 30):
        self._num_assignees = num_assignees
        self._num_license_per_assignee = num_license_per_assignee
        self._cache = { }

    def insert_license(self, assignee, value):
        # Check if the value is an actual license
        if not isinstance(value, License):
            raise ValueError # FIXME: Make a more specific exception
        # Check if assignee is in dict.  If not:
        if str(assignee) not in self._cache:
            # Check if assignee dict is full.  If so, remove the assignee with the oldest last use time.
            if len(self._cache) > self._num_assignees:
                # Find the oldest assignee and remove it
                # FIXME: do this part
                pass
            # Create assignee with license list and last use time.
            self._cache[str(assignee)] = { 'last_used': datetime.Datetime.utcnow(), 'licenses': [] }
        # Check if license list is full.
        if len(self._cache[str(assignee)]['licenses']) > self._num_license_per_assignee:
            # Find the oldest license and remove it
            # FIXME: do this part
            pass
        # Insert license into assignee license list and update last use time.
        self._cache[str(assignee)]['last_used'] = datetime.Datetime.utcnow()
        self._cache[str(assignee)]['licenses'].append(value)

    # FIXME: Should there be an insert_license_list?

    def check_for_licenses(self, assignee):
        # FIXME: Do the following:
        #        - Check if assignee is in dict. If not, return empty list.
        #        - Return list of licenses for the assignee.
        if str(assignee) in self._cache:
            return self._cache[str(assignee)]['licenses']
        return []
