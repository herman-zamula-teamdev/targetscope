# targetscope

We use the [JSON Schema v0.4](http://json-schema.org/) specification to write an initial schema document (``target_gene_schema.json``) that describes an object graph of inputs, outputs, and a vocabulary of intermediate operations ("predicates" and options) used for this subsetted portion of the Targetscope application, which is intended to be flexible enough to be used with the full application, as well as to allow the web service to validate incoming requests.

We include a sample or test web request that follows the schema (``target_gene_test_request.json``) which can be validated with the included Python script (``target_gene_request_validation.py``) with the installation of the ``jsonschema`` package.