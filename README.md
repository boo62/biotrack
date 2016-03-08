# biotrack

The aim is to track changes to components of a biological model in a database
(or databases). An extentsion could track changes to a whole pathway (in
e.g. KEGG).


The Problem:

If an author has many models, it may be hard to keep track of the literature for
all of them, or some of them may be abandoned. An author may revisit a model
after several years or it may be picked up by another researcher. It would be
useful to see whether there have been any developments, which might be used to
revise the model, without having to trawl through databases for all of the
components.

Proposal:

- At the time that a component or parameter for a component is used in a model,
the version number of the database is saved allowing access to the past state of
the database at some future time. Alternatively, the entry for that component is
downloaded and saved in a compressed format.

- Given a list of model components and accessions, or simply the compressed past
entries, the present entries for each component is obtained.

- A user specifies which fields (e.g. rate constant, function, expression and
  regulation) they want to compare for a given component, and any differences
  between the past and present versions are shown.

- This doesn't necessitate that the components are part of a model
  (i.e. anything written in SMBL, CellML, etc.,), that is just a suggested
  use.

- At first I will just try to do this for rate constants in UniProt. However, it
  would probably be more useful to track function, expression, regulation,
  and changes in pathway databases.


Issues:

- Information is spread across different databases and some of these (SubtiWiki)
  are species specific.

- Will database stucture have changed between versions so that it is
  difficult to compare? Merging of entries etc.

- It is relatively easy to track changes to known components which we
  specify. How do we detect new components in a pathway? Could study pathway
  databases (KEGG). BioModels has Path2Models which automatically generates
  models from pathway resources.


Alternative Approaches:

- For automatically generated models (Path2Models) this is not an issue since a
  model is generated from the latest information in a database.