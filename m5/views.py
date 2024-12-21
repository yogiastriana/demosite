from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from demosite.views import process_form, process_stats_data, convert_to_standard_date_format, transform_metric, format_strategy_name, format_table_value, generate_optimization_summary_html_table
import time 
import json

from .model_result import model_output_data

from runs.models import Run


# M4 form processing function
def process_m5_form(rq):
    # Fetch form data
    start_date = convert_to_standard_date_format(rq.POST.get('start_date'))
    end_date = convert_to_standard_date_format(rq.POST.get('end_date'))
    
    # Calculation parameters
    return_calculation = rq.POST.get('return_calculation')
    price_frequency = rq.POST.get('price_frequency')
    invested_amount = float(rq.POST.get('invested_amount', 0))
    risk_free_rate = float(rq.POST.get('risk_free_rate', 0))
    
    # Optimization parameters
    benchmark_portfolio = rq.POST.get('benchmark_portfolio')
    factors = float(rq.POST.get('factors', 0))
    confidence_interval = float(rq.POST.get('confidence_interval', 0))
    rolling_regression_mths = float(rq.POST.get('rolling_regression_mths', 0))
    projection_end_date = convert_to_standard_date_format(rq.POST.get('projection_end_date'))

    
    # Ticker data - assuming the tickers and their related data are sent as lists
    symbols = rq.POST.getlist('symbols[]')
    shortnames = rq.POST.getlist('shortnames[]')    
    pws = rq.POST.getlist('pws[]')
    pdas = rq.POST.getlist('pdas[]')
    sectors = rq.POST.getlist('sectors[]')
    marketcaps = rq.POST.getlist('marketcaps[]') 


    # Create the ticker data structure
    ticker_data = []
    for i in range(len(symbols)):
        ticker_data.append({
            "symbol": symbols[i],
            "shortname": shortnames[i],
            "pw": pws[i],
            "pda": pdas[i],
            "sector": sectors[i],
            "marketcap": marketcaps[i].replace(',', ''),
            
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
            "factors": factors,
            "confidence_interval": confidence_interval,
            "rolling_regression_mths": rolling_regression_mths,
            "projection_end_date": projection_end_date,
        },
        "ticker_data": ticker_data
    }

    return form_data


@login_required(login_url='/login/')
def input_form_view(request):

    if request.user.userprofile.role == 'admin':
        runs = Run.objects.all()
    else:
        runs = Run.objects.filter(user=request.user.id)

    context = {
        "runs": runs
    }

    return render(request, 'm5/index.html', context)


def generate_html_table(data):
    if not data:
        return "<p>No data available to display.</p>"

    # Extract column headers from keys of the first row
    headers = data[0].keys()

    # Start building the HTML table
    html = "<table class='table table-striped'>"
    html += """
        <thead>
            <tr>
    """
    # Add table headers
    for header in headers:
        html += f"<th class='p-2'>{header}</th>"
    html += "</tr></thead>"

    # Add table rows
    html += "<tbody>"
    for row in data:
        html += "<tr>"
        for header in headers:
            value = row.get(header, "")
            if isinstance(value, float):  # Format floats to 2 decimal places
                formatted_value = f"{value:.2f}" if isinstance(value, float) else f"{value:}"
                html_output = (
                    f'<span class="formatted-value">{formatted_value}</span>'
                    f'<span class="original-value">{value}</span>'
                )
                html += f"<td class='p-2 table-value-cell'>{html_output}</td>"
            else:
                html += f"<td class='p-2'>{value}</td>"
        html += "</tr>"
    html += "</tbody></table>"

    return html


def generate_residual_html_table(data):
    if not data:
        return "<p>No data available to display.</p>"

    # Extract column headers from keys of the first row
    headers = data[0].keys()

    # Start building the HTML table
    html = "<table class='table table-striped'>"
    html += """
        <thead>
            <tr>
    """
    # Add table headers
    for header in headers:
        html += f"<th class='p-2'>{header}</th>"
    html += "</tr></thead>"

    # Add table rows
    html += "<tbody>"
    for row in data:
        html += "<tr>"
        for header in headers:
            value = row.get(header, "")
            if isinstance(value, float):  # Format floats to 2 decimal places
                formatted_value = f"{value:.5f}" if isinstance(value, float) else f"{value:}"
                html_output = (
                    f'<span class="formatted-value">{formatted_value}</span>'
                    f'<span class="original-value">{value}</span>'
                )
                html += f"<td class='p-2 table-value-cell'>{html_output}</td>"
            else:
                html += f"<td class='p-2'>{value}</td>"
        html += "</tr>"
    html += "</tbody></table>"

    return html


def generate_overview_table(overview_data):
    if not overview_data:
        return "<p>No overview data available.</p>"

    html = '<table class="table table-striped">'
    html += '<thead><tr><th class="p-2" style="width: 110px;">Metric</th><th class="p-2" style="width: 110px;">Value</th></tr></thead>'
    html += '<tbody>'

    for key, value in overview_data.items():
        if isinstance(value, (float, int)):
            # Format numeric values and include additional HTML
            formatted_value = f"{value:.2f}" if isinstance(value, float) else f"{value:}"
            html_output = (
                f'<span class="formatted-value">{formatted_value}</span>'
                f'<span class="original-value">{value}</span>'
            )
            html += f"<tr><td class='p-2'>{key}</td><td class='p-2 table-value-cell'>{html_output}</td></tr>"
        else:
            # Non-numeric values are added directly
            html += f"<tr><td class='p-2'>{key}</td><td class='p-2'><div style='width: 100px;'>{value}</div></td></tr>"

    html += '</tbody></table>'
    return html


