from biotrack.fields import Fields
from component import Component, AutoComponent


a_dict = {"one": 1, "two": 2, "a_list": [1, 2]}
print a_dict


a_list = range(10)
print a_list

comments = [
    "FUNCTION: Lays eggs. {ECO:0000269|PubMed:6766130}.",
    "SIMILARITY: Goose. {ECO:0000255|PROSITE-ProRule:PRU00524}.",
     ]


a_field = Fields(comments)
print a_field


c1 = Component("5", "4")
c2 = Component("5", "3")

c_set = set([c1, c2])
print c_set
print c1 == c2
