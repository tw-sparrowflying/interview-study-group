class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        width, height = 0, len(grid)
        travelledLand = []
        for r in grid:
            width = len(r)
            travelledLand.append([False]*len(r))
        queue = []
        islandCnt = 0
        for y, row in enumerate(grid):
            for x, p in enumerate(row):
                if p == '0' or travelledLand[y][x]:
                    continue
                queue.append((y,x))
                islandCnt += 1
                while 0 < len(queue):
                    p = queue.pop()
                    travelledLand[p[0]][p[1]] = True
                    p_neighbor = [(p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)]
                    for n in p_neighbor:
                        if n[0] < height and n[0] >= 0 and n[1] < width and n[1] >= 0:
                            if grid[n[0]][n[1]] == '1' and not travelledLand[n[0]][n[1]]:
                                queue.append(n)
        return islandCnt