'''
you are given two linked list representing two non-negative number.
the digit are sorted in reverse order and each node contain a single digit.
add two number and return it as a linked list
time - o(max(m,n))  where m and n are length of input of l1 and l2 respectively
space - o(max(m,n))
'''

class ListNode:

    def __init__(self,x=None):
        self.val = x
        self.next = None



def AddTwoNumber(l1,l2):


    prev= result= ListNode()
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next


        prev.next = ListNode(carry%10)

        prev = prev.next
        carry = carry // 10

    return result.next



l1 = ListNode(5)
l1.next = ListNode(5)

t1 = l1
while t1 is not None:
    print(t1.val,end=" ")
    t1 = t1.next

print()
l2 = ListNode(8)
l2.next = ListNode(6)

t2 = l2

while t2 is not None:
    print(t2.val, end=" ")
    t2 = t2.next

print()

result = AddTwoNumber(l1,l2)

while result is not None:
    print(result.val,end=" ")
    result = result.next








