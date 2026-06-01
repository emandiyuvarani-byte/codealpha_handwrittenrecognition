# Handwritten Character Recognition Using CNN

## 📌 Overview

This project was developed as part of the **CodeAlpha Internship Program**. The objective of this project is to recognize handwritten digits using a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**. The model learns patterns from handwritten digit images and accurately predicts the corresponding digit.

---

## 🚀 Features

* Handwritten Digit Recognition
* Deep Learning using CNN
* Image Classification
* Data Normalization
* Model Training and Evaluation
* Prediction of Unseen Images
* Model Saving for Future Use

---

## 🛠 Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib

---

## 📂 Dataset Information

The project uses the **MNIST Dataset**, one of the most popular datasets for image classification.

### Dataset Details

* Training Images: 60,000
* Testing Images: 10,000
* Image Size: 28 × 28 Pixels
* Number of Classes: 10 Digits (0–9)

---

## 🧠 CNN Architecture

Input Layer (28×28×1)

↓

Conv2D (32 Filters)

↓

MaxPooling2D

↓

Conv2D (64 Filters)

↓

MaxPooling2D

↓

Flatten Layer

↓

Dense Layer (64 Neurons)

↓

Output Layer (10 Classes)

---

## ⚙️ Project Workflow

### Step 1: Load Dataset

The MNIST dataset is loaded using TensorFlow.

### Step 2: Data Preprocessing

* Normalize pixel values.
* Reshape images for CNN input.

### Step 3: Build CNN Model

Create convolutional and pooling layers followed by dense layers.

### Step 4: Train Model

Train the CNN using the training dataset.

### Step 5: Evaluate Model

Measure model accuracy on test data.

### Step 6: Prediction

Predict handwritten digits from unseen images.

### Step 7: Save Model

Store the trained model as:

```bash
handwritten_model.h5
```

---

## 📊 Results

The CNN model successfully recognized handwritten digits from the MNIST dataset.

### Output Generated

* Test Accuracy
* Predicted Digit
* Actual Digit Comparison
* Saved Trained Model

---

## 🎯 Applications

* Optical Character Recognition (OCR)
* Bank Cheque Processing
* Postal Code Recognition
* Document Digitization
* Educational Software
* Automated Form Processing

---

## 📁 Project Structure

```text
Handwritten-Character-Recognition/
│
├── main.py
├── handwritten_model.h5
├── README.md
└── screenshots/
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Deep Learning Fundamentals
* Convolutional Neural Networks (CNN)
* TensorFlow & Keras
* Image Processing
* Data Normalization
* Model Training & Evaluation
* Computer Vision Applications

---

## ✅ Conclusion

This project successfully implemented a Handwritten Character Recognition System using Convolutional Neural Networks (CNN). The model achieved effective digit classification by learning patterns from handwritten images in the MNIST dataset, demonstrating the practical use of Deep Learning in Computer Vision tasks.

---

## 👩‍💻 Author

**Emandi Yuvarani**

### Internship

**CodeAlpha Internship Program**
