import unittest

from py.test import *
import biotrack


class TestExample(unittest.TestCase):
    def test_pass(self):
        pass

## Ideas for unittests

# Comparison should be between the same species

# Comparisons should be between the same component

# Older version should have older date

# Newer version should have recent date

# We should detect a difference if there is one.

# We should not detect a difference if there isn't one.

# The difference should be in the specified field.

# An entry should not be found if it does not exist.

# An field should found if it is added even if it is not in the previous version


## Ideas for testcases

# One example for which rate constant does change

# One example for which rate constant does not change

# An example where species differs (1 and 1000)

# A larger set of data from the same species say 10, 100, 1000, species.

# A small and large set of data from mixed species.

# A comparison with a very old database

# A comparison with a more recent database
