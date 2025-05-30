#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kafka import KafkaProducer
import yfinance as yf
import json
import time

# Connect to Kafka broker (replace IP with your Kafka VM's external IP)
producer = KafkaProducer(
    bootstrap_servers='34.56.9.91:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    # Download 1 month of data with 3-minute intervals
    data = yf.download(tickers='GOOG', period='1mo', interval='2m')

    # Send each row as a message to Kafka
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

    # Wait 3 minutes before fetching next batch
    time.sleep(120)



# In[ ]:




