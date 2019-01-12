def get_not_repeat_seq(l):
    not_repeat_seq = ''
    for x in l:
        if x not in not_repeat_seq:
            not_repeat_seq += x
            continue
        break
    return (not_repeat_seq, len(not_repeat_seq))


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s_temp = []
        for i in range(len(s)):
            if not s[i:]:
                break
            s_temp.append(get_not_repeat_seq(s[i:]))
        # print s_temp
        return sorted(s_temp, key=lambda item:item[1])[-1][1]