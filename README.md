# targetscope

We use the [JSON Schema v0.4](http://json-schema.org/) specification to write an initial schema document (``target_gene_schema.json``) that describes an object graph of inputs, outputs, and a vocabulary of intermediate operations ("predicates" and options) used for a subset of functionality in the Targetscope application.

The goal is to write a schema that is flexible enough to ultimately be used with the full application, as well as to be usable now with a web service to validate incoming requests.

We include a sample or test web request that follows the schema (``target_gene_test_request.json``) which can be validated with the included Python script (``target_gene_request_validation.py``) with the installation of the ``jsonschema`` package.

An initial pass at a specification for Targetscope entities and predicates is described in the ``targetscope_predicate_specification_outline.doc`` document. This document helps describe terminology used in the schema and in web service requests.