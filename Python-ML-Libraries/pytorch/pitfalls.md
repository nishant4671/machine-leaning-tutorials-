# PyTorch Pitfalls ⚠️

1. **Forgetting `zero_grad()`**: Gradients accumulate by default. If you don't reset them, your model will "learn" from the wrong math!
   *Fix*: Always call `optimizer.zero_grad()` at the start of your loop.

2. **CPU/GPU Mismatch**: Trying to do math between a tensor on a GPU and one on a CPU.
   *Fix*: Use `.to(device)` on both.

3. **In-place Operations**: Modifying a tensor that is needed for gradient calculation.
   *Fix*: Avoid `x += y`, use `x = x + y`.

4. **Not setting `eval()` mode**: Dropout and BatchNormalization behave differently during testing.
   *Fix*: Use `model.eval()` before testing.

5. **Shape Errors**: Deep learning is 90% fixing dimension mismatches.
   *Fix*: Use `print(tensor.shape)` everywhere!
