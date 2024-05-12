from catboost.datasets import titanic
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Загрузка датасета Titanic
train_df, _ = titanic()

# Сохранение датасета в CSV
try:
    train_df.to_csv('../datasets/dataset_titanic.csv', index=False)
    print("Datasets successfully saved in the directory ../dataset under names dataset_titanic.csv.")
except Exception as e:
    print("An error occurred while saving datasets:", e)

# Разделение на признаки и целевую переменную
X = train_df.drop('Survived', axis=1)
y = train_df['Survived']

# Разделение на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели случайного леса
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Предсказание на тестовом наборе
y_pred = rf_model.predict(X_test)

# Оценка качества модели
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

print('Classification Report:')
print(classification_report(y_test, y_pred)[:10])
