from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/smallcase', methods=['GET', 'POST'])
def smallcase():
    f = request.form

    print(f)
    
    val = int(f['investamt'])
    risk = f['options'] + 'Volatility'

    df = pd.DataFrame(pd.read_excel('./Data/Smallcase dataset.xlsx'))

    df = df[df['Risk'] == risk]
    try:
        df['MIN VALUE OF INVESTMENT'] = list(map(lambda x:int(str(x).replace(',','')), df['MIN VALUE OF INVESTMENT']))
        df = df[df['MIN VALUE OF INVESTMENT'] <= val]

        df.to_csv('./Data/temp.csv', index=False) 
        df = pd.DataFrame(pd.read_csv('./Data/temp.csv', index_col=False))

        df = df.to_json()    
    except:
        pass

    return render_template('interface2.html', arr = df)

@app.route('/stocks', methods=['GET','POST']) 
def stocks():
    os.system("start cmd /K python training.py")

    return render_template('index.html')

app.run()