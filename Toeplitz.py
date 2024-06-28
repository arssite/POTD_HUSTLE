'''A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant, i.e.,
all elements in a diagonal are the same. Given a rectangular matrix mat, your task is to complete the function
isToeplitz which returns true if the matrix is Toeplitz otherwise, it returns false.'''

#___________________________________________________________________________________

'''
Input:
mat = [[6, 7, 8],
       [4, 6, 7],
       [1, 4, 6]]
Output: true
Explanation: The test case represents a 3x3 matrix
 6 7 8 
 4 6 7 
 1 4 6
Output will be true, as values in all downward diagonals from left to right contain the same elements.


Input: 
mat = [[1,2,3],
       [4,5,6]]
Output: false
Explanation: Matrix of order 2x3 will be 1 2 3 4 5 6 Output: false as values in all diagonals are not the same.'''


#CODE
def isToepliz(mat):
    #code here
    n,m=len(mat),len(mat[0])
    for i in range(1,n):
        for j in range(1,m):
            if mat[i][j]!=mat[i-1][j-1]:
                return False
    return True
#mat is matrix


#------------------------------------------------------------------------------
#JS
function isToeplitz(matrix) {
    const n = matrix.length;
    const m = matrix[0].length;
    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            if (matrix[i][j] !== matrix[i - 1][j - 1]) {
                return false;
            }
        }
    }
    return true;
}

#-------
const matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
];

console.log(isToeplitz(matrix));  // Output: true
