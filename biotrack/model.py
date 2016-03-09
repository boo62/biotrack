"""Class for retrieving and comparing new and old model components."""
import urllib
import csv
import itertools

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
        old_entry (Bio.SwissProt.Record)
        new_entry (Bio.SwissProt.Record)
        
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

        
    def compare_accessions(self, group_as="comps"):
        """Determine whether any components are the same.

        Group components whose accessions refer to the same
        protein. Groups are returned as list of sets of Component
        objects. Returns an empty list if no groups are present.

        """
        # Store components that have already been grouped.
        grouped = []
        # Groups of Component objects.
        groups = []
        # Groups of Component accessions.
        group_accs = []
        for comp in self.components:
            if comp not in grouped:
                group = filter(comp.__eq__, self.components)
                # Do not want matches to self.
                if len(group) >= 2:
                    grouped += group
                    accessions = [comp.accession for comp in group]
                    # Group of component accessions.
                    group_accs.append(set(accessions))
                    # Group of Component objects.
                    groups.append(set(group))
        if group_as == "accs":
            return group_accs
        elif group_as == "comps":
            return groups
        
        
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
