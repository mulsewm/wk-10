import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima import auto_arima
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from arch import arch_model
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True, errors='coerce')
    df = df.sort_values(by='Date')
    return df

# Check stationarity using ADF test
def check_stationarity(timeseries):
    result = adfuller(timeseries.dropna())
    print("\nAugmented Dickey-Fuller Test:")
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    return result[1]  # Return p-value

# Determine optimal ARIMA parameters
def find_optimal_arima(timeseries):
    model = auto_arima(timeseries, seasonal=False, stepwise=True, suppress_warnings=True)
    return model.order  # Returns (p, d, q)

# Fit ARIMA model and forecast
def fit_arima_model(timeseries, order, steps=30):
    model = sm.tsa.ARIMA(timeseries, order=order)
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=steps)
    return fitted_model, forecast

# Fit GARCH model
def fit_garch_model(timeseries):
    model = arch_model(timeseries, vol='Garch', p=1, q=1)
    fitted_model = model.fit(disp='off')
    forecast = fitted_model.forecast(start=len(timeseries)-30)
    return fitted_model, forecast

# Evaluate model performance
def evaluate_model(actual, predicted, model_name):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    r2 = r2_score(actual, predicted) if len(actual) == len(predicted) else None
    print(f"\n{model_name} Model Evaluation:")
    print(f"MAE: {mae}")
    print(f"RMSE: {rmse}")
    if r2 is not None:
        print(f"R-squared: {r2}")
    return mae, rmse, r2

# Backtesting function
def backtest_arima(df, order):
    train_size = int(len(df) * 0.8)
    train, test = df.iloc[:train_size], df.iloc[train_size:]
    model = sm.tsa.ARIMA(train['Price'], order=order)
    fitted_model = model.fit()
    predictions = fitted_model.forecast(steps=len(test))
    evaluate_model(test['Price'], predictions, "ARIMA Backtest")

# Main execution block
def main():
    data_path = "../data/processed/BrentOilPrices_cleaned.csv"  # Update if needed
    df = load_data(data_path)
    
    # Check for stationarity
    p_value = check_stationarity(df['Price'])
    
    # If not stationary, apply differencing
    if p_value > 0.05:
        df['Price_Diff'] = df['Price'].diff()
        print("Applying first-order differencing...")
        p_value = check_stationarity(df['Price_Diff'])
    
    # Determine ARIMA parameters
    optimal_order = find_optimal_arima(df['Price'].dropna())
    print(f"\nOptimal ARIMA Order: {optimal_order}")
    
    # Fit and forecast using ARIMA
    fitted_arima, forecast_arima = fit_arima_model(df['Price'].dropna(), optimal_order)
    
    # Plot ARIMA forecast
    plt.figure(figsize=(12, 5))
    plt.plot(df['Date'], df['Price'], label='Actual Prices', color='blue')
    plt.plot(pd.date_range(df['Date'].iloc[-1], periods=30, freq='D'), forecast_arima, label='ARIMA Forecast', color='red')
    plt.xlabel('Year')
    plt.ylabel('Price (USD per Barrel)')
    plt.title('Brent Oil Price Forecast (ARIMA)')
    plt.legend()
    plt.show()
    
    # Evaluate ARIMA Model
    evaluate_model(df['Price'].dropna().iloc[-30:], forecast_arima, "ARIMA")
    
    # Fit and forecast using GARCH
    fitted_garch, forecast_garch = fit_garch_model(df['Price'].dropna())
    
    # Plot GARCH forecast
    plt.figure(figsize=(12, 5))
    plt.plot(df['Date'], df['Price'], label='Actual Prices', color='blue')
    plt.plot(df['Date'].iloc[-30:], forecast_garch.variance.iloc[-30:], label='GARCH Volatility Forecast', color='orange')
    plt.xlabel('Year')
    plt.ylabel('Price Volatility')
    plt.title('Brent Oil Price Volatility Forecast (GARCH)')
    plt.legend()
    plt.show()
    
    # Evaluate GARCH Model
    evaluate_model(df['Price'].dropna().iloc[-30:], forecast_garch.variance.iloc[-30:], "GARCH")
    
    # Perform backtesting on ARIMA
    backtest_arima(df, optimal_order)

if __name__ == "__main__":
    main()
