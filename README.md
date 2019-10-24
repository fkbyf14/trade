
You are given a content of CSV-file with information about set of trades. It contains the following columns:

TIME - Timestamp of a trade in format Hour:Minute:Second.Millisecond
PRICE - Price of one share
SIZE - Count of shares executed in this trade
EXCHANGE - The exchange that executed this trade
For each exchange find the one minute-window during which the largest number of trades took place on this exchange.

Sample  
Input  
09:30:01.034,36.99,100,V  
09:30:55.000,37.08,205,V  
09:30:55.554,36.90,54,V  
09:30:55.556,36.91,99,D  
09:31:01.033,36.94,100,D  
09:31:01.034,36.95,900,V  
Output  
2  
3  
