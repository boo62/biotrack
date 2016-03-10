#!/usr/bin/env python
import sys, os, csv

from biotrack.model import Model

try:
    model_path = os.path.dirname(os.path.abspath(__file__)) + "/" + sys.argv[1]
except IndexError:
    raise IndexError("Requires a '.csv' file as first argument.")
except IOError:
    raise IOError("First argument must be a '.csv' file.")

model = Model(model_path)
print model
print("")
print("Accession Merging:")
model.print_groups()
print("")
print("Annotation Changes:")
model.compare_entries()
