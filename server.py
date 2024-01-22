from flask import Flask, render_template, request
from linear_regression_model import linear_regression, lag
from waitress import serve #used to serve our app

app = Flask(__name__) #makes our application a flask app, will be our WSGI application.

#main route can be called by either url
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/prediction')
def make_prediction():
    ticker = request.args.get('ticker')#get arguments from previous form request 
    interval = request.args.get('interval')
    start_date = request.args.get('start-date')

    #error handling
    try:
        data = linear_regression(ticker,interval,start_date)
    except:
        return render_template('error.html')

    prediction = data.get("nxt_prediction")
    if prediction == 1:
        prediction = "Buy"
    else:
        prediction = "Sell" 

    if data.get("model_performance")[0] == 1:
        perf = "outperformed"
    else:
        perf = "underperformed"

    if interval == "1mo":
        interval = "month"
    elif interval == "1wk":
        interval = "week"
    else:
        interval = "day"            

    percentage = int(data.get("model_performance")[1])
    percentage = str(percentage)
    size_of_training = data.get("size_of_training")

    return render_template("prediction.html",ticker=ticker.upper(),percentage=percentage,perf=perf,interval=interval,
                           start_date = start_date,prediction=prediction,size_of_training=size_of_training) 

@app.route('/about')
def about():
    return render_template("about.html")



#when the file is ran directly it will run the app server.
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

