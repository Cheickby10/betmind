import numpy as np

def mines_safety_map(grid=5, mines=3, sims=5000):
    counts=np.zeros((grid,grid))
    for _ in range(sims):
        mine_pos=np.random.choice(grid*grid,mines,replace=False)
        safe=set(range(grid*grid))-set(mine_pos)
        for s in safe:
            r=s//grid
            c=s%grid
            counts[r,c]+=1
    return counts/sims
