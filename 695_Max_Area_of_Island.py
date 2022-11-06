class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid == None:return image
        
        visit = set()
        
        def search (pos):
            if pos[0]<0 or pos[0] ==len(grid) or pos[1]<0 or pos[1]==len(grid[0]) or grid[pos[0]][pos[1]] == 0 or pos in visit:
                return 0
            
            visit.add(pos)
            return (1+ search((pos[0]+1,pos[1]))+
            search((pos[0]-1,pos[1]))+
            search((pos[0],pos[1]+1))+
            search((pos[0],pos[1]-1)))
           

        maxx = 0
        for x in range (len(grid)):
            for y in range (len(grid[x])):
                maxx = max(maxx,search((x,y)))
        return maxx
