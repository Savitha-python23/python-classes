def sort_dict(d):
	sort_me = sorted(zip(d.values(), d.keys()))
	form_new_dict = {} # create
	for data in sort_me:
		form_new_dict[data[1]] = data[0]
	return form_new_dict # return 
input_dict = {"shiva": 24, "dinesh": 22, "subash": 21, "sanath": 29}
print(sort_dict(input_dict))