'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def length(self , head):
        if head:
            return 1+ self.length( head.next)
        return 0
    

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        size = self.length(head)
        print(size, size-n)
        pos = size-n
    
        if(pos<0):
            return head
    
        if pos == 0:
            return head.next
    
    
        currpos = 0
        curr = head
        prev = None
        next = curr.next
    
        while next and currpos < pos :
            prev = curr
            curr = next
            next = next.next
            currpos += 1
    
        prev.next = next
    
        return head
        