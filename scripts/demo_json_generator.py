import sys
import os
import json
pwd = os.getcwd().replace("scripts","")
new_path="{0}".format(pwd)
sys.path.append(new_path)
from utils.json_generator import JSONGenerator

helper = JSONGenerator()

def print_nice(parsed):
	print json.dumps(parsed, indent=4, sort_keys=True)

def demo_single_dimension_array():
	print '\n Single Dimension Array with max array size = 10 \n'
	print_nice(helper.random_single_dimension_array(max_array_size = 10))

def demo_multi_dimension_array():
	print '\n Multi Dimension Array with max array size = 2 and dimensionality = 10 \n'
	print_nice =(helper.random_multi_dimension_array(max_array_size = 10))

def demo_random_json():
	print '\n Random JSON with nesting level = 1 \n'
	print_nice(helper.random_json())

def demo_nested_random_json():
	print '\n Random JSON with nesting level = 3 \n'
	print_nice(helper.nested_random_json(nested_level=3))

def demo_json_from_template():
	print '\n Random JSON from Template \n'
	sample_json= {"int_field":1, "float_field":1.1, "array_field": [0, 1], "json":{"int_field":1}}
	print " \n SAMPLE TEMPLATE \n"
	print_nice(sample_json)
	print " \n RANDOM JSON FROM TEMPLATE \n"
	print_nice(helper.gen_json_from_template(source = sample_json))

print "\n ------------------- JSON Generator DEMO ---------------------- \n"
print " --------- Random Generation without template ----------"
demo_single_dimension_array()
demo_multi_dimension_array()
demo_random_json()
demo_nested_random_json()
print " --------- Random Generation from template ----------"
demo_json_from_template()
print " --------------------------------------------------------------"
