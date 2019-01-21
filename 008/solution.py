class Solution(object):
    '''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=1:
            return 0
        temp_max_area = 0
        len_height = len(height)
        for i in range(len_height-1):
            for j in range(i+1, len_height):
                temp_height_min = height[i] if height[i] < height[j] else height[j]
                temp_area = (j-i) * temp_height_min
                if temp_area > temp_max_area:
                    temp_max_area = temp_area
        return temp_max_area
    '''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_area = 0
        while l<r:
            max_temp = (r-l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            if max_temp > max_area:
                max_area = max_temp
        return max_area