def generate_grouped_tables(regression_data):
    html = ""
    
    for key, value in regression_data.items():
        html += "<div class='card card-stretched'>"
        html += '<div class="card-header">'
        html += f"<h2 class='card-title mb-1 mt-1'>{key}</h2>"
        html += '</div><div class="card-body">'
        # Add a title for the group
        

        html += '<div class="regression-table-container parent-container">'
        # Generate the overview table
        table_overview = value.get("table_overview", {})
        if table_overview:
            html += "<div><h3>Overview</h3>"
            html += generate_overview_table(table_overview)
            html += "</div>"

        # Generate the factor table
        table_factor = value.get("table_factor", [])
        if table_factor:
            html += "<div><h3>Factor Analysis</h3>"
            html += generate_html_table(table_factor)
            html += "</div>"
        
        html += '</div></div></div>'

    return html


@login_required(login_url='/login/')
def output_view(request):
    if request.method == 'POST':
        form_data = process_m5_form(request)
   
        start_time = time.perf_counter()
        factor_breakdown_data = model_output_data.get('table_factor_breakdown', [])
        factor_breakdown_table = generate_html_table(factor_breakdown_data)
        regression_data = model_output_data.get('regression_data', [])
        regression_tables = generate_grouped_tables(regression_data)
        charts_overunder_data = model_output_data.get('charts_overunder', [])
        charts_portfolio_factors_data = model_output_data.get('charts_portfolio_factors', [])
        table_residuals = model_output_data.get('table_residuals', [])
        table_residuals_html = generate_residual_html_table(table_residuals)


        m5_runs = request.session.get('m5_runs', [])
        new_m5_runs = {
            'run_id': len(m5_runs) + 1,  
            'title': 'M5 Run ' + str(len(m5_runs) + 1),
            'form_data': form_data,
            'output': model_output_data
        }
        m5_runs.append(new_m5_runs)
        request.session['m5_runs'] = m5_runs

        
        context = {
            "factor_breakdown_table": factor_breakdown_table,
            "regression_tables": regression_tables,
            "charts_overunder_data": charts_overunder_data,
            "charts_portfolio_factors_data": charts_portfolio_factors_data,
            "table_residuals": table_residuals,
            "table_residuals_html": table_residuals_html,
        }

        return render(request, 'm5/run_output.html', context)
    

@login_required(login_url='/login/')
def fetch_m5_error_view(request):

    m5_runs = request.session.get('m5_runs', [])
    # Get the last run if available, or None if m5_runs is empty
    last_run = m5_runs[-1] if m5_runs else None

    
    if last_run:
        output = last_run.get('output')
        error = output.get('stacktraces')
    else:
        error = 'There is no error'
 
    error_context = {
        'error': error
    }
    error_html = render_to_string('m5/error.html', error_context, request=request)
    return HttpResponse(error_html)


@login_required(login_url='/login/')
def current_m5_result_view(request):
    m5_runs = request.session.get('m5_runs', [])

    # Get the last run if available, or None if m5_runs is empty
    last_run = m5_runs[-1] if m5_runs else None

    start_time = time.perf_counter()
    model_output = last_run.get('output')

    factor_breakdown_data = model_output.get('table_factor_breakdown', [])
    factor_breakdown_table = generate_html_table(factor_breakdown_data)
    regression_data = model_output.get('regression_data', [])
    regression_tables = generate_grouped_tables(regression_data)
    charts_overunder_data = model_output.get('charts_overunder', [])
    charts_portfolio_factors_data = model_output.get('charts_portfolio_factors', [])
    table_residuals = model_output.get('table_residuals', [])
    table_residuals_html = generate_residual_html_table(table_residuals)
    
    context = {
        "factor_breakdown_table": factor_breakdown_table,
        "regression_tables": regression_tables,
        "charts_overunder_data": charts_overunder_data,
        "charts_portfolio_factors_data": charts_portfolio_factors_data,
        "table_residuals": table_residuals,
        "table_residuals_html": table_residuals_html,
    }

    return render(request, 'm5/run_output.html', context)


@login_required(login_url='/login/')
def run_m5_model_view(request):
    if request.method == 'POST':
        form_data = process_m5_form(request)


        model_output = model_output_data

        error = model_output.get('error', None)

        m5_runs = request.session.get('m5_runs', [])
        new_m5_runs = {
            'run_id': len(m5_runs) + 1,  
            'title': 'M5 Run ' + str(len(m5_runs) + 1),
            'form_data': form_data,
            'output': model_output
        }
        m5_runs.append(new_m5_runs)
        request.session['m5_runs'] = m5_runs

        charts_overunder_data = model_output.get('charts_overunder', {})
        charts_portfolio_factors_data = model_output.get('charts_portfolio_factors', {})

        # Get the 'Benchmark Portfolio' data from both sections
        benchmark_overunder = charts_overunder_data.get("Benchmark Portfolio", {})
        benchmark_portfolio_factors = charts_portfolio_factors_data.get("Benchmark Portfolio", {})

        # Pass only the relevant data for Benchmark Portfolio
        context = {
            "benchmark_overunder": benchmark_overunder,
            "benchmark_portfolio_factors": benchmark_portfolio_factors,
        }

        return render(request, 'm5/summary_result.html', context)
    
