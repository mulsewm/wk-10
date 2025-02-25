from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load processed Brent oil price data
data_path = "../../../data/processed/BrentOilPrices_cleaned.csv"
df = pd.read_csv(data_path)
df['Date'] = pd.to_datetime(df['Date'])

# API Route to get historical Brent oil prices
@app.route('/api/prices', methods=['GET'])
def get_prices():
    data = df.tail(500).to_dict(orient='records')  # Return last 500 records
    return jsonify(data)

# API Route to get ARIMA forecast (dummy response for now)
@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    forecast_data = {"message": "Forecasting results will be added here"}
    return jsonify(forecast_data)

# API Route to get detected change points (dummy response for now)
@app.route('/api/change-points', methods=['GET'])
def get_change_points():
    change_points_data = {"message": "Change point detection results will be added here"}
    return jsonify(change_points_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
