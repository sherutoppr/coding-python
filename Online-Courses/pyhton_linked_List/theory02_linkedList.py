class LinkedList:

    # nested class represent the element of linked list
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    # constructor of linked list
    def __init__(self):
        self.head = None
        self.size = 0

    # get size of linked list
    def length(self):
        return self.size

    def isEmpty(self):
        return self.size==0

    # insert at the starting
    def addHead(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1
    
    # insert at the ending
    def addTail(self, value):
        if not self.isEmpty():
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = self.Node(value)
            self.size += 1
        else:
            self.addHead(value)

    # insert sorted
    def insertSorted(self, value):
        newnode = self.Node(value)
        curr = self.head
        if curr==None or curr.val > value:
            newnode.next = self.head
            self.head = newnode
            self.size += 1
            return
        while curr.next and curr.next.val < value:
            curr = curr.next
        newnode.next = curr.next
        curr.next = newnode
        self.size += 1

    # search the element in the linked list
    def isPresent(self, value):
        curr = self.head
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False

    # delete the first element
    def removeHead(self):
        if self.isEmpty():
            raise RuntimeError("empty list exception")
        value = self.head.val
        self.head = self.head.next
        self.size -= 1
        return value

    # delete by value
    def deleteNode(self, value):
        if self.isEmpty():
            return False
        if self.head.val == value:
            self.head = self.head.next
            self.size -= 1
            return True

        curr = self.head
        while curr.next:
            if curr.next.val == value:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    # delete all occurances
    def deleteAllNode(self, value):
        curr = self.head
        while curr and curr.val == value:
            self.head = curr.next
            curr = self.head
            self.size -= 1
        while curr:
            nextnode = curr.next
            if nextnode and nextnode.val == value:
                curr.next = nextnode.next
                self.size -= 1
            else:
                curr = curr.next

    # delete the single link list
    def freeList(self):
        self.head = None
        self.size = 0

    # reverse the linked list
    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    # remove duplicate from sorted list
    def RemoveDuplicate(self):
        curr = self.head
        while curr:
            if curr.next and curr.next.val==curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

    # compare lists
    def CompareList(self, l2):
        if self.CompareListUtil(self.head, l2.head):
            return "Both are same list"
        else:
            return "Not same"

    # compare list helper function
    def CompareListUtil(self, head1, head2):
        if head1 == None and head2 == None:
            return True
        elif (head1==None) or (head2==None) or (head1.val != head2.val):
            return False
        else:
            return self.CompareListUtil(head1.next, head2.next)

    # copy the list to another reversely
    def CopyListReverse(self):
        curr1 = self.head
        prev2 = None
        while curr1:
            curr2 = self.Node(curr1.val)
            curr2.next = prev2
            prev2 = curr2
            curr1 = curr1.next

        l2 = LinkedList()
        l2.head = prev2
        return l2

    # traversing the linked list
    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        print("")


if __name__ == "__main__":
    ll = LinkedList()
    val = [2,4,1,8,4,6,9,10]
    for v in val:
        ll.insertSorted(v)
    ll.PrintList()
    ll2 = ll.CopyListReverse()
    ll2.PrintList()
    ll.reverse()
    print(ll.CompareList(ll2))






