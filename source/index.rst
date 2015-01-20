.. _home:

About
=====

We provide a specification for *targetscope* entities and predicates, which helps describe terminology used in the (JSON) schema and in web service requests used by the *targetscope* front-end. 

:ref:`Predicates <ops>` are modeled on BEDOPS set and map operations described in the documentation for ``bedops`` and ``bedmap`` binaries (see the `BEDOPS documentation <http://bedops.readthedocs.org/en/latest/>`_ for more detail), while :ref:`data entities <data>` are derived from columnar data found in BED files, or are composed into :ref:`compound <compound>` elements by using :ref:`base <base>` types as building blocks.

The :ref:`TFBS example <example_tfbs>` describes a complete pipeline of predicates and data entities used to find the binding sites of a transcription factor. This example describes (in broad terms) how the components of this specification document can be used to construct and perform tasks in the *targetscope* application.

We use the `JSON Schema v0.4 <http://json-schema.org/>`_ specification to write an initial schema document (``target_gene_schema.json``) that describes a directed acyclic object graph of inputs, outputs, and a vocabulary of intermediate operations ("predicates" and options) used for a subset of functionality in the *targetscope* application.

The goal is to write a schema that is flexible enough to ultimately be used with the full application, as well as to be usable now with a web service to validate incoming requests.

We include a test web request that follows the schema (``target_gene_test_request.json``) which can be validated with the included Python script (``target_gene_request_validation.py``) with the installation of the `jsonschema <http://json-schema.org>`_ Python package.

.. toctree::
   :maxdepth: 3

   example/index.rst
   data/index.rst
   operations/index.rst
   glossary.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

