"""Retrieve a specified field given a UniProt accession"""
import urllib

from Bio import SwissProt

from model import Model

URL = "http://www.ebi.ac.uk/uniprot/unisave/rest/raw/"

def write_entry(url, filename):
    with urllib.urlopen(URL + url) as handle:
        record1 = SwissProt.read(handle)
        with open(filename, 'w') as f:
            pass



        
url_old = "P94465/79"
url_new = "P94465/97"

url_ribE_new = "P16440/126"
url_new_ribE = "http://www.uniprot.org/uniprot/P16440.txt"

handle1 = urllib.urlopen(url_new_ribE)
record1 = SwissProt.read(handle1)

#print record.annotation_update
#print record.description
#print record.features
#print record.taxonomy_id
print record1.accessions
for comment in record1.comments:
    print comment
# could match FUNCTION: with a regular expression
    
    #print record.comments[0]
#print("hello")
# Test out UniSaves's RESTful Web-Services on ribR in B. subtilis
# http://www.ebi.ac.uk/uniprot/unisave/rest/raw/Q00001/79

# Find the given UniProtKB-AC in a version of the uniprot database.
# Retrieve a field from the accession, or if it does not exist
# determine so.
# Do this for rate constant to begin with.







