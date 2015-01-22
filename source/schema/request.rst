.. _schema_request:

Request
=======

We use the `JSON Schema v0.4 <http://json-schema.org/>`_ specification to write a schema that describes a `directed acyclic object graph <http://en.wikipedia.org/wiki/Directed_acyclic_graph>`_ of structured inputs, outputs, and a vocabulary of intermediate operations (:ref:`predicates <ops>` and :ref:`options <data>`) used for accessing functionality in the *targetscope* application.

The schema aims to be flexible enough to be extended for use with the full application, as well as to be usable now with a web service to validate incoming sample requests.

===========
JSON Schema
===========

Refer to the ``target_gene_schema.json`` file (`GitHub link <https://github.com/alexpreynolds/targetscope/blob/master/target_gene_schema.json>`__) for the current *targetscope* schema.

.. _schema_request_base:

----
Base
----

.. _schema_request_base_version:

*version*
  String. Specifies version of web request payload. One of ``v1.0.0`` or ``v1.1.0``.

.. _schema_request_base_id:

*id*
  String. A unique server-side identifier for the web request (*e.g.*, `GUID <http://en.wikipedia.org/wiki/Globally_unique_identifier>`_).

.. _schema_request_base_name:

*name*
  String. Nickname for request.

.. _schema_request_base_dtsubmission:

*dtsubmission*
  String (date-time). `RFC3339-formatted <http://tools.ietf.org/html/rfc3339>`_ submission timestamp (UTC).

.. _schema_request_sets:

----
Sets
----

Array of *id* and *kind* elements for each :ref:`Set <compound_set>`.

.. _schema_request_sets_id:

*id*
  String. A unique identifier for the Set (*e.g.*, `GUID <http://en.wikipedia.org/wiki/Globally_unique_identifier>`_).

.. _schema_request_sets_kind:

*kind*
  String. Specified member type of Set. One of ``element`` or ``interaction``.

.. _schema_request_op:

----------
Operations
----------

Operations in the request payload are made up of an array of objects containing two objects: *kind* and *option*. The *kind* is a key-value pair that describes the type or kind of operation, while *option* describes an array of option or parameter key-value pairings for that operation.

.. _schema_request_op_kind:

+++++
Kinds
+++++

The following are short descriptions of the JSON keywords used to describe an operation-kind. View the linked operation document for the full description and parameter list.

_______
Element
_______

.. _schema_request_op_kind_element_set_attributes:

:ref:`element_set_attributes <ops_map_summary>`
  Summarizes attributes of an :ref:`Element <compound_element>` :ref:`Set <compound_set>`. This summary could be the result of a numerical calculation on :ref:`Score <base_score>` data, or a listing of :ref:`Name <base_name>` values.

.. _schema_request_op_kind_element_set_component:

:ref:`element_set_component <ops_filter_component>`
  Filters an :ref:`Interaction <compound_interaction>` to return either the first or second :ref:`Element <compound_element>` :ref:`Set <compound_set>` (promoter or DHS component).

.. _schema_request_op_kind_element_set_difference:

:ref:`element_set_difference <ops_set_difference>`
  Creates a new :ref:`Set <compound_set>` from :ref:`Ranges <base_range>` found in the first input Set, excluding overlaps with Ranges in the second and subsequent input Sets.

.. _schema_request_op_kind_element_set_element_of:

:ref:`element_set_element_of <ops_set_inclusive_filter>`
  Creates a new :ref:`Set <compound_set>` from :ref:`Elements <compound_element>` in the first set, where :ref:`Range <base_range>` components of Elements in the second (and subsequent) Sets overlap the first Set's Elements by the specified integer or float value. 

.. _schema_request_op_kind_element_set_filter_chromosome:

:ref:`element_set_filter_chromosome <ops_filter_chromosome>`
  Filters :ref:`Elements <compound_element>` with a :ref:`Range <base_range>` component by the specified, exact chromosome string name.

.. _schema_request_op_kind_element_set_filter_name:

:ref:`element_set_filter_name <ops_filter_name>`
  Filters :ref:`Elements <compound_element>` with :ref:`Name <base_name>` components by the specified string value.

.. _schema_request_op_kind_element_set_filter_score:

:ref:`element_set_filter_score <ops_filter_score>`
  Filters :ref:`Elements <compound_element>` with :ref:`Score <base_score>` components by the specified numerical value and relational operator.

.. _schema_request_op_kind_element_set_filter_strand:

:ref:`element_set_filter_strand <ops_filter_strand>`
  Filters :ref:`Elements <compound_element>` with :ref:`Name <base_name>` components by the specified :ref:`Strand <base_strand>` value.

.. _schema_request_op_kind_element_set_map_on_element_set:

:ref:`element_set_map_on_element_set <ops_map_element_onto_element>`
  Maps elements in one "map" :ref:`Set <compound_set>` to :ref:`Elements <compound_element>` in another "reference" set, if mapped Elements meet the specified overlap criteria. 

.. _schema_request_op_kind_element_set_map_on_interaction_set:

