# Iris Classifier Project

## Overview
This project demonstrates how to build a simple AI model using the Iris dataset from scikit-learn.  
It follows the required structure for the “Building Your First AI Model” submission.  

The project includes:
- A Jupyter Notebook walkthrough (`notebooks/iris_model.ipynb`)
- A training script (`src/train.py`) that saves the model and confusion matrix
- Automated tests (`tests/test_train.py`) to verify outputs
- A requirements file (`requirements.txt`) for dependencies

---

## Project Structure

iris-classifier/
├── data/ # empty (Iris dataset is loaded from scikit-learn)
├── notebooks/
│ └── iris_model.ipynb # walkthrough notebook
├── src/
│ └── train.py # training script
├── tests/
│ └── test_train.py # pytest file
├── outputs/ # generated automatically after running train.py
│ ├── confusion_matrix.png
│ └── model.joblib
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/iris-classifier.git
   cd iris-classifier
