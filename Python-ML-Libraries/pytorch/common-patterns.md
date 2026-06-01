# PyTorch Common Patterns 💡

### 1. The Basic Training Loop
The standard rhythm of deep learning.
```python
for data, target in dataloader:
    optimizer.zero_grad()    # Reset old math
    output = model(data)     # Guess
    loss = criterion(output, target) # Check error
    loss.backward()          # Backpropagate
    optimizer.step()         # Update
```

### 2. Defining a Model
The "Lego" way of building networks.
```python
import torch.nn as nn
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 1)
    def forward(self, x):
        return self.fc(x)
```

### 3. Using the GPU
Speeding up your math.
```python
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
data = data.to(device)
```
