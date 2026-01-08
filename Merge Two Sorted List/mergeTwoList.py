'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4
tail: 1 -> 2 -> 4
'''

class ListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        tail = dummy
        
        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                tail.nextNode = list1
                list1 = list1.nextNode
                print('list1', list1.nextNode, end=' -> ')
            else:
                tail.nextNode = list2
                list2 = list2.nextNode
                print('list2', list2.nextNode, end=' -> ')
            tail = tail.nextNode
        
        if list1 is not None:
            tail.nextNode = list1
        elif list2 is not None:
            tail.nextNode = list2
        
        return dummy.nextNode

# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))   
merged_list = Solution().mergeTwoLists(list1, list2)
while merged_list is not None:
    print(merged_list.value, end=" -> ")
    merged_list = merged_list.nextNode
print("None")