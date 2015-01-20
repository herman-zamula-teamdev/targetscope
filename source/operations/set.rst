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

This filter creates a new :ref:`set <compound_set>` from :ref:`elements <compound_element>` in the first set, where :ref:`range <base_range>` components of elements in the second (and subsequent) sets overlap the first set's elements by the specified integer or float value. 

If that value is an integer, overlap is calculated as a measure of required overlap of bases in the elements' :ref:`range <base_range>` components. If that value is a percentage, overlap is calculated as a required minimum fraction of overlap between ranges.

If there are more than two :ref:`sets <compound_set>` specified as input, the second and subsequent :ref:`sets <compound_set>` are first merged into an intermediate set. The first set is then filtered against this intermediate set using the specified overlap threshold.

Because the output set is made up of elements from the first set, those :ref:`elements <compound_element>` should preserve all additional attributes (:ref:`Name <base_name>`, :ref:`Score <base_score>`, *etc.*) where applicable.

The ordering of sets in this operation matters; *e.g.*, compare these two inclusion operations, where the two sets are in different order.

In the first example, we filter set A against set B:

.. image:: ../../_static/ops_set_inclusive_filter_ab.png
   :width: 99%

In the second example, we filter set B against set A:

.. image:: ../../_static/ops_set_inclusive_filter_ba.png
   :width: 99%

