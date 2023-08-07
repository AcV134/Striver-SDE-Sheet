class Solution:
    def uniquePaths(self, m: int, n: int,arr = None, i = 0, j = 0) -> int:
        if arr is None:
            arr = [[-1 for _ in range(n)] for _ in range(m)]
        if i>=m or j>=n:
            return 0
        if arr[i][j]!= (-1):
            return arr[i][j]
        if i == m - 1 and j == n - 1:
            return 1
        value =  self.uniquePaths(m,n,arr,i + 1,j) +self.uniquePaths(m,n,arr,i,j + 1)
        arr[i][j] = value
        return value
        
