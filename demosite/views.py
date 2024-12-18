from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
import json
import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder
import time
import re
from datetime import datetime
from .model_result_new import model_output_data
from .model_result_3 import mode_output_3

from .output import output_data

from runs.models import Run



@login_required(login_url='/login/')
def home_view(request):
    context = {
        'page_title': 'Welcome to the template home page'
    }
    

    return render(request, 'dashboard.html', context)


@login_required(login_url='/login/')
def dashboard_view(request):
    user_id = request.user.id 
    if request.user.userprofile.role == 'admin':
        runs = Run.objects.all()
    else:
        runs = Run.objects.filter(user=request.user.id)

    # Check if 'mvoh_runs' exists in the session
    is_mvoh_run_exist = 1 if 'mvoh_runs' in request.session and request.session['mvoh_runs'] else 0
    is_m2_run_exist = 1 if 'm2_runs' in request.session and request.session['m2_runs'] else 0
    is_m3_run_exist = 1 if 'm3_runs' in request.session and request.session['m3_runs'] else 0
    is_m4_run_exist = 1 if 'm4_runs' in request.session and request.session['m4_runs'] else 0
    is_m5_run_exist = 1 if 'm5_runs' in request.session and request.session['m5_runs'] else 0
    is_m6_run_exist = 1 if 'm6_runs' in request.session and request.session['m6_runs'] else 0
    is_m7_run_exist = 1 if 'm7_runs' in request.session and request.session['m7_runs'] else 0
    is_m8_run_exist = 1 if 'm8_runs' in request.session and request.session['m8_runs'] else 0

    context = {
        'runs': runs,
        'is_mvoh_run_exist': is_mvoh_run_exist,
        'is_m2_run_exist': is_m2_run_exist,
        'is_m3_run_exist': is_m3_run_exist,
        'is_m4_run_exist': is_m4_run_exist,
        'is_m5_run_exist': is_m5_run_exist,
        'is_m6_run_exist': is_m6_run_exist,
        'is_m7_run_exist': is_m7_run_exist,
        'is_m8_run_exist': is_m8_run_exist,
    }

    return render(request, 'dashboard.html', context)


def api_data_view(request):
    if request.method == 'POST':
        # Fetch form data
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Calculation parameters
        return_calculation = request.POST.get('return_calculation')
        price_frequency = request.POST.get('price_frequency')
        risk_free_rate = float(request.POST.get('risk_free_rate', 0))
        invested_amount = float(request.POST.get('invested_amount', 0))
        
        # Optimization parameters
        benchmark_portfolio = request.POST.get('benchmark_portfolio')
        trv_min = float(request.POST.get('target_return_for_min_volatility', 0))
        trv_max = float(request.POST.get('target_volatility_for_max_return', 0))
        default_min_weight = float(request.POST.get('default_min_weight', 0))
        default_max_weight = float(request.POST.get('default_max_weight', 0))
        frontier_runs = int(request.POST.get('frontier_runs', 0))
        monte_carlo_simulations = int(request.POST.get('monte_carlo_simulations', 0))
        solver = request.POST.get('solver')
        dendogram_segment = request.POST.get('dendogram_segment')
        
        # Ticker data - assuming the tickers and their related data are sent as lists
        symbols = request.POST.getlist('symbols[]')  # Ticker symbols
        baw_list = request.POST.getlist('baw[]')     # Benchmark asset weight
        amax_list = request.POST.getlist('amax[]')   # Asset maximum weight
        ba_list = request.POST.getlist('ba[]')       # Benchmark amount

        # Create the ticker data structure
        ticker_data = []
        for i in range(len(tickers)):
            ticker_data.append({
                "symbol": tickers[i],
                "benchmark_asset_weight": float(baw_list[i]),
                "asset_minimum_weight": 0,  # Modify this if you need it from form
                "asset_maximum_weight": float(amax_list[i]),
                "benchmark_amount": float(ba_list[i]),
                "stock_prices": []  # You can handle stock prices data here if needed
            })
        
        # Construct final JSON structure
        form_data = {
            "start_date": start_date,
            "end_date": end_date,
            "calculation_parameters": {
                "return_calculation": return_calculation,
                "price_frequency": price_frequency,
                "risk_free_rate": risk_free_rate,
                "invested_amount": invested_amount
            },
            "optimization_parameters": {
                "benchmark_portfolio": benchmark_portfolio,
                "target_return_for_min_volatility": trv_min,
                "target_volatility_for_max_return": trv_max,
                "default_min_weight": default_min_weight,
                "default_max_weight": default_max_weight,
                "frontier_runs": frontier_runs,
                "monte_carlo_simulations": monte_carlo_simulations,
                "benchmark_ticker": "^GSPC",  # Hardcoded for now, modify if needed
                "solver": solver,
                "dendogram_segment": dendogram_segment
            },
            "ticker_data": ticker_data
        }

        
        # Render the form if it's a GET request
        x_y_data = []
        table_data = []

        strageties = output_data['strategies']
        for strategy in strageties:
            if strategy['data'] is not None:  # Check if 'data' is not None
                x = strategy['data']['portfolio_summary']['annualized_mean']
                y = strategy['data']['portfolio_summary']['standard_deviation']
                x_y_data.append({
                    'annualized_mean': x,
                    'standard_deviation': y
                })
                table_data.append({
                    'exp_return': strategy['data']['expected_return'],
                    'std_dev': strategy['data']['standard_deviation'],
                    'sharpe_ratio': strategy['data']['sharpe_ratio']
                })
        
        # Convert the x_y_data to JSON
        x_y_data_json = json.dumps(x_y_data)
        print(table_data) 

        context = {
            'data': x_y_data_json,
            'table_data': table_data
        }
        # Return JSON response for demonstration
        # return JsonResponse(data)
        return render(request, 'data.html', context)

    # Render the form if it's a GET request
    x_y_data = []
    table_data = []

    strageties = output_data['strategies']
    for strategy in strageties:
        if strategy['data'] is not None:  # Check if 'data' is not None
            x = strategy['data']['portfolio_summary']['annualized_mean']
            y = strategy['data']['portfolio_summary']['standard_deviation']
            x_y_data.append({
                'annualized_mean': x,
                'standard_deviation': y
            })
            table_data.append({
                'exp_return': strategy['data']['expected_return'],
                'std_dev': strategy['data']['standard_deviation'],
                'sharpe_ratio': strategy['data']['sharpe_ratio']
            })
    
    # Convert the x_y_data to JSON
    x_y_data_json = json.dumps(x_y_data)

    context = {
        'data': x_y_data_json,
        'table_data': table_data
    }

    # print("Strategies: ", output_data['strategies'])
    return render(request, 'data2.html', context)


def api_data_view_2(request):
    if request.method == 'POST':
        frontier_runs = output_data['frontier_runs']
        frontier_x = frontier_runs['x']
        frontier_y = frontier_runs['y']
        strageties = output_data['frontier_positions']
        strategy_x = strageties['x']
        strategy_y = strageties['y']
        strategy_labels = strageties['strategy_names']

        fig1 = go.Figure()

        # Add Efficient Frontier (Blue Line)
        fig1.add_trace(go.Scatter(
            x=frontier_x, 
            y=frontier_y, 
            mode='lines+markers', 
            name='Efficient Frontier',
            line=dict(color='blue'),
            marker=dict(color='blue')
        ))

        # Add Portfolio Strategy points (Yellow Dots)
        fig1.add_trace(go.Scatter(
            x=strategy_x, 
            y=strategy_y, 
            mode='markers+text',
            text=strategy_labels, 
            name='Portfolios',
            marker=dict(color='orange', size=10),
             textposition='top center',
             textfont=dict(
                family="Arial",  # Font family
                size=12,         # Font size
                color="black"    # Font color
            ),
             texttemplate="<span style='border: 1px solid black; background-color: red; padding: 2px;'>%{text}</span>"
        ))

        # Set axis titles and layout
        fig1.update_layout(
            xaxis_title="Risk (%)",
            yaxis_title="Return (%)",
            legend=dict(yanchor="top", y=1.1, xanchor="center", x=0.5, orientation='h'),
        )

        # Convert Plotly figure to JSON
        graph_json_1 = json.dumps(fig1, cls=PlotlyJSONEncoder)

        max_cap_weight_data = output_data['strategies'][0]['data']
        max_cap_weight_tbl = {
            'Expected Return': f"{max_cap_weight_data['expected_return'] * 100:.2f}%",
            'Standard Deviation': f"{max_cap_weight_data['standard_deviation'] * 100:.2f}%",
            'Sharpe Ratio': f"{max_cap_weight_data['sharpe_ratio'] * 100:.2f}%",  # If Sharpe Ratio is not a percentage, you can skip formatting
            'CVaR 90%': f"{max_cap_weight_data['cvar_090'] * 100:.2f}%",
            'CVaR 95%': f"{max_cap_weight_data['cvar_095'] * 100:.2f}%",
            'CVaR 99%': f"{max_cap_weight_data['cvar_099'] * 100:.2f}%",
        }

        max_cap_weight_labels = []
        max_cap_weight_allocation = []
        colors = ['#FF5733', '#33FF57']
        
        for label in max_cap_weight_data['symbol_allocations']:
            max_cap_weight_labels.append(label['symbol'])
            max_cap_weight_allocation.append(label['allocation_weight'])

        fig2 = go.Figure(data=[go.Pie(
            labels=max_cap_weight_labels,
            values=max_cap_weight_allocation,
            hole=0.4,
            marker=dict(colors=colors),
            textfont=dict(color='white'),  # Set the label text color
            hoverinfo='label+value',  # Show label and value in tooltip
            hovertemplate='<b>%{label}</b><br>Value: %{value}<extra></extra>',  # Customize hover content
            hoverlabel=dict(
                font=dict(
                    family='Arial, sans-serif',
                    size=14,
                    color='white'  # Tooltip text color
                ),
                bgcolor='#ffffff',  # Tooltip background color
                bordercolor='#FF0000'  # Tooltip border color
            )
        )])
        fig2.update_layout(
            template='plotly_white',
            legend=dict(yanchor="top", y=1, xanchor="center", x=0.5, orientation='h'),
        )

        graph_json_2 = json.dumps(fig2, cls=PlotlyJSONEncoder)
        max_cap_weight_tracking_error = max_cap_weight_data['tracking_errors']
        max_cap_weight_tracking_error['ratio'] = round(max_cap_weight_tracking_error['ratio'], 2)

        min_variance_data = output_data['strategies'][1]['data']
        min_variance_tbl = {
            'Expected Return': f"{min_variance_data['expected_return'] * 100:.2f}%",
            'Standard Deviation': f"{min_variance_data['standard_deviation'] * 100:.2f}%",
            'Sharpe Ratio': f"{min_variance_data['sharpe_ratio'] * 100:.2f}%",  # If Sharpe Ratio is not a percentage, you can skip formatting
            'CVaR 90%': f"{min_variance_data['cvar_090'] * 100:.2f}%",
            'CVaR 95%': f"{min_variance_data['cvar_095'] * 100:.2f}%",
            'CVaR 99%': f"{min_variance_data['cvar_099'] * 100:.2f}%",
        }

        min_variance_labels = []
        min_variance_allocation = []

        for label in min_variance_data['symbol_allocations']:
            min_variance_labels.append(label['symbol'])
            min_variance_allocation.append(label['allocation_weight'])

        fig3 = go.Figure(data=[go.Pie(
            labels=min_variance_labels,
            values=min_variance_allocation,
            hole=0.4,
            marker=dict(colors=colors),
            textfont=dict(color='white'),  # Set the label text color
            hoverinfo='label+value',  # Show label and value in tooltip
            hovertemplate='<b>%{label}</b><br>Value: %{value}<extra></extra>',  # Customize hover content
            hoverlabel=dict(
                font=dict(
                    family='Arial, sans-serif',
                    size=14,
                    color='white'  # Tooltip text color
                ),
                bgcolor='#ffffff',  # Tooltip background color
                bordercolor='#FF0000'  # Tooltip border color
            )
        )])
        fig3.update_layout(
            template='plotly_white',
            legend=dict(yanchor="top", y=1, xanchor="center", x=0.5, orientation='h'),
        )

        graph_json_3 = json.dumps(fig3, cls=PlotlyJSONEncoder)
        min_variance_tracking_error = min_variance_data['tracking_errors']
        min_variance_tracking_error['ratio'] = round(min_variance_tracking_error['ratio'], 2)

        summary_tbl_data = output_data['strategies']
        summary_tbl = []
        for strategy in summary_tbl_data:
            if strategy['data'] is not None and strategy['data']['portfolio_summary'] is not None:
                portfolio_summary = strategy['data']['portfolio_summary']

                # Create a new dictionary with the required fields
                summary_item = {
                    'strategy_name': strategy['name'],
                    'expected_return': f"{portfolio_summary.get('annualized_mean', None)* 100:.2f}%",
                    'standard_deviation': f"{portfolio_summary.get('annualized_standard_deviation', None)* 100:.2f}%",
                    'sharpe_ratio': f"{portfolio_summary.get('annualized_sharpe_ratio', None)* 100:.2f}%",
                    'sortino_ratio': f"{portfolio_summary.get('annualized_sortino_ratio', None)* 100:.2f}%",
                    'cvar_090': f"{portfolio_summary.get('cvar_at_95', None)* 100:.2f}%",  # Adjust based on your requirements
                    'cvar_095': f"{portfolio_summary.get('cvar_at_95', None)* 100:.2f}%",  # Adjust based on your requirements
                    'cvar_099': f"{portfolio_summary.get('cvar_at_95', None)* 100:.2f}%"   # Adjust based on your requirements
                }

                # Append the summary_item to summary_tbl
                summary_tbl.append(summary_item)


        context = {
            'graph_json_1': graph_json_1,
            'max_cap_weight_tbl': max_cap_weight_tbl,
            'summary_tbl': summary_tbl,
            'graph_json_2': graph_json_2,
            'max_cap_weight_tracking_error': max_cap_weight_tracking_error,
            'min_variance_tbl': min_variance_tbl,
            'graph_json_3': graph_json_3,
            'min_variance_tracking_error': min_variance_tracking_error
        }

        return render(request, 'data3.html', context)

    # Render the form if it's a GET request
    x_y_data = []
    table_data = []

    strageties = output_data['strategies']
    for strategy in strageties:
        if strategy['data'] is not None:  # Check if 'data' is not None
            x = strategy['data']['portfolio_summary']['annualized_mean']
            y = strategy['data']['portfolio_summary']['standard_deviation']
            x_y_data.append({
                'annualized_mean': x,
                'standard_deviation': y
            })
            table_data.append({
                'exp_return': strategy['data']['expected_return'],
                'std_dev': strategy['data']['standard_deviation'],
                'sharpe_ratio': strategy['data']['sharpe_ratio']
            })
    
    # Convert the x_y_data to JSON
    x_y_data_json = json.dumps(x_y_data)
    # print(table_data) 

    context = {
        'data': x_y_data_json,
        'table_data': table_data
    }

    # print("Strategies: ", output_data['strategies'])
    return render(request, 'data3.html', context)


