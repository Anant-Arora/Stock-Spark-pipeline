
from kafka import KafkaProducer
import yfinance as yf
import json
import time


producer = KafkaProducer(
    bootstrap_servers='34.56.9.91:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
  
    data = yf.download(tickers='GOOG', period='1mo', interval='2m')

    for timestamp, row in data.iterrows():
        message = {
            'timestamp': str(timestamp),
            'open': float(row['Open']),
            'high': float(row['High']),
            'low': float(row['Low']),
            'close': float(row['Close']),
            'volume': int(row['Volume'])
        }
        producer.send('stock-data', value=message)
        print("Sent:", message)

    time.sleep(120)
