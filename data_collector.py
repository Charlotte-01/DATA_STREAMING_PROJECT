import json
import boto3
import random
import os
import subprocess
import sys
import yfinance 

def lambda_handler(event, context):

    ST = '2020-05-14'
    EN = '2020-05-15'
    Interval = '1m'
    Stocks = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    Fh = boto3.client("firehose", "us-east-2")

    for stock in stocks:
        dl = yfinance.Ticker(stock).history(start=start, end=end, interval=interval)
        for index, rows in dl.iterrows():
            as_jsonstr = json.dumps({
                "high": rows.High, 
                "low": rows.Low, 
                "ts": str(index), 
                "name": stock
                })

            fh.put_record(DeliveryStreamName="project3-char-qq", Record={
                "Data": as_jsonstr.encode('utf-8')
                })

    # return
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }