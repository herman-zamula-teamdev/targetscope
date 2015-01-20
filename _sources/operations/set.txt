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