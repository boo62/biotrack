import os
from biotrack.model import Model

# Try out Model entry comparison
test_path = os.path.dirname(os.path.realpath(__file__))
model_path = (test_path + "/example_models/two_components.csv")

model = Model(model_path)
model.compare_entries()

model_most_recent_path = (test_path + "/example_models/two_components_most_recent.csv")
model_most_recent = Model(model_most_recent_path)
model_most_recent.compare_entries()
