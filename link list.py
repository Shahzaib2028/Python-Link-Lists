class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class link_list:
    def __init__(self):
        self.head = None
        self.tail = None



    def Insert_First(self,value):
        x = Node(value)
        if self.head == None and self.tail == None:
            self.head = x
            self.tail = x
        else:
            temp = self.head
            x.next = temp
            self.head = x

    def Insert_Last(self,value):
        x = Node(value)
        temp = self.tail
        if self.head == None and self.tail == None:
            self.head = x
            self.tail = x
        else:
            temp.next = x
            self.tail = x

    def Insert_Middle(self,add,value):
        x = Node(value)
        temp = self.head
        while temp.next:
            if temp.value == add:
                x.next = temp.next
                temp.next = x
                break
            else:
                temp = temp.next

    def Delete_First(self):
        temp = self.head
        temp = temp.next
        self.head = temp

    def Delete_End(self):
        p = self.head
        q = self.head.next
        while q.next:
            p = p.next
            q = q.next
        p.next = None
        return q


    def Delete_Value(self,value):
        p = self.head
        q = self.head.next
        while q:
            if q.value == value:
                p.next = q.next
                break
            else:
                p = p.next
                q = q.next


    def replace(self,add,value):
        temp = self.head
        while temp.next:
            if temp.value == add:
                temp.value = value
                break
            else:
                temp = temp.next


    def Print(self):
        if self.head == None:
            return False

        x = self.head
        while x:
            print(x.value, end=' ')
            x = x.next

    def ReverseL(self):
        self._ListR(self.head)

    def _ListR(self,temp):
        while temp:
            self._ListR(temp.next)
            print(temp.value, end=' ')
            return


a = link_list()
a.Insert_First(2)
a.Insert_First(3)
a.Insert_First(5)
a.Insert_First(4)
a.Insert_Last(5)
a.Insert_Last(6)
a.Insert_Middle(2,7)
a.Delete_First()
#a.Delete_End()
#a.Delete_Value(7)
#a.replace(2,9)

a.Print()

