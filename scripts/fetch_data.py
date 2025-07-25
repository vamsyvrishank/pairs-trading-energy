
import yfinance as yf
import pandas as pd 
from pathlib import Path
from datetime import datetime



start_date = '2015-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

#equity ticekrs for gics 10102020

tickers = [
    "COP",  # ConocoPhillips
    "EOG",  # EOG Resources
    "HES",  # Hess Corp
    "OXY",  # Occidental Petroleum
    "FANG", # Diamondback Energy
    "EQT",  # EQT Corp
    "DVN",  # Devon Energy
    "CTRA", # Coterra Energy
    "PR",   # Permian Resources
    "AR",   # Antero Resources
    "OVV",  # Ovintiv Inc
    "RRC",  # Range Resources
    "APA",  # APA Corporation
    "MTDR", # Matador Resources
    "CRK",  # Comstock Resources
    "CHRD", # Chord Energy
    "CNX",  # CNX Resources
    "MGY",  # Magnolia Oil & Gas
    "CRC",  # California Resources
]

# Create a directory to save the data
data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)

# Fetch and save WTI Crude Oil Futures data

start_date = '2015-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')


# Fetch WTI Crude Oil Futures data
wti_ticker = "CL=F"
# Natural Gas Futures
ng_ticker = "NG=F"



# Fetch and save WTI Crude Oil Futures data
for ticker , label in [("CL=F", "WTI_Crude_Oil_Futures"), ("NG=F", "Natural_Gas_Futures")]:

    try: 
        print(f"Fetching {label} data...")
        futures_data = yf.download(ticker, start_date, end_date)
        futures_data.to_csv(data_dir / f"{label}.csv")
        print(f"{label} data saved.")
    except Exception as e:
        print(f"Failed to fetch {label} data: {e}")

# Fetch and save data for each ticker
for ticker in tickers:
    try:
        print(f"Fetching data for {ticker}...")
        stock_data = yf.download(ticker, start_date , end_date)
        stock_data.to_csv(data_dir / f"{ticker}.csv")
        print(f"Data for {ticker} saved.")  
    except Exception as e:
        print(f"Failed to fetch data for {ticker}: {e}")
        continue
print("Data fetching complete.")

