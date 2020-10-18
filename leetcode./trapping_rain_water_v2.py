def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        max_element_idx = 0
        for i in range(len(height)):
            if height[i] > height[max_element_idx]:
                max_element_idx = i
                
        res = 0
        max_left = 0
        for i in range(max_element_idx):
            if height[i] < max_left:
                res += max_left - height[i]
            max_left = max(max_left, height[i])
        
        max_right = 0
        for i in range(len(height) - 1, max_element_idx, -1):
            if height[i] < max_right:
                res += max_right - height[i]
            max_right = max(max_right, height[i])
        return res
