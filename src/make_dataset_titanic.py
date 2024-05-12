import pandas as pd
from catboost.datasets import titanic

train_df, test_df = titanic()
print("Information about the native dataset:")
print(train_df.info())

# Заполнение пропущенных значений в поле "Age" средним значением
mean_age = train_df['Age'].mean()
print(f"Average age: {mean_age}")

train_df['Age'] = train_df['Age'].fillna(mean_age)
test_df['Age'] = test_df['Age'].fillna(mean_age)

print("Information about the dataset after replacing missing results:")
print(train_df.info())

try:
    # Сохранение обновленных датасетов в CSV
    train_df.to_csv('../datasets/train.csv', index=False)
    test_df.to_csv('../datasets/test.csv', index=False)
    print("Datasets successfully saved in the directory ../dataset under names train.csv and test.csv.")
except Exception as e:
    print("An error occurred while saving datasets:", e)

# print("Train dataset:")
# print(train_df.head())

#print(test_df.info())
# print("\nTest dataset:")
# print(test_df.head())