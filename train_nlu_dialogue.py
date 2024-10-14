import logging
from rasa import train
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Cấu hình logging
logging.basicConfig(level=logging.INFO)

# Train mô hình với dữ liệu nlu, stories và domain
def train_rasa_model():
    model_path = "models/nlu_dialogue"
    
    # Train mô hình Rasa
    train(
        domain="domain.yml",
        config="config.yml",
        training_files=["data/nlu.yml", "data/stories.yml"],
        output=model_path,
    )
    print(f"Training complete! Model saved at: {model_path}")

# Gọi hàm để bắt đầu huấn luyện
train_rasa_model()
# để train thêm thì dùng cách thêm vào policies ở file config