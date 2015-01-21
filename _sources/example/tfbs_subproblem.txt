.. _example_tfbs_subset:

Target gene-to-TFBS subproblem
==============================

In the process of building a framework to run the *targetscope* application, we want to build a smaller problem that can be used to start creating a web service that will accept requests, process dependencies and push responses.

We start with the larger problem described in the :ref:`target gene-to-TFBS <example_tfbs>` document:

**Inputs**
        1. :ref:`Set <compound_set>` of target gene :ref:`transcription start sites <compound_element>` (TSSs)
        2. :ref:`Set <compound_set>` of all correlated :ref:`interactions <compound_interaction>` (pairings of promoter :ref:`regions <compound_element>` and distal element regions)

**Outputs**
        1. :ref:`Set <compound_set>` of target gene TSSs, filtered on the :ref:`gene name <base_name>` RARA ("RARA TSSs")
        2. :ref:`Set <compound_set>` of all correlated :ref:`interactions <compound_interaction>` that are filtered on the set of RARA TSSs

**Operations**
        1. :ref:`Filter operation <ops_filter>` that creates "RARA TSSs" set
        2. :ref:`Map operation <ops_map>` that finds all RARA TSSs that overlap interaction promoter regions

Here is a graphical overview of the pipeline:

.. image:: ../../_static/tfbs_rara_subproblem.png
   :width: 50%

One of the two outputs is in the middle of the pipeline. The web service will generate a list of intermediate dependencies and push them to the next step of analysis, as needed.

A web request that embodies these operations, sets and parameters might begin to look like this:

.. code-block:: json

  {
    "version" : "v1.1.0",
    "dtsubmission": "2014-08-13T00:21:17", 
    "id": "abcd1234", 
    "name": "Test request graph for finding RARA TSSs that associate with interaction promoters", 
    "operations": [
        {
            "id": "map_rara_TSSs_to_interaction_promoters", 
            "name": "Map RARA TSSs to interaction promoters", 
            "parameters": [
                {
                    "arguments": [
                        {
                            "options": [
                                {
                                    "kind": "filter_interaction_component", 
                                    "value": "0"
                                },
                                {
                                    "kind": "set_overlap_bases",
                                    "value": "1"
                                }
                            ], 
                            "sets": [
                                {
                                    "id": "0001_rara_TSSs", 
                                    "kind": "input_map"
                                }, 
                                {
                                    "id": "0002_all_interactions", 
                                    "kind": "input_reference"
                                }, 
                                {
                                    "id": "0003_all_interactions_between_rara_tss_and_promoters", 
                                    "kind": "output"
                                }
                            ]
                        }
                    ], 
                    "kind": "element_set_map_on_interaction_set"
                }
            ], 
            "summary": "Build a list of interaction promoters and RARA TSSs which overlap the promoter region"
        }, 
        {
            "id": "element_filter_TSSs", 
            "name": "Filter TSSs by RARA", 
            "parameters": [
                {
                    "arguments": [
                        {
                            "options": [
                                {
                                    "kind": "filter_name", 
                                    "value": "RARA"
                                }
                            ], 
                            "sets": [
                                {
                                    "id": "0000_target_gene_TSSs", 
                                    "kind": "input"
                                }, 
                                {
                                    "id": "0001_rara_TSSs", 
                                    "kind": "output"
                                }
                            ]
                        }
                    ], 
                    "kind": "element_set_filter_name"
                }
            ], 
            "summary": "We take the target gene TSSs and filter them on the name RARA"
        }
    ], 
    "sets": [
        {
            "id": "0000_target_gene_TSSs", 
            "kind": "element"
        }, 
        {
            "id": "0001_rara_TSSs", 
            "kind": "element"
        }, 
        {
            "id": "0002_all_interactions", 
            "kind": "interaction"
        }, 
        {
            "id": "0003_all_interactions_between_rara_tss_and_promoters", 
            "kind": "interaction"
        }
    ]
  }