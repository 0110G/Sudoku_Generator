import random

count = 0		
i = 0						  #i is the row coordinate
j = 0						  #j is the column coordinate 
de = [[0,0,0,0,0,0,0,0,0],    #de is template sudoku 
	  [0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0,0]]

#checks if the current sudoku is valid or not
def sudo_chk (x):
	
	#checks across rows 
	for i in x:
		for j in i:
			s = set()
			if j in s and j != 0 : return 0
			s.add(j)
	
	#checks across columns
	for i in range (9):
		for j in x:
			s = set()
			if j[i] in s and j[i]!= 0 : return 0
			s.add(j[i])

	#checks across 3*3 grids
	for i in range (1,8,3):
		for j in range (1,8,3):
			s = set()
			temp_row = i+2
			temp_col = j+2
			for u in range (i-1,temp_row):
				for v in range (j-1,temp_col):
					if x[u][v] in s and x[u][v]!=0 : return 0
					s.add(x[u][v])

	return 1

#returns a set consisting of possible values at coordinates i,j
def sudo_pos (x,i,j):

	s = set([1,2,3,4,5,6,7,8,9])
	

	for u in range (9):

		if u!=i:
			if x[u][j]!=0:
				if x[u][j] in s:
					s.remove(x[u][j])

		if u!=j:
			if x[i][u]!=0:
				if x[i][u] in s:
					s.remove(x[i][u])

	temp_row = ((i//3)*3)+3
	temp_col = ((j//3)*3)+3
	
	for u in range ( ( (i//3)*3 ),temp_row):
		for v in range ( ( (j//3)*3),temp_col):
			if u!=i and v!=j:
				if x[u][v]!=0:
					if x[u][v] in s:
						s.remove(x[u][v])


	if len(s) == 0 : return 0
	return s 

sudo_iter = 0

#generates the sudoku recursively. In order to stay within recursive limits, variable sudo_iter is introduced.  
def sudo_gen ():
	global de
	global i
	global j
	global sudo_iter
	sudo_iter = sudo_iter + 1
	if (sudo_iter>900):
		return 0
	else :

		if i*j == 64 and len(sudo_pos(de,8,8))==1 :
			return 1

		else:
			if sudo_pos(de,i,j) == 0:
				i = 0
				j = 0
				sudo_gen()

			else:
				de[i][j] = random.sample(sudo_pos(de,i,j),1)[0]
				if j==8:
					i = i+1
					j = 0
				else:
					j = j+1

				sudo_gen()

#print sudoku generated
def sudo_prt(x):
	for i in range(9):
		for j in range(9):
			if (j+1)%3 == 0:
				print(x[i][j],end='   ')
			else:
				print(x[i][j],end=' ')
		if (i+1)%3 == 0:
			print()
			print()
		else:
			print()


while (len(sudo_pos(de,8,8)) != 1):
	count = count + 1
	sudo_iter = 0
	i = 0
	j = 0
	de = [[0,0,0,0,0,0,0,0,0],
	  	  [0,0,0,0,0,0,0,0,0],
	  	  [0,0,0,0,0,0,0,0,0],
	      [0,0,0,0,0,0,0,0,0],
	      [0,0,0,0,0,0,0,0,0],
	      [0,0,0,0,0,0,0,0,0],
	      [0,0,0,0,0,0,0,0,0],
	      [0,0,0,0,0,0,0,0,0],
	      [0,0,0,0,0,0,0,0,0]]
	sudo_gen()
	
de[8][8] = random.sample(sudo_pos(de,8,8),1)[0]

sudo_prt(de)	
print(sudo_chk(de))


				
				

