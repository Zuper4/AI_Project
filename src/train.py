import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Paths
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def train():
    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Save model
    model_path = os.path.join(OUTPUT_DIR, "model.joblib")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

    # Confusion matrix
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=iris.target_names,
                yticklabels=iris.target_names)
    plt.title("Confusion Matrix")
    fig_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
    plt.savefig(fig_path)
    print(f"Confusion matrix saved to {fig_path}")

if __name__ == "__main__":
    train()
