.. _tfbs:

Target gene to transcription factor binding sites
=================================================

This figure describes a complete operational pipeline to retrieve the names of transcription factors which lie within DHS peaks, which are associated with interactions whose promoters overlap **RARA** transcription start sites:

.. image:: ../../_static/tfbs_rara.png
   :width: 99%

Reading from left to right, we start with the :ref:`Element <compound_element>` :ref:`Set <compound_set>` of target gene transcription start sites (TSSs). We :ref:`filter <ops_filter_name>` these on the :ref:`name <base_name>` **RARA** to retrieve an element set of **RARA** -specific TSSs.

Next, we :ref:`map this element set against the promoter elements of our Interaction Set <ops_map_element_onto_interaction>` of all interactions. This gives us all the **RARA** -specific interactions, which we filter to retrieve an element set of DHS peaks.

Subsequently, we apply an :ref:`inclusive element <ops_set_inclusive_filter>` filter against this set of DHS peaks and an element set of transcription factor binding sites. We apply overlap criteria of 100% to ensure that the transcription factor binding site lies entirely within the DHS peak.

Finally, we have an element set of transcription factor binding sites that lie within DHS peaks. We apply a :ref:`report filter <ops_map_summary>` on the :ref:`Name <base_name>` attribute, to retrieve a final result: an ordered list of unique transcription factor names.
