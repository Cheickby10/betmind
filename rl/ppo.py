import torch
import torch.nn as nn
import torch.optim as optim

class Policy(nn.Module):
    def __init__(self):
        super().__init__()
        self.net=nn.Sequential(
            nn.Linear(4,64),
            nn.ReLU(),
            nn.Linear(64,2)
        )
    def forward(self,x):
        return self.net(x)

def train_ppo(steps=200):
    model=Policy()
    opt=optim.Adam(model.parameters(),lr=0.01)
    total=0
    for _ in range(steps):
        x=torch.randn(1,4)
        out=model(x)
        loss=(out**2).mean()
        opt.zero_grad()
        loss.backward()
        opt.step()
        total+=loss.item()
    return round(total,3)
