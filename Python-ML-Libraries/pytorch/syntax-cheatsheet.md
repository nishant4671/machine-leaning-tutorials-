# PyTorch Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `torch.tensor(data)` | Create a tensor | `torch.tensor([1, 2])` |
| `t.to('cuda')` | Move tensor to GPU | `t.to('cuda')` |
| `t.shape` | Dimensions of tensor | `t.shape` |
| `t.view(new_shape)` | Reshape (like NumPy) | `t.view(-1, 10)` |
| `loss.backward()` | Compute gradients | `loss.backward()` |
| `optimizer.step()` | Update model weights | `optimizer.step()` |
| `nn.Linear(in, out)` | Fully connected layer | `nn.Linear(10, 2)` |
| `nn.ReLU()` | Activation function | `nn.ReLU()` |
| `optim.SGD(params)` | Optimizer algorithm | `optim.SGD(model.parameters(), lr=0.01)` |
| `torch.save(obj, path)`| Save model to disk | `torch.save(model, 'm.pt')` |
