# tag : aztek_v_1.0.3.300
# increment last version number by 1 each call of function

tag = "aztek_v_1.0.3.300"
# remove . and extract last number
arr_str = tag.split(".")
print("tag at first:", tag)
def extract_v_num(tag):
    return arr_str[len(arr_str)-1]

tag_num = int(extract_v_num(tag))

#returns incremented version number with full str name
def increment_version_number_return_full_tag (tag_num, list):
    tag_num+=1
    list[len(list)-1] = str(tag_num)
    new_version = '.'.join(list)
    tag = new_version
    return tag
print("list:", arr_str)
print("tag:",tag)

print("extracted version number:", extract_v_num(tag))
tag = increment_version_number_return_full_tag(int(extract_v_num(tag)), arr_str)

print("new tag: ",tag)
tag = increment_version_number_return_full_tag(int(extract_v_num(tag)), arr_str)
print("newer tag: ",tag)
