# import pandas as pd
from catboost.datasets import titanic
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import os

# Путь к датасетам
DATASETS_PATH = "..\\datasets"

# Проверяем, существует ли директория
if not os.path.exists(DATASETS_PATH):
    try:
        os.makedirs(DATASETS_PATH)
        print(f"The {DATASETS_PATH} directory was created successfully.")
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

# Заполнение пропущенных значений
train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
train_df['Embarked'] = train_df['Embarked'].fillna(train_df['Embarked'].mode()[0])

# Преобразование категориальных признаков
label_encoders = {}
for col in ['Sex', 'Embarked']:
    le = LabelEncoder()
    train_df[col] = le.fit_transform(train_df[col])
    label_encoders[col] = le

# Разделение данных на признаки и целевую переменную
X = train_df.drop(['Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
y = train_df['Survived']

# Разделение на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели случайного леса
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Предсказание на тестовом наборе
y_pred = rf_model.predict(X_test)

# Оценка качества модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

print('Classification Report:')
print(classification_report(y_test, y_pred)[:10])
