





def help(s,left,right):
    l_index = 0
    r_index = 0

    while left >= 0 and right < len(s):

        if s[left] == s[right]:
            l_index = left
            r_index = right
        else:
            break

        left -= 1
        right += 1

    return s[l_index:r_index+1]






def lps(s):

    res = ""

    for i in range(len(s)):
        c_word = help(s,i,i)
        c_line = help(s,i,i+1)

        temp = c_word if len(c_word) > len(c_line) else c_line
        res = res if len(res) > len(temp) else temp

    return res













ss = ['racecar' ,' abbcbbc','google' ]

for s in ss:
    print(lps(s))