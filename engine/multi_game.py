
def choose_game(metrics):
    best=None
    score=-999
    for g,m in metrics.items():
        s=m["edge"]-m["risk"]
        if s>score:
            best=g
            score=s
    return best
