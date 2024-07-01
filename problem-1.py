# Breadth first search


# Time Complexity : O(m*n)
# space complexity : O(m*n)

# Approach :

# use bfs
# use a queue and append to it the row and column of current color
# for a particular row and column change it to the target color by moving 4 adjacent dimensionally
# and if changed store the value of the affected row and column in queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if not image or image[sr][sc] == color:
            return image

        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        rows = len(image)
        cols = len(image[0])
        currColor = image[sr][sc]
        q = deque()
        q.append([sr, sc])
        image[sr][sc] = color

        while q:
            size = len(q)
            for i in range(size):
                poppedVal = q.popleft()
                for dirVal in dirs:
                    affectRow = dirVal[0] + poppedVal[0]
                    affectCol = dirVal[1] + poppedVal[1]
                    if (affectRow >= 0 and affectCol >= 0 and affectRow < rows and affectCol < cols and image[affectRow][affectCol] == currColor):
                        image[affectRow][affectCol] = color
                        q.append([affectRow, affectCol])

        return image


# Depth first search


# Time Complexity : O(m*n)
# space complexity : O(m*n)

# Approach :

# use dfs
# for a particular row and column change it to the target color by moving 4 adjacent dimensionally
# inside the for loop for directions array, keep recursively calling the dfs to the new affected color
# and if changed store the value of the affected row and column in queue


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if not image or image[sr][sc] == color:
            return image

        self.rows = len(image)
        self.cols = len(image[0])
        self.image = image
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.currColor = image[sr][sc]
        self.targetColor = color
        self.dfs(sr, sc)
        return self.image

    def dfs(self, currRow, currCol):

        if (currRow < 0 or currRow == self.rows or currCol < 0 or currCol == self.cols or self.image[currRow][currCol] != self.currColor):
            return

        self.image[currRow][currCol] = self.targetColor

        for dirVal in self.dirs:

            targetRow = dirVal[0] + currRow
            targetCol = dirVal[1] + currCol
            self.dfs(targetRow, targetCol)
