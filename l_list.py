#!/usr/bin/env python3
import random
import time
import array

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def getLast(self):
        if self.length == 0:
            return None
        return self.getNode(self.length-1)

    def getNode(self, index):
        node = self.head
        if node == None:
            return None
        
        count = 0
        while node != None:
            if count == index:
                return node
            node = node.next
            count += 1
        return None

    def push(self, data):
        node = self.getLast()
        if node == None:
            self.head = Node(data)
        else:
            node.next = Node(data)
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            node = self.head
            self.head = None
            self.length = 0
            return node
        
        node = self.getNode(self.length-1)
        self.getNode(self.length-2).next = None
        self.length -= 1
        return node
    
    def insertAfter(self, index, data):
        if index >= self.length:
            raise Exception("Tried inserting after list end.")

        self.length += 1

        if index == -1:
            old = self.head
            self.head = Node(data)
            self.head.next = old
            return
        
        node = self.getNode(index+1)
        node2 = self.getNode(index)
        node2.next = Node(data)
        node2.next.next = node

    def remove(self, index):
        if index >= self.length:
            raise Exception("Tried removing after list end.")
        
        self.length -= 1

        if index == 0:
            self.head = self.head.next
            return
        
        one_before = self.getNode(index-1)
        one_before.next = self.getNode(index+1)

    def sortAsc(self):
        current = self.head
        if current == None:
            return
        
        while(current.next != None):
            next = current.next
            while(next != None):
                if(current.data > next.data):
                    tmp = current.data
                    current.data = next.data
                    next.data = tmp
                next = next.next
            current = current.next
    
    def sortAsc(self):
        current = self.head
        if current == None:
            return
        
        while(current.next != None):
            next = current.next
            while(next != None):
                if(current.data < next.data):
                    tmp = current.data
                    current.data = next.data
                    next.data = tmp
                next = next.next
            current = current.next
    
    def find(self, to_find):
        node = self.head
        count = -1
        while node != None:
            count += 1
            if node.data == to_find:
                return count
            node = node.next
        return None
    
    def __str__(self):
        s = ""
        node = self.head
        while node != None:
            s += str(node.data)
            node = node.next
            if node != None:
                s += ", "
        return s
    
def sortAsc(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    
def sortDesc(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] > a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

if __name__ == '__main__':
    #linked list
    list = LinkedList()
    start = time.time()
    for x in range(0,10000):
        list.push(random.randint(0, 100000))
    t = time.time() - start
    print("Fill time:" + str(t))

    start = time.time()
    list.sortAsc()
    t = time.time() - start
    print("Sort time:" + str(t))

    #array
    a = array.array('i')
    start = time.time()
    for x in range(0,10000):
        a.append(random.randint(0, 100000))
    t = time.time() - start
    print("Fill time:" + str(t))

    start = time.time()
    sortAsc(a)
    t = time.time() - start
    print("Sort time:" + str(t))