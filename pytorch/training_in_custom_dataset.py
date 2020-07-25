import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math
import torch.nn as nn

# --> divide dataset into small batches for faster computation
# --> Dataloader can do the batch computation for us

# implement custom dataset, implement __init__, __getitem__, __len__

class CustomDataset(Dataset):
    def __init__(self):
        xy = np.loadtxt('wine.csv', delimiter=',', dtype=np.float32, skiprows=1)
        self.n_samples = xy.shape[0]

        self.x_data = torch.from_numpy(xy[:, 1:])
        self.y_data = torch.from_numpy(xy[:, 0].astype(np.long))
        #self.y_data = self.y_data.view(self.y_data.shape[0], 1) # reshape to column vector
    
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples

# step 0, create dataset
print('Preparing Data')
dataset = CustomDataset()
first_data = dataset[0]
features, labels = first_data 
print(features, labels)

# Load whole dataset with DataLoader
# shuffle: shuffle data, good for training
# num_workers: faster loading with multiple subprocesses
# !!! IF YOU GET AN ERROR DURING LOADING, SET num_workers TO 0 !!!
train_loader = DataLoader(dataset=dataset, batch_size=4, shuffle=True, num_workers=0)

# convert to an iterator and look at one random sample
dataiter = iter(train_loader)
features, labels = dataiter.next()
n_samples, n_features = dataset.x_data.shape
print(features, labels)
# Dataset is ready for training

# Step 1: Model
class Model(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(Model, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        # no softmax at the end if loss is cross entropy
        # if you use sigmoid with BCELoss, then you need to implement sigmoid here
        return out

print('Model')
input_size = n_features
output_size = 1
model = Model(input_size=input_size, hidden_size=5, num_classes=4) # classes insex should be 0 to num_classes - 1

# Step 2: Loss and optimizer
print('Loss and Optimizer')
learning_rate = 0.001
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# Step 3: Training Loop
print('Start of Training Loop')
num_epochs = 1000
for epoch in range(num_epochs):
    # forward pass and loss
    y_predicted = model.forward(dataset.x_data)
    loss = criterion(y_predicted, dataset.y_data)

    # backward pass
    loss.backward()

    # update
    optimizer.step()
    optimizer.zero_grad()

    if (epoch + 1) % 1000 == 0:
        print (f'epoch: {epoch+1}, loss = {loss.item():.4f}')

y_pred = model(dataset.x_data).detach()
_, predictions = torch.max(y_pred, 1)
print(predictions)
print(dataset.y_data)
match = torch.sum(predictions == dataset.y_data).item()
accuracy = match / n_samples * 100.0
print(f'Accuracy: {accuracy:0.4f}')
print('All Done')
