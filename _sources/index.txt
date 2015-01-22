.. _home:

About
=====

We provide a specification for *targetscope* entities and predicates, which helps describe terminology used in the :ref:`JSON schema <schema_request>` and in web service requests used by the *targetscope* front-end. 

:ref:`Predicates <ops>` are modeled on BEDOPS set and map operations described in the documentation for ``bedops`` and ``bedmap`` binaries (see the `BEDOPS documentation <http://bedops.readthedocs.org/en/latest/>`_ for more detail), while :ref:`data entities <data>` are derived from columnar data found in BED files, or are composed into :ref:`compound <compound>` elements by using :ref:`base <base>` types as building blocks.

The :ref:`TFBS example <example_tfbs>` describes a complete pipeline of predicates and data entities used to find the binding sites of a transcription factor. This example describes one way (in broad terms) how the components of this specification document could be used to construct and perform tasks in the *targetscope* application.

.. toctree::
   :maxdepth: 4

   schema/index.rst
   example/index.rst
   data/index.rst
   operations/index.rst
   glossary.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

