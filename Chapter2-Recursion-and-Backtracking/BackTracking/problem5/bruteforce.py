
def scanGraphForConnections(g):
	length = 0;
	maxlength = 0;
	i = j = 0;
	rows = len(graph)
	cols = len(graph[0])
	while(i < rows):
		while(j < rows):
			if g[i][j] == 1 :
				length+=1

			if length > maxlength:
				maxlength = length

			if j+1 < cols and g[i][j+1] == 1:
				j+=1
			elif i+1 < rows and g[i+1][j] == 1:
				i+=1
			elif i+1 < rows:
				i+=1
				j=0
				length=0
			else:
				length=0
				return maxlength
	return maxlength;


graph = [[1,1,0,0,0],
	 [0,1,1,0,0],
  	 [0,0,1,0,1],
	 [1,0,0,0,1],
	 [0,1,0,1,1]]


maxlength = scanGraphForConnections(graph)
print(maxlength)
