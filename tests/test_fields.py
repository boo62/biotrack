import unittest

from biotrack.component import Component
from biotrack.fields import Fields


class TestField(unittest.TestCase):

    def setUp(self):
        """Load a pickled AutoComponent as a test case."""
        # Test on the components field of a UniProt entry of a pickled
        # AutoComponent test case.
        PICKLE_DIR = (os.path.dirname(os.path.realpath(__file__))
                      + "/pickled_testcases/")
        with open(PICKLE_DIR + "P94465_ac_pickle.txt", 'r') as f:
            auto_comp = pickle.load(f)
        self.comments_old = auto_comp.old_entry.components
        self.comments_new = auto_comp.new_entry.components


    def tearDown(self):
        self.comments_old = None
        self.comments_new = None
