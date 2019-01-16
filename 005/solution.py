# author : chenshao

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        recyle_temp = numRows-1
        results = []
        col = len(s)/(numRows-1)
        temp_test = []
        for i in range(col):
            recyle = (i//numRows)*(2*numRows-2)
            if i%(numRows-1) == 0:
                results.append(s[recyle*(i//(numRows-1)):recyle*(i//(numRows-1))+numRows])
            else:
                temp_result = ''
                for j in range(1, numRows-1):
                    if i//recyle_temp +j != (recyle_temp-1):
                        temp_result += '0'
                    else:
                        temp_test.append(i//numRows)
                        temp_result += s[numRows*(i//numRows) + j]
                print temp_test
                results.append(temp_result)
        print results