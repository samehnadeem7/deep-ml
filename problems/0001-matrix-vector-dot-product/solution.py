def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0])==len(b):
		result=[]
		
		for j in range (len(a)):
			sum=0
			for i in range (len(b)):

				sum=sum+a[j][i]*b[i]
			result.append(sum)
		return result



	else:
		return -1
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	