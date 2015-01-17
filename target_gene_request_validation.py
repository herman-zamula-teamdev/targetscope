#!/usr/bin/env python

import json
from jsonschema import validate

schema_fh = open("target_gene_schema.json", "r")
schema = json.load(schema_fh)
test_request_fh = open("target_gene_test_request.json", "r")
test_request = json.load(test_request_fh)
validate(test_request, schema)
