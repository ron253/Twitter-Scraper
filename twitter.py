import pandas as pd
import GetOldTweets3 as got
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time




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
                                columns=["Id", "Tweet", "Date", "Links"]).sort_values("Date", ascending=True, ignore_index=True)
        df_state['Date'] = df_state['Date'].apply(lambda x:x.date())
        return df_state


    def append_Data(self):
        dataFrame = self.toDataFrame()
        #time.sleep(600) include this if extracting large amounts of tweets otherwise an API timeout request will occur
        get_last_date = dataFrame.iloc[-1]["Date"].strftime('%Y-%m-%d')
        split_latest_date_range = get_last_date.split("-")
        end_date = str(datetime(year=int(split_latest_date_range[0]), month=int(split_latest_date_range[1]), day=int(split_latest_date_range[2])) + relativedelta(months=+2))
        split_End_Date = end_date.split(" ")
        print("Now extracting Twitter Tweets From: " + get_last_date + " to " + split_End_Date[0] + " on a bi-monthly basis and onwards.")
        list_of_dataframes = [dataFrame]
        while(True):
            if(not(get_last_date >= "End Date")):
                self.startDate = get_last_date
                self.endDate = split_End_Date[0]
                self.maxtweet = "Set max tweet"
                list_of_tweets = self.getTweets()
                text_tweets = [[tw.id, tw.text, tw.date, tw.permalink] for tw in list_of_tweets]
                new_df_state = pd.DataFrame(text_tweets,
                                             columns=["Id", "Tweet", "Date", "Links"]).sort_values("Date", ascending=True, ignore_index=True)
                new_df_state['Date'] = new_df_state['Date'].apply(lambda x: x.date())
                list_of_dataframes.append(new_df_state)
                get_last_date = new_df_state.iloc[-1]["Date"].strftime('%Y-%m-%d')
                split_latest_date_range = get_last_date.split("-")
                end_date = str(datetime(year=int(split_latest_date_range[0]), month=int(split_latest_date_range[1]),
                                        day=int(split_latest_date_range[2])) + relativedelta(months=+2))
                split_End_Date = end_date.split(" ")
                time.sleep(600)

            else:
                break

        output = pd.concat(list_of_dataframes, ignore_index=True)
        output.to_excel(r'file path', index=False)






