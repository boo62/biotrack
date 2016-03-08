import re


class Fields(object):

    # get comments into a dictionary.
    def __init__(comments):
        # A set of fields so can do comparisions using union and
        # intersection. Can then give new and old Comments attributes
        # to Components.
        # Fields as a dictionary (or nested dictionary).
        # split(s, sep=":", maxsplit=1)
        fields = parse_comments(comments)
        self.field_set = fields[0]
        self.field_dict = fields[1]

    def parse_comments(self, comments):
        comments = [split(comment, sep=":", maxsplit=1) for comment in comments]
        fields = [str.lower(comment[0]) for comment in comments]
        return set(fields), dict(comments)
        
