========
biotrack
========

Track changes to components of a biological model in UniProt.


The Problem
-----------

If an author has many models, it may be hard to keep track of the literature for
all of them, or some of them may be abandoned. An author may revisit a model
after several years or it may be picked up by another researcher. It would be
useful to see whether there have been any developments which might be used to
revise the model, without having to trawl through databases for all of the
components.

Suggested Usage
---------------

At the time that a component or parameter for a component is used in a
model, a user the version number of the database is saved allowing
access to the past state of the database at some future
time. Alternatively, the entry for that component is downloaded and
saved in a compressed format.

* Given a list of model components and accessions, or simply the compressed past
  entries, the present entries for each component is obtained.

* A user specifies which fields (e.g. rate constant, function, expression and
  regulation) they want to compare for a given component, and any differences
  between the past and present versions are shown.

* This doesn't necessitate that the components are part of a model
  (i.e. anything written in SMBL, CellML, etc.,), that is just a suggested
  use.

* At first I will just try to do this for rate constants in UniProt. However, it
  would probably be more useful to track function, expression, regulation,
  and changes in pathway databases.


How to install
--------------

biotrack is available as a Python package. Istallation requires
setuptools and is tested for Python 2.7.6 and higher.

Uncompress the tar.gz file and cd inside it. (If you are reading this
you probably already have.)

To run tests before installing

  python setup.py test

To install

  python setup.py install

To see that biotrack (0.1) is installed.
 
  pip list

To uninstall
------------

  pip uninstall biotrack


Requirements
------------

Hopefully the dependencies will be handled in the installation.
Insallation requires setuptools.

requirements.txt gives a list of packaged used in the development environment.

To install these:

 pip intall requirements.txt

Run modcomp
-----------

Once installed you can run the script modcomp on the example models
provided.

 cd tests/example_models/

 modcomp <filename>

This compares past UniProt entries of proteins in the model file to the
current entries in the UniProt database. It will tell you whether any
function annotations have changed or been updated and if so will print
the updated fields. A check is also performed to see if any accessions
have merged and if so the groups are printed.
 
Model files should be in .csv format.

 UniProt accession, version, other fields...

Other fields are ignored by the parser.

To see examples of both behaviours I suggest you run modcomp on the
following two example models.

 two_components.csv

 two_groups_same_protein.csv

The second model contains some very old entries p53 entries and so
spews out a long list of annotation changes. What we are interested in
is the merging of groups of the same protein at the end of the output.
 
Issues:
-------


* Currently no exception handling for non-existant UniProt entries.
  
  - Future and non-existant versions will cause a crash.
  
  - It will crash if an accession is in valid UniProt format but does
    not exist on the database.



* Very old entries.

  - You cannot use a secodary accession to retrieve a UniSave entry after
    merging. UniSave entries before merging and the current
    http://www.uniprot.org/ entry can be retrieved with a secondary
    accession. TrEMBLE entries will generally parse with
    SwissProt.read() but I have found an example where a very old ribE
    entry raises AssertionError: Missing braces. Hopefully UniProt
    formats are now stable and error free and will parse for anyone
    beginning to record accessions and versions. The model file
    containing the failing accession is "two_ribE_accessions.csv".


Ideas for future releases
-------------------------

* Use difflib to find diffs between fields rather than just spitting
  out the entire field. Sometimes all that has changed with a field is
  that a reference has been added.

* Compare by GO (Gene Ontology). A Bio.SwissProt.Record object does
  not contain any GO terms. Use an alternative method to retreive
  these from UniProt.

* There should be an option to return an updated model file with the
  latest entry versions.

* Make it interactive. It should be possible to specify for which
  fields of the SwissProt.Record.comments list a user wants to view
  changes. This will require fecthing the records first and then
  giving a list of options to the user.

* Django implementation. This could tell the user if any proteins have
  merged and provide links to a UniSave diff comparison for any
  annotation changes.

* Explore options for interfacing with the BioModels database.
  
* It is relatively easy to track changes to known components which we
  specify. How do we detect new components to include? We could study
  pathway databases (e.g. KEGG, UniPathway) or use GO.

* Expand to other types of records and databases.
