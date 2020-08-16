print("welcome to challenge 11")
n = int(input("how many value u want to convert : "))
val = [x for x in range(1, n+1)]
binval = [bin(x) for x in val]
hexaval = [hex(x) for x in val]
print("lists are complete ")
start = int(input("starting index of values : "))
end = int(input("ending index of values : "))
print("\n your list : ")
print("\n decimal \t binary \t hexadecimal ")
for x in range(start-1, end):
    print("\n " + str(val[x]) + "\t\t" + str(binval[x]) + "\t\t" + str(hexaval[x]))


input("press ENTER to watch entire list : ")
for d,b,h in zip(val,binval,hexaval):
    print(str(d) + "\t\t" + str(b) + "\t\t" + str(h))
