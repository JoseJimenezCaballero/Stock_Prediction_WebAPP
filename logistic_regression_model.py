import yfinance as yf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#funct is used to add to the data frame the previous return values up to amnt_of_days. It will also return the names of the columns added
def lag(data_frame, amnt_of_days):
    names = []
    for n in range(1,amnt_of_days + 1):
        data_frame[str(n) + "day(s) prev ret"] = data_frame['returns'].shift(n) #creates a column n days prev close and it shifts the 
         #returns by n times and now our model knows the previous returns. 

         #we make a new column with the previous direction of the chosen amount of days this will be the binary data to train model with
        data_frame[str(n) + "day(s) prev direction"] = [1 if j > 0 else -1 for j in data_frame[str(n) + "day(s) prev ret"]]
        names.append(str(n) + "day(s) prev direction")
    return names



def logistic_regression(ticker,interval,start):
    data_frame = yf.download(ticker,start=start,interval=interval) #call yfinance download to download data

    #---DATA MANIPULATION---

    #we will add a returns and direction columns to the data which will calculate the percentage return from the prev close and which direction it is going(up or down)
    data_frame['returns'] = np.log(data_frame.Close.pct_change()+1)
    data_frame['direction'] = [1 if i > 0 else -1 for i in data_frame.returns]

    lag_names = lag(data_frame,5) #add the lag
    data_frame.dropna(inplace=True)#drop the 'na' values in the data which is caused by there not being prev values for the beginning data

    #Data splitting
    train, test= train_test_split(data_frame,test_size=0.30,shuffle = False, random_state=0)#test size = 25% and no suffling so we dont lose
                                                                                           #linearity of data
    train = train.copy()
    test = test.copy()
    #---MODEL BUILDING---S

    #train the model
    lr = LogisticRegression()
    lr.fit(train[lag_names], train['direction'])#this will train the empty linear regression model 'lr' on the variables given
    #.fit method takes train[lag_names] to be the data to train from and train[direction] to be the target(dependent) data to train from

    #---MODEL APPLICATION---

    test['prediction_LR'] = lr.predict(test[lag_names]) #adding to test dataset the prediction values of test data set
    test["direction_LR"] = [1 if i > 0 else -1 for i in test.prediction_LR]#gives a pos 1 if prediction is pos and -1 if neg.
    #this will be our indicator of buying or selling. If the value is -1 then its predicting next value will be lower so its
    #time to sell. If its 1, then we buy

    test['strat_LR'] = test['prediction_LR'] * test['returns'] #used to compare performance vs real values

    #---MODEL PERFORMANCE----

    comp = np.exp(test[['returns','strat_LR']].sum())#compares the returns with the prediction. If the strat_LR is higher then there is
                                                    #expected profit, otherwise its loss


    #data will contain dictionary with data to be returned. a model_performance key will contain if model outperformed(1) data or 
    #underperformed(-1) as well as the percentage difference in performance.
    #data will also contain "nxt_prediction key" which will return 1 if buy or -1 if sell for that interval

    info = yf.Ticker(ticker)

    data = {"model_performance":[1 if comp["returns"] < comp["strat_LR"] else -1,
                           abs(comp["returns"] - comp["strat_LR"])/((comp["returns"] + comp["strat_LR"])/2) *100],
                           "nxt_prediction":test.iloc[-1, -2],"size_of_training":len(train), "name":info.info.get("shortName"),
                           "current_price":info.info.get('currentPrice') if info.info.get('currentPrice') != None else info.info.get('bid') }
    
    if(info.info.get('quoteType') == 'CRYPTOCURRENCY'):#specific for crypto
        data['current_price'] = info.info.get('regularMarketPreviousClose')

    return data

#if the file is executed directly through the terminal
if __name__ == "__main__":
    ticker = input('Please enter a stock ticker:')
    interval = input('Please enter an interval of the following list:\n1d, 1wk, 1mo:')
    date = input('Please enter the data start date(yyyy-mm-dd): ')
    dat = logistic_regression(ticker,interval,date)
    print(dat)