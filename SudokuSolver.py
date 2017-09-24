import math
global EMPTY_ENTRY 

EMPTY_ENTRY =0

def validToAddVal(partialAssignment, i,  j,  val) :
    
    #may be fast to use list.index ?
    #// Check row constraints.
    for element in partialAssignment: # (List<Integer> element : partialAssignment):
        if (val == element[j]):
            return False
    

     #// Check column constraints.
    lenPA =len(partialAssignment)
    for k in range(0,lenPA): # (int k = ®; k < partialAssignment.size(); ++k) {
        if (val == partialAssignment[i][k]):
            return False
 
    #// Check region constraints.
    regionSize = int(math.sqrt( len(partialAssignment)))
    I = i / regionSize
    J = j / regionSize
    for a in range(regionSize) : # (int a = ® ; a < regionSize; ++a) {
        for b in range(regionSize): # (int b = ® ; b < regionSize; ++b) {
            if (val == partialAssignment[(regionSize * I + a)][(regionSize * J + b)]):
                return False
   
    
    return True 





def solveSudoku(partialAssignment):
       #partialAssignment - 2 d array
    return solvePartialSudoku(0, 0, partialAssignment)

def solvePartialSudoku(i, j, partialAssignment):
    global EMPTY_ENTRY 
    if (i == len(partialAssignment)):
        i = 0 # Starts a new row.
        j =j+1
        if (j == len(partialAssignment[i])):
           return True #; // Entire matrix has been filled without conflict.
           #pass
    
    # // Skips nonempty entries.
    if (partialAssignment[i][j]!= EMPTY_ENTRY) :
        return solvePartialSudoku(i +1, j, partialAssignment)
    
    lenPartialAssignment =len(partialAssignment)+1
    for val in range (1, lenPartialAssignment): # (int val = 1; val <= partialAssignment.size(); ++val):
        #// It?s substantially quicker to check if entry val conflicts
        #// with any of the constraints if we add it at (i,j) before
        #// adding it, rather than adding it and then checking all constraints.
        #// The reason is that we are starting with a valid configuration,
        #// and the only entry which can cause a problem is entryval at (i,j).
        if (validToAddVal(partialAssignment , i, j, val)):
            partialAssignment[i][j]= val
            if (solvePartialSudoku(i + 1, j, partialAssignment)):
                return True 
    

    partialAssignment[i][j] = EMPTY_ENTRY #); // Undo assignment.
    return False



arr=[[0]*9 for i in range(9)]

arr[0][0] =5
arr[0][3] =3
arr[0][4] =9
arr[0][8] =7

arr[1][1] =6
arr[1][3] =7
arr[1][5] =1
arr[1][7] =2
arr[1][8] =8


arr[2][6] =9
arr[2][8] =3

#4th row
arr[3][0] =9
arr[3][2] =6
arr[3][3] =8
arr[3][6] =3
arr[3][7] =4

#5th row
arr[4][3] =4
arr[4][5] =6

#6th
arr[5][1] =2
arr[5][2] =4
arr[5][5] =5
arr[5][6] =1
arr[5][8] =6

#7th
arr[6][0] =4
arr[6][2] =3


#8th row
arr[7][0] =6
arr[7][1] =9
arr[7][3] =2
arr[7][5] =3
arr[7][7] =8

#9th row
arr[8][0] =7
arr[8][4] =6
arr[8][5] =9
arr[8][8] =4
###


arr[0][0]=0
arr[1][0]=0
arr[2][0]=8
arr[3][0]=0
arr[4][0]=0
arr[5][0]=5
arr[6][0]=0
arr[7][0]=1
arr[8][0]=0

arr[0][1]=0
arr[1][1]=5
arr[2][1]=0
arr[3][1]=0
arr[4][1]=3
arr[5][1]=7
arr[6][1]=0
arr[7][1]=0
arr[8][1]=4

arr[0][2]=6
arr[1][2]=0
arr[2][2]=7
arr[3][2]=0
arr[4][2]=0
arr[5][2]=0
arr[6][2]=0
arr[7][2]=0
arr[8][2]=0

arr[0][3]=8
arr[1][3]=7
arr[2][3]=0
arr[3][3]=0
arr[4][3]=0
arr[5][3]=3
arr[6][3]=0
arr[7][3]=0
arr[8][3]=9

arr[0][4]=0
arr[1][4]=0
arr[2][4]=0
arr[3][4]=0
arr[4][4]=0
arr[5][4]=0
arr[6][4]=0
arr[7][4]=0
arr[8][4]=0

arr[0][5]=3
arr[1][5]=0
arr[2][5]=0
arr[3][5]=7
arr[4][5]=0
arr[5][5]=0
arr[6][5]=0
arr[7][5]=6
arr[8][5]=1

arr[0][6]=0
arr[1][6]=0
arr[2][6]=0
arr[3][6]=0
arr[4][6]=0
arr[5][6]=0
arr[6][6]=6
arr[7][6]=0
arr[8][6]=8

arr[0][7]=5
arr[1][7]=0
arr[2][7]=0
arr[3][7]=2
arr[4][7]=9
arr[5][7]=0
arr[6][7]=0
arr[7][7]=3
arr[8][7]=0

arr[0][8]=0
arr[1][8]=6
arr[2][8]=0
arr[3][8]=4
arr[4][8]=0
arr[5][8]=0
arr[6][8]=2
arr[7][8]=0
arr[8][8]=0

############3
arr[0][0]=0
arr[1][0]=0
arr[2][0]=3
arr[3][0]=0
arr[4][0]=6
arr[5][0]=7
arr[6][0]=0
arr[7][0]=0
arr[8][0]=0

arr[0][1]=5
arr[1][1]=0
arr[2][1]=7
arr[3][1]=0
arr[4][1]=0
arr[5][1]=0
arr[6][1]=0
arr[7][1]=0
arr[8][1]=0

arr[0][2]=8
arr[1][2]=2
arr[2][2]=0
arr[3][2]=1
arr[4][2]=0
arr[5][2]=0
arr[6][2]=0
arr[7][2]=0
arr[8][2]=0

arr[0][3]=0
arr[1][3]=0
arr[2][3]=0
arr[3][3]=0
arr[4][3]=2
arr[5][3]=0
arr[6][3]=9
arr[7][3]=0
arr[8][3]=7

arr[0][4]=3
arr[1][4]=0
arr[2][4]=0
arr[3][4]=9
arr[4][4]=0
arr[5][4]=4
arr[6][4]=0
arr[7][4]=0
arr[8][4]=1

arr[0][5]=4
arr[1][5]=0
arr[2][5]=9
arr[3][5]=0
arr[4][5]=1
arr[5][5]=0
arr[6][5]=0
arr[7][5]=0
arr[8][5]=0

arr[0][6]=0
arr[1][6]=0
arr[2][6]=0
arr[3][6]=0
arr[4][6]=0
arr[5][6]=3
arr[6][6]=0
arr[7][6]=5
arr[8][6]=4


arr[0][7]=0
arr[1][7]=0
arr[2][7]=0
arr[3][7]=0
arr[4][7]=0
arr[5][7]=0
arr[6][7]=1
arr[7][7]=0
arr[8][7]=9

arr[0][8]=0
arr[1][8]=0
arr[2][8]=0
arr[3][8]=2
arr[4][8]=7
arr[5][8]=0
arr[6][8]=8
arr[7][8]=0
arr[8][8]=0


result=solveSudoku(arr)
print (result)
#
for item in arr:
    print (item)



