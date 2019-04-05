class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not len(heights):return 0
        stack = [0] ; area = 0 ; maxArea = 0 ; i = 1
        while (i<len(heights)):
            if heights[i]>=heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) and heights[stack[-1]]>heights[i]:
                    top = stack.pop()
                    if len(stack):
                        area = heights[top]*(i-1-stack[-1])
                    else:
                        area = heights[top]*i
                    maxArea = max(maxArea,area)
                stack.append(i)
            i+=1
        while len(stack):
            top = stack.pop()
            if len(stack):
                area = heights[top]*(i-1-stack[-1])
            else:
                area = heights[top]*i
            maxArea = max(maxArea,area)

        return maxArea
