import os
from catboost.datasets import titanic


# Путь к датасетам
DATASETS_PATH = "../datasets"
MODELS_PATH = "../models"

# Проверяем, существует ли директория DATASETS_PATH
if not os.path.exists(DATASETS_PATH):
    try:
        os.makedirs(DATASETS_PATH)
        print(f"The {DATASETS_PATH} directory was created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")

# Проверяем, существует ли директория MODELS_PATH
if not os.path.exists(MODELS_PATH):
    try:
        os.makedirs(MODELS_PATH)
        print(f"The {MODELS_PATH} directory was created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")

# Загрузка датасета Titanic
train_df, _ = titanic()

# Сохранение датасета в CSV
try:
    train_df.to_csv('../datasets/dataset_titanic.csv', index=False)
    print("Datasets successfully saved in the directory ../dataset under names dataset_titanic.csv.")
except Exception as e:
    print("An error occurred while saving datasets:", e)
