import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import pandas as pd
import argparse

def train_and_save_model(data_path, target_column, model_output_path):
    # Load dataset
    data = pd.read_parquet(data_path)

    # Split features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize XGBoost model
    xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)

    # Train the model
    print("Training the XGBoost model...")
    xgb_model.fit(X_train, y_train)

    # Evaluate the model
    print("Evaluating the model...")
    y_pred = xgb_model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

    # Save the trained model to a file
    print(f"Saving the model to {model_output_path}...")
    joblib.dump(xgb_model, model_output_path)
    print("Model saved successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train and save an XGBoost model.")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the dataset.")
    parser.add_argument("--target_column", type=str, required=True, help="Name of the target column.")
    parser.add_argument("--model_output_path", type=str, required=True, help="Path to save the trained model.")

    args = parser.parse_args()

    train_and_save_model(args.data_path, args.target_column, args.model_output_path)
