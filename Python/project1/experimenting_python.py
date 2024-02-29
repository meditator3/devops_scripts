string = """asjdhaksjhd\n"""
print(string)
print("new libne")
string2 = string.strip('\n')
print(string2)
print("new libne")

array = ["11:00\n"]
print(array)
new = array[0].strip(":00\n")
print(new)
new_int = int(new)
newest = new_int+1
newest_int = f"{newest}:00"
print(newest_int)
arr = [1,2,3,4,5]
#print(arr)
arr2 = "1 3 4 5 6 "
if 1 in arr:
    print("ARR")

stringes = "1 2 3 4"
print(stringes[1:]) # from index=1 and forth
strgs = stringes.split(" ")
print(strgs)
print(type(strgs))
print(len(stringes))
string3 = "abcdefgh"
word = ""
for index in range(0,4):
    word +=string3[index]
word_list = [word]
print(word_list)
