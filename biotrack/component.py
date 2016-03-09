# Component class
import re, urllib

from Bio import SwissProt

from biotrack.fields import Fields


class Component(object):

    # Class variables. Make sure that these are always immutable or
    # start as None.
    # Url templates for obtaining past and present UniProt entries.
    OLD_URL = "http://www.ebi.ac.uk/uniprot/unisave/rest/raw/{0}/{1}"
    NEW_URL = "http://www.uniprot.org/uniprot/{0}.txt"
    # UniProt accession regex
    UNIPROT_ACCESSION = ("[OPQ][0-9][A-Z0-9]{3}[0-9]|" +
                         "[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}")


    def __init__(self, accession, version):
        # Accession should be in Uniprot format. Version should exist
        # in UniSave.
        try:
            assert (re.match(self.UNIPROT_ACCESSION, accession) is not None)
            self.accession = str(accession)
        except AssertionError:
            template = "Accession '{}' not in UniProt format."
            print(template.format(accession))
            self.accession = str(accession)
        # Version should be an integer or string representation of an
        # integer.
        try:
            # Cannot int the str of a float.
            int(str(version))
            self.version = str(version)
        except ValueError:
            print("Version '{}' is not an integer.".format(version))
        self.old_entry = None
        self.new_entry = None

    
    
    def __eq__(self, comp2):
        """Test equivalance of Components by accession.

        Return True if both Components accessions refer to the same
        protein. Otherwise return False.

        Try first to compare accessions in most recent UniProt entries
        (new_entry attributes). If neither component has a new_entry
        attribute compare accession attributes and print a warning.

        """
        # There a several more possible permutaions here. Not sure if
        # it is worth doing them all
        try:
            return self.accession in comp2.new_entry.accessions
        except AttributeError:
            try:
                return comp2.accession in self.new_entry.accessions
            except AttributeError:
                print ("Not comparing from new lists of accessions. "
                       "Instead compare self.accession")
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

    
    def fetch_old_entry(self):
        handle = urllib.urlopen(self.OLD_URL.format(self.accession, self.version))
        return SwissProt.read(handle)

    
    def fetch_new_entry(self):
        handle = urllib.urlopen(self.NEW_URL.format(self.accession))
        return SwissProt.read(handle)


    # Compare SwissProt.Record comments using Fields objects.
    def compare_entry_fields(self):
        """Return Fields object containing changes."""
        old = Fields(self.old_entry.comments)
        new = Fields(self.new_entry.comments)
        return new - old
    
        
    # Do diff between a field in new and old entries.
    def diff_field(self, field):
        # old = self.old_entry.comments
        # new = self.new_entry.comments
        pass


    # Greater than of equal based on version number or date. 
    def __ge__(self, comp2):
        pass
 

# A Component subclass which automatically retrieves UniProt Entries
# on instantiation.
class AutoComponent(Component):
    """Component subclass which retrieves UniProt entries on instantiation."""

    def __init__(self, accession, version):
        # Call Component (super)  __init__.
        super(AutoComponent, self).__init__(accession, version)
        # Fetch the UniProt entries on instantiation
        self.old_entry = self.fetch_old_entry()
        self.new_entry = self.fetch_new_entry()
