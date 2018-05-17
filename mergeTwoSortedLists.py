# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l1_node = l1
    l2_node = l2
    output_list = []
    while l1_node and l2_node:
      print(l1_node.val, l2_node.val)
      if l1_node.val > l2_node.val:
        output_list.append(l2_node.val)
        l2_node = l2_node.next
      else:
        output_list.append(l1_node.val)
        l1_node = l1_node.next
    while l1_node:
      output_list.append(l1_node.val)
      l1_node = l1_node.next
    while l2_node:
      output_list.append(l2_node.val)
      l2_node = l2_node.next
    return output_list