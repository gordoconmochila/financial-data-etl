import requests
import pandas as pd
import datetime
#import psycopg2

api_key = 'W1NZYYGF2AYLKBM1'
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'BRK.B', 'JPM', 'JNJ', 'V', 'PG', 'NVDA', 'HD', 'MA', 'DIS', 'PYPL']# Lista ampliada de símbolos a obtener
#esto crea el documento donde se guardaran todas las consultas
all_data = []
#el for ejecuta una consulta por ticker o symbol
for symbol in symbols:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbols}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
#&datatype=json poner esto es lo mismo que el response.json?
#&symbol=AAPL es requisito, no así el symbol = 'AAPL' debajo del apikey

# Verificar si la respuesta contiene un mensaje de error
if 'Error Message' in data:
    print("Error en la solicitud:", data['Error Message'])
elif 'Time Series (Daily)'  in data:
    # Procesar los datos si la clave está presente
    time_series = data["Time Series (Daily)"]
    rows = []

    for date, daily_data in time_series.items():
        row = {
            "date": date,
            "open": float(daily_data["1. open"]),
            "high": float(daily_data["2. high"]),
            "low": float(daily_data["3. low"]),
            "close": float(daily_data["4. close"]),
            "volume": float(daily_data["5. volume"]),
            "timestamp": datetime.datetime.now()
        }
        rows.append(row)

    # Convertir la lista de diccionarios a un DataFrame de pandas
    df = pd.DataFrame(rows)
    print(df)
    df.to_csv('financial_data.csv', index=False)
else:
    print("Respuesta inesperada:", data)