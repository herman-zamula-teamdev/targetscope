.. _ops_range:

Range
=====

.. _ops_range_adjust:

======
Adjust
======

**Input**
      1 or 2 integers for “left” and “right” :ref:`ranges <base_range>`; :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**Output**
      :ref:`Element <compound_element>` :ref:`Set <compound_set>`
**CLI example**
      ``bedops --range L:R --everything ElemSetA > ElemSetB``

This operation shrinks or grows :ref:`Elements <compound_element>` by specified integer values. 

Positive values expand elements; negative values shrink elements. Any :ref:`Element <compound_element>` with a processed :ref:`Range <base_range>` with a length 0 or less is discarded. 

If the values of L and R are equal and positive, the element grows symmetrically. If the values of L and R are equal and negative, the element shrinks symmetrically.
