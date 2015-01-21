.. _ops_interaction:

Interaction
===========

.. _ops_interaction_range:

=====
Range
=====

**Input**
        1 or 2 integers for promoter or DHS peak component :ref:`range(s) <base_range>`; :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>`; index of desired interaction component (0/promoter or 1/peak)
**Output**
      :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>`

This operation shrinks or grows either the promoter or DHS component of specified :ref:`Interactions <compound_interaction>` by specified integer values. 

Positive values for the range component expand elements; negative values shrink elements. A positive left value expands the element on the left edge of its :ref:`range <base_range>`; conversely, a negative left value shrinks the element on its left edge. The same applies for the right value, to the right edge of the element’s range. 

Any :ref:`Element <compound_element>` with a post-processed :ref:`Range <base_range>` with a length 0 or less causes the entire :ref:`Interaction <compound_interaction>` to be discarded. 

If the values of L and R are equal and positive, the promoter or peak component grows symmetrically. If the values of L and R are equal and negative, the promoter or peak component shrinks symmetrically.

The command-line equivalent would likely be a :ref:`BEDOPS <glossary_bedops>` ``bedops --range`` operation on the specified component.

.. _ops_interaction_union:

=====
Union
=====

**Input**
      1 or more :ref:`Interaction <compound_interaction>` :ref:`Sets <compound_set>`
**Output**
      :ref:`Interaction <compound_interaction>` :ref:`Sets <compound_set>`

This operation takes the union of :ref:`Interactions <compound_interaction>` in a :ref:`Set <compound_set>`, yielding one :ref:`Set <compound_set>` made up of each of the input interactions. Each Interaction in the output set preserves its attributes. The union of one interaction set is the set itself.
