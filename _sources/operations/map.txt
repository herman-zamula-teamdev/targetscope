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

The result of this most basic mapping example is a set of reference elements, where each reference element has another element set associated with it.

Some reference elements may associate with map sets with elements. Other reference elements may associate with an empty set, if the overlap criteria means that there are no overlapping (no mappable) elements.

In this example, we report the reference set elements along with all mapped elements. However, we may use operators to only report mapped elements:

::

  $ bedmap --echo-map --bp-ovr 1 ref.bed map.bed | sort-bed - > mapped_map.bed

Alternative arguments to ``bedmap`` may summarize or "report" attributes about mapped elements. Discussion of these follow.

.. Note:: 
   The default overlap criteria that is used by ``bedmap`` is one or more bases. 



