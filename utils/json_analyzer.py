'''
	Method to find the path pairs in any nested object of json type
'''
def find_paths(data, data_pairs={}, path=None):
	if isinstance(data, dict):
		for key, val in data.iteritems():
			if path is not None:
				find_paths(val, data_pairs, path+"."+key)
			else:
				find_paths(val, data_pairs, key)
	elif isinstance(data, list):
		for index in range(len(data)):
			if path is not None:
				find_paths(data[index], data_pairs, path+"["+str(index)+"]")
			else:
				find_paths(data[index], data_pairs,"["+str(index)+"]")
	if path is not None:
		data_pairs[path]=data
	else:
		data_pairs["."]=data

'''
	Method to check if two json objects are similar
'''
def check_similar(source, target):
	s_pairs={}
	t_pairs={}
	find_paths(source, s_pairs)
	find_paths(target, t_pairs)
	#if len(s_pairs.keys()) != len(t_pairs.keys()):
	#	return False, "Failure since length of paths in source {0} != target {1}".format(len(s_pairs.keys()), len(t_pairs.keys()))
	s_minus_t_diff_type = list(set(s_pairs.keys()) - set(t_pairs.keys()))
	t_minus_t_diff_type = list(set(t_pairs.keys()) - set(s_pairs.keys()))
	check_str=""
	check_logic=True
	if len(s_minus_t_diff_type) != 0:
		check_logic=False
		check_str += " Data path Error :: in souce data - target data  : {0}".format(s_minus_t_diff_type)
	if len(t_minus_t_diff_type) != 0:
		check_logic=False
		check_str +=  " Data path Error :: in data path in target data type - source data type : {0}".format(t_minus_t_diff_type)
	if not check_logic:
		return check_logic, check_str
	for s_k, s_v in s_pairs.iteritems():
		if type(s_v) != type(t_pairs[s_k]):
			check_logic=False
			check_str+=" for key :: {0} :: source data type {1} != target data type {2}".format(s_k, type(s_v), type(t_pairs[s_k]))
	return check_logic, check_str

def compare_data_type_pairs(source, target):
	check_logic=True
	check_str-""
	for d_type in source.keys():
		s_val=source[d_type]
		t_val=target[d_type]
		s_minus_t_diff_type = list(set(s_val.keys()) - set(t_val.keys()))
		t_minus_t_diff_type = list(set(t_val.keys()) - set(s_val.keys()))
		if len(s_minus_t_diff_type) != 0:
			check_logic=False
			check_logic + " Key Error Observed :: data type {0} :: (souce - target) :: {1}".format(d_type, s_minus_t_diff_type)
		if len(t_minus_s_diff_type) != 0:
			check_logic=False
			check_logic + " Key Error Observed :: data type {0} :: (souce - target) :: {1}".format(d_type, t_minus_s_diff_type)
		if check_logic:
			for s_k, s_v in s_val.iteritems():
				if type(s_v) != type(t_val[s_k]):
					check_logic=False
					check_str+=" for key {0}, source data type {1} != target data type {2}".format(s_k, type(s_v), type(t_val[s_k]))
		else:
			print "Values not being checked, restricting to schema !!!"
	return check_logic, check_str

'''
	Method to find data_type, path, value
'''
def find_type_pairs(data):
	type_pairs={}
	for k, v in data.iteritems():
		if not (isinstance(v, dict) and isinstance(v, list)):
			d_type=str(type(v))
			if d_type not in type_pairs.keys():
				type_pairs[d_type] = {}
			type_pairs[d_type][k]=v
	return type_pairs

'''
	Method to print data_type, path, values
'''
def print_type_pairs(type_pairs):
	for k, v in type_pairs.iteritems():
		print "---------------------------------------------------------"
		print " Type :: {0}".format(k)
		print "---------------------------------------------------------"
		for key, val in v.iteritems():
			print " {0} :: {1}".format(key, val)

'''
	Method to print path, value information
'''
def print_pairs(pairs):
	print "----------------------------------"
	print "Path value pairs"
	print "----------------------------------"
	for k, v in pairs.iteritems():
		print " {0} = {1}".format(k, v)

'''
	Method to print path information
'''
def print_paths(pairs):
	print "----------------------------------"
	print "Path values"
	print "----------------------------------"
	for k in pairs.keys():
		print k

data_pairs={}
sing_dim_array = [0, 1, 2]
multi_dim_array = [0, 1, 2, [ 0, 1, 2]]
blank_json = {}
simple_json = { "int_value": 1, "str_value": "sample_str_value", "null_value": None}
nested_json = { "int_value": 1, "str_value": "sample_str_value" , "json": simple_json}
data_set = { "simple_json":simple_json, "nestedjson": nested_json , "sing_dim_array": sing_dim_array, "multi_dim_array": multi_dim_array}
data_set_1 = { "simple_json":simple_json, "sing_dim_array": sing_dim_array, "multi_dim_array": multi_dim_array}
find_paths(data_set, data_pairs)
print_pairs(data_pairs)
print_paths(data_pairs)
t_pairs = find_type_pairs(data_pairs)
print_type_pairs(t_pairs)
print check_similar(data_set, data_set)
print check_similar(data_set, data_set_1)
print check_similar(data_set_1, data_set)
print check_similar({"array":[0, 1]}, {"array":[1, 1, 2]})
print check_similar({"field1":1}, {"array":[1, 1, 2]})
print check_similar({"field":1}, {"field":"str"})
print check_similar({"json":{"field":1}},{"json":{"field":"str"}})