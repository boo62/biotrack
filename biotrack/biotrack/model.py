"""Class for retrieving and comparing new and old model components."""
from Bio import SwissProt
import urllib
import csv

# Could potentially hold the entries in a biopython object, presumably
# one exists, rather than writing to file.
# Could probably also retreive only the relevent field rather than
# doing all of the initial setup.
class Model(object):
    """Class containing model components, versions, and accessions."""
    def __init__(self, filename):
        self.components = self.parse_accessions(filename)
        # self.new_entries = self.fetch_new_entries()
        # self.old_entries = self.fetch_old_entries()
        self.OLD_URL = "http://www.ebi.ac.uk/uniprot/unisave/rest/raw/{0}/{1}"
        self.NEW_URL = "http://www.uniprot.org/uniprot/{0}.txt"
        self.old_records = self.fetch_old_entries()

    
    def parse_accessions(self, filename):
        """Read in a list of UniProt accessions with entry versions."""
        with open(filename, 'r') as f:
            component_reader = csv.reader(f, skipinitialspace=True)
            components = [(row[0], row[1]) for row in component_reader]
            return components


    def fetch_old_entries(self):
        """Obtain the past UniProt entries of model components.

        Write these to file for later comparison.
        """
        old_records = []
        for comp in self.components:
            handle = urllib.urlopen(self.OLD_URL.format(comp[0], comp[1]))
            old_records.append(SwissProt.read(handle))
        return old_records


    def fetch_new_entries(self):
        """Obtain the present UniProt entries of model components.

        Write these to file for later comparison.
        """
        # with open(filename, 'a') as f:
        pass

    
    def compare_entries(self, field):
        """Find differeces in a field between new and old entries."""
        pass


