import datetime
'''
challenge 9 learning : 
list.pop(x) --> pop the element at x index of list
list.insert(x,new_element) - add the new_element to idnex x

challenge 10 learning : 
print("asbf" + str(sorted(list, reverse = True))) - sort the list in print function
list.remove(e) - remove the element e from the list
'''

g_list = ["Meat", "Cheese"]
print("Welcome to the Grocery List App")

time  = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hh = str(time.hour)
minute = str(time.minute)

print("Current date and time is : "+month+"/"+day + " " + hh + "/" + minute)
print("you currently have " + g_list[0] + " and " + g_list[1] + "  in your list.")

for i in range(3):
    x = input("Type of food you want to add to the list : ").title()
    g_list.append(x)

print("here is grocery list : "+str(g_list))
g_list.sort()
print("here sorted grocery list : " + str(g_list))

print("simulating grocery shopping...")

while True:
    print("currently grocery list :" + str(len(g_list)) + " items")
    print(g_list)
    if len(g_list) == 2:
        print("sorry , store is out of " + g_list[0])
        x = input("what item u want instead : ").title()
        g_list.remove(g_list[0])
        g_list.append(x)
        break
    x = input("what food did u just buy : ").title()
    g_list.remove(x)
    print("removing "+x+" from the list..")


print("here is what remain in grocery list")
print(g_list)





