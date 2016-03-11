# Trow away script to look at the output from Model methods.
import os, pickle
from biotrack.model import Model


# Try out Model entry comparison
test_path = os.path.dirname(os.path.realpath(__file__))

# Two component rib old entries
model_path = (test_path + "/example_models/two_components.csv")
model = Model(model_path)
model.print_groups()

# # Same as current UniProt database
# model_most_recent_path = (test_path + "/example_models/two_components_most_recent.csv")
# model_most_recent = Model(model_most_recent_path)
# model_most_recent.compare_entries()

# # In some of these all that has happened is that references have been added ECO.
# # Could either split these off or add an option to ignore.
# recent_model_path = (test_path + "/example_models/two_components_recent_changes.csv")
# recent_model = Model(recent_model_path)
# recent_model.compare_entries()

# Three p53 accessions, two rhodopsin accesssoins and two other proteins.
# groups_model_path = (test_path +
#                      "/example_models/two_groups_same_protein.csv")
# groups_model = Model(groups_model_path)
# With pickle
groups_pickle_path = (test_path +
                      "/pickled_testcases/two_groups_same_protein_pickle.txt")
with open(groups_pickle_path, 'r') as f:
    groups_model = pickle.load(f)
#Groupsco_model.compare_entries()
groups_model.print_groups()


