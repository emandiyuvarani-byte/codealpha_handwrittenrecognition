# Handwritten Character Recognition using CNN and MNIST Dataset

# STEP 1: Import Libraries
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np


# STEP 2: Load MNIST Dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

print("Training Images Shape:", train_images.shape)
print("Testing Images Shape:", test_images.shape)


# STEP 3: Display Sample Image
plt.imshow(train_images[0], cmap='gray')
plt.title(f"Label: {train_labels[0]}")
plt.show()


# STEP 4: Normalize Data
train_images = train_images / 255.0
test_images = test_images / 255.0


# STEP 5: Reshape Images for CNN
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))


# STEP 6: Build CNN Model
model = models.Sequential()

# First Convolution Layer
model.add(layers.Conv2D(
    32,
    (3, 3),
    activation='relu',
    input_shape=(28, 28, 1)
))

# First Pooling Layer
model.add(layers.MaxPooling2D((2, 2)))

# Second Convolution Layer
model.add(layers.Conv2D(
    64,
    (3, 3),
    activation='relu'
))

# Second Pooling Layer
model.add(layers.MaxPooling2D((2, 2)))

# Flatten Layer
model.add(layers.Flatten())

# Dense Hidden Layer
model.add(layers.Dense(64, activation='relu'))

# Output Layer
model.add(layers.Dense(10, activation='softmax'))


# STEP 7: Compile Model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


# STEP 8: Train Model
history = model.fit(
    train_images,
    train_labels,
    epochs=1,
    validation_data=(test_images, test_labels),
    verbose=0
)


# STEP 9: Evaluate Model
test_loss, test_acc = model.evaluate(test_images, test_labels)

print("\nTest Accuracy:", test_acc)


# STEP 10: Predict Sample Image
prediction = model.predict(test_images)

predicted_label = np.argmax(prediction[0])

print("Predicted Digit:", predicted_label)
print("Actual Digit:", test_labels[0])


# STEP 11: Show Predicted Image
plt.imshow(test_images[0].reshape(28, 28), cmap='gray')
plt.title(f"Predicted: {predicted_label}")
plt.show()


# STEP 12: Save Model
model.save("handwritten_model.h5")

print("\nModel saved successfully as handwritten_model.h5")
