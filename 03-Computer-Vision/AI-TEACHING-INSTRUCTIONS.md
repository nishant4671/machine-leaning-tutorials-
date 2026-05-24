# AI Teaching Instructions — Module 3: Computer Vision & Optimized Serving

## 🧑‍🏫 Role
> "You are a computer vision expert and production engineer. You guide your student through training a Pneumonia Detector from chest X‑rays, exporting to ONNX, adding interpretability, and handling drift in image data."

## 📚 Prompts

- "Explain a convolutional neural network to a beginner using a torch (light) passing over an image."
- "What is transfer learning? Why use a pretrained ResNet for medical images? Weigh pros and cons."
- "I’m handling class imbalance in X‑ray data. Walk me through three techniques (weighted loss, oversampling, Focal Loss) and when to use each."
- "Export my PyTorch model to ONNX. Show me the code and explain what happens under the hood."
- "I want to serve my model with ONNX Runtime. Write a FastAPI endpoint that loads an .onnx file and performs inference."
- "Teach me Grad‑CAM. First conceptually, then with code snippets. How do I overlay the heatmap on the original X‑ray?"
- "I need to detect when my image data drifts (e.g., new X‑ray machines). What features can I monitor? Generate a drift detection script using Evidently on image metadata."
- "Act as a medical AI auditor. Question my model’s performance metrics. Would you trust it in a hospital? Why not?"
