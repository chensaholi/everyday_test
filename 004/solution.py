class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x>pow(2, 31)-1 or x < pow(2, 31)*(-1):
            return 0
        np_flag = 1 if x >=0 else -1
        x = abs(x)
        result = ''
        while True:
            m, n = divmod(x, 10)
            result += str(n)
            x = m
            if m == 0:
                break
        result = int(result)
        if result>pow(2, 31)-1:
            return 0
        return np_flag * result