class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1

def playground(N, M, Q, A):
    uf = UnionFind(N * M)
    
    walls = set()
    for wall in A:
        x1, y1, x2, y2 = wall
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        if x1 > x2 or (x1 == x2 and y1 > y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        walls.add((x1, y1, x2, y2))
    
    for i in range(N):
        for j in range(M):
            cell = i * M + j
            
            if i < N - 1:
                neighbor = (i + 1) * M + j
                if (i, j, i + 1, j) not in walls:
                    uf.union(cell, neighbor)
            
            if j < M - 1:
                neighbor = i * M + (j + 1)
                if (i, j, i, j + 1) not in walls:
                    uf.union(cell, neighbor)
    
    return uf.components

T = int(input())
for _ in range(T):
    N, M, Q = map(int, input().split())
    A = []
    for _ in range(Q):
        wall = list(map(int, input().split()))
        A.append(wall)
    print(playground(N, M, Q, A))