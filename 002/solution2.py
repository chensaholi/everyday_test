# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ltemp = []
        while True:
            if l1 and l2 and l1.val == 0 and l2.val ==0:
                l12 = 0
            elif l1 and l2 and l1.val == 0 and l2.val:
                l12 = l2.val
            elif l1 and l2 and l1.val and l2.val == 0:
                print l1.val, l2.val
                l12 = l1.val
            elif l1 and l2 and l1.val and l2.val:
                l12 = l1.val + l2.val
            elif l1 and l2 and not l1.val and not l2.val:
                break
            elif l1 and not l1.val:
                if l2:
                    ltemp.append(l2.val)
                    l2 = l2.next
                if l2 and not l2.val and l2.val != 0:
                    break
            else:
                ltemp.append(l1.val)
                l1 = l1.next
                if l1 and not l1.val and l1.val !=0:
                    break

            if l12<10:
                ltemp.append(l12)
            else:
                ltemp.append(l12-10)
                if l1 and not l1.next:
                    ltemp.append(1)
                    break
                if l1 and l1.next:
                    l1.next.val += 1

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1:
                break
        return listToListNode(ltemp)

def listToListNode(num_list):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in num_list:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr