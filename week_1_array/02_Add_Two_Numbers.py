# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        num1 = 0
        while l1 != None:            
            num1 += l1.val * (10 ** (i))           
            l1 = l1.next
            i +=1        
        i = 0
        num2 = 0
        while l2 != None:            
            num2 += l2.val * (10 ** (i))           
            l2 = l2.next
            i +=1
        num = num1 + num2        
        l =list()
        if num == 0:
            l.append(num) 
        while num != 0:         
            l.append(num % 10)
            num = num // 10
        return l
        
# Runtime: 140 ms，Memory Usage: 13.3 MB

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        node = head
        carry = 0
        while l1 and l2 :
            value = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1.val = value
            node.next = l1
            node = node.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            value = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1.val = value
            node.next = l1
            node = node.next
            l1 = l1.next
       
        while l2:
            value = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2.val = value
            node.next = l2
            node = node.next
            l2 = l2.next
            
        if carry :
            node.next = ListNode(carry)
        return head.next
            
        # Runtime: 104 ms,Memory Usage: 13.3 MB
