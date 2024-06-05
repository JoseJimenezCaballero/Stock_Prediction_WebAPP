# Stock Prediction WebAPP
Live at: https://stock-prediction-dxym.onrender.com/

This web application uses machine learning to make dynamic predictions on a stocks return. Just add the ticker and choose the intervals and start date of data and the application will take care of the rest!

This app was built using a combination of programming languages and libraries. It uses a linear regression model to predict if the next return of the given interval will be positive or negative. The model is dinamically trained every time it is called which ensures the most recent data is used. It uses a training model of 80% of the inputted data and runs tests on 20% of the data. The data the model uses is directly downloaded from yahoo finance using their api.
API calls can be done by https://stock-prediction-dxym.onrender.com/api_?ticker=[TICKER]



To do:
  Add about and models pages
  Add more prediction models, so the user can pick the best one
