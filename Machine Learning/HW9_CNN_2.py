import torch
import torch.nn as nn
from torch.utils.data import TensorDataset
from torch.autograd import Variable

import matplotlib.pyplot as plt
import scipy.io
import numpy as np

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


data = scipy.io.loadmat("07HW2_digit.mat")

train_x = data["train0"]/255
train_y = np.zeros([500])
test_x = data["test0"]/255
test_y = np.zeros([100])

for i in range(1, 10):
    train_x_append = np.array(data[f"train{i}"])/255
    train_y_append = np.ones([500]) * i
    test_x_append = np.array(data[f"test{i}"])/255
    test_y_append = np.ones([100]) * i

    # concatenate the dataset
    train_x = np.r_[train_x, train_x_append].astype(np.float32)  # can't be int
    train_y = np.r_[train_y, train_y_append]
    test_x = np.r_[test_x, test_x_append].astype(np.float32)
    test_y = np.r_[test_y, test_y_append]

# print("train_x", train_x.shape) # (5000, 784)
# print("train_y", train_y.shape) # (5000,)
# print("test_x ", test_x.shape)  # (1000, 784)
# print("test_y ", test_y.shape)  # (1000,)


train_x = torch.from_numpy(train_x)
train_y = torch.from_numpy(train_y).type(torch.LongTensor)  # can't be int
test_x = torch.from_numpy(test_x)
test_y = torch.from_numpy(test_y).type(torch.LongTensor)

# convert to torch dataset
train_dataset = TensorDataset(train_x, train_y)
test_dataset = TensorDataset(test_x, test_y)

# batch_size, epoch and iteration
batch_size = 600
n_iters = 10001
num_epochs = n_iters / (len(train_x) / batch_size)
num_epochs = int(num_epochs)


# data loader
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=batch_size, shuffle=False)
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=batch_size, shuffle=False)


class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.cnn1 = nn.Conv2d(in_channels=1, out_channels=16,
                              kernel_size=5, stride=1, padding=0)
        self.relu1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(kernel_size=2)
        self.cnn2 = nn.Conv2d(in_channels=16, out_channels=32,
                              kernel_size=5, stride=1, padding=0)
        self.relu2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(kernel_size=2)
        self.fc1 = nn.Linear(32 * 4 * 4, 10)

    def forward(self, x):
        out = self.cnn1(x)
        out = self.relu1(out)
        out = self.maxpool1(out)
        out = self.cnn2(out)
        out = self.relu2(out)
        out = self.maxpool2(out)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        return out


model = CNNModel()
error = nn.CrossEntropyLoss()

# SGD Optimizer
learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)


# model training
count = 0
loss_list = []
iteration_list = []
accuracy_list = []

for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):

        train = Variable(images.view(-1, 1, 28, 28))
        labels = Variable(labels)

        optimizer.zero_grad()  # Clear gradients
        outputs = model(train)  # Forward propagation
        # Calculate softmax and cross entropy loss
        loss = error(outputs, labels)
        loss.backward()  # Calculating gradients
        optimizer.step()  # Update parameters

        count += 1

        if count % 50 == 0:
            # Calculate Accuracy
            correct = 0
            total = 0

            # Predict test dataset
            for images, labels in test_loader:
                test = Variable(images.view(-1, 1, 28, 28))
                outputs = model(test)  # Forward propagation
                # Get predictions from the maximum value
                predicted = torch.max(outputs.data, 1)[1]
                total += len(labels)  # Total number of labels
                # Total correct predictions
                correct += (predicted == labels).sum()

            accuracy = 100.0 * correct.item() / total

            # store loss and iteration
            loss_list.append(loss.data.item())
            iteration_list.append(count)
            accuracy_list.append(accuracy)
            if count % 500 == 0:
                print('Iteration: {}  Loss: {}  Accuracy: {} %'.format(
                    count, loss.data.item(), accuracy))


# visualization loss
plt.plot(iteration_list, loss_list)
plt.xlabel("Number of iteration")
plt.ylabel("Loss")
plt.title("CNN: Test loss vs Number of iteration")
plt.savefig("9-2_LossCurve.jpg")

# visualization accuracy
plt.cla()
plt.plot(iteration_list, accuracy_list, color="red")
plt.xlabel("Number of iteration")
plt.ylabel("Accuracy")
plt.title("CNN: Accuracy vs Number of iteration")
plt.savefig("9-2_Accuracy curve.jpg")
