"""Class for retrieving and comparing new and old model components."""
import urllib
import csv

from Bio import SwissProt

from component import AutoComponent


class Model(object):
    """Class containing model components and UniProt entries."""

    def __init__(self, filename):
        """Parse model from file and collect new and old UniProt entries.

        The file should be in .csv format:
        UniProt_accession, entry_version, ...
        where ... are any number of other fields, for instance protein
        name, which are ignored by the parser.

        Components are stored as a list of AutoComponent objects which
        have the following attributes:
        accession
        version
        old_entry (Bio.UniProt.Record)
        new_entry (Bio.UniProt.Record)
        
        The past and most recent UniProt entries are retrieved
        automatically through AutoComponent instantiation.
        """
        # List of model AutoComponent objects
        self.components = self.parse_components(filename)
      
    
    def parse_components(self, filename):
        """Read file and return a list of AutoComponent objects.

        The file should be in .csv format:
        UniProt_accession, entry_version, ...
        where ... are any number of other fields, for instance protein
        name, which are ignored by the parser.
        """
        with open(filename, 'r') as f:
            component_reader = csv.reader(f, skipinitialspace=True)
            components = [AutoComponent(row[0], row[1]) for row in component_reader]
        return components

        
    def same_accessions(self):
        """Determine whether any components are the same.

        I.e. If accessions give the same protein.
        """
        pass
        
    def compare_entries(self):
        """Find differeces in a field between new and old entries."""
        difs = []
        for component in self.components:
            acc = component.accession
            name = component.new_entry.gene_name
            changes = component.compare_entry_fields()
            print acc
            print name
            print changes


    def compare_entry_comments(self, old_record, new_record):
        pass


if __name__ == "__main__":
    model_1 = Model("../tests/example_models/two_components.csv")
