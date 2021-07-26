import torch
import torch.nn.functional as F
import torch.nn as nn

class ConvNet(nn.Module):
    def __init__(self, num_classes):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(8, 32, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        #self.drop_out = nn.Dropout()
        # 64x6x8 (widht, height, out_channels) /2 (MaxPool2d) = 16384 /2 (MaxPool2d) = 8192
        self.fc1 = nn.Linear(8192, 64)
        self.fc2 = nn.Linear(64, num_classes)


    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = torch.flatten(out, 1)
        #out = self.drop_out(out)
        out = self.fc1(out)
        out = self.fc2(out)
        #out = F.log_softmax(out, dim = 1)
        return out   