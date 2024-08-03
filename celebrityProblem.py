    def celebrity(self, mat):
        # code here
        n=len(mat)
        r,l=n-1,0
        while l<r:
            if mat[l][r]==1:
                l+=1
            else:
                r=r-1
        for i in range(n):
            if i!=l and (mat[l][i]==1 or mat[i][l]==0):
                return -1
        return l



#----------------------------------------------------------

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, Mat, N):
        # code here 
        indegree = [0] * N
        outdegree = [0] * N

        # Query for all edges
        for i in range(N):
            for j in range(N):
                x = Mat[i][j]

                # Set the degrees
                outdegree[i] += x
                indegree[j] += x

        # Find a person with indegree N-1 and outdegree 0
        for i in range(N):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i

        return -1
