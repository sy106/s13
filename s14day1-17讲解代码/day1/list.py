__author__ = "Alex Li"

names = [ 'alex', '1eric','chushi ge','jack' ,'rain','#jack']

py_names = ["kandao ge","..."]
#name_count = names.count("jack")
#print("count:",name_count)
#names.append("")
names.insert(3,'qian ge')
#names.clear()
name_index = names.index("jack")
names[name_index] = "JACK"
names.remove("chushi ge")
names.sort()

names.extend(py_names)

print(names,name_index,names[name_index])
names.reverse()
print(names,name_index,names[name_index])