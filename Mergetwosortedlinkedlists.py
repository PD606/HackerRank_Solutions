#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):

    # temp=SinglyLinkedListNode

    if(head1.data<head2.data):
        temp=head1
        head1=temp.next
    else:
        temp=head2
        head2=temp.next

    nh=temp

    while(head1 != None and head2 != None):

        if(head1.data <= head2.data):
            temp.next=head1
            temp=head1
            head1=temp.next
            
        else:
            temp.next=head2
            temp=head2
            head2=temp.next
    
    if(head1!=None):
        temp.next=head1
        temp=head1
        head1=temp.next
    else:
        temp.next=head2
        temp=head2
        head2=temp.next
               
    return nh
        

if __name__ == '__main__':