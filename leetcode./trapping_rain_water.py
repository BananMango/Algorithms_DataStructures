def trap(self, height: List[int]) -> int:
	if len(height) == 0:
		return 0
        
    max_left = [None] * len(height)
    max_left[0] = height[0]
    for i in range(1, len(height)):
		max_left[i] = max(height[i], max_left[i-1])
	
	max_right = [None] * len(height)
    max_right[-1] = height[-1] 
    for i in range(len(height)-2, -1, -1):
		max_right[i] = max(height[i], max_right[i+1])
	
	res = 0
    for i in range(len(height)):
		if height[i] < max_right[i] and height[i] < max_left[i]:
			res += min(max_right[i], max_left[i]) - height[i]
	return res
