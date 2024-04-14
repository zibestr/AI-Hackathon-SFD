import os
from flask import Flask, request, render_template, redirect, send_from_directory
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from ml.model import Model


app = Flask(__name__, template_folder=os.path.join(os.path.abspath("./"),
                                                   "src\\templates"))
model = Model(os.path.join(os.path.abspath("./"), "src\\ensemble.bin"))


def from_model(data: pd.DataFrame) -> np.ndarray[float]:
    """Add new columns and calculate model prediction
    Args:
        data (pd.DataFrame): data with columns same train.csv

    Returns:
        np.ndarray[float]: model prediction
    """
    currency_df = pd.read_csv(os.path.join(os.path.abspath("./"), "external_data\\currency.csv"))
    GDP_df = pd.read_csv(os.path.join(os.path.abspath("./"), "external_data\\GDP.csv"))
    inflation_df = pd.read_csv(os.path.join(os.path.abspath("./"), "external_data\\inflation.csv"))
    unemployment_df = pd.read_csv(os.path.join(os.path.abspath("./"), "external_data\\Unemployment.csv") ) # Загрузка столбцов из csv
    for i, quarter in enumerate(currency_df.loc[:, 'quarter']): # Загрузка в dataFrame
        data.loc[data['quarter'] == quarter, 'currency'] = currency_df.iloc[i, 1]
        data.loc[data['quarter'] == quarter, 'GDP'] = GDP_df.iloc[i, 1]
        data.loc[data['quarter'] == quarter, 'inflation'] = inflation_df.iloc[i, 1]
        data.loc[data['quarter'] == quarter, 'unemployment'] = unemployment_df.iloc[i, 0]
    return model.predict(data) # Вовзрат


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filename)
            test_df = pd.read_csv(filename)
            answer = pd.Series(from_model(test_df))
            answer.to_csv(os.path.join(app.config['DOWNLOAD_FOLDER'], "out.csv"))
            # os.remove(filename)
            return redirect("/result")

    return render_template("index.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("result.html")


@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], "out.csv", as_attachment=True)


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath("./"), "data\\server")
    app.config['DOWNLOAD_FOLDER'] = os.path.join(os.path.abspath("./"), "data\\server")
    app.run(port=8000)
