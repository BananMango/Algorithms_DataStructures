def inverse_tree(direct, center):
    global result
    root = direct[0]
    root_index_center = center.index(root)
    
    left_sub_center = center[:root_index_center]
    right_sub_center = center[root_index_center + 1:]
    
    left_sub_direct = direct[1:len(left_sub_center) + 1]
    right_sub_direct = direct[len(left_sub_center) + 1:]
    
    if len(left_sub_center) != 0 and len(left_sub_direct) != 0:
        inverse_tree(left_sub_direct, left_sub_center)
    if len(right_sub_center) != 0 and len(right_sub_direct) != 0:
        inverse_tree(right_sub_direct, right_sub_center)
    result += root


if __name__ == '__main__':
	n = int(input())
	for i in range(n):
		result = ''
		number_nodes, direct, center = input().split()
		inverse_tree(direct, center)
		print(result)