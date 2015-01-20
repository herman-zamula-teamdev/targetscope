.. _ops_range:

Range
=====

.. _ops_range_adjust_element:

==============
Adjust element
==============

**Input**
      1 or 2 integers for “left” and “right” :ref:`ranges <base_range>`; :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --range L:R --everything ElemSetA > ElemSetB``

This operation shrinks or grows :ref:`Elements <compound_element>` by specified integer values. 

Positive values expand elements; negative values shrink elements. Any :ref:`Element <compound_element>` with a processed :ref:`Range <base_range>` with a length 0 or less is discarded. 

If the values of L and R are equal and positive, the element grows symmetrically. If the values of L and R are equal and negative, the element shrinks symmetrically.

.. _ops_range_adjust_interaction:

==================
Adjust interaction
==================

**Input**
        1 or 2 integers for promoter :ref:`range(s) <base_range>`; 1 or 2 integers for DHS peak :ref:`range(s) <base_range>`; :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>`
**Output**
        :ref:`Interaction <compound_interaction>` :ref:`Set <compound_set>`
**CLI example**
        NA

This operation shrinks or grows either or both of the promoter and DHS components of specified :ref:`Interactions <compound_interaction>` by specified integer values. 

Positive values for the promoter expand promoter elements; negative values shrink promoter elements. A positive left value expands the promoter on the left edge of its :ref:`range <base_range>`; conversely, a negative left value shrinks the promoter on its left edge. The same applies for the right value, to the right edge of the element’s range. 

Any promoter :ref:`Element <compound_element>` with a post-processed :ref:`Range <base_range>` with a length 0 or less causes the entire :ref:`Interaction <compound_interaction>` to be discarded. 

Similar rules are applied to the DHS peak component of the :ref:`Interaction <compound_interaction>`.

If the values of L and R are equal and positive, the promoter or peak component grows symmetrically. If the values of L and R are equal and negative, the promoter or peak component shrinks symmetrically.

The command-line equivalent would likely be a combination of two :ref:`BEDOPS <glossary_bedops>` ``bedops --range`` operations on each component.