def api_data_view_3(request):
    if request.method == 'POST':
        # Efficient Frontier Data (blue points and line)
        efficient_frontier_data = [
            {'x': 22, 'y': 10},
            {'x': 23, 'y': 12},
            {'x': 24, 'y': 14},
            {'x': 25, 'y': 16},
            {'x': 26, 'y': 18},
            {'x': 27, 'y': 20},
            {'x': 28, 'y': 22},
            {'x': 29, 'y': 24},
            {'x': 30, 'y': 26},
            {'x': 31, 'y': 28},
            {'x': 32, 'y': 30},
        ]

        # Specific Portfolios Data (orange points)
        portfolio_data = [
            {'x': 22, 'y': 10, 'label': 'Min Var'},
            {'x': 24, 'y': 15, 'label': 'HRP'},
            {'x': 26, 'y': 8, 'label': '90% CVaR'},
            {'x': 28, 'y': 28, 'label': 'Max Sharpe'},
        ]

        # Efficient Frontier (Line + Blue Circles)
        efficient_frontier_trace = go.Scatter(
            x=[point['x'] for point in efficient_frontier_data],
            y=[point['y'] for point in efficient_frontier_data],
            mode='lines+markers',
            name='Efficient Frontier',
            line=dict(color='blue'),
            marker=dict(color='blue', size=8),
        )

        # Portfolio Points (Orange Circles with Labels)
        portfolio_trace = go.Scatter(
            x=[point['x'] for point in portfolio_data],
            y=[point['y'] for point in portfolio_data],
            mode='markers+text',
            name='Portfolios',
            marker=dict(color='orange', size=10),
            text=[point['label'] for point in portfolio_data],
            textposition='top right',
            hovertemplate='Label: %{text}<br>Risk: %{x}%<br>Return: %{y}%<extra></extra>',
        )

        # Generate random portfolios (Red Points)
        np.random.seed(42)
        random_risk = np.random.uniform(22, 32, 500)
        random_return = np.random.uniform(5, 30, 500)

        random_portfolios_trace = go.Scatter(
            x=random_risk,
            y=random_return,
            mode='markers',
            name='Random Portfolios',
            marker=dict(color='red', size=5),
            hovertemplate='Risk: %{x}%<br>Return: %{y}%<extra></extra>',
        )

        # Layout (Title, Labels, etc.)
        layout = go.Layout(
            title='Efficient Frontier with Random Portfolios',
            xaxis=dict(title='Risk (%)'),
            yaxis=dict(title='Return (%)'),
            showlegend=True,  # Show the legend
            legend=dict(
                x=0.5,  # Center the legend horizontally
                y=1.02,  # Position it just above the plot area
                xanchor='center',  # Anchor the x-position to the center
                yanchor='bottom',  # Anchor the y-position to the bottom
                orientation='h',  # Horizontal orientation
                bgcolor='rgba(255, 255, 255, 0.5)',  # Background color (optional)
                bordercolor='black',  # Border color (optional)
                borderwidth=1  # Border width (optional)
            )
        )

        # Create the figure with the traces and layout
        fig = go.Figure(data=[random_portfolios_trace, efficient_frontier_trace, portfolio_trace], layout=layout)

        # Convert Plotly figure to JSON
        graph_json = json.dumps(fig, cls=PlotlyJSONEncoder)

        return render(request, 'data3.html', {'graph_json': graph_json})

    # Render the form if it's a GET request
    x_y_data = []
    table_data = []

    strageties = output_data['strategies']
    for strategy in strageties:
        if strategy['data'] is not None:  # Check if 'data' is not None
            x = strategy['data']['portfolio_summary']['annualized_mean']
            y = strategy['data']['portfolio_summary']['standard_deviation']
            x_y_data.append({
                'annualized_mean': x,
                'standard_deviation': y
            })
            table_data.append({
                'exp_return': strategy['data']['expected_return'],
                'std_dev': strategy['data']['standard_deviation'],
                'sharpe_ratio': strategy['data']['sharpe_ratio']
            })
    
    # Convert the x_y_data to JSON
    x_y_data_json = json.dumps(x_y_data)
    print(table_data) 

    context = {
        'data': x_y_data_json,
        'table_data': table_data
    }

    # print("Strategies: ", output_data['strategies'])
    return render(request, 'data3.html', context)


def convert_to_standard_date_format(date_str):
    # List of common date formats to try
    date_formats = [
        '%Y-%m-%d',  # Example: 2024-10-16
        '%d/%m/%Y',  # Example: 16/10/2024
        '%m/%d/%Y',  # Example: 10/16/2024
        '%d-%m-%Y',  # Example: 16-10-2024
        '%m-%d-%Y',  # Example: 10-16-2024
        '%Y/%m/%d',  # Example: 2024/10/16
        '%d.%m.%Y',  # Example: 16.10.2024
        '%m.%d.%Y',  # Example: 10.16.2024
    ]
    
    parsed_date = None

    
    # Try parsing the input date string using the formats
    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            break
        except ValueError:
            continue 
    
    if parsed_date:
        # Convert to the desired format: YYYY-MM-DD
        return parsed_date.strftime('%Y-%m-%d')
    else:
        # Raise an error or return None if parsing fails
        raise ValueError("Invalid date format")


