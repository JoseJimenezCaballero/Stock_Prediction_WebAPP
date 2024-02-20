from flask import Flask, render_template, request
from linear_regression_model import linear_regression, lag
from waitress import serve #used to serve our app
from stock_name import get_ticker #used to get stock ticker based on user input

app = Flask(__name__) #makes our application a flask app, will be our WSGI application.

#main route can be called by either url
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/chooser')
def chooser():
    ticker = request.args.get('ticker')#get arguments from previous form request
    try:
        ticker = get_ticker(ticker)
    except:
        return render_template('error.html') #implement error page

    try:
        data = linear_regression(ticker,"1d","2024-01-01")
    except:
        return render_template('error.html') #implement error page
    
    ticker_name = data.get("name")
    current_price = data.get('current_price')
    current_price = "{:.2f}".format(current_price) #make sure the value is only two decimal places.

    return render_template("chooser.html", ticker=ticker, ticker_name=ticker_name, current_price=current_price)
    

@app.route('/final')    
def make_prediction():
    ticker = request.args.get('ticker')#get arguments from previous form request 


    #error handling/monthly
    try:
        data_m = linear_regression(ticker,"1mo","1970-01-01")
    except:
        return render_template('error.html')
    
    month_pred = data_m.get("nxt_prediction")
    if month_pred == 1:
        month_pred = "Buy"
    else:
        month_pred = "Sell" 

    if data_m.get("model_performance")[0] == 1:
        perf_m = "Outperformed"
    else:
        perf_m = "Underperformed"           

    percentage_m = int(data_m.get("model_performance")[1])
    percentage_m = str(percentage_m)
    size_of_train_m = data_m.get("size_of_training")


    #error handling/weekly
    try:
        data_w = linear_regression(ticker,"1wk","1970-01-01")
    except:
        return render_template('error.html')
    
    week_pred = data_w.get("nxt_prediction")
    if week_pred == 1:
        week_pred = "Buy"
    else:
        week_pred = "Sell" 

    if data_w.get("model_performance")[0] == 1:
        perf_w = "Outperformed"
    else:
        perf_w = "Underperformed"           

    percentage_w = int(data_w.get("model_performance")[1])
    percentage_w = str(percentage_w)
    size_of_train_w = data_w.get("size_of_training")

    #error handling/daily
    try:
        data_d = linear_regression(ticker,"1d","1970-01-01")
    except:
        return render_template('error.html')
    
    day_pred = data_d.get("nxt_prediction")
    if day_pred == 1:
        day_pred = "Buy"
    else:
        day_pred = "Sell" 

    if data_d.get("model_performance")[0] == 1:
        perf_d = "Outperformed"
    else:
        perf_d = "Underperformed"           

    percentage_d = int(data_d.get("model_performance")[1])
    percentage_d = str(percentage_d)
    size_of_train_d = data_d.get("size_of_training")


    ticker = data_d.get("name")
    current_price = data_d.get('current_price')
    current_price = "{:.2f}".format(current_price) #make sure the value is only two decimal places.

    return render_template("final.html",ticker=ticker, current_price=current_price, percentage_m=percentage_m, perf_m=perf_m, month_pred=month_pred
                           ,size_of_train_m=size_of_train_m, percentage_w=percentage_w, perf_w=perf_w, week_pred=week_pred
                           ,size_of_train_w=size_of_train_w, percentage_d=percentage_d, perf_d=perf_d, day_pred=day_pred
                           ,size_of_train_d=size_of_train_d) 

@app.route('/about')
def about():
    return render_template("about.html")



#when the file is ran directly it will run the app server.
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

