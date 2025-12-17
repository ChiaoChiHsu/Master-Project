import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import math

x = torch.unsqueeze(torch.arange(0, 2, 0.01), dim=1)
y = torch.sin(2*math.pi*x) + 0.1*torch.rand(x.size())
LR = 0.05


class NN(nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(NN, self).__init__()

        self.layer = nn.Sequential(
            nn.Linear(n_feature, n_hidden),
            nn.Tanh(),
            nn.Linear(n_hidden, n_output)
        )

    def forward(self, x):
        x = self.layer(x)
        return x


net = NN(n_feature=1, n_hidden=3, n_output=1)     # define the network
optimizer = torch.optim.Adam(net.parameters(), lr=LR)
loss_func = nn.MSELoss()
loss_list = []
iteration_list = []
accuracy_list = []

for count in range(5001):
    prediction = net(x)     # input x and predict based on x

    loss = loss_func(prediction, y)     # must be (1. nn output, 2. target)

    optimizer.zero_grad()   # clear gradients
    loss.backward()         # backpropagation, compute gradients
    optimizer.step()        # apply gradients

    if count % 50 == 0:
        loss_list.append(loss.data.item())
        iteration_list.append(count)

        if count % 1000 == 0:
            plt.cla()
            plt.title(f"Iteration = {count}")
            plt.xlabel("X"), plt.ylabel("Y")
            plt.scatter(x.data.numpy(), y.data.numpy())
            plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
            plt.text(1.4, 1, f'Loss={loss.data.numpy():.4f}', fontdict={
                     'size': 15, 'color':  'black'})
            plt.savefig(f"9-1_demo_{count:>04}.jpg")

            print(count, loss)


plt.cla()
plt.plot(iteration_list, loss_list)
plt.xlabel("Number of iteration")
plt.ylabel("Loss")
plt.title("ANN: Loss vs Number of iteration")
plt.savefig("9-1_loss_curve")
