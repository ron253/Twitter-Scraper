**Documentation**

**Title**: Twitter Web Scraper 

**Author**: Ron Huang

**About** <br />

Developed a twitter scraper to extract flu-related tweets to feed into an LSTM model.

**Installation** <br/> 
Use any IDE/editor of your choice. 

**What Each Function Does** <br/>
1) Tweets(). Takes in 6 parameters with a specified flu-related keyword, state, radius, maximum tweet to be extracted, start date, and end date to be extracted. <br/>
2) getTweets(): Gets flu-related tweets and returns a list of tweets and related meta-data.<br/>
3) toDataFrame(): Converts the list of tweets returned by getTweets()  into a DataFrame with columns and its respected data “Id, Tweet, Date, and Links”. Returns a DataFrame sorted by ascending order. <br/>
4) append_Data(): Appends the next two-month date range until a condition is met.  For example, data is continuously appended in two-month intervals until “latest date range >= End Date”. <br/>

**Necessary Packages To Be Installed**<br/>
1) Pandas<br/>
2) GetOldTweets3<br/>
3) Datetime<br/>
4) Dateutil.relativedelta <br/>
5) time


**Limitations**<br/>
1) The module "GetOldTweets" will extract tweets from setSince(inclusive) to setUntil(not inclusive) of the end date. For example, if setSince() is 2019-08-01 and setUntil() is 2019-08-10, tweets will be extracted at the end date of 2019-08-09 instead of 2019-08-10. Therefore, the while loop condition within append_Data() must include the date before the end date for the condition to end, otherwise, the loop will run indefinitely. <br/>
2) There is a restriction on how many tweets a user is allowed to extract on a per-minute basis. A workaround to this problem is to time out the code for 10 minutes before beginning the next iteration. Use this if you are extracting large amounts of data. <br/>
3) GetOldTweets extracts tweets on a bi-monthly basis. 



 
