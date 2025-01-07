str = "abcdefab"

# which pair returns the most times
length = len(str)








                                                 # main sabroutine:
                #  method  1)  scan first pair, with rest of string. then scan second etc. add 1 for each find. << with arrays/list
                #  method 2(faster) use dict to populate and use get(key) to increment pair instances. 

# iterate and populate the dict
# dict can update value, since it knows the object key!
# 
def pair_more_than_one():
    times = 1
    starting_pair = str[0:2]
    print(f"starting_pair {starting_pair}")
    pairs = dict({starting_pair:times})
    for i in range (1, length) : # starts loop from second pair
        if i+1 < length:  # to avoid overflow
            pair_iterate = str[i]+str[i+1]  # current pair iteration
            print(pair_iterate)
            value_of_key = pairs.get(pair_iterate)  # extracts value number of instances from dict, if exists.
            sum = times  # gives value of 1 unless
            if value_of_key : # already has value in dict
                sum = value_of_key + times
            pairs.update({pair_iterate:sum})
            print(f"value_of_key - {value_of_key}")
            print(f"pairs = {pairs}") 
            times = 1

        if pairs.get(pair_iterate) > 1:    
            return pair_iterate, pairs.get(pair_iterate)
print(pair_more_than_one())