def process_form(rq):
    # Fetch form data
    start_date = convert_to_standard_date_format(rq.POST.get('start_date'))
    end_date = convert_to_standard_date_format(rq.POST.get('end_date'))
    
    # Calculation parameters
    return_calculation = rq.POST.get('return_calculation')
    price_frequency = rq.POST.get('price_frequency')
    risk_free_rate = float(rq.POST.get('risk_free_rate', 0))
    invested_amount = float(rq.POST.get('invested_amount', 0))
    
    # Optimization parameters
    benchmark_portfolio = rq.POST.get('benchmark_portfolio')
    trv_min = float(rq.POST.get('target_return_for_min_volatility', 0))
    trv_max = float(rq.POST.get('target_volatility_for_max_return', 0))
    default_min_weight = float(rq.POST.get('default_min_weight', 0))
    default_max_weight = float(rq.POST.get('default_max_weight', 0))
    frontier_runs = int(rq.POST.get('frontier_runs', 0))
    monte_carlo_simulations = int(rq.POST.get('monte_carlo_simulations', 0))
    solver = rq.POST.get('solver')
    dendogram_segment = rq.POST.get('dendogram_segment')
    
    # Ticker data - assuming the tickers and their related data are sent as lists
    symbols = rq.POST.getlist('symbols[]')
    shortnames = rq.POST.getlist('shortnames[]')    
    industries = rq.POST.getlist('industries[]')
    previous_closes = rq.POST.getlist('previous_closes[]')
    betas = rq.POST.getlist('betas[]')
    baws = rq.POST.getlist('baws[]')    
    amins = rq.POST.getlist('amins[]')    
    amaxs = rq.POST.getlist('amaxs[]')    
    sectors = rq.POST.getlist('sectors[]') 
    marketcaps = rq.POST.getlist('marketcaps[]') 
    correlations = rq.POST.getlist('correlations[]') 


    # Create the ticker data structure
    ticker_data = []
    for i in range(len(symbols)):
        ticker_data.append({
            "symbol": symbols[i],
            "shortname": shortnames[i],
            "sector": sectors[i],
            "industry": industries[i],
            "marketcap": marketcaps[i].replace(',', ''),
            "previous_close": previous_closes[i],
            "beta": betas[i],
            "baw": baws[i],
            "amin": amins[i],
            "amax": amaxs[i],
            "correlation": correlations[i],
            
        })
    
    
    # Construct final JSON structure
    form_data = {
        "start_date": start_date,
        "end_date": end_date,
        "calculation_parameters": {
            "return_calculation": return_calculation,
            "price_frequency": price_frequency,
            "risk_free_rate": risk_free_rate,
            "invested_amount": invested_amount
        },
        "optimization_parameters": {
            "benchmark_portfolio": benchmark_portfolio,
            "target_return_for_min_volatility": trv_min,
            "target_volatility_for_max_return": trv_max,
            "default_min_weight": default_min_weight,
            "default_max_weight": default_max_weight,
            "frontier_runs": frontier_runs,
            "monte_carlo_simulations": monte_carlo_simulations,
            "benchmark_ticker": "^GSPC",  # Hardcoded for now, modify if needed
            "solver": solver,
            "dendogram_segment": dendogram_segment
        },
        "ticker_data": ticker_data
    }

    return form_data
    

def create_table(data):
    return {
            'Expected Return': f"{data['expected_return'] * 100:.2f}%",
            'Standard Deviation': f"{data['standard_deviation'] * 100:.2f}%",
            'Sharpe Ratio': f"{data['sharpe_ratio'] * 100:.2f}%",  
            'CVaR 90%': f"{data['cvar_090'] * 100:.2f}%",
            'CVaR 95%': f"{data['cvar_095'] * 100:.2f}%",
            'CVaR 99%': f"{data['cvar_099'] * 100:.2f}%",
            'Tracking Error': data['tracking_errors']
        }


def create_pie_chart(labels, values):
    colors = ['#FF5733', '#33FF57'] 
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(colors=colors),
        textfont=dict(color='white'),
        hoverinfo='label+value',
        hovertemplate='<b>%{label}</b><br>Value: %{value}<extra></extra>',
        hoverlabel=dict(
            font=dict(family='Arial, sans-serif', size=14, color='white'),
            bgcolor='#ffffff',
            bordercolor='#FF0000'
        )
    )])
    fig.update_layout(
        template='plotly_white',
        legend=dict(yanchor="top", y=1.2, xanchor="center", x=0.5, orientation='h'),
    )
    return json.dumps(fig, cls=PlotlyJSONEncoder)


def create_consolidate_table(all_symbols, consolidated_table):
    table_html = '<table class="table table-striped"><thead class="bg-dark text-light"><tr>'
    table_html += '<th>Strategy Name</th>'
    table_html += '<th>Expected Return (%)</th>'
    table_html += '<th>Standard Deviation (%)</th>'
    table_html += '<th>Sharpe Ratio</th>'
    
    # Add symbols as headers
    for symbol in all_symbols:
        table_html += f'<th>{symbol}</th>'
    
    table_html += '</tr></thead><tbody>'
    
    # Populate table rows
    for row in consolidated_table:
        table_html += '<tr>'
        table_html += f'<td>{row["strategy_name"]}</td>'
        table_html += f'<td>{row["expected_return"]}</td>'
        table_html += f'<td>{row["standard_deviation"]}</td>'
        table_html += f'<td>{row["sharpe_ratio"]}</td>'
        
        # Populate symbol values
        for symbol in all_symbols:
            table_html += f'<td>{row.get(symbol, "0.00%")}</td>'  # Default to "0.00%" if the symbol doesn't exist
            
        table_html += '</tr>'
    
    table_html += '</tbody></table>'

    return table_html


def create_return_risk_chart(frontier_runs, strategy_x, strategy_y, scatter_do_color, strategy_labels):
    frontier_x = frontier_runs['x']
    frontier_y = frontier_runs['y']

    fig = go.Figure()

    # Add Efficient Frontier (Blue Line)
    fig.add_trace(go.Scatter(
        x=frontier_x, 
        y=frontier_y, 
        mode='lines+markers', 
        name='Efficient Frontier',
        line=dict(color='blue'),
        marker=dict(color='blue')
    ))

    # Add Portfolio Strategy points (Yellow Dots)
    scatter_trace = go.Scatter(
        x=strategy_x, 
        y=strategy_y, 
        mode='markers+text',
        text=strategy_labels, 
        name='Strategies',
        marker=dict(color=scatter_do_color, size=10),
        textposition='top center',
        textfont=dict(
            family="Arial",  # Font family
            size=12,         # Font size
            color="black"    # Font color
        )
    )

    # Conditionally add the texttemplate if strategy_labels is not empty
    if strategy_labels and any(strategy_labels):
        scatter_trace['texttemplate'] = "<span style='border: 1px solid black; background-color: red; padding: 2px;'>%{text}</span>"

    # Add the trace to the figure
    fig.add_trace(scatter_trace)

    # Set axis titles and layout
    fig.update_layout(
        xaxis_title="Risk (%)",
        yaxis_title="Return (%)",
        legend=dict(yanchor="top", y=1.1, xanchor="center", x=0.5, orientation='h'),
    )

    # Convert Plotly figure to JSON
    graph_json = json.dumps(fig, cls=PlotlyJSONEncoder)

    return graph_json


def format_strategy_name(strategy_name):
    # Replace underscores with spaces
    strategy_name = strategy_name.replace('_', ' ').title()
    
    # Replace 'cvar' with 'CVaR' (case insensitive)
    strategy_name = strategy_name.replace('Cvar', 'CVaR')
    strategy_name = strategy_name.replace('CVaR 999', 'CVaR 99.9')
 
    if strategy_name.lower() == 'hrp':
        strategy_name = 'HRP'
    
    return strategy_name


def transform_key(key):
    return key.replace('_', ' ').title()


def transform_metric(metric):
    transformed_metric = metric.replace('_', ' ').title()
    return re.sub(r'\bAnnual\s*', '', transformed_metric)

float_metrics = {
    'annual_sharpe_ratio', 'annual_sortino_ratio', 'beta', 'skew', 'kurtosis', 'daily_sharpe_ratio', 'daily_sortino_ratio', 'entropic_risk_measure_at_95', 'ulcer_index', 'mean_absolute_deviation_ratio', 'first_lower_partial_moment_ratio', 'value_at_risk_ratio_at_95', 'conditional_var_ratio_at_95',  'entropic_risk_measure_ratio_at_95', 'entropic_var_ratio_at_95', 'worst_realization_ratio', 'drawdown_at_risk_ratio_at_95', 'conditional_dar_ratio_at_95',  'calmar_ratio', 'average_drawdown_ratio', 'entropic_dar_ratio_at_95', 'ulcer_index_ratio', 'gini_mean_difference_ratio'
}


def format_table_value(metric_name, value):
    # Format the value based on the metric name
    if metric_name in float_metrics:
        if 'e-' in str(value):
            base, exponent = str(value).split('e-')
            formatted_value = f"{float(base):.2f}e-{exponent}"
        else:
            formatted_value = f"{value:.2f}"
        
        # Create the HTML structure
        html_output = (
            f'<span class="formatted-value">{formatted_value}</span>'
            f'<span class="original-value">{value}</span>'
        )
    else:
        formatted_value = f"{(value * 100):.2f}%"
        
        # Create the HTML structure for percentage
        html_output = (
            f'<span class="formatted-value">{formatted_value}</span>'
            f'<span class="original-value">{value}</span>'
        )

    return html_output

# SL data processing function
def process_stats_data(strategy_symbol_portfolios, stat_type_key, sl_stats_data):

    for strategy, strategy_data in strategy_symbol_portfolios.items():
        if stat_type_key in strategy_data:
            if strategy not in sl_stats_data:
                sl_stats_data[strategy] = []
            
            # Loop through each statistic within the strategy
            for stat_name, metrics in strategy_data[stat_type_key].items():
                metric_entry = {
                    'metric': transform_metric(stat_name)  # Transform metric name as needed
                }
                
                # Add symbol-value pairs to the entry and format the value
                for symbol, value in metrics.items():
                    metric_entry[symbol] = format_table_value(stat_name, value)
                
                sl_stats_data[strategy].append(metric_entry)

# Generate table for strategy optimization summary
def generate_optimization_summary_html_table(data):
    table_html = '<div class="table-reponsive"><table class="table table-striped">'
    table_html += '<thead>'
    table_html += '<tr>'
    table_html += f'<th class="p-2">Strategy</th>'
    table_html += '<th class="p-2">Expected Return</th>'
    table_html += '<th class="p-2">Volatility</th>'
    table_html += '<th class="p-2">Sharpe Ratio</th>'
    table_html += '<th class="p-2">Sortino Ratio</th>'
    table_html += '<th class="p-2">#Symbols</th>'
    table_html += '<th class="p-2">Top 3 Symbol Allocation</th>'
    table_html += '<th class="p-2">Top 3 Sector Allocation</th>'
    table_html += '</tr>'
    table_html += '</thead>'
    table_html += '<tbody>'

    for strategy, metrics in data.items():
        top_3_symbol_allocation = metrics["Top 3 Symbol Allocation"].replace(", ", "<br>")
        top_3_sector_allocation = metrics["Top 3 Sector Allocation"].replace(", ", "<br>")
        table_html += '<tr>'
        table_html += f'<td>{format_strategy_name(strategy)}</td>'
        table_html += f'<td class="table-value-cell p-2">{format_table_value("Expected Return", metrics["Expected Return"])}</td>'
        table_html += f'<td class="table-value-cell p-2">{format_table_value("Volatility", metrics["Volatility"])}</td>'
        table_html += f'<td class="table-value-cell p-2">{format_table_value("Sharpe Ratio", metrics["Sharpe Ratio"])}</td>'
        table_html += f'<td class="table-value-cell p-2">{format_table_value("Sortino Ratio", metrics["Sortino Ratio"])}</td>'
        table_html += f'<td class="p-2">{metrics["#Symbols"]}</td>'
        table_html += f'<td class="p-2" style="line-height: 24px;">{top_3_symbol_allocation}</td>'
        table_html += f'<td class="p-2" style="line-height: 24px;">{top_3_sector_allocation}</td>'
        table_html += '</tr>'
    
    table_html += '</tbody>'
    table_html += '</table></div>'
    
    return table_html

def api_data_view_4(request):

    if request.method == 'POST':
        form_data = process_form(request)
        # print("=========================================================")
        # print("Form Data: ", form_data)
        # print("=========================================================")

        start_time = time.time()
        # Return-Risk Chart data
        frontier_runs = output_data['frontier_runs']
        strageties = output_data['frontier_positions']
        strategy_x = strageties['x']
        strategy_y = strageties['y']
        strategy_labels = strageties['strategy_names']
        scatter_do_color = 'orange'

        graph_json_1 = create_return_risk_chart(frontier_runs, strategy_x, strategy_y, scatter_do_color, strategy_labels)


        summary_tbl_data = output_data['strategies']
        summary_tbl = []
        for strategy in summary_tbl_data:
            if strategy['data'] is not None and strategy['data']['portfolio_summary'] is not None:
                portfolio_summary = strategy['data']['portfolio_summary']

                # Create a new dictionary with the required fields
                summary_item = {
                    'strategy_name': strategy['name'],
                    'expected_return': f"{portfolio_summary.get('annualized_mean', None)* 100:.2f}%",
                    'standard_deviation': f"{portfolio_summary.get('annualized_standard_deviation', None)* 100:.2f}%",
                    'sharpe_ratio': f"{portfolio_summary.get('annualized_sharpe_ratio', None)* 100:.2f}%",
                    'sortino_ratio': f"{portfolio_summary.get('annualized_sortino_ratio', None)* 100:.2f}%",
                    'cvar_090': f"{portfolio_summary.get('cvar_at_95', None)* 100:.2f}%",  # Adjust based on your requirements
                    'cvar_095': f"{portfolio_summary.get('cvar_at_95', None)* 100:.2f}%",  # Adjust based on your requirements
                    'cvar_099': f"{portfolio_summary.get('cvar_at_95', None)* 100:.2f}%"   # Adjust based on your requirements
                }

                # Append the summary_item to summary_tbl
                summary_tbl.append(summary_item)

        results = []
        consolidated_table = []
        all_symbols = set()
        strategy_expected_return = []
        strategy_standard_deviation = []

        for strategy in output_data['strategies']:
            strategy_data = strategy['data']
            if strategy_data is not None:
                allocation_data = strategy_data['symbol_allocations']
                strategy_expected_return.append(strategy_data['expected_return'])
                strategy_standard_deviation.append(strategy_data['standard_deviation'])
                labels = []
                allocations = []

                # Extract labels and allocations
                if isinstance(allocation_data, list) and len(allocation_data) > 0:
                    for label in allocation_data:
                        labels.append(label['symbol'])
                        allocations.append(label['allocation_weight'])
                        all_symbols.add(label['symbol'])  # Collect all symbols for the consolidated table

                elif isinstance(allocation_data, dict) and allocation_data:
                    labels.append(allocation_data['symbol'])
                    allocations.append(allocation_data['allocation_weight'])
                    all_symbols.add(allocation_data['symbol'])  # Collect all symbols for the consolidated table

                # Create the chart and table for the current strategy
                chart = create_pie_chart(labels, allocations)
                table = create_table(strategy_data)

                # Prepare the row for the consolidated table
                row = {
                    'strategy_name': strategy['name'],
                    'expected_return': f"{strategy_data['expected_return'] * 100:.2f}%",
                    'standard_deviation': f"{strategy_data['standard_deviation'] * 100:.2f}%",
                    'sharpe_ratio': f"{strategy_data['sharpe_ratio']:.2f}",
                }

                # Initialize allocation data for all symbols (default to 0.00%)
                for symbol in all_symbols:
                    row[symbol] = "0.00%"  # Start with 0.00% for every symbol

                # Populate allocation data for the current strategy
                if isinstance(allocation_data, list):
                    for allocation in allocation_data:
                        row[allocation['symbol']] = f"{allocation['allocation_weight'] * 100:.2f}%"
                elif isinstance(allocation_data, dict):
                    row[allocation_data['symbol']] = f"{allocation_data['allocation_weight'] * 100:.2f}%"

                # Append the row to the consolidated table
                consolidated_table.append(row)


                # Append the chart and table data to results
                results.append({
                    'strategy_name': strategy['name'],
                    'table_data': table,
                    'chart_data': chart
                })

        table_html = create_consolidate_table(all_symbols, consolidated_table)
        scatter_do_color = 'red'
        graph_json_2 = create_return_risk_chart(frontier_runs, strategy_expected_return, strategy_standard_deviation, scatter_do_color, [])
        end_time = time.time()
        # Calculate the processing time
        processing_time = end_time - start_time
    
        context = {
            'graph_json_1': graph_json_1,
            'graph_json_2': graph_json_2,
            'summary_tbl': summary_tbl,
            'strategies': results,
            'consolidated_table': consolidated_table,
            'all_symbols': all_symbols,
            'table_html': table_html,
            'processing_time': processing_time
        }

        # Pass the results to your template
        return render(request, 'data4.html', context)
    

@login_required(login_url='/login/')
def api_data_view_5(request):

    if request.method == 'POST':
        form_data = process_form(request)
   

        start_time = time.perf_counter()
        model_output = model_output_data

        mvoh_runs = request.session.get('mvoh_runs', [])

        new_mvoh_run = {
            'run_id': len(mvoh_runs) + 1,  
            'title': 'Run ' + str(len(mvoh_runs) + 1),
            'form_data': form_data,
            'output': model_output
        }

        mvoh_runs.append(new_mvoh_run)
        request.session['mvoh_runs'] = mvoh_runs

        frontier_runs_x = model_output.get('frontier_runs').get('x')
        frontier_runs_y = model_output.get('frontier_runs').get('y')
        frontier_positions_random_x = model_output.get('frontier_positions_random').get('x')
        frontier_positions_random_y = model_output.get('frontier_positions_random').get('y')

        frontier_runs_x = [x * 100 for x in frontier_runs_x]
        frontier_runs_y = [y * 100 for y in frontier_runs_y]
        frontier_positions_random_x = [x * 100 for x in frontier_positions_random_x]
        frontier_positions_random_y = [y * 100 for y in frontier_positions_random_y]

        frontier_runs = model_output.get('frontier_runs')
        frontier_positions = model_output.get('frontier_positions')
        
        
        strategy_allocation_data = []
        strategy_purchase_allocations = model_output.get('strategy_results', {}).get('strategy_purchase_allocation', {})
        strategy_current_allocations = model_output.get('strategy_results', {}).get('strategy_current_allocation', {})
        strategy_sector_purchase_allocations = model_output.get('strategy_results', {}).get('strategy_sector_purchase_allocation', {})
        strategy_sector_current_allocations = model_output.get('strategy_results', {}).get('strategy_sector_current_allocation', {})
        strategy_performances = model_output.get('strategy_results', {}).get('strategy_performance', {})
        strategy_stats_descriptives = model_output.get('strategy_results', {}).get('strategy_stats_descriptive', {})
        strategy_stats_moments = model_output.get('strategy_results', {}).get('strategy_stats_moments', {})
        strategy_stats_risk_measures = model_output.get('strategy_results', {}).get('strategy_stats_risk_measures', {})
        strategy_stats_ratios = model_output.get('strategy_results', {}).get('strategy_stats_ratios', {})
        strategy_symbol_portfolios = model_output.get('strategy_results', {}).get('strategy_symbol_portfolios', {})
        strategy_symbol_contributions = model_output.get('strategy_results', {}).get('strategy_symbol_contributions', {})
        
        # Testing Data
        strategy_performance_testing = model_output.get('strategy_results', {}).get('strategy_performance_testing', {})
        strategy_stats_descriptive_testing = model_output.get('strategy_results', {}).get('strategy_stats_descriptive_testing', {})
        strategy_stats_moments_testing = model_output.get('strategy_results', {}).get('strategy_stats_moments_testing', {})
        strategy_stats_risk_measures_testing = model_output.get('strategy_results', {}).get('strategy_stats_risk_measures_testing', {})
        strategy_stats_ratios_testing = model_output.get('strategy_results', {}).get('strategy_stats_ratios_testing', {})

        strategy_symbol_contributions_testing = model_output.get('strategy_results', {}).get('strategy_symbol_contributions_testing', {})
        strategy_symbol_portfolios_testing = model_output.get('strategy_results', {}).get('strategy_symbol_portfolios_testing', {})

        # Security Level Risk
        sl_main_stats_data = {}
        sl_descriptive_stats_data = {}
        sl_moments_stats_data = {}
        sl_risk_measure_stats_data = {}
        sl_ratio_stats_data = {}

        # Security-contribution Level
        cl_descriptive_stats_data = {}
        cl_moment_stats_data = {}
        cl_risk_measure_stats_data = {}
        cl_ratio_stats_data = {}

        # Testing Assets
        cl_testing_descriptive_stats_data = {}
        cl_testing_stats_moments_data = {}
        cl_testing_risk_measures_stats_data = {}
        cl_testing_ratio_stats_data = {}

        pl_testing_main_stats_data = {}
        pl_testing_descriptive_stats_data = {}
        pl_testing_stats_moments_data = {}
        pl_testing_risk_measures_stats_data = {}
        pl_testing_ratio_stats_data = {}

        # Security Level Risk  Assets
        # Process the 'main' stats
        process_stats_data(strategy_symbol_portfolios, 'strategy_symbol_stats_main', sl_main_stats_data)
        # Process the 'descriptive' stats
        process_stats_data(strategy_symbol_portfolios, 'strategy_symbol_stats_descriptive', sl_descriptive_stats_data)
        # Process the 'moment' stats
        process_stats_data(strategy_symbol_portfolios, 'strategy_symbol_stats_moments', sl_moments_stats_data)
        # Process the 'moment' stats
        process_stats_data(strategy_symbol_portfolios, 'strategy_symbol_stats_risk_measures', sl_risk_measure_stats_data)
        # Process the 'moment' stats
        process_stats_data(strategy_symbol_portfolios, 'strategy_symbol_stats_ratios', sl_ratio_stats_data)

        # Security-Contribution Assets
        # Process the 'descriptive' stats
        process_stats_data(strategy_symbol_contributions, 'symbol_contribution_stats_descriptive', cl_descriptive_stats_data)
        # Process the 'descriptive' stats
        process_stats_data(strategy_symbol_contributions, 'symbol_contribution_stats_moments', cl_moment_stats_data)
        # Process the 'descriptive' stats
        process_stats_data(strategy_symbol_contributions, 'symbol_contribution_stats_risk_measures', cl_risk_measure_stats_data)
        # Process the 'descriptive' stats
        process_stats_data(strategy_symbol_contributions, 'symbol_contribution_stats_ratios', cl_ratio_stats_data)

        # Testing Assets
        process_stats_data(strategy_symbol_contributions_testing, 'symbol_contribution_stats_descriptive', cl_testing_descriptive_stats_data)
        process_stats_data(strategy_symbol_contributions_testing, 'symbol_contribution_stats_moments', cl_testing_stats_moments_data)
        process_stats_data(strategy_symbol_contributions_testing, 'symbol_contribution_stats_risk_measures', cl_testing_risk_measures_stats_data)
        process_stats_data(strategy_symbol_contributions_testing, 'symbol_contribution_stats_ratios', cl_testing_ratio_stats_data)

        process_stats_data(strategy_symbol_portfolios_testing, 'strategy_symbol_stats_main', pl_testing_main_stats_data)
        process_stats_data(strategy_symbol_portfolios_testing, 'strategy_symbol_stats_descriptive', pl_testing_descriptive_stats_data)
        process_stats_data(strategy_symbol_portfolios_testing, 'strategy_symbol_stats_moments', pl_testing_stats_moments_data)
        process_stats_data(strategy_symbol_portfolios_testing, 'strategy_symbol_stats_risk_measures', pl_testing_risk_measures_stats_data)
        process_stats_data(strategy_symbol_portfolios_testing, 'strategy_symbol_stats_ratios', pl_testing_ratio_stats_data)



        formatted_allocations = {}
        for strategy, allocations in strategy_purchase_allocations.items():
            # Prepare the allocations as a JSON serializable format
            formatted_allocations[strategy] = [
                {"value": round(allocation  * 100, 2), "name": stock }  
                for stock, allocation in allocations.items()
            ] 
        
        formatted_strategy_current_allocations = {} 
        for strategy, allocations in strategy_current_allocations.items():
            # Prepare the allocations as a JSON serializable format
            formatted_strategy_current_allocations[strategy] = [
                {"value": round(allocation  * 100, 2), "name": stock}  
                for stock, allocation in allocations.items()
            ]

        formatted_sector_allocations = {}
        for strategy, allocations in strategy_sector_purchase_allocations.items():
            # Prepare the allocations as a JSON serializable format
            formatted_sector_allocations[strategy] = [
                {"value": round(allocation  * 100, 2), "name": stock}  # Correct format for the chart data
                for stock, allocation in allocations.items()
            ]

        formatted_strategy_sector_current_allocations = {}
        for strategy, allocations in strategy_sector_current_allocations.items():
            # Prepare the allocations as a JSON serializable format
            formatted_strategy_sector_current_allocations[strategy] = [
                {"value": round(allocation  * 100, 2), "name": stock}  # Correct format for the chart data
                for stock, allocation in allocations.items()
            ]

        
        symbol_hex_colors = model_output.get('hex_colors', {}).get('symbol_hex_colors', {})
        sector_hex_colors = model_output.get('hex_colors', {}).get('sector_hex_colors', {})

        strategy_allocation_data.append({
            'strategy_performances': strategy_performances,
            'strategy_stats_descriptives': strategy_stats_descriptives,
            'strategy_stats_moments': strategy_stats_moments,
            'strategy_stats_risk_measures': strategy_stats_risk_measures,
            'strategy_stats_ratios': strategy_stats_ratios,
            'strategy_purchase_allocations': formatted_allocations,
            'strategy_current_allocations': formatted_strategy_current_allocations,
            'strategy_sector_purchase_allocations': formatted_sector_allocations,
            'strategy_sector_current_allocations': formatted_strategy_sector_current_allocations,
            'sl_main_stats_data': sl_main_stats_data,
            'sl_descriptive_stats_data': sl_descriptive_stats_data,
            'sl_moments_stats_data': sl_moments_stats_data,
            'sl_risk_measure_stats_data': sl_risk_measure_stats_data,
            'sl_ratio_stats_data': sl_ratio_stats_data,
            'cl_descriptive_stats_data': cl_descriptive_stats_data,
            'cl_moment_stats_data': cl_moment_stats_data,
            'cl_risk_measure_stats_data': cl_risk_measure_stats_data,
            'cl_ratio_stats_data': cl_ratio_stats_data,
            'cl_testing_descriptive_stats_data': cl_testing_descriptive_stats_data,
            'cl_testing_stats_moments_data': cl_testing_stats_moments_data,
            'cl_testing_risk_measures_stats_data': cl_testing_risk_measures_stats_data,
            'cl_testing_ratio_stats_data': cl_testing_ratio_stats_data,
            'pl_testing_main_stats_data': pl_testing_main_stats_data,
            'pl_testing_descriptive_stats_data': pl_testing_descriptive_stats_data,
            'pl_testing_stats_moments_data': pl_testing_stats_moments_data,
            'pl_testing_risk_measures_stats_data': pl_testing_risk_measures_stats_data,
            'pl_testing_ratio_stats_data': pl_testing_ratio_stats_data,
            'strategy_performance_testing': strategy_performance_testing,
            'strategy_stats_descriptive_testing': strategy_stats_descriptive_testing,
            'strategy_stats_moments_testing': strategy_stats_moments_testing,
            'strategy_stats_risk_measures_testing': strategy_stats_risk_measures_testing,
            'strategy_stats_ratios_testing': strategy_stats_ratios_testing,

        })

        # top level heatmap
        covariance_data = model_output.get('covariance', {})
        covariance_stock_symbols = list(covariance_data.keys())
        covariance_heatmap_data = []
        for i, stock_x in enumerate(covariance_stock_symbols):
            for j, stock_y in enumerate(covariance_stock_symbols):
                covariance_heatmap_data.append([i, j, covariance_data[stock_x][stock_y]])


        correlation_data = model_output.get('correlation', {})
        correlation_stock_symbols = list(correlation_data.keys())
        correlation_heatmap_data = []
        for i, stock_x in enumerate(correlation_stock_symbols):
            for j, stock_y in enumerate(correlation_stock_symbols):
                correlation_heatmap_data.append([i, j, correlation_data[stock_x][stock_y]])

        # Strategy level heatmap
        strategy_covariance_data = model_output.get('strategy_results', {}).get('strategy_covariance', {})
        strategy_correlation_data = model_output.get('strategy_results', {}).get('strategy_correlation', {})

        symbol_portfolios_data = []

        symbol_portfolios = model_output.get('symbol_portfolios')
        
        

        # List all the symbols
        all_symbols = set()
        for main_label, inner_dict in symbol_portfolios.items():
            for inner_label, symbols in inner_dict.items():
                for symbol in symbols:
                    all_symbols.add(symbol)
        
        all_symbols = list(all_symbols)


        # Initialize the final HTML structure
        all_tables_html = ''

        for key in symbol_portfolios:
            metrics = symbol_portfolios.get(key)
            transformed_key = "SL Risk: " + key.replace('symbol_stats_', '').replace('_', ' ').title()

            symbol_portfolios_data = []
            for metric in metrics:
                transformed_metric = transform_metric(metric)

                row = {
                    "metric": transformed_metric, 
                    **{
                        symbol: format_table_value(metric, metrics[metric].get(symbol))
                        for symbol in all_symbols
                    }
                }
                symbol_portfolios_data.append(row)

            # Build the HTML table for each key (without the "key" column)
            symbol_portfolios_html_table = f'<h3 id="sl-risk-{key}">{transformed_key}</h3>' 
            symbol_portfolios_html_table += '<table class="table table-striped">'
            symbol_portfolios_html_table += '<thead><tr>'
            symbol_portfolios_html_table += '<th class="font-weight-bold">Metrics Name</th>'
            
            # Add headers for each symbol
            for symbol in all_symbols:
                symbol_portfolios_html_table += f'<th class="font-weight-bold">{symbol}</th>'
            
            symbol_portfolios_html_table += '</tr></thead><tbody>'
            
            # Add data rows for each metric (without the "key" column)
            for row in symbol_portfolios_data:
                symbol_portfolios_html_table += f'<tr><td class="p-2">{row["metric"]}</td>'
                
                for symbol in all_symbols:
                    symbol_portfolios_html_table += f'<td class="table-value-cell p-2">{row.get(symbol, "N/A")}</td>'
                
                symbol_portfolios_html_table += '</tr>'
            
            symbol_portfolios_html_table += '</tbody></table><br><br>'
            
            # Add this table to the final output HTML
            all_tables_html += symbol_portfolios_html_table


        structured_strategies = []
        strategy_summaries = model_output.get('strategy_results', {}).get('strategy_performance', {})
        
        for strategy_name, strategy_data in strategy_summaries.items():
            # Create the structure for each strategy

            structured_strategy = {
                "strategy_id": strategy_name,
                "strategy_name": format_strategy_name(strategy_name),
                "annual_expected_return": format_table_value('annual_expected_return', strategy_data.get('annual_expected_return')),
                "annual_standard_deviation": format_table_value('annual_standard_deviation', strategy_data.get('annual_standard_deviation')),
                "annual_sharpe_ratio": format_table_value('annual_sharpe_ratio', strategy_data.get('annual_sharpe_ratio')),
                "annual_sortino_ratio": format_table_value('annual_sortino_ratio', strategy_data.get('annual_sortino_ratio')),
                "cvar_900": format_table_value('cvar_900', strategy_data.get('cvar_900')),
                "cvar_950": format_table_value('cvar_950', strategy_data.get('cvar_950')),
                "cvar_990": format_table_value('cvar_990', strategy_data.get('cvar_990')),
                "cvar_999": format_table_value('cvar_999', strategy_data.get('cvar_999'))
            }

            # Append the structured strategy data to the list
            structured_strategies.append(structured_strategy)
            

        top_level_lines_chart_data =   model_output.get('total_return_testing', {})
        strategy_level_line_chart_data = model_output.get('strategy_results', {}).get('strategy_total_return_testing', {})

        
        formatted_top_level_lines_data = []
    
        for strategy_name, strategy_data in top_level_lines_chart_data.items():
            formatted_top_level_lines_data.append({
                'name': strategy_name,  # Benchmark, min_variance, max_sharpe
                'x': strategy_data['x'],
                'y': strategy_data['y']
            })

    
    
        strategy_optimization_summary = model_output.get('strategy_results', {}).get('strategy_optimization_summary', {})
        strategy_testing_summary = model_output.get('strategy_results', {}).get('strategy_testing_summary', {})
        strategy_optimization_summary_table = generate_optimization_summary_html_table(strategy_optimization_summary)
        strategy_testing_summary_table = generate_optimization_summary_html_table(strategy_testing_summary)


        end_time = time.perf_counter()
        processing_time = (end_time - start_time)
        # dummy model time
        # time_model_data_processing = 1
        # time_model_execusion = 2
        # time_model_output_allocation = 7
        # time_model_total = time_model_data_processing + time_model_execusion + time_model_output_allocation
        # total_processing_time = processing_time + time_model_total

        context = {
            'frontier_runs': frontier_runs,
            'frontier_positions': frontier_positions,
            'strategy_allocation_data': strategy_allocation_data,
            'covariance_stock_symbols': covariance_stock_symbols,
            'covariance_heatmap_data': covariance_heatmap_data,
            'correlation_stock_symbols': correlation_stock_symbols,
            'correlation_heatmap_data': correlation_heatmap_data,
            'symbol_portfolios_html_table': all_tables_html,
            'strategy_summaries': structured_strategies,
            'symbol_hex_colors': symbol_hex_colors,
            'sector_hex_colors': sector_hex_colors,
            'frontier_runs_x': frontier_runs_x,
            'frontier_runs_y': frontier_runs_y,
            'frontier_positions_random_x': frontier_positions_random_x,
            'frontier_positions_random_y': frontier_positions_random_y,
            'processing_time': processing_time,
            'formatted_top_level_lines_data': json.dumps(formatted_top_level_lines_data), 
            'strategy_level_line_chart_data': json.dumps(strategy_level_line_chart_data),
            'strategy_optimization_summary': json.dumps(strategy_optimization_summary),
            'strategy_testing_summary': json.dumps(strategy_testing_summary),
            'strategy_optimization_summary_table': strategy_optimization_summary_table,
            'strategy_testing_summary_table': strategy_testing_summary_table,
            'strategy_covariance_heatmap_data': strategy_covariance_data,
            'strategy_correlation_heatmap_data': strategy_correlation_data,
            
        }

        return render(request, 'data5.html', context)


    start_time = time.time()
    # Return-Risk Chart data
    frontier_runs = output_data['frontier_runs']
    strageties = output_data['frontier_positions']
    strategy_x = strageties['x']
    strategy_y = strageties['y']
    strategy_labels = strageties['strategy_names']
    scatter_do_color = 'orange'

    graph_json_1 = create_return_risk_chart(frontier_runs, strategy_x, strategy_y, scatter_do_color, strategy_labels)

    context = {
        'graph_json_1': graph_json_1
    }

    # Pass the results to your template
    return render(request, 'data6.html', context)


