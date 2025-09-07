import os
import sys
import pytest

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from train import train

def test_train_creates_outputs():
    train()
    outputs = os.path.join(os.path.dirname(__file__), "..", "outputs")
    assert os.path.exists(os.path.join(outputs, "model.joblib"))
    assert os.path.exists(os.path.join(outputs, "confusion_matrix.png"))
