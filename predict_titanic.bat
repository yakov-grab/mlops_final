curl -X POST -H "Content-Type: application/json" -d "{\"Pclass\": 1, \"Sex\": male, \"Age\": 20.0, \"SibSp\": 0, \"Parch\": 0, \"Fare\": 15}" http://127.0.0.1:8091/predict

curl -X POST -H "Content-Type: application/json" -d "{\"Pclass\": 2, \"Sex\": female, \"Age\": 40.0, \"SibSp\": 1, \"Parch\": 0, \"Fare\": 30}" http://127.0.0.1:8091/predict

