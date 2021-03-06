#!/usr/bin/env python2

from AWSScout2.finding import *

class S3Finding(Finding):

    def __init__(self, description, entity, callback, callback_args, level, questions):
        self.keyword_prefix = 's3'
        Finding.__init__(self, description, entity, callback, callback_args, level, questions)

    def checkWorldWritableBucket(self, key, obj):
        for grant in obj['grants']:
            if 'All users' in grant:
                if obj['grants']['All users']['write']:
                    self.addItem(key)

    def checkWorldWritableBucketPerms(self, key, obj):
        for grant in obj['grants']:
            if 'All users' in grant:
                if obj['grants']['All users']['write_acp']:
                    self.addItem(key)


    def checkWorldReadableBucket(self, key, obj):
        for grant in obj['grants']:
            if 'All users' in grant and obj['grants']['All users']['read']:
                self.addItem(key)

    def checkLogging(self, key, obj):
        if obj['logging'] == 'Disabled':
            self.addItem(key)

    def checkWebhosting(self, key, obj):
        if obj['web_hosting'] == 'Enabled':
            self.addItem(key)
