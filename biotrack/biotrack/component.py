# Component class


class Component(object):

    def __init__(self, accession, version):
        self.accession = accession
        self.version = version
        self.old_entry = None
        self.new_entry = None

    def __eq__(self, comp2):
        """Two components are equal if their accessions are
        equivalent."""
        # There a several more permutaions here. Not sure if it is
        # worth doing them all
        if self.new_entry is not None and comp2.new_entry is not None:
            return self.accession in comp2.new_entry.accessions
        else:
            raise ValueError("Not comparing from new lists of accessions.")
            return self.accession == comp2.accession


    def __str__(self):
        """Return string representation of Component object.

        If the component has old and new UniProt entries, those fields
        are True.
        """
        template ="Component: Acc. {}, Ver. {}, Old = {}, New = {}."
        has_old = (self.old_entry is not None)
        has_new = (self.new_entry is not None)
        return template.format(self.accession, self.version,
                               has_old, has_new) 
            
        
