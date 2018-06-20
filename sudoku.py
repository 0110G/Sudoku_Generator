# ************************************************* SUDOKU SOLVER AND GENERATOR ************************************************************
# Instructions : To solve sudoku, initialize the matrix de to the required sudoku. To generate a sudoku, initialize the matrix de to all 0.
# AUTHOR : Bhavya Saraf
import random

#checks if the current sudoku is valid or not
def sudo_chk (x):
    
    #checks across rows 
    for i in x:
        for j in i:
            s = set()
            if j in s and j != 0 : return 0
            s.add(j)
            if j == 0:
                continue
    
    #checks across columns
    for i in range (9):
        s = set()
        for j in x:
            if j[i] in s and j[i]!= 0 : return 0
            s.add(j[i])
            if j[i] == 0:
                continue

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
                    if x[u][v] == 0:
                        continue

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

    return s 

#checks which position of the given sudoku are assigned values.
def sudo_chk_zero():
    sa=set()
    global de 
    for u in range(9) :
        for v in range (9):
            if de[u][v] != 0 :
                sa.add((u,v))
    return sa

#advances the sudoku indexes by one unit columnwise
def front_track():
    global i,j
    if j==8:
        i = i+1
        j = 0
    else:
        j = j+1

#generates the sudoku recursively and backtracking. In order to stay within recursive limits, variable sudo_iter is introduced.  
def sudo_gen ():
    global de,non_zero_pos
    global i
    global j

    if i*j == 64  :
        return 1

    if (i,j) not in non_zero_pos :
        

        sample_set = sudo_pos(de,i,j)
        while (len(sample_set)!=0) :
            de[i][j] = random.sample(sample_set,1)[0]
            rem_x = i
            rem_y = j
            sample_set.remove(de[i][j])
            front_track()
            if sudo_gen() == 1 :
                return 1
            i = rem_x
            j = rem_y
            de[rem_x][rem_y] = 0

        return 0

    else :
        front_track()
        if sudo_gen() == 1 :
            return 1 

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

#***************************INITIALIZE***********************************    
i = 0
j = 0
de = [[0,0,0,0,0,1,2,3,0],
      [1,2,3,0,0,8,0,4,0],
      [8,0,4,0,0,7,6,5,0],
      [7,6,5,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,1,2,3],
      [0,1,2,3,0,0,8,0,4],
      [0,8,0,4,0,0,7,6,5],
      [0,7,6,5,0,0,0,0,0]]

non_zero_pos = sudo_chk_zero()
if sudo_chk(de) == 0:
    print("NOT SOLVABLE")
else :
    
    if sudo_gen() == 0:
        print("NOT SOLVABLE")
    else :
        de[8][8] = random.sample(sudo_pos(de,8,8),1)[0]
        sudo_prt(de)
        print(sudo_chk(de))


                


