import yfinance as yf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


#call it as such: linear_regression("MSFT","1wk","1993-01-01")


#funct is used to add to the data frame the previous return values up to amnt_of_days. It will also return the names of the columns added
def lag(data_frame, amnt_of_days):
    names = []
    for n in range(1,amnt_of_days + 1):
        data_frame[str(n) + "day(s) prev ret"] = data_frame['returns'].shift(n) #creates a column n days prev close and it shifts the 
         #returns by n times and now our model knows the previous returns. 
        names.append(str(n) + "day(s) prev ret")
    return names

#this function will take for args the ticker, the interval of data(weekly or daily), and the start of the data.
#it will return a dictionary of info necesarry to predict stock movement for next interval chosen. It will return
#an indicator if the model is profitable, and by how much in % and a prediction value of 1 or -1 for the next interval as well as the size
#of the training data.

def linear_regression(ticker,interval,start):
    data_frame = yf.download(ticker,start=start,interval=interval) #call yfinance download to download data

    #---DATA MANIPULATION---

    #we will add a returns columns to the data which will calculate the percentage return from the prev close
    data_frame['returns'] = np.log(data_frame.Close.pct_change()+1)

    lag_names = lag(data_frame,5) #add the lag
    data_frame.dropna(inplace=True)#drop the 'na' values in the data which is caused by there not being prev values for the beginning data

    #Data splitting
    train, test= train_test_split(data_frame,test_size=0.2,shuffle = False, random_state=0)#test size = 20% and no suffling so we dont lose
                                                                                           #linearity of data

    #---MODEL BUILDING---

    #train the model
    lr = LinearRegression()
    lr.fit(train[lag_names], train['returns'])#this will train the empty linear regression model 'lr' on the variables given
    #.fit method takes train[lag_names] to be the data to train from and train[returns] to be the target(dependent) data to train from

    #---MODEL APPLICATION---

    test['prediction_LR'] = lr.predict(test[lag_names]) #adding to test dataset the prediction values of test data set
    test["direction_LR"] = [1 if i > 0 else -1 for i in test.prediction_LR]#gives a pos 1 if prediction is pos and -1 if neg.
    #this will be our indicator of buying or selling. If the value is -1 then its predicting next value will be lower so its
    #time to sell. If its 1, then we buy

    test['strat_LR'] = test['direction_LR'] * test['returns'] #used to compare performance vs real values

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
                           "current_price":info.info.get('bid')}

    
    return data

#if the file is executed directly through the terminal
if __name__ == "__main__":
    ticker = input('Please enter a stock ticker:')
    interval = input('Please enter an interval of the following list:\n1d, 1wk, 1mo:')
    date = input('Please enter the data start date(yyyy-mm-dd): ')
    dat = linear_regression(ticker,interval,date)
    print(dat)