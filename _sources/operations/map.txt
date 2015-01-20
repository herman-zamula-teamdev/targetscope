.. _ops_map:

Map
===

.. _ops_map_element_onto_element:

============================
Element set onto element set
============================

**Input**
      1 or 2 :ref:`Element <compound_element>` :ref:`Sets <compound_set>`; overlap criteria (integer/bases or float/percentage); report operator(s)
**Output**
      :ref:`Element <compound_element>` :ref:`Sets <compound_set>`
**CLI example**
      ``bedmap --echo --echo-map --bp-ovr 1 ref.bed map.bed > ref_with_mapped_map.bed``

This operation maps elements in one "map" :ref:`set <compound_set>` to :ref:`elements <compound_element>` in another "reference" set, if mapped elements meet the specified overlap criteria. 

For instance, take the following command:

::

  $ bedmap --echo --echo-map --bp-ovr 1 ref.bed map.bed > ref_with_mapped_map.bed

This command associates elements in the file ``map.bed`` with each element in ``ref.bed``, where each map element overlaps a reference element by one or more bases. The ``--echo-map`` operation reports all map elements that associate with a reference element.

The result of this most basic mapping example is a set of reference elements, where each reference element has another element set associated with it:

.. image:: ../../_static/ops_map_element_onto_element.png
   :width: 50%

Some reference elements may associate with map sets with elements. Other reference elements may associate with an empty set, if the overlap criteria means that there are no overlapping (no mappable) elements.

In this example, we report the reference set elements along with all mapped elements. However, we may use operators to only report mapped elements:

::

  $ bedmap --echo-map --bp-ovr 1 ref.bed map.bed | sort-bed - > mapped_map.bed

Alternative arguments to ``bedmap`` may summarize or "report" attributes about mapped elements. Discussion of these follow.

.. Note:: 
   The default overlap criteria that is used by ``bedmap`` is one or more bases. 

.. _ops_map_element_onto_interaction:

================================
Element set onto interaction set
================================

**Input**
      1 :ref:`Element <compound_element>` :ref:`Set <compound_set>`; 1 :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>`; index of desired interaction component to act as reference set; overlap criteria (integer/bases or float/percentage); report operator(s)
**Output**
      :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>`

This is identical to mapping an :ref:`Element <compound_element>` :ref:`Set <compound_set>` against another element set, with the same default overlap criteria, except that we specify which of the two components of the :ref:`Interaction <compound_interaction>` we would like to treat as the reference set to map our input element set against.

For instance, let's say we want a list of :ref:`Interactions <compound_interaction>`, whose promoter components overlap with some genes of interest.

We start with an :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>` that pairs promoter components with DHS peak components. For this example, the index of the promoter component in this set is ``0`` and the index of the DHS peak component is ``1``.

We also start with an element set of transcription start sites (TSSs) for target genes. These contain genomic :ref:`Ranges <base_range>` and gene :ref:`Names <base_name>`.

For this map operation, we specify an index of ``0`` to retrieve the set of interactions whose promoter components' ranges are overlapped by the TSS ranges.

.. _ops_map_summary:

==============
Summary report
==============

**Input**
      1 :ref:`Element <compound_element>` :ref:`Set <compound_set>`; summary operator
**Output**
      :ref:`Set <compound_set>`, :ref:`Array <compound_array>` or :ref:`base type <base>`
**CLI example**
      ``bedmap --mean --bp-ovr 1 ref.bed map.bed > mean_map_signal_over_refs.bed``

This operation summarizes attributes of an :ref:`Element <compound_element>` :ref:`Set <compound_set>`. This summary could be the result of a numerical calculation on :ref:`Score <base_score>` data, or a listing of :ref:`Name <base_name>` values.

*Examples:*

* For all the mappable elements that associate with a reference element, we may want a :ref:`Set <compound_set>` of names of those mapped elements, leaving out duplicates.

* For all the mappable elements that associate with a reference element, we want the arithmetic mean and variance of the signal or a :ref:`Score <base_score>` value derived from mapped elements.

+----------------+-------------------+---------------------------------------+---------------------------------+
| Operation      | Argument          | Description                           | Output                          |
+================+===================+=======================================+=================================+
| bases          | NA                | Report the total number of bases in   | :ref:`Score <base_score>`       |
|                |                   | the :ref:`Ranges <base_range>` in the |                                 |
|                |                   | input set                             |                                 |
+----------------+-------------------+---------------------------------------+---------------------------------+
| bases-uniq     | NA                | Report the unique (non-overlapping)   | :ref:`Score <base_score>`       |
|                |                   | number of bases in the :ref:`Ranges   |                                 |
|                |                   | <base_range>` in the input set        |                                 |
+----------------+-------------------+---------------------------------------+---------------------------------+