"""Views for the base app"""

from django.shortcuts import render
from plotly.offline import plot 
import plotly.graph_objects as go 
import plotly.express as px
import numpy as np
import datetime

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def charts(request):
    """ Default view for the root """
    
    def histogram():
        x0 = np.random.randn(500)
        # Add 1 to shift the mean of the Gaussian distribution
        x1 = np.random.randn(500) + 1

        fig = go.Figure()
        fig.add_trace(go.Histogram(x=x0))
        fig.add_trace(go.Histogram(x=x1))

        # Overlay both histograms
        fig.update_layout(barmode='overlay')
        fig.update_layout(title='Histogram')
        # Reduce opacity to see both histograms
        fig.update_traces(opacity=0.75)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div
    
    def box_plot():
        np.random.seed(1)
        y0 = np.random.randn(50) - 1
        y1 = np.random.randn(50) + 1

        fig = go.Figure()
        fig.add_trace(go.Box(y=y0))
        fig.add_trace(go.Box(y=y1))
        fig.update_layout(title='Box Plot')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div
    
    def heat_map():
        
        np.random.seed(1)
        programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']
        base = datetime.datetime.today()
        dates = base - np.arange(180) * datetime.timedelta(days=1)
        z = np.random.poisson(size=(len(programmers), len(dates)))

        fig = go.Figure(data=go.Heatmap(
                z=z,
                x=dates,
                y=programmers,
                colorscale='Viridis'))

        fig.update_layout(
            title='Heat Map',
            xaxis_nticks=36)

        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div
    
    def scatter():
        x1 = [1,2,3,4]
        y1 = [30, 35, 25, 45]
        text1 = ['A', 'B', 'C', 'D']
        trace = go.Scatter(
            x=x1, y = y1, text= text1, mode='markers+text'
        )
        layout = dict(
            title='Scatter Plots',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)])
        )
        fig = go.Figure(data=[trace],layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot1':heat_map(),
        'plot2':scatter(),
        'plot3':histogram(),
        'plot4':box_plot()
    }
    return render(request, 'base/charts.html', context)