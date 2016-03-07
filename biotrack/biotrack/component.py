# Component class


class Component(object):

    def __init__(self, accession, version):
        self.accession = accession
        self.version = version
        self.old_entry = None
        self.new_entry = None

    def __eq__(self):
        """Two components are equal if their accessions are equivalent."""
        pass
        
