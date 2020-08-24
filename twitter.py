import pandas as pd
import GetOldTweets3 as got
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
words = ["headache","flu", "influenza","contagious", "cough"]


class Tweets:
    def __init__(self, keywords, state, radius, maxtweet, startDate, endDate):
        self.keywords = keywords
        self.state = state
        self.radius = radius
        self.maxtweet = maxtweet
        self.startDate = startDate
        self.endDate = endDate

    def getTweets(self):
        tweet_criteria = got.manager.TweetCriteria().setQuerySearch(self.keywords).setSince(self.startDate).setUntil(
            self.endDate).setNear(self.state).setWithin(self.radius).setMaxTweets(self.maxtweet)
        tweet = got.manager.TweetManager.getTweets(tweet_criteria)
        return tweet

    def toDataFrame(self):
        list_of_tweets = self.getTweets()
        text_tweets = [[tw.id, tw.text, tw.date, tw.permalink] for tw in list_of_tweets]
        df_state = pd.DataFrame(text_tweets,
                                columns=["Id", "Tweet", "Date", "Links"]).sort_values("Date", ascending=True)
        df_state['Date'] = df_state['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        return df_state


    def append_Data(self):
        get_Data_Frame = self.toDataFrame()
        latest_Date_Range = get_Data_Frame["Date"].iloc[-1]
        split_Latest_Date_Range = latest_Date_Range.split("-")
        end_date = str(datetime(year=int(split_Latest_Date_Range[0]), month=int(split_Latest_Date_Range[1]), day=int(split_Latest_Date_Range[2])) + relativedelta(months=+2))
        split_End_Date = end_date.split(" ")
        print("Extracting Twitter Tweets From: " + latest_Date_Range + " to " + split_End_Date[0] + " two month-intervals and onwards ")
        while(True):
            if(not(latest_Date_Range >= "End_Date")):
                self.startDate = latest_Date_Range
                self.endDate = split_End_Date[0]
                list_of_tweets = self.getTweets()
                text_tweets = [[tw.id, tw.text, tw.date, tw.permalink] for tw in list_of_tweets]
                new_df_state = pd.DataFrame(text_tweets,
                                             columns=["Id", "Tweet", "Date", "Links"]).sort_values("Date", ascending=True)
                new_df_state['Date'] = new_df_state['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))

                get_Data_Frame = get_Data_Frame.append(new_df_state, ignore_index = True)
                writer = pd.ExcelWriter('File Path', engine='openpyxl')
                get_Data_Frame.to_excel(writer, sheet_name="sheet 1")
                writer.save()
                latest_Date_Range = get_Data_Frame["Date"].iloc[-1]
                time.sleep(600)
            else:
                break
        print("Final Date Extracted is: " + latest_Date_Range)







