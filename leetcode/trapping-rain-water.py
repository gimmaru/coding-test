height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [0, 1, 0, 2, 1, 0, 1, 3, 0, 1, 3, 1, 2, 1]
height = [2, 0, 2]
height = [2, 2]
height = [0]

result = 0
total_max = max(height)
r_pos, l_pos = len(height)-1, 0
r_max, l_max = 0, 0

while l_pos < r_pos:
	l_vol, r_vol = height[l_pos], height[r_pos]
	
	if l_max != total_max:
		if l_vol > l_max:
			l_max = l_vol
		else:
			result += l_max - l_vol
		
		if l_max != total_max:
			l_pos += 1
	
	if r_max != total_max:
		if r_vol > r_max:
			r_max = r_vol
		else:
			result += r_max - r_vol
		
		if r_max != total_max:
			r_pos -= 1

	if (l_max == total_max) and (l_max == r_max):
		break

if (l_pos+1) != r_pos:
	result += sum( [total_max - h for h in height[l_pos+1 : r_pos]] )

print(height)
print(result)