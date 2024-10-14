import rasa
# from rasa.model import TrainingResult

# def train_nlu():
#     # Đường dẫn tới các file cần thiết
#     training_files = 'data/nlu.yml'  # File chứa dữ liệu NLU
#     config_file = 'config.yml'        # Cấu hình cho NLU
#     model_path = 'models/nlu/'        # Thư mục để lưu mô hình NLU

#     # Huấn luyện mô hình NLU
#     result: TrainingResult = rasa.train_nlu(
#         config=config_file,
#         nlu_data=training_files,
#         output=model_path
#     )

#     return result

# if __name__ == "__main__":
#     train_nlu()

# from rasa.model_training import train
# from rasa import train_nlu

from rasa.model_training import train_nlu #as train_nlu_model
import os
# đặt trên hàm tránh đặt trùng với tên thư viện không sẽ gây lỗi
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def train_nlu_model():   
    # Đường dẫn tới các file cần thiết
    training_files = 'data/nlu.yml'  # File chứa dữ liệu NLU
    config_file = 'config.yml'        # Cấu hình cho NLU
    model_path = 'models/nlu'        # Thư mục để lưu mô hình NLU

    # Huấn luyện mô hình NLU
    result = train_nlu(
        config=config_file,
        nlu_data=training_files,
        output=model_path
    )

    return result

if __name__ == "__main__":
    train_nlu_model()


# code claude
# from rasa.model_training import train_nlu as rasa_train_nlu
# import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# def train_nlu_model():
#     # Đường dẫn tới các file cần thiết
#     training_files = 'data/nlu.yml'  # File chứa dữ liệu NLU
#     config_file = 'config.yml'        # Cấu hình cho NLU
#     model_path = 'models/nlu'        # Thư mục để lưu mô hình NLU
    
#     # Huấn luyện mô hình NLU
#     result = rasa_train_nlu(
#         config=config_file,
#         nlu_data=training_files,
#         output=model_path
#     )
    
#     return result

# if __name__ == "__main__":
#     train_nlu_model()