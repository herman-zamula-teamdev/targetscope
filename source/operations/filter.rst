.. _op_filter:

Filter operations
=================

.. _op_filter_score:

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
