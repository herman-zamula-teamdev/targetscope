.. _compound:

Compound types
==============

.. _compound_element:

=======
Element
=======

+--------------------+-------------------------------------------------------+
| **Data**           | *Range* (optional: 1 or more *Name*; 1 *Score*; 1     |
|                    | *Strand*, 1+ *Metadata*, 1+ *Set*)                    |
+--------------------+-------------------------------------------------------+
| **Examples**       | Target gene promoter, gene annotation record, DHS     |
|                    | peak, transcription factor hit                        |
+--------------------+-------------------------------------------------------+

Operations can be applied on an *Element* or on a *Set* of *Elements*.

.. topic:: Example 1

   Here, we filter a set of transcription start sites for target gene **RARA**:
   ::

        $ grep -w RARA tss.bed
        chr17   38465445  38465446      RARA    41      +
        chr17   38474532  38474533      RARA    90      +
        chr17   38474536  38474537      RARA    15      +
        chr17   38497639  38497640      RARA    1       +
        chr17   38498614  38498615      RARA    20      +
        chr17   38501492  38501493      RARA    150     +
        chr17   38507638  38507639      RARA    3       +

   Therefore, the set of **RARA** transcription start sites is on chromosome 17, with the Ranges of ``[38465445, 38465446)``, ``[38474532, 38474533)``, *etc.* The *Name* value is **RARA**. The *Scores* are varied. The *Strand* value of each is ``+``. Each of these makes up an *Element*.

.. topic:: Example 2

   Here we show an example of some transcription factor binding sites, each an *Element*, also on chromosome 17:
   ::

        $ unstarch chr19 fimo.combined.xfac.1e-5.parsed.starch | more
        chr17   2      23       -V_NRSF_01          5.89317e-06     -       TGCAGGAACAGGGTGAGAAGC
        chr17   27     42       -V_OCT4_02          5.78775e-06     -       ATTGTCATGCAATTA
        chr17   125    141      -V_TAL1BETAE47_01   4.13235e-06     -       CTGGACAGATGTTTGT
        chr17   125    141      -V_TAL1BETAITF2_01  9.97644e-06     -       CTGGACAGATGTTTGT
        chr17   126    138      +V_RP58_01          5.58617e-06     +       CAAACATCTGTC...

   The fourth column of this file is the TRANSFAC name of the transcription factor (TRANSFAC is the name of a database of transcription factors — there are other databases; *e.g.*, Jaspar and UniPROBE). Note here that the start character of the ID field matches the strand field on which the factor is located, and that the seventh column contains the reference sequence at that range.

.. _compound_interaction:

===========
Interaction
===========

+--------------------+-------------------------------------------------------+
| **Data**           | 2 *Elements*; 1 *Score*; 1 *Name*; 1 *Strand*;        |
|                    | optional, 1+ *Metadata*                               |
+--------------------+-------------------------------------------------------+
| **Example**        | Long-range interaction                                |
+--------------------+-------------------------------------------------------+

An interaction pair is a special *Set* that defines a connection between two *Element* values. For the *targetscope* application specifically, this can be a gene promoter *Element* and a distal DHS peak *Element*. 

Operations can be applied on an interaction or on a grouping of interactions.

.. topic:: Example 1

   Here is an example of interactions centered around the gene **RARA**, in a BED format used for internal visualization. This is a special form of BED6, where the ID field contains a condensed form of the second pair of the interaction pairing, along with the interaction correlation score:
   ::

        $ more interactions.bed
        chr17   38498520        38498670        chr17:38107440-38107590,0.731035        3525    -
        chr17   38498520        38498670        chr17:38174060-38174210,0.727828        3541    -
        chr17   38498520        38498670        chr17:38184060-38184210,0.707405        3543    -
        chr17   38498520        38498670        chr17:38221800-38221950,0.763215        3545    -
        chr17   38498520        38498670        chr17:38222220-38222370,0.773827        3547    -
        ...

   The first three columns represent the genomic :ref:`Range <base_range>` of the gene promoter *Element*. The fourth column is a condensed string showing the DHS peak *Element* associated with that promoter, along with a correlation :ref:`Score <base_score>` for that interaction. The fifth column, usually a score field in a BED file, is used here as a replacement :ref:`Name <base_name>` for the pairing. The sixth column is the :ref:`Strand <base_strand>` of the promoter element.

   To get a list of interactions associated with **RARA** promoters, we first filter on strand, and then use *bedmap* to map interactions to the **RARA** promoters:
   ::

        $ awk '($6=="+")' interactions.bed > interactions_forward.bed
        $ grep -w RARA tss.bed | bedmap --echo --echo-map - interactions_forward.bed
        chr17  38465445        38465446 RARA   41         +|
        chr17  38474532        38474533 RARA   90         +|
        chr17  38474536        38474537 RARA   15         +|
        chr17  38497639        38497640 RARA   1          +|
        chr17  38498614        38498615 RARA   20         +|chr17       38498520        38498670        chr17:38512520-38512670,0.782996        3657    +;chr17 38498520 38498670        chr17:38514200-38514350,0.726464        3659    +;chr17 38498520 38498670        chr17:38603540-38603690,0.732044        3709    +;chr17 38498520 38498670        chr17:38698620-38698770,0.71501 3739    +;chr17 38498520 38498670        chr17:38713300-38713450,0.782635        3743    +;chr17 38498520 38498670        chr17:38714500-38714650,0.702538        3745    +
        ...     

   The **RARA** transcription start site (TSS) element on ``chr17`` at range ``[38498614,38498615)`` has several interactions associated with it, on the basis of one or more bases of overlap between the TSS and the interaction's promoter component.

.. _compound_set:

===
Set
===

+--------------------+-------------------------------------------------------+
| **Data**           | 1+ *Name*; 0+ *Metadata*, 0+ *Elements*,              |
|                    | *Interactions* or *Sets*                              |
+--------------------+-------------------------------------------------------+
| **Examples**       | DHS peaks for a particular cell type or sequencing    |
|                    | experiment, promoters, transcription factor binding   |
|                    | sites, other sets                                     |
+--------------------+-------------------------------------------------------+

Examples of *Sets* include the "target gene" (a set of promoter *Elements*) or groups of multiple interactions for a given promoter *Element*. 

A *Set* could also be made up of base types, like a set of unique :ref:`Name <base_name>` values, etc.

*Sets* could go by other descriptive names. An *Experiment* is one type of a set, which contains a specific type of *Element* values. A set of *Experiments* can be grouped into another set called a *Category*. For instance, one *Category* of cell types might be called "ectoderm", which includes various cell line-specific *Experiments* with names like "BE2_C", "HMEC", "Hela", etc. In turn, each of those *Experiments* contains DHS peaks that are specific to that cell line.

A *Category* could group other categories. For example, a category called "karyotype" could contain three subcategories called "cancer", "normal" and "unassigned". Each of the three subcategories could contain cell-line specific *Experiments* that contain data for cancerous cell lines, normal cell lines, and cell lines unassigned to the cancerous or normal subsets.

Some operations can be applied on a *Set*, depending on what features the set offers or exposes.

.. _compound_array:

=====
Array
=====

+--------------------+-------------------------------------------------------+
| **Data**           | 1+ *Name*; 0+ base types                              |
+--------------------+-------------------------------------------------------+

Examples of *Arrays* are ordered lists of base types (:ref:`Score <base_score>`, :ref:`Name <base_name>`, :ref:`Strand <base_strand>`, :ref:`Metadata <base_metadata>`). 