class Solution(object):
    def myAtoi(self, num_str):
        """
        :type str: str
        :rtype: int
        """
        num_str = num_str.strip()
        temp_s = tuple(str(i) for i in range(10))
        minus_flag = 1
        if num_str.startswith('-'):
            minus_flag = -1
            num_str = num_str[1:]
        elif num_str.startswith('+'):
            num_str = num_str[1:]
        if not num_str.startswith(temp_s):
            return 0
        re_str = ''
        for x in num_str:
            if x not in temp_s:
                break
            re_str += x
        if int(re_str)*minus_flag > pow(2, 31)-1:
            return pow(2, 31) -1
        if int(re_str)*minus_flag < -1*pow(2, 31):
            return -pow(2, 31)
        return int(re_str) * minus_flag