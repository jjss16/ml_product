import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utils.load as ld
import plotly.express as px
import os

def load_data():
    df = pd.read_csv('data\cars.csv')
    return df

def plot_fig():
    fig = px.box(data_frame=load_data(), y= 'price_usd')
    fig.show()

def run():
    return (load_data().head())

if __name__ == '__main__':
    run()