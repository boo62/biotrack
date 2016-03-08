import os
from biotrack.model import Model

# Try out Model entry comparison
test_path = os.path.dirname(os.path.realpath(__file__))

# 
model_path = (test_path + "/example_models/two_components.csv")
model = Model(model_path)
model.compare_entries()

# Same as current UniProt database
model_most_recent_path = (test_path + "/example_models/two_components_most_recent.csv")
model_most_recent = Model(model_most_recent_path)
model_most_recent.compare_entries()

# In some of these all that has happened is that references have been added ECO.
# Could either split these off or add an option to ignore.
recent_model_path = (test_path + "/example_models/two_components_recent_changes.csv")
recent_model = Model(recent_model_path)
recent_model.compare_entries()


