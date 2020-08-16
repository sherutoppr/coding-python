'''
Given a string ,find the length of longest substring without repeating character.
time = o(n)
space = o(1)
'''

def lswrc(s):

    last_char = {}
    start = 0
    res = 0

    for i,c in enumerate(s):

        if c in last_char and last_char[c] >= start:
            start = last_char[c]+1
        else:
            res = max(res,i-start+1)

        last_char[c] = i

    return res









s = "abacbdbsbabsbc"

res = lswrc(s)
print("longest substring without repeating character in {} is {} ".format(s,res))