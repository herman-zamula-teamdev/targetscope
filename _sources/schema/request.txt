.. _schema_request:

Request
=======

We use the `JSON Schema v0.4 <http://json-schema.org/>`_ specification to write a schema that describes a `directed acyclic object graph <http://en.wikipedia.org/wiki/Directed_acyclic_graph>`_ of structured inputs, outputs, and a vocabulary of intermediate operations (:ref:`predicates <ops>` and :ref:`options <data>`) used for accessing functionality in the *targetscope* application.

The schema aims to be flexible enough to be extended for use with the full application, as well as to be usable now with a web service to validate incoming sample requests.

===========
JSON Schema
===========

Refer to the ``target_gene_schema.json`` file (`GitHub link <https://github.com/alexpreynolds/targetscope/blob/master/target_gene_schema.json>`__) for the current *targetscope* schema.

==========
Validation
==========

We include a test web request that follows the schema (``target_gene_test_request.json``, `GitHub link <https://github.com/alexpreynolds/targetscope/blob/master/target_gene_test_request.json>`__) which can be validated with the included Python script (``target_gene_request_validation.py``, `GitHub link <https://github.com/alexpreynolds/targetscope/blob/master/target_gene_request_validation.py>`__) with the installation of the `jsonschema <http://json-schema.org>`_ Python package.

.. topic:: Example

   ::

     $ python
     Python 2.7.6 (default, Jul  9 2014, 20:49:24) 
     [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.38)] on darwin
     Type "help", "copyright", "credits" or "license" for more information.
     >>> import json
     >>> from jsonschema import validate
     >>> schema_fh = open("target_gene_schema.json", "r")
     >>> schema = json.load(schema_fh)
     >>> test_request_fh = open("target_gene_test_request.json", "r")
     >>> test_request = json.load(test_request_fh)
     >>> validate(test_request, schema)
     >>>

In this example, if validation fails (some field is missing or of the incorrect type), a ``ValidationError`` exception is thrown with errors that point to the offending object.