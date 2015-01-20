.. _glossary:

Glossary
========

===
BED
===

BED is short for *Browser Extensible Display*. It is a tab-delimited text format that can span three or more columns, used to represent zero-indexed, half-open elements or areas of interest:

+--------------------+-------------+------------------------+----------------+
| Column index       | Name        | Type                   | Nickname       |
+====================+=============+========================+================+
| 1                  | Chromosome  | String                 | BED3, 4, 5, 6+ |
+--------------------+-------------+------------------------+----------------+
| 2                  | Start index | Integer (i >= 0)       | BED3, 4, 5, 6+ |
+--------------------+-------------+------------------------+----------------+
| 3                  | Stop index  | Integer (j > i)        | BED3, 4, 5, 6+ |
+--------------------+-------------+------------------------+----------------+
| 4                  | ID          | String                 | BED4, 5, 6+    |
+--------------------+-------------+------------------------+----------------+
| 5                  | Score       | Float                  | BED5, 6+       |
+--------------------+-------------+------------------------+----------------+
| 6                  | Strand      | Character ("+" or "-") | BED6+          |
+--------------------+-------------+------------------------+----------------+
| 7+                 | Metadata    | String                 | Various        |
+--------------------+-------------+------------------------+----------------+

A BED record must minimally have three columns that define the genomic range of that record. Variants of BED with more than six columns exist. Records with more than six columns generally have display metadata associated with them, or represent specialized annotations.

BED records could be provided in any order. However, our analyses make use of `BEDOPS <https://github.com/bedops/bedops>`_ tools, which require a lexicographical sorting on the chromosome column, followed by numerical sort on the start and stop indices. BEDOPS includes a command-line tool called ``sort-bed`` to apply this ordering on BED records.

*Example of sorted BED6 data:*
::

  chr1    1000      2000 foo      0       +
  chr17   100       200  bar      1       -
  chr2    300       500  baz      3.14    -
  chrX    100       400  bing     2       +

Where data are not available for the fourth through sixth columns, it is conventional to use a period as a placeholder.

======
BEDOPS
======

Toolkit for management of and applying set and statistical operations on BED files (see: `https://github.com/bedops/bedops <https://github.com/bedops/bedops>`_).

========
DHS peak
========

Genomic range that (for this purpose) is the source of a long-range interaction with a target gene. Contains (or overlaps) transcription factors of interest.

====
Gene
====

A set of genomic ranges that has some function for an organism and is copied from one generation to the next.

===============
Gene annotation
===============

A set of genomic ranges that usually specifies the coordinates of a gene's components (*e.g.*, in eukaryotes like humans, exons and introns). 

=============
Gene promoter
=============

A genomic range that contains a transcription start site element.

=============
Genomic range
=============

Minimally, a chromosome name and a start/stop coordinate pair. Analogous to a BED3 element.

======================
Long-range interaction
======================

A pair of genomic ranges that connect a target gene's promoter with an overlapping DHS.

===========
Target gene
===========

A set of genomic ranges (representing the gene's promoters) that is the starting point for analyses. Filters or predicates are applied on this initial input set, which expand the regions covered over the genome to search for TFs.

====================
Transcription factor
====================

A transcription factor ("TF") is a protein that binds to DNA and controls how other proteins get made (or, indirectly, how cell signaling occurs). For a given transcription factor's name, we provide a set of locations on the genome (one or more genomic ranges) where that transcription factor binds. Obtaining a set of transcription factor binding sites is the end goal of the target viewer component of Targetscope.

.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim: