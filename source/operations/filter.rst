.. _ops_filter:

Filter
======

.. _ops_filter_score:

=====
Score
=====

**Input**
      1 :ref:`Score <base_score>`; 1 :ref:`Element <compound_element>` :ref:`Set <compound_set>`; relational operator; 1 Boolean value
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``awk ‘($5 > threshold)’ foo.bed > foo_thresholded.bed``

This operation filters :ref:`Elements <compound_element>` with :ref:`Score <base_score>` components by the specified numerical value and relational operator. A false Boolean value allows specifying the inverse of the operation.

After filtering, the output set should either be a proper subset of the input, the empty set, or the input itself.

.. _ops_filter_name:

====
Name
====

**Input**
      1 :ref:`Name <base_name>`; 1 :ref:`Element <compound_element>` :ref:`Set <compound_set>`; 2 Boolean values
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``awk ‘($4 == "RARA")’ foo.bed > foo_RARA.bed``

This operation filters :ref:`Elements <compound_element>` with :ref:`Name <base_name>` components by the specified string value. The first Boolean operator decides if the filtering is an exact or partial match on the input name string. A second, false Boolean value allows specifying the inverse of the operation.

After filtering, the output set should either be a proper subset of the input, the empty set, or the input itself.

.. _ops_filter_strand:

======
Strand
======

**Input**
      1 :ref:`Strand <base_strand>`; 1 :ref:`Element <compound_element>` :ref:`Set <compound_set>`; 1 Boolean value
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``awk ‘($6==”+”)’ foo.bed > foo_forward_stranded.bed``

This operation filters :ref:`Elements <compound_element>` with :ref:`Name <base_name>` components by the specified :ref:`Strand <base_strand>` value. A false Boolean value allows specifying the inverse of the result set (*e.g.*, all elements but those which are forward-stranded).

After filtering, the output set should either be a proper subset of the input, the empty set, or the input itself.

.. _ops_filter_chromosome:

==========
Chromosome
==========

**Input**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`; string; Boolean
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedextract chr17 foo.bed > foo_chr17.bed``

This operation filters :ref:`Elements <compound_element>` by the specified, exact chromosome string name. A false Boolean value allows specifying the inverse of the result set (all elements but those on the specified chromosome).

.. _ops_filter_component:

=========
Component
=========

**Input**
      :ref:`Interaction <compound_interaction>`; integer (index)
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      NA

This operation filters an :ref:`Interaction <compound_interaction>` to return either the first or second :ref:`Element <compound_element>` :ref:`Set <compound_set>` (promoter or DHS component).

