"""Class for retrieving and comparing new and old model components."""
from Bio import SwissProt
import urllib
import csv

from component import Component



class Model2(object):
    """Class containing model components and UniProt entries."""
    # Class variables. Make sure that these are always mutable or
    # start as None.
    # Url templates for obtaining past and present UniProt entries.
    OLD_URL = "http://www.ebi.ac.uk/uniprot/unisave/rest/raw/{0}/{1}"
    NEW_URL = "http://www.uniprot.org/uniprot/{0}.txt"

    def __init__(self, filename):
        """Parse model from file and collect new and old UniProt entries.

        The file should be .csv fromat:
        UniProt_accession, entry_version, ...
        where ... are any number of other fields, for instance protein
        name, which are ignored by the parser.
        """
        # List of model Component objects
        self.components = self.parse_accessions(filename)
        # Lists of SwissProt.Record objects
        self.old_entries = self.fetch_old_entries()
        self.new_entries = self.fetch_new_entries()

    
    def parse_accessions(self, filename):
        """Read in a list of UniProt accessions with entry versions."""
        with open(filename, 'r') as f:
            component_reader = csv.reader(f, skipinitialspace=True)
            components = [Component(row[0], row[1]) for row in component_reader]
            return components


    def fetch_old_entries(self):
        """Obtain the past UniProt entries of model components."""
        old_entries = []
        for comp in self.components:
            handle = urllib.urlopen(self.OLD_URL.format(comp.accession, comp.version))
            old_entries.append(SwissProt.read(handle))
        return old_entries


    def fetch_new_entries(self):
        """Obtain the present UniProt entries of model components."""
        new_entries = []
        for comp in self.components:
            handle = urllib.urlopen(self.NEW_URL.format(comp.accession))
            new_entries.append(SwissProt.read(handle))
        return new_entries

    
    def same_accessions(self):
        """Determine whether any components are the same.

        I.e. if both accessions appear in the same UniProt entry.
        """
        pass
        
    def compare_entries(self, field):
        """Find differeces in a field between new and old entries."""
        pass


    def compare_entry_comments(self, old_record, new_record):
        old_comments = old_record.comments
        print old_comments[0]
        new_comments = new_record.comments
        print new_comments[0]


class Model(object):
    """Class containing model components and UniProt entries."""
    # Class variables. Make sure that these are always mutable or
    # start as None.
    # Url templates for obtaining past and present UniProt entries.
    OLD_URL = "http://www.ebi.ac.uk/uniprot/unisave/rest/raw/{0}/{1}"
    NEW_URL = "http://www.uniprot.org/uniprot/{0}.txt"

    def __init__(self, filename):
        """Parse model from file and collect new and old UniProt entries.

        The file should be .csv fromat:
        UniProt_accession, entry_version, ...
        where ... are any number of other fields, for instance protein
        name, which are ignored by the parser.
        """
        # List of model Component objects
        self.components = self.parse_accessions(filename)
        # Lists of SwissProt.Record objects
        self.old_entries = self.fetch_old_entries()
        self.new_entries = self.fetch_new_entries()

    
    def parse_accessions(self, filename):
        """Read in a list of UniProt accessions with entry versions."""
        with open(filename, 'r') as f:
            component_reader = csv.reader(f, skipinitialspace=True)
            components = [Component(row[0], row[1]) for row in component_reader]
            return components


    def fetch_old_entries(self):
        """Obtain the past UniProt entries of model components."""
        old_entries = []
        for comp in self.components:
            handle = urllib.urlopen(self.OLD_URL.format(comp.accession, comp.version))
            old_entries.append(SwissProt.read(handle))
        return old_entries


    def fetch_new_entries(self):
        """Obtain the present UniProt entries of model components."""
        new_entries = []
        for comp in self.components:
            handle = urllib.urlopen(self.NEW_URL.format(comp.accession))
            new_entries.append(SwissProt.read(handle))
        return new_entries

    
    def same_accessions(self):
        """Determine whether any components are the same.

        I.e. if both accessions appear in the same UniProt entry.
        """
        pass
        
    def compare_entries(self, field):
        """Find differeces in a field between new and old entries."""
        pass


    def compare_entry_comments(self, old_record, new_record):
        old_comments = old_record.comments
        print old_comments[0]
        new_comments = new_record.comments
        print new_comments[0]


if __name__ == "__main__":
    model_1 = Model("../tests/example_models/two_components.csv")
    model_1.compare_entry_comments(model_1.old_entries[0],
                                   model_1.new_entries[0])
