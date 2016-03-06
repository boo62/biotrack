"""Class for retrieving and comparing new and old model components."""
import Bio
import urllib

# Could potentially hold the entries in a biopython object, presumably
# one exists, rather than writing to file.
# Could probably also retreive only the relevent field rather than
# doing all of the initial setup.
class Model(object):
    """Class containing model components, versions, and accessions."""
    def __init__(self, new_filename, old_filename):
        # self.components = self.parse_accessions(filename)
        # self.new_entries = self.fetch_new_entries(new_filename)
        # self.old_entries = self.fetch_old_entries(old_filename)
        pass

    
    def parse_accessions(self, filename):
        """Read in a list of UniProt accessions with entry versions."""
        pass


    def fetch_old_entries(self, filename):
        """Obtain the past UniProt entries of model components.

        Write these to file for later comparison.
        """
        # handle = urllib.urlopen("http://www.somelocation.org/data/someswissprotfile.dat")

        # with open(filename, 'a') as f:
        pass


    def fetch_new_entries(self, filename):
        """Obtain the present UniProt entries of model components.

        Write these to file for later comparison.
        """
        # with open(filename, 'a') as f:
        pass

    
    def compare_entries(self, field):
        """Find differeces in a field between new and old entries."""
        pass


