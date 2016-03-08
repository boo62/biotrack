# Fields object to hold the comments section of a Bio.SwissProt.Record
# object in more convenient and manipulatable data structures. Parses
# comments as field_set and field_dict attributes of Fields. 


class Fields(object):

    # get comments into a dictionary.
    def __init__(self, comments=None):
        # A set of fields so can do comparisions using union and
        # intersection. Can then give new and old Comments attributes
        # to Components.
        # Fields as a dictionary (or nested dictionary).
        # split(s, sep=":", maxsplit=1)
        if comments is not None:
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
        

    # Compare if the fields of two Fields are equal.
    # Sets are dicts are both equal.
    def __eq__(self, fields2):
        sets_equal = (self.field_set == fields2.field_set)
        dicts_equal = (self.field_dict == fields2.field_dict)
        return sets_equal and dicts_equal

    
    # Subtract to Fields objects.
    def __sub__(self, other):
        """Return a Fields object containing differences.

        Differences are new fields or changed field values but
        not removed fields. If there are no differnces returns None.
        """
        # Do I need to check if other is a Field or let it fail?
        if self == other:
            return None
        else:
            # Need to test not only if fields are new but if fields
            # have changed. Does not test removed fields.
            # Find new fields.
            new = self.field_set - other.field_set
            # Find common fields whose values have changed.
            common = self.field_set & other.field_set
            changed = [field for field in common if
                       self.field_dict[field] != other.field_dict[field]]
            # Attributes for Fields object containing the changes
            new_field_set = set(changed) | new
            new_field_dict = {k: self.field_dict[k] for k in new_field_set}
            # Create Fields object containing the changes.
            dif = Fields()
            dif.field_set = new_field_set
            dif.field_dict = new_field_dict
            return dif

    
    def __str__(self):
        """Return string representation of Fields object."""
        str_list = []
        for field, value in self.field_dict.iteritems():
            str_list.append(field + ": " + value)
        str_list.sort()
        return "\n".join(str_list)
            
        
