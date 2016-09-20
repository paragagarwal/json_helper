import sys
import os
import json
pwd = os.getcwd().replace("scripts","")
new_path="{0}".format(pwd)
sys.path.append(new_path)
from utils.json_analyzer import *

sing_dim_array = [0, 1, 2]
multi_dim_array = [0, 1, 2, [ 0, 1, 2]]
blank_json = {}
simple_json = { "int_value": 1, "str_value": "sample_str_value", "null_value": None}
nested_json = { "int_value": 1, "str_value": "sample_str_value" , "json": simple_json}
source_json = { "simple_json":simple_json, "nestedjson": nested_json , "sing_dim_array": sing_dim_array, "multi_dim_array": multi_dim_array}
target_json = { "simple_json":simple_json, "sing_dim_array": sing_dim_array, "multi_dim_array": multi_dim_array}

def print_nice(parsed):
	print json.dumps(parsed, indent=4, sort_keys=True)

def demo_find_path_simple_json():
	print "========================================="
	print "\n Will find all paths in simple JSON \n"
	print "\n Sample JSON \n"
	data_pairs={}
	print_nice(simple_json)
	find_paths(simple_json, data_pairs)
	print_pairs(data_pairs)
	print "========================================="

def demo_find_path_simple_json():
	print "========================================="
	print "\n Will find all paths in nested JSON \n"
	print "\n Nested JSON \n"
	data_pairs={}
	print_nice(nested_json)
	find_paths(nested_json, data_pairs)
	print_pairs(data_pairs)
	print "========================================="

def demo_json_comparison_diff_jsons():
	print "========================================="
	print "\n Will differences between two JSON objects \n"
	print "\n SOURCE JSON \n"
	print_nice(source_json)
	print "\n TARGET JSON \n"
	print_nice(target_json)
	print "\n OUTPUT \n"
	print check_similar(source_json, target_json)
	print "========================================="

def demo_json_comparison_sim_jsons():
	print "========================================="
	print "\n Will differences between two JSON objects \n"
	print "\n SOURCE JSON \n"
	print_nice(source_json)
	print "\n TARGET JSON \n"
	print_nice(source_json)
	print "\n OUTPUT \n"
	print check_similar(source_json, source_json)
	print "========================================="

print "\n ------------------- JSON Analyzer DEMO ---------------------- \n"
print "\n Demo path finding in JSON objects \n"
demo_find_path_simple_json()
demo_find_path_simple_json()
print "\n Demo path JSON comparison \n"
demo_json_comparison_diff_jsons()
demo_json_comparison_sim_jsons()