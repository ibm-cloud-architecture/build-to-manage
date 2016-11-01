# Log Correlation in Python

Example implementation of Log Correlation using TransactionID using the standard Python Logging framework.

## Example output from Cloud Foundry logs

```
2016-10-28T17:34:41.24+0100 [App/0]      ERR INFO [service1,1421901503] : Got a request with transactionID 1421901503. Now calling Service2
2016-10-28T17:34:41.29+0100 [App/0]      ERR INFO [service2,1421901503] : Got a request with transactionID 1421901503. Now calling Service3
2016-10-28T17:34:41.36+0100 [App/0]      ERR INFO [service3,1421901503] : Got a request. Returning the answer you want
2016-10-28T17:34:41.37+0100 [App/0]      ERR INFO [service2,1421901503] : Got response from Service3
2016-10-28T17:34:41.38+0100 [App/0]      ERR INFO [service1,1421901503] : Got response from Service2
```

Explanation of fields:

| Timestamp from Cloud Foundry | Cloud Foundry Component and Index | Output type | LogLevel | Defined appname and TransactionID | General Log Message                                               |
|------------------------------|-----------------------------------|-------------|----------| ----------------------------------|-------------------------------------------------------------------|
| 2016-10-28T17:34:41.24+0100  | [App/0]                           | ERR         | INFO     | [service1,1421901503]             | Got a request with transactionID 1421901503. Now calling Service2 |


More details on the Cloud Foundry provided fields available on [bluemix documentation pages for logging](https://console.ng.bluemix.net/docs/monitor_log/monitoringandlogging.html#log_format)


## To try the code

1. Login to Cloud Foundry
2. cf push service3
3. Update service2/app.py to reflect service3 URL
4. cf push service2
5. Update service1/app.py to reflect service2 URL
6. cf push service1
7. Generate log entries by making a call to service1: ```curl <Service1_URL>/service```

You can now see the individual service logs with the command ```cf logs <application_name>```

To send the applications log streams to a central location, follow the [bluemix log drain guide](https://console.ng.bluemix.net/docs/monitor_log/monitoringandlogging.html#thirdparty_logging)

Then you can use the relevant search tool on the log management tool of choice to search for the appropriate TransactionID and get a correlated output as displayed above.
