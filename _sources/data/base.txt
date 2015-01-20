.. _base:

Base types
==========

.. _base_score:

=====
Score
=====

+--------------------+-------------------------------------------------------+
| **Data**           | Integer, float, scientific notation                   |
+--------------------+-------------------------------------------------------+

*Score* adds an integer or decimal numerical attribute to :ref:`Element <compound_element>`, :ref:`Interaction <compound_interaction>` or :ref:`Set <compound_set>` compound types. 

.. _base_name:

====
Name
====

+--------------------+-------------------------------------------------------+
| **Data**           | String                                                |
+--------------------+-------------------------------------------------------+

*Name* adds an identifying attribute to :ref:`Element <compound_element>`, :ref:`Interaction <compound_interaction>` or :ref:`Set <compound_set>` compound types.

.. _base_strand:

======
Strand
======

+--------------------+-------------------------------------------------------+
| **Data**           | Character (+/-/.)                                     |
+--------------------+-------------------------------------------------------+

*Strand* adds an orientation attribute to :ref:`Element <compound_element>` and :ref:`Interaction <compound_interaction>` compound types.

.. _base_range:

=====
Range
=====

+--------------------+-------------------------------------------------------+
| **Data**           | BED3                                                  |
+--------------------+-------------------------------------------------------+

*Range* consists of a chromosome name, start and stop index. The chromosome name follows UCSC convention and starts with the string ``chr``. The start and stop indices are integers greater than or equal to zero. The stop index must be greater than the start index.

.. _base_metadata:

========
Metadata
========

+--------------------+-------------------------------------------------------+
| **Data**           | JSON-formatted string                                 |
+--------------------+-------------------------------------------------------+

The *Metadata* type adds a free-form, JSON-formatted descriptive attribute to :ref:`Element <compound_element>`, :ref:`Interaction <compound_interaction>` or :ref:`Set <compound_set>` compound types.

