class Node:
    def __init__(self,value):
        self.value  = value
        self.next = None
        self.pre = None

class Double:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert_F(self,value):
        x = Node(value)
        if self.head == None or self.tail == None:
            self.head = x
            self.tail = x
        else:
            temp = self.head
            x.next = temp
            temp.pre = x
            self.head = x

    def Insert_L(self,value):
        x = Node(value)
        if self.head == None or self.tail == None:
            self.head = x
            self.tail = x
        else:
            temp = self.tail
            temp.next = x
            x.pre = temp
            self.tail = x

    def Insert_M(self,add,value):
        x = Node(value)
        if self.head == None or self.tail == None:
            self.head = x
            self.tail = x
        else:
            temp = self.head
            while temp:
                if temp.value == add:
                    x.next = temp.next
                    temp.next.pre = x
                    temp.next = x
                    x.pre = temp
                    break
                else:
                    temp = temp.next

    def Delete_F(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            self.head = temp.next
            self.head.pre = None
            temp = None

    def Delete_L(self):
        temp = self.tail
        self.tail = temp.pre
        self.tail.next = None
        temp = None

    def Delete_M(self,add):
        temp = self.head
        while temp:
            if temp.value == add:
                temp.next.pre = temp.pre
                temp.pre.next = temp.next
                break
            else:
                temp = temp.next

    def replace(self,add,value):
        temp = self.head
        while temp:
            if temp.value == add:
                temp.value = value
            else:
                temp = temp.next

    def Delete_All(self,value):
        if self.head == None:
            print('empty')
        else:
            if self.head.value == value:
                self.Delete_F()
                self.Delete_All(value)
                return
            elif self.tail.value == value:
                self.Delete_L()
                self.Delete_All(value)
                return
            else:
                temp = self.head
                while temp:
                    if temp.value == value:
                        temp.next.pre = temp.pre
                        temp.pre.next = temp.next
                        self.Delete_All(value)
                        return
                    else:
                        temp = temp.next

    def sum(self):
        if self.head == None:
            print('empty')
        else:
            sum = 0
            temp = self.head
            while temp:
                sum = sum + temp.value
                temp = temp.next
            return sum

    def lenght(self):
        temp = self.head
        length = 0
        while temp:
            length = length + 1
            temp = temp.next
        return length



    def print(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.head
            while temp:
                print(temp.value, end=' ')
                temp = temp.next

    def printR(self):
        if self.head == None:
            print('empty')
        else:
            temp = self.tail
            while temp:
                print(temp.value, end= ' ')
                temp = temp.pre

a = Double()
a.Insert_F(2)
a.Insert_F(3)
a.Insert_F(10)
a.Insert_F(5)
a.Insert_F(6)
a.Insert_F(7)
a.Insert_L(10)
a.Insert_L(234)
a.Insert_L(43)
a.Insert_L(3)
a.Insert_L(99)
a.Insert_L(2)
a.Insert_M(5,43)
a.Delete_F()
a.Delete_L()
a.Delete_M(234)
a.replace(10,11)
a.Delete_All(11)
a.Delete_All(3)
a.print()
print(' ')
a.printR()
print('')
print('sum is ', a.sum())
print('')
print('lenght is ', a.lenght())