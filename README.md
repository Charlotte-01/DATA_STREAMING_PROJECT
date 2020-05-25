# DATA_STREAMING_PROJECT

This project we processed the “real time” data and then dumped it in a manner that facilitates querying and further analysis.

### Infrastructure 

##### DataCollector Lambda configuration page

![img](https://github.com/Charlotte-01/DATA_STREAMING_PROJECT/blob/master/Lambda.png)

##### Kinesis Data Firehose Delivery Stream Monitoring

![img](https://github.com/Charlotte-01/DATA_STREAMING_PROJECT/blob/master/Monitoring.png)


#### API Gateway of DataCollector
https://fd5z0s487d.execute-api.us-east-2.amazonaws.com/default/project-collector

### Data collection
We use the yfinance module (documentation here), grabing pricing information for each of the following stocks:
Facebook (FB), Shopify (SHOP), Beyond Meat (BYND), Netflix (NFLX),Pinterest (PINS), Square (SQ), The Trade Desk (TTD), Snap (SNAP), Datadog (DDOG).

We collect one full day’s worth of stock HIGH and LOW prices for each company listed above on Thursday, May 14th 2020, at an one minute interval. 

### Data analysis
AWS Athena and Glue crawler