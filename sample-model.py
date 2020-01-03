# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:49:04 2019

@author: Shayan
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import Imputer
from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api',methods=['GET'])
def graphPoints():
    IndicatorList =[[]]
    df = pd.read_csv("pak-data-updated.csv")
    df = df.drop(columns=['Indicator Name', 'Country Code', 'Indicator Code', 'Country Name'], axis=1)
    # print(df.head())
    for i in range(202):
        IndicatorList.append(df.iloc[i].T)

    for i in range(1,202):
        IndicatorList[i] =  IndicatorList[i].dropna()
    print(IndicatorList)
    return jsonify(customers=IndicatorList)  
    # list = [
    #         {'a': 1, 'b': 2},
    #         {'a': 5, 'b': 10}
    #     ]
    # return json.dumps(list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=False, threaded=True)



    # def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    #     plt.figure(figsize=(16,5), dpi=dpi)
    #     plt.plot(x, y, color='tab:red')
    #     plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    #     plt.show()

    # plot_df(df, x=df.index, y=df.Values, title='Employment in industry (% of total employment) (modeled ILO 