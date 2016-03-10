# Fields object to hold the comments section of a Bio.SwissProt.Record
# object in more convenient and manipulatable data structures. Parses
# comments as field_set and field_dict attributes of Fields. 


# Parses a SwissProt.Record.comments from a list to a dictionary which
# is stored as the attribute field_dict. Provides methods for
# manipulating, comparing, and printing the fields in the comments
# attribute of a SwissProt.Record. Alternatively, could just have a
# parser method in Component and use dictionaries.
class Fields(object):

    # get comments into a dictionary.
    def __init__(self, comments=None):
        # A set of fields so can do comparisions using union and
        # intersection. Can then give new and old Comments attributes
        # to Components.
        # Fields as a dictionary (or nested dictionary).
        # split(s, sep=":", maxsplit=1)
        if comments is not None:
            self.field_dict = self.parse_comments(comments)
            
    def parse_comments(self, comments):
        # Keep fields as uppercase in case we want to compare back with
        # UniProt.Record.comments
        comments = [str.split(comment, ":", 1) for comment in comments]
        comments = [(str.strip(comment[0]), str.strip(comment[1])) for comment in comments]
        return dict(comments)
        

    # Compare if the fields of two Fields are equal.
    # Sets are dicts are both equal.
    def __eq__(self, fields2):
        return (self.field_dict == fields2.field_dict)

    
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
            new = set(self.field_dict.keys()) - set(other.field_dict.keys())
            # Find common fields whose values have changed.
            common = set(self.field_dict.keys()) & set(other.field_dict.keys())
            changed = [field for field in common if
                       self.field_dict[field] != other.field_dict[field]]
            # Attributes for Fields object containing the changes
            updated_fields = set(changed) | new
            updated_dict = {k: self.field_dict[k] for k in updated_fields}
            # Create Fields object containing the changes.
            dif = Fields()
            dif.field_dict = updated_dict
            return dif

    
    def __str__(self):
        """Return string representation of Fields object."""
        str_list = []
        # Should test if attributes exist.
        for field, value in self.field_dict.iteritems():
            str_list.append(field + ": " + value)
        str_list.sort()
        return "\n".join(str_list)
            
        
