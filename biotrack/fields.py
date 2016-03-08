# Fields object to hold the comments section of a Bio.UniProt.Record
# object in more convenient and manipulatable data structures. Parses
# comments as field_set and field_dict attributes of Fields. 

import re


class Fields(object):

    # get comments into a dictionary.
    def __init__(self, comments):
        # A set of fields so can do comparisions using union and
        # intersection. Can then give new and old Comments attributes
        # to Components.
        # Fields as a dictionary (or nested dictionary).
        # split(s, sep=":", maxsplit=1)
        fields = self.parse_comments(comments)
        self.field_set = fields[0]
        self.field_dict = fields[1]

    def parse_comments(self, comments):
        # Keep fields as uppercase in case we want to compare back with
        # UniProt.Record.comments
        comments = [str.split(comment, ":", 1) for comment in comments]
        comments = [(comment[0], str.strip(comment[1])) for comment in comments]
        fields = [comment[0] for comment in comments]
        return set(fields), dict(comments)
        
