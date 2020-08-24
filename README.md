# Twitter-WebScraper

Title: Twitter Web Scraper

Author: Ron Huang

About <br />

This code is sed for extracting flu-related tweets from twitter to feed into machine learning model for influenza predictions. 

Installation <br/> 
Use any IDE/editor of your choice. The one I am using is pycharm. Click here to download the community version. 
https://www.jetbrains.com/pycharm/

What Each Function Does <br/>
Tweets(). Takes in 6 parameters with a specified flu-related keyword, state, radius, maximum tweet to be extracted, start date, and end date to be extracted. <br/>
getTweets(): Gets flu-related tweets and returns a list of tweets and related meta-data.<br/>
toDataFrame(): Converts the list of tweets returned by getTweets()  into a DataFrame with columns and its respected data “Id, Tweet, Date, and Links”. Returns a DataFrame sorted by ascending order. <br/>
append_Data(): Appends the next two-month date range until a condition is met.  For example, data is continuously appended in two-month intervals until “latest date range >= End Date”. <br/>

Necessary Packages To Be Installed<br/>
Pandas<br/>
GetOldTweets3<br/>
Datetime<br/>
Dateutil.relativedelta <br/>
time


Limitations<br/>
GetOldTweets will extract tweets from setSince(inclusive) to setUntil(not inclusive) of the end date. For example, if setSince() is 2019-08-01 and setUntil() is 2019-08-10, tweets will be extracted at the end date of 2019-08-09 instead of 2019-08-10. Therefore, the while loop condition within append_Data() must include the date before the end date for the condition to end, otherwise, the loop will run indefinitely. <br/>
There is a restriction on how many tweets a user is allowed to extract on a per-minute basis. A workaround to this problem is to time out the code for 10 minutes before beginning the next iteration. 


Test Cases <br/>
To make sure code works, please test by setting parameters to 
Tweets("flu", "Denver,Colorado", "1000mi",10000, "2019-08-01", "2019-08-03")
And within append_Data(), change the condition of while loop to end date “2019-08-09” and self.endDate to “2019-08-10”. The result of latest extracted data should be 2019-08-09. 
