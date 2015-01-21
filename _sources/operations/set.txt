.. _ops_set:

Set
===

.. _ops_set_union:

=====
Union
=====

**Input**
      1 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --everything foo1.bed foo2.bed ... > union.bed``

This operation takes the union of :ref:`Elements <compound_element>` in a set, yielding one set made up of each of the input elements. Each Element in the output set preserves its basic :ref:`Score <base_score>`, :ref:`Name <base_name>`, *etc.* attributes. The union of one input set is the set itself.

.. image:: ../../_static/ops_set_union.png
   :width: 99%

.. _ops_set_merge:

=====
Merge
=====

**Input**
      1 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --merge foo1.bed foo2.bed ... > merge.bed``

This operation takes the merge of :ref:`Ranges <base_range>` of input :ref:`Elements <compound_element>` in a set, yielding one set made up of new :ref:`Element <compound_element>` values calculated from the ranges. 

.. Note:: 
   Because this result is calculated, each new :ref:`Element <compound_element>` in the output set loses any input attributes. 

The merge of one input set is the set of contiguous ranges of overlapping input elements.

.. image:: ../../_static/ops_set_merge.png
   :width: 99%

.. _ops_set_inclusive_filter:

================
Inclusive filter
================

**Input**
      2 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`; integer (base) or float (percentage) overlap parameter
**Output**
      :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**CLI example**
      ``bedops --element-of -1 foo.bed bar1.bed bar2.bed ... > inclusive_filter.bed``

This filter creates a new :ref:`Set <compound_set>` from :ref:`Elements <compound_element>` in the first Set, where :ref:`Range <base_range>` components of Elements in the second (and subsequent) Sets overlap the first Set's elements by the specified integer or float value. 

If that value is an integer, overlap is calculated as a measure of required overlap of bases in the Elements' :ref:`Range <base_range>` components. If that value is a percentage, overlap is calculated as a required minimum fraction of overlap between ranges.

If there are more than two :ref:`Sets <compound_set>` specified as input, the second and subsequent :ref:`Sets <compound_set>` are first merged into an intermediate Set. The first Set is then filtered against this intermediate set using the specified overlap threshold.

Because the output set is made up of elements from the first Set, those :ref:`Elements <compound_element>` should preserve all additional attributes (:ref:`Name <base_name>`, :ref:`Score <base_score>`, *etc.*) where applicable.

The ordering of Sets in this operation matters; *e.g.*, compare these two inclusion operations, where the two Sets are in different order.

In the first example, we filter Set A against Set B:

.. image:: ../../_static/ops_set_inclusive_filter_ab.png
   :width: 99%

In the second example, we filter Set B against Set A:

.. image:: ../../_static/ops_set_inclusive_filter_ba.png
   :width: 99%

As shown, this is not a symmetric operation.

.. _ops_set_exclusive_filter:

================
Exclusive filter
================

**Input**
      2 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`; integer (base) or float (percentage) overlap parameter
**Output**
      :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**CLI example**
      ``bedops --not-element-of -1 foo.bed bar1.bed bar2.bed ... > exclusive_filter.bed``

This filter creates a new :ref:`Set <compound_set>` from elements in the first :ref:`Set <compound_set>`, where :ref:`Range <base_range>` components of :ref:`Elements <compound_element>` in the second (and subsequent) Sets do not overlap the first Set's Elements by the specified integer or float value. 

If that value is an integer, overlap is calculated as a measure of required overlap of bases in the Elements' Range components. If that value is a percentage, overlap is calculated as a required minimum fraction of overlap between Ranges.

If there are more than two Sets specified as input, the second and subsequent Sets are first merged into an intermediate Set. The first Set is then filtered against this intermediate Set using the specified overlap threshold.

Because the output Set is made up of Elements from the first Set, those elements should preserve all additional attributes (:ref:`Name <base_name>`, :ref:`Score <base_score>`, etc.) where applicable.

.. image:: ../../_static/ops_set_exclusive_filter_ab.png
   :width: 99%

.. _ops_set_complement:

==========
Complement
==========

**Input**
      1 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --complement foo1.bed foo2.bed ... > complement.bed``

This filter creates a new :ref:`set <compound_set>` of :ref:`elements <compound_element>` from gaps between the contiguous :ref:`ranges <base_range>` defined by one or more input sets. 

The complement of one set excludes the start- and end-pieces of a chromosome. To include those ranges, one can calculate the difference operation between the input set and a "full chromosome" :ref:`Element <compound_element>`, taking the first and last elements of the result. Those two elements would be unioned with the complement of the input set to get the full extents set.

.. image:: ../../_static/ops_set_complement.png
   :width: 99%

.. _ops_set_difference:

==========
Difference
==========

**Input**
      2 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --difference foo.bed bar1.bed bar2.bed ... > difference.bed``

This filter creates a new :ref:`set <compound_set>` from :ref:`ranges <base_range>` found in the first input set, excluding overlaps with ranges in the second and subsequent input sets.

Like the :ref:`complement <ops_set_complement>` operation, this calculates new elements and so :ref:`name <base_name>` and other attributes of elements in the first set are discarded.

.. image:: ../../_static/ops_set_difference.png
   :width: 99%

.. _ops_set_symmdiff:

====================
Symmetric difference
====================

**Input**
      2 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --symmdiff foo.bed bar.bed baz.bed ... > symmdiff.bed``

This filter creates a new :ref:`set <compound_set>` from :ref:`ranges <base_range>` found in the first input set, excluding overlaps with ranges in the second and subsequent input sets, unionized with ranges found in the second input set, excluding overlaps with ranges in all other input sets, etc.

Like the :ref:`complement <ops_set_complement>` operation, this calculates new elements and so :ref:`name <base_name>` and other attributes of elements in all sets are discarded.

.. image:: ../../_static/ops_set_symmdiff.png
   :width: 99%

.. _ops_set_partition:

=========
Partition
=========

**Input**
      1 or more :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --partition foo.bed bar.bed baz.bed ... > partition.bed``

This filter creates a new :ref:`set <compound_set>` from disjoint ranges computed from all input sets. A partition of one set alone will segment any overlapping elements within that set.

.. image:: ../../_static/ops_set_partition.png
   :width: 99%

|