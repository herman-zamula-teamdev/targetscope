.. _base:

Base types
==========

=====
Score
=====

+--------------------+-------------------------------------------------------+
| **Data**           | Integer, float, scientific notation                   |
+--------------------+-------------------------------------------------------+

*Score* adds an integer or decimal numerical attribute to *Element*, *Interaction* or *Set* compound types. 

====
Name
====

+--------------------+-------------------------------------------------------+
| **Data**           | String                                                |
+--------------------+-------------------------------------------------------+

*Name* adds an identifying attribute to *Element*, *Interaction* or *Set* compound types.

======
Strand
======

+--------------------+-------------------------------------------------------+
| **Data**           | Character (+/-/.)                                     |
+--------------------+-------------------------------------------------------+

*Strand* adds an orientation attribute to *Element* and *Interaction* compound types.

=====
Range
=====

+--------------------+-------------------------------------------------------+
| **Data**           | BED3                                                  |
+--------------------+-------------------------------------------------------+

*Range* consists of a chromosome name, start and stop index. The chromosome name follows UCSC convention and starts with the string ``chr``. The start and stop indices are integers greater than or equal to zero. The stop index must be greater than the start index.

========
Metadata
========

+--------------------+-------------------------------------------------------+
| **Data**           | JSON-formatted string                                 |
+--------------------+-------------------------------------------------------+

The *Metadata* type adds a free-form, JSON-formatted descriptive attribute to *Element*, *Interaction* or *Set* compound types.

