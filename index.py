python
import pandas as pd
import plotly.express as px
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def load_data(file_path):
    # Load the XLSX dataset
    data = pd.read_excel(file_path)
    return data

data = load_data('Non-oil_Merchandise_Trade-MAR2026.xlsx')

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/trade_data')
def get_trade_data():
    # Return data as JSON
    return jsonify(data.to_dict(orient='records'))

@app.route('/plot')
def plot():
    # Generate a plot using Plotly
    fig = px.bar(data, x='Country', y='Export Value', color='HS Code',
                 title='Non-Oil Exports by Country and HS Code',
                 labels={'Export Value': 'Value in AED'})
    return fig.to_html()

if __name__ == '__main__':
    app.run(debug=True)
