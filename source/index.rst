.. targetscope documentation master file, created by
   sphinx-quickstart on Mon Jan 19 13:19:12 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

About
=======================================

We use the `JSON Schema v0.4 <http://json-schema.org/>`_ specification to write an initial schema document (``target_gene_schema.json``) that describes a directed acyclic object graph of inputs, outputs, and a vocabulary of intermediate operations ("predicates" and options) used for a subset of functionality in the *targetscope* application.

The goal is to write a schema that is flexible enough to ultimately be used with the full application, as well as to be usable now with a web service to validate incoming requests.

We include a test web request that follows the schema (``target_gene_test_request.json``) which can be validated with the included Python script (``target_gene_request_validation.py``) with the installation of the `jsonschema <http://json-schema.org>`_ Python package.

An initial pass at a specification for *targetscope* entities and predicates is described in this document, which helps describe terminology used in the schema and in web service requests. Predicates are very much like BEDOPS set and map operations described in the documentation for ``bedops`` and ``bedmap`` binaries (see the `BEDOPS documentation <http://bedops.readthedocs.org/en/latest/>`_ for more detail).

.. toctree::
   :maxdepth: 2
   :numbered:

   glossary.rst
   data/base.rst
   data/compound.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

