from django.shortcuts import render 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
 
class Prediction(APIView): 
    def post(self, request): 
        # Extract input values from request 
        v1 = request.data.get('v1') 
        v2 = request.data.get('v2') 
        v3 = request.data.get('v3') 
        v4 = request.data.get('v4') 
        v5 = request.data.get('v5') 
         
        # Check if any value is None 
        if None in [v1, v2, v3, v4, v5]: 
            return Response({'prediction': 'One or more values are missing'}, status=status.HTTP_400_BAD_REQUEST) 
 
        # Convert values to float 
        try: 
            v1 = float(v1) 
            v2 = float(v2) 
            v3 = int(v3) 
            v4 = float(v4) 
            v5 = float(v5) 
        except ValueError: 
            return Response({'prediction': 'One or more values are not valid numbers'}, status=status.HTTP_400_BAD_REQUEST)
        
        #Importing the dataset
        data = pd.read_csv("/Dataset/Obesity_Risk.csv")

        # Split the data into features and target
        features = ["Height", "Weight",	"family_history_with_overweight", "FCVC_minmax", "Age_bin_minmax"]
        X= data[features]
        y = data["NObeyesdad"]

        # Split the data into Training and Testing datasets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

        scaler = StandardScaler()
        xtrain_scaled = scaler.fit_transform(X_train)
        xtest_scaled = scaler.transform(X_test)

        # Training the Logistic Regression model
        model = LogisticRegression()
        model.fit(xtrain_scaled, y_train)

        # Making predictions
        predict_ = model.predict(np.array([v1, v2, v3, v4, v5]).reshape(1, -1))
        out = int(predict_[0])

        # Return the prediction 
        return Response({'prediction': out}, status=status.HTTP_200_OK)
