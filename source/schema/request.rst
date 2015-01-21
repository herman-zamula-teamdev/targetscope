.. _schema_request:

Request
=======

We use the `JSON Schema v0.4 <http://json-schema.org/>`_ specification to write a schema that describes a `directed acyclic object graph <http://en.wikipedia.org/wiki/Directed_acyclic_graph>`_ of structured inputs, outputs, and a vocabulary of intermediate operations (:ref:`predicates <ops>` and :ref:`options <data>`) used for accessing functionality in the *targetscope* application.

The schema aims to be flexible enough to be extended for use with the full application, as well as to be usable now with a web service to validate incoming sample requests.

===========
JSON Schema
===========

Refer to the ``target_gene_schema.json`` file (`GitHub link <https://github.com/alexpreynolds/targetscope/blob/master/target_gene_schema.json>`__) for the current *targetscope* schema.

----------
Operations
----------

Operation components of the request payload are split into two descriptors: *kind* and *option*. The *kind* describes the type or kind of operation, while *option* describes options or parameters for that operation.

+++++
Kinds
+++++

.. _schema_request_op_kind_element_set_range:

:ref:`element_set_range <ops_range_adjust_element>`
  Symmetrically or asymmetrically shrinks or grows :ref:`Elements <compound_element>` by specified integer parameter(s).

.. _schema_request_op_kind_interaction_set_range:

:ref:`interaction_set_range <ops_interaction_range>`
  Symmetrically or asymmetrically shrinks or grows a component of an :ref:`Interaction <compound_interaction>` in a larger :ref:`Set <compound_set>`.

.. _schema_request_op_kind_element_set_filter_score:

:ref:`element_set_filter_score <ops_filter_score>`
  Filters :ref:`Elements <compound_element>` with :ref:`Score <base_score>` components by the specified numerical value and relational operator.

::

  "element_set_filter_score",
  "element_set_filter_name",
  "element_set_filter_strand",
  "element_set_filter_chromosome",
  "interaction_set_filter_component",
  "element_set_union",
  "element_set_merge",
  "element_set_element_of",
  "element_set_not_element_of",
  "element_set_component",
  "element_set_difference",
  "element_set_symmetric_difference",
  "element_set_partition",
  "element_set_map_on_element_set",
  "element_set_map_on_interaction_set",
  "element_set_attributes",
  "interaction_set_union"

+++++++
Options
+++++++

::

  "range_start",
  "range_stop",
  "filter_score",
  "filter_name",
  "filter_strand",
  "filter_chromosome",
  "filter_interaction_component",
  "set_range_left",
  "set_range_right"

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

For example, if the request contains an invalid ``version`` key value, then the validation script will throw a detailed exception report: 

.. code-block:: python

  Traceback (most recent call last):
    File "./target_gene_request_validation.py", line 10, in <module>
      validate(test_request, schema)
    File "/Library/Python/2.7/site-packages/jsonschema-2.3.0-py2.7.egg/jsonschema/validators.py", line 428, in validate
      cls(schema, *args, **kwargs).validate(instance)
    File "/Library/Python/2.7/site-packages/jsonschema-2.3.0-py2.7.egg/jsonschema/validators.py", line 117, in validate
      raise error
  jsonschema.exceptions.ValidationError: u'v1.2.0' is not one of [u'v1.0.0', u'v1.1.0']

  Failed validating u'enum' in schema[u'properties'][u'version']:
      {u'enum': [u'v1.0.0', u'v1.1.0']}

  On instance[u'version']:
      u'v1.2.0'