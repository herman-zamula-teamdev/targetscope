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

