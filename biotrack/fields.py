"""Class to contain annotation information on a model component."""


class Fields(object):
    """Parses a SwissProt.Record.comments from a list to a dictionary.

    Dictionary is stored as the attribute field_dict. Provides methods
    for manipulating, comparing, and printing the fields.
    """
    # Alternatively, I could just have a parser method in Component
    # and use dictionaries, or I could look into subclassing the base
    # python dict object.
    
    def __init__(self, comments=None):
        """Parse comments to a dictionary if given.

        Comments is expected in Bio.SwissProt.Records.comments format
        in order for methods to work.
        
        Attributes: 
        field_dict

        field_dict is a dictionary represtation of a
        Bio.SwissProt.Records.comments attribute for easier
        manipulation.

        """
        # Could add code to raise error if comments is not in expected
        # format.
        if comments is not None:
            self.field_dict = self.parse_comments(comments)

            
    def parse_comments(self, comments):
        """Parse SwissProt.Record.comments to a dictionary."""
        # Keep fields as uppercase in case we want to compare back with
        # UniProt.Record.comments
        comments = [str.split(comment, ":", 1) for comment in comments]
        comments = [(str.strip(comment[0]), str.strip(comment[1])) for
                    comment in comments]
        return dict(comments)
        


    def __eq__(self, fields2):
        """Return True if the field_dicts of two Fields are equal."""
        return (self.field_dict == fields2.field_dict)

    
    def __sub__(self, other):
        """Return a Fields object containing differences.

        Differences are (currently) new fields or changed field values
        but not removed fields. If there are no differnces returns
        None.

        """
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
            
        
