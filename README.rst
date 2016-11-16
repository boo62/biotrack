==================
biotrack (Python2)
==================

Track changes to a list of UniProt entries.

The Problem
-----------

Biological databases are under constant revision due to new discoveries. Biological models often contain tens or hundreds of components (e.g. proteins and metabolites), making it impractical to manually track changes in databases for entire models. It would save time if updates could be automatically tracked from the date that a model is created. This would be particularly useful if a model is revisted after a long time.

Description
-----------

* biotrack will track changes to a list of UniProt entries recorded in a csv file.

* When information about a component is used in a model, the modeller should record the accession and version number of
  the component's UniProt entry in a csv file. A description can also be added (e.g. parameter used, or interaction). 

* Using the csv file, biotrack obtains the recorded and current version of UniProt entries for each component.

* The new and old versions are compared to see if any of the protein accessions have
  merged or if annotations
  (e.g. function, kinetic parameters, regulation) have changed. in the
  SwissProt.Record.components representation of the entries.

* Chages are displayed to the user.

How to install
--------------

Clone and then install using

    python setup.py install

Run modcomp
-----------

Once installed you can run the script modcomp on the example models
provided.

    cd tests/example_models/

    modcomp <filename>

This compares past UniProt entries of proteins in the model file to
the current entries in the UniProt database. It will tell you whether
any function annotations have changed or been added, and if so will
print the new versions of the fields. A check is also performed to see
if any accessions have merged and if so the groups are printed.
 
To see examples of both behaviours run modcomp on the example models
below.

   two_components.csv and
  
   two_groups_same_protein.csv
  
The first contains two proteins, only one of which has changes. The 
second contains some very old p53 entries and shows the merging of
accessions at the end of the output.

Model files should be in .csv format.

    UniProt accession, version, other fields...

Other fields are ignored by the parser but useful for comment.

Issues
------

* Currently no exception handling for non-existant UniProt entries.
  
  - Future and non-existant versions or entries will cause a crash.
  
  - It will crash if an accession has a valid UniProt format but does
    not exist in the database.


* Very old entries.

  - Some very old entries are in non-standard format and raise an error
    when biopython attempts to read them (see e.g.
    tests/example_models/two_ribE_accessions.csv)

..
  - You cannot use a secodary accession to retrieve a UniSave entry after
    merging. You can however formUniSave entries before merging and the current
    http://www.uniprot.org/ entry can be retrieved with a secondary
    accession.

.. 
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

  * Explore options for interfacing with the BioModels database. These
    have minimum information standards. Can I get the components in the
    correct format from either version numbers or dates?
  
  * It is relatively easy to track changes to known components which we
    specify. How do we detect new components to include? We could study
    pathway databases (e.g. KEGG, UniPathway) or use GO.

  * Expand to other types of molecule and databases.
