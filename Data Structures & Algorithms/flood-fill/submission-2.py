class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(image, r, c, color):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return
            
            image[r][c] = color

            dfs(image, r + 1, c, color)
            dfs(image, r - 1, c, color)
            dfs(image, r, c+1, color)
            dfs(image, r, c-1, color)
        
        dfs(image, sr, sc, color)
        return image
            