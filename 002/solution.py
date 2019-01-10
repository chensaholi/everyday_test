# author : shaolichen
# Definition for singly-linked list.

import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ltemp = []
        while True:
            if l1.val == 0 and l2.val:
                l12 = l1.val + l2.val
            elif l1.val and l2.val == 0:
                l12 = l1.val + l2.val
            elif l1.val and l2.val:
                l12 = l1.val + l2.val
            elif not l1.val and not l2.val:
                break
            elif not l1.val:
                ltemp.append(l2.val)
                l2 = l2.next
                if not l2.val and l2.val != 0:
                    break
            else:
                ltemp.append(l1.val)
                l1 = l1.next
                if not l1.val and l1.val !=0:
                    break

            if l12<10:
                ltemp.append(l12)
            else:
                ltemp.append(l12-10)
                if not l1.next:
                    ltemp.append(1)
                    break
                l1.next.val += 1

            l1 = l1.next
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

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()