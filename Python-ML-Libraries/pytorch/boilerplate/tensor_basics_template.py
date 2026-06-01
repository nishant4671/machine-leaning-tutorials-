import torch
import torch.nn as nn

# 1. Create random tensors (data and labels)
X = torch.randn(100, 5)
y = torch.randn(100, 1)

# 2. Define a tiny model
model = nn.Sequential(
    nn.Linear(5, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

# 3. Training setup
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 4. One training step
optimizer.zero_grad()
output = model(X)
loss = criterion(output, y)
loss.backward()
optimizer.step()

print(f"Step 1 Loss: {loss.item():.4f}")
