# Breadth first search


# Time Complexity : O(m*n)
# space complexity : O(m*n)

# Approach :

# use bfs
# check and append in the queue the row and column of zeros and make all the ones -1
# for a particular row and column check if it is -1 or not  by moving 4 adjacent dimensionally
# if so, change it to level+1, so as to not reviit that location again and add its row and column in the queue
# increment the level once one  bfs level traversal is complete

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        if not mat:
            return mat

        rows = len(mat)
        cols = len(mat[0])
        q = deque()

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append([i, j])
                if mat[i][j] == 1:
                    mat[i][j] = -1

        level = 0
        while q:

            size = len(q)
            for i in range(size):

                poppedVal = q.popleft()

                for dirVal in dirs:
                    nr = dirVal[0] + poppedVal[0]
                    nc = dirVal[1] + poppedVal[1]

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and mat[nr][nc] == -1:
                        mat[nr][nc] = level+1
                        q.append([nr, nc])

            level = level+1

        return mat
