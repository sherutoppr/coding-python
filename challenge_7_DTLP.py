num_string = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [2.34, 4.98, 10.47, 55.28]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]


print("\t\t Summary Table ")
print("\nthe variable num_strings is a " + str(type(num_string)))
print("it contain the elements : "+str(num_string))
print("the element "+str(num_string[0])+"is a "+str(type(num_string[0])))

print("\nthe variable num_strings is a " + str(type(num_ints)))
print("it contain the elements : "+str(num_ints))
print("the element "+str(num_ints[0])+"is a "+str(type(num_ints[0])))

print("\nthe variable num_strings is a " + str(type(num_floats)))
print("it contain the elements : "+str(num_floats))
print("the element "+str(num_floats[0])+"is a "+str(type(num_floats[0])))

print("\nthe variable num_strings is a " + str(type(num_lists)))
print("it contain the elements : "+str(num_lists))
print("the element "+str(num_lists[0])+"is a "+str(type(num_lists[0])))


# sorting the num_string and num_ints
num_string.sort()
num_ints.sort()
print("Now sorting the num_string and num_ints..")
print("sorted num_strings : "+str(num_string))
print("sorted num_ints : "+str(num_ints))

print("string are sorted alphabatically but interger are soted numerically!!!")


