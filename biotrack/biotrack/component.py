# Component class
import re, urllib

class Component(object):

    # Class variables. Make sure that these are always mutable or
    # start as None.
    # Url templates for obtaining past and present UniProt entries.
    OLD_URL = "http://www.ebi.ac.uk/uniprot/unisave/rest/raw/{0}/{1}"
    NEW_URL = "http://www.uniprot.org/uniprot/{0}.txt"
    UNIPROT_ACCESSION = ("[OPQ][0-9][A-Z0-9]{3}[0-9]|" +
                         "[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}")

    def __init__(self, accession, version):
        try:
            assert (re.match(self.UNIPROT_ACCESSION, accession) is not None)
            self.accession = str(accession)
        except AssertionError:
            template = "Accession {} not in UniProt format."
        try:
            self.version = str(int(version))
        except TypeError:
            print("Version {} does not convert to int.".format(version))
            raise
        self.old_entry = None
        self.new_entry = None

        
    def __eq__(self, comp2):
        """Two components are equal if their accessions are
        equivalent."""
        # There a several more possible permutaions here. Not sure if
        # it is worth doing them all
        try:
            return self.accession in comp2.new_entry.accessions
        except TypeError:
            try:
                return comp2.accession in self.new_entry.accessions
            except TypeError:
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
        handle = urllib.urlopen(cls.OLD_URL.format(comp.accession, comp.version))
        self.old_entries.append(SwissProt.read(handle))
 
        
