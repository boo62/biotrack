"""Retrieve a specified field given a UniProt accession"""
import urllib

from Bio import SwissProt

from model import Model

URL = "http://www.ebi.ac.uk/uniprot/unisave/rest/raw/"

def write_entry(url, filename):
    with urllib.urlopen(URL + url) as handle:
        record1 = SwissProt.read(handle)




        
url_old = "P94465/79"
url_new = "P94465/97"

url_ribE_new = "P16440/126"
url_new_ribE = "http://www.uniprot.org/uniprot/P16440.txt"
# p53 is not an enzyme and has functional annotations in the same place Record.comments
# There is a very long list so a diff is necesssary to determine what is new and what is not.
p53 = "http://www.uniprot.org/uniprot/P04637.txt"

#handle1 = urllib.urlopen(URL + url_ribE_new)
print "old"
handle_old = urllib.urlopen(URL + url_old)
record_old = SwissProt.read(handle_old)
print type(record_old)
print record_old.created
print record_old.sequence_update
print record_old.annotation_update

print "new"
handle_new = urllib.urlopen(URL + url_new)
record_new = SwissProt.read(handle_new)
print type(record_new)
print record_new.created
print record_new.sequence_update
print record_new.annotation_update

print record_new.comments

#print record.annotation_update
#print record.description
#print record.features
#print record.taxonomy_id
#print record1.accessions

# for comment in record1.comments:
#    print comment
#could match FUNCTION: with a regular expression
    
    #print record.comments[0]
#print("hello")
# Test out UniSaves's RESTful Web-Services on ribR in B. subtilis
# http://www.ebi.ac.uk/uniprot/unisave/rest/raw/Q00001/79

# Find the given UniProtKB-AC in a version of the uniprot database.
# Retrieve a field from the accession, or if it does not exist
# determine so.
# Do this for rate constant to begin with.