:ref:`element_set_map_on_interaction_set <ops_map_element_onto_interaction>`
  Identical to mapping an :ref:`Element <compound_element>` :ref:`Set <compound_set>` against another Element Set, with the same default overlap criteria, except that we specify which of the two components of the :ref:`Interaction <compound_interaction>` we would like to treat as the reference Set to map our input Element Set against.

.. _schema_request_op_kind_element_set_merge:

:ref:`element_set_merge <ops_set_merge>`
  Takes merge of :ref:`Ranges <base_range>` of input :ref:`Elements <compound_element>` in one or more :ref:`Sets <compound_set>`.

.. _schema_request_op_kind_element_set_not_element_of:

:ref:`element_set_not_element_of <ops_set_exclusive_filter>`
  Creates a new :ref:`Set <compound_set>` from elements in the first :ref:`Set <compound_set>`, where :ref:`Range <base_range>` components of :ref:`Elements <compound_element>` in the second (and subsequent) Sets do not overlap the first Set's Elements by the specified integer or float value. 

.. _schema_request_op_kind_element_set_partition:

:ref:`element_set_partition <ops_set_partition>`
  Creates a new :ref:`Set <compound_set>` from disjoint Ranges computed from all input Sets. A partition of one Set alone will segment any overlapping Elements within that Set.

.. _schema_request_op_kind_element_set_range:

:ref:`element_set_range <ops_range_adjust_element>`
  Symmetrically or asymmetrically shrinks or grows :ref:`Elements <compound_element>` by specified integer parameter(s).

.. _schema_request_op_kind_element_set_symmetric_difference:

:ref:`element_set_symmetric_difference <ops_set_symmdiff>`
  Creates a new :ref:`Set <compound_set>` from :ref:`Ranges <base_range>` found in the first input Set, excluding overlaps with Ranges in the second and subsequent input Sets, unionized with Ranges found in the second input Set, excluding overlaps with Ranges in all other input Sets, etc.

.. _schema_request_op_kind_element_set_union:

:ref:`element_set_union <ops_set_union>`
  Takes union of :ref:`Elements <compound_element>` in one or more :ref:`Sets <compound_set>`, returning one :ref:`Set <compound_set>` containing all elements.

___________
Interaction
___________

.. _schema_request_op_kind_interaction_set_filter_component:

:ref:`interaction_set_filter_component <ops_filter_component>`
  Filters an :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>` to return either the first or second component as an :ref:`Element <compound_element>` :ref:`Set <compound_set>`.

.. _schema_request_op_kind_interaction_set_range:

:ref:`interaction_set_range <ops_interaction_range>`
  Symmetrically or asymmetrically shrinks or grows a component of an :ref:`Interaction <compound_interaction>` in a larger :ref:`Set <compound_set>`.

.. _schema_request_op_kind_interaction_set_union:

:ref:`interaction_set_union <ops_interaction_union>`
  Takes the union of :ref:`Interactions <compound_interaction>` in a :ref:`Set <compound_set>`, yielding one :ref:`Set <compound_set>` made up of each of the input Interactions.

+++++++
Options
+++++++

.. _schema_request_op_option_range_start:

:ref:`range_start <ops_range_adjust_element>`
  In conjunction with :ref:`element_set_range <schema_request_op_kind_element_set_range>` this parameter adjusts the left or start edge of :ref:`Elements <compound_element>` by the specified integer value. 

.. _schema_request_op_option_range_stop:

:ref:`range_stop <ops_range_adjust_element>`
  In conjunction with :ref:`element_set_range <schema_request_op_kind_element_set_range>` this parameter adjusts the right or stop edge of :ref:`Elements <compound_element>` by the specified integer value. 

.. _schema_request_op_option_filter_score:

:ref:`filter_score <ops_filter_score>`
  In conjunction with :ref:`element_set_filter_score <schema_request_op_kind_element_set_filter_score>` this parameter filters :ref:`Elements <compound_element>` by the specified numerical value and relational operator. This value is a semi-colon-delimited string specifying the value and operator, *e.g.* "5.12;<", "0.0000298;>=" etc.

.. _schema_request_op_option_filter_name:

:ref:`filter_name <ops_filter_name>`
  In conjunction with :ref:`element_set_filter_name <schema_request_op_kind_element_set_filter_name>` this parameter filters :ref:`Elements <compound_element>` by an exact match with the specified name value.

.. _schema_request_op_option_filter_strand:

:ref:`filter_strand <ops_filter_strand>`
  In conjunction with :ref:`element_set_filter_strand <schema_request_op_kind_element_set_filter_strand>` this parameter filters :ref:`Elements <compound_element>` by an exact match with the specified :ref:`Strand <base_strand>` value.

::

  "filter_strand",
  "filter_chromosome",
  "filter_interaction_component",
  "set_range_left",
  "set_range_right"
  "set_overlap_bases",
  "set_overlap_fraction_both",
  "set_overlap_fraction_either",
  "set_overlap_fraction_map",
  "set_overlap_fraction_ref",
  "set_overlap_exact",
  "set_overlap_range_start",
  "set_overlap_range_stop"

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