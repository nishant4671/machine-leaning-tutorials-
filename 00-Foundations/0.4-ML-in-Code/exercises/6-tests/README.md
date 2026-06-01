# Exercise 6: Automated Testing

## Question
Write a test (pytest) that checks the loaded model’s prediction is within a small tolerance of the original.

## Detailed Explanation
ML Engineering isn't just about training models; it's about ensuring they are reliable and maintainable. Automated testing is a key part of this.

### The Task:
Write a test using the `pytest` framework. The test should:
1. Load the model saved in Exercise 5.
2. Generate or provide a sample input.
3. Compare the output of the loaded model against a known expected value (or the output of the original model if available in the test context).

### Key Technical Point:
**Floating-Point Precision**: Because computers represent decimal numbers with finite precision, $0.1 + 0.2$ is not exactly $0.3$. When comparing ML model outputs, you should never use `assert a == b`. 

Instead, use:
- `pytest.approx()`: `assert prediction == pytest.approx(expected_value, rel=1e-5)`
- `numpy.testing.assert_allclose()`

This ensures your tests pass even if there are tiny, insignificant differences in calculations.
