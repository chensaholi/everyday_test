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
        if not l1:
            return listToListNode(l2)
        if not l2:
            return listToListNode(l1)
        l1_list, l2_list = [], []
        while True:
            l1_list.append(l1.val)
            if l1.next == None:
                break
            l1 = l1.next
        while True:
            l2_list.append(l2.val)
            if l2.next == None:
                break
            l2 = l2.next
        ltemp = self.list_add(l1_list, l2_list)
        return listToListNode(ltemp)
    
    def list_add(self, l1, l2):
        l1.reverse()
        l2.reverse()
        l1_str, l2_str = '', ''
        for l in l1:
            l1_str += str(l)
        for l in l2:
            l2_str += str(l)
        result = int(l1_str) + int(l2_str)
        return self.int_to_list(result)
    
    def int_to_list(self, num):
        assert num >=0, "the num must be positive"
        if num< 10:
            return [num]
        num_list = []
        while True:
            a, b = divmod(num, 10)
            num_list.append(b)
            if a == 0:
                break
            num = a
        return num_list

def listToListNode(num_list):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in num_list:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

if __name__ == '__main__':
    print(Solution().int_to_list(1234))