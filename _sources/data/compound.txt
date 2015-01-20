.. _compound:

Compound types
==============

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
        chr17   2 23       -V_NRSF_01                                  5.89317e-06      -       TGCAGGAACAGGGTGAGAAGC
        chr17   27         42                                          -V_OCT4_02       5.78775e-06     -       ATTGTCATGCAATTA
        chr17   125        141                                         -V_TAL1BETAE47_01                4.13235e-06     -       CTGGACAGATGTTTGT
        chr17   125        141                                         -V_TAL1BETAITF2_01               9.97644e-06     -       CTGGACAGATGTTTGT
        chr17   126        138                                         +V_RP58_01                       5.58617e-06     +       CAAACATCTGTC...

   The fourth column of this file is the TRANSFAC name of the transcription factor (TRANSFAC is the name of a database of transcription factors — there are other databases; *e.g.*, Jaspar and UniPROBE). Note here that the start character of the ID field matches the strand field on which the factor is located, and that the seventh column contains the reference sequence at that range.