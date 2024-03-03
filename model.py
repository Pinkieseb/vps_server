import torch
import timm
from torch import nn

class RegressionModel(nn.Module):
    def __init__(self, device):
        super(RegressionModel, self).__init__()
        self.device = device
        self.model = timm.create_model('efficientnet_b3', pretrained=True)
        num_features = self.model.classifier.in_features
        self.model.classifier = nn.Linear(num_features, 1)

    def forward(self, x):
        x = x.to(self.device)
        return self.model(x)