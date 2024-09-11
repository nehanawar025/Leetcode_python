class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        ans = [[1]*i for i in range(1,n+1)]
        for i in range(1,n):
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        
        return ans
