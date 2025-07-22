import json
import os


def test_case_parameters(json_filename, arg="argumento", name="expected_status"):
    json_dir = os.path.join(os.path.dirname(__file__), "..", "tests", "data_test", json_filename)
    with open(json_dir, "r") as f:
        return [(case[arg], case[name]) for case in json.load(f)]
