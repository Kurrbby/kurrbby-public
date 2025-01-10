# Risk Management Functions

import numpy as np
import pandas as pd
from arch import arch_model  # For GARCH modeling
from scipy.stats import norm



def load_data(file_path, date_col, price_col):
    """
    Loads and preprocesses time series data.
    
    Parameters:
        file_path (str): Path to the CSV file.
        date_col (str): Column name for the date.
        price_col (str): Column name for the prices.
    
    Returns:
        pd.DataFrame: Preprocessed DataFrame with returns.
    """
    data = pd.read_csv(file_path, parse_dates=[date_col])
    data.set_index(date_col, inplace=True)
    data['Returns'] = np.log(data[price_col] / data[price_col].shift(1))
    data.dropna(inplace=True)
    return data

def historical_volatility(data, window=30):
    """
    Computes historical volatility as rolling standard deviation.
    
    Parameters:
        data (pd.Series): Log returns series.
        window (int): Rolling window size.
    
    Returns:
        pd.Series: Historical volatility.
    """
    return data.rolling(window).std() * np.sqrt(365)  # Annualized for crypto; adjust as needed for other assets (e.g., 252 for stocks)


def garch_model(data, p=1, q=1):
    """
    Fits a GARCH(p, q) model to the log returns.
    
    Parameters:
        data (pd.Series): Log returns series.
        p (int): Order of GARCH terms.
        q (int): Order of ARCH terms.
    
    Returns:
        arch_model.FittedModel: Fitted GARCH model.
    """
    model = arch_model(data, vol='Garch', p=p, q=q)
    fitted_model = model.fit(disp='off')
    return fitted_model
 
def var_parametric(data, confidence_level=0.95):
    """
    Calculates the parametric VaR.
    
    Parameters:
        data (pd.Series): Log returns series.
        confidence_level (float): Confidence level for VaR.
    
    Returns:
        float: VaR value.
    """
    mean = data.mean()
    std = data.std()
    z = norm.ppf(1 - confidence_level)
    return mean + z * std

