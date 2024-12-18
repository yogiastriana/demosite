from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from demosite.views import process_form, process_stats_data, transform_metric, format_strategy_name, format_table_value, generate_optimization_summary_html_table
import time 
import json
from .mode_result import model_output_data

from runs.models import Run

# Create your views here.
@login_required(login_url='/login/')
def input_form_view(request):

    if request.user.userprofile.role == 'admin':
        runs = Run.objects.all()
    else:
        runs = Run.objects.filter(user=request.user.id)

    context = {
        "runs": runs
    }

    return render(request, 'mvoh/index.html', context)


@login_required(login_url='/login/')
def output_view(request):

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

        print("Top level line data: ", formatted_top_level_lines_data)
    
    
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

        return render(request, 'mvoh/run_output.html', context)


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


@login_required(login_url='/login/')
def run_mvoh_model_view(request):
    if request.method == 'POST':
        form_data = process_form(request)
   

        model_output = model_output_data

        error = model_output.get('error', None)

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

        strategy_purchase_allocations = model_output.get('strategy_results', {}).get('strategy_purchase_allocation', {})

        symbol_hex_colors = model_output.get('hex_colors', {}).get('symbol_hex_colors', {})
        sector_hex_colors = model_output.get('hex_colors', {}).get('sector_hex_colors', {})

        strategy_min_variance = strategy_purchase_allocations.get('min_variance', {})
        strategy_max_sharpe = strategy_purchase_allocations.get('max_sharpe', {})

        

        context = {
            'frontier_runs_x': frontier_runs_x,
            'frontier_runs_y': frontier_runs_y,
            'frontier_positions_random_x': frontier_positions_random_x,
            'frontier_positions_random_y': frontier_positions_random_y,
            'frontier_runs': frontier_runs,
            'frontier_positions': frontier_positions,
            'symbol_hex_colors': symbol_hex_colors,
            'sector_hex_colors': sector_hex_colors,
            'strategy_min_variance': strategy_min_variance,
            'strategy_max_sharpe': strategy_max_sharpe,
        }

        error_context = {
            'error': error
        }

        # summary_html = render_to_string('mvoh/summary_result.html', context, request=request)
        # error_html = render_to_string('mvoh/error.html', error_context, request=request)

        # # Combine the fragments in a single HttpResponse with OOB swaps
        # response_content = summary_html + error_html
        # return HttpResponse(response_content)

        return render(request, 'mvoh/summary_result.html', context)


@login_required(login_url='/login/')
def current_mvoh_result_view(request):
    mvoh_runs = request.session.get('mvoh_runs', [])

    # Get the last run if available, or None if mvoh_runs is empty
    last_run = mvoh_runs[-1] if mvoh_runs else None

    start_time = time.perf_counter()
    model_output = last_run.get('output')

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

    return render(request, 'mvoh/run_output.html', context)


@login_required(login_url='/login/')
def fetch_mvoh_error_view(request):

    mvoh_runs = request.session.get('mvoh_runs', [])
    # Get the last run if available, or None if mvoh_runs is empty
    last_run = mvoh_runs[-1] if mvoh_runs else None

    
    if last_run:
        output = last_run.get('output')
        error = output.get('stacktraces')
    else:
        error = 'There is no error'
 
    error_context = {
        'error': error
    }
    error_html = render_to_string('mvoh/error.html', error_context, request=request)
    return HttpResponse(error_html)


@login_required(login_url='/login/')
def fetch_mvoh_ticker_view(request):

    ticker_data = [
        {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Technology",
            "beta": "1.25",
            "current_price": "$226.05",
            "pe_ratio": "34.46",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.03"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.05"},
                {"quarter": "Q3 24", "status": "Beat", "eps_change": "+0.04"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.03"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 42, "strong_buy": 10, "buy": 24, "hold": 7, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 50, "strong_buy": 12, "buy": 28, "hold": 8, "underperform": 1, "sell": 1},
                {"month": "Oct", "analyst_num": 38, "strong_buy": 8, "buy": 20, "hold": 7, "underperform": 2, "sell": 1},
                {"month": "Nov", "analyst_num": 45, "strong_buy": 15, "buy": 20, "hold": 5, "underperform": 3, "sell": 2},
            ],
            "price_targets":{
                "low": "183.86",
                "current": "183.86",
                "average": "183.86",
                "high": "300.00"
            },
        },
        {
            "ticker": "GOOGL",
            "name": "Alphabet Inc.",
            "sector": "Technology",
            "beta": "1.10",
            "current_price": "$2,745.00",
            "pe_ratio": "28.50",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.10"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.12"},
                {"quarter": "Q3 24", "status": "Miss", "eps_change": "-0.02"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.08"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 40, "strong_buy": 15, "buy": 20, "hold": 4, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 48, "strong_buy": 18, "buy": 22, "hold": 5, "underperform": 2, "sell": 1},
                {"month": "Oct", "analyst_num": 35, "strong_buy": 10, "buy": 18, "hold": 6, "underperform": 0, "sell": 1},
                {"month": "Nov", "analyst_num": 50, "strong_buy": 20, "buy": 25, "hold": 4, "underperform": 1, "sell": 0},
            ],
            "price_targets": [
                {"low": "183.86"},
                {"current": "183.86"},
                {"average": "183.86"},
                {"high": "300.00"}
            ],
        },
        {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Technology",
            "beta": "1.25",
            "current_price": "$226.05",
            "pe_ratio": "34.46",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.03"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.05"},
                {"quarter": "Q3 24", "status": "Beat", "eps_change": "+0.04"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.03"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 42, "strong_buy": 10, "buy": 24, "hold": 7, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 50, "strong_buy": 12, "buy": 28, "hold": 8, "underperform": 1, "sell": 1},
                {"month": "Oct", "analyst_num": 38, "strong_buy": 8, "buy": 20, "hold": 7, "underperform": 2, "sell": 1},
                {"month": "Nov", "analyst_num": 45, "strong_buy": 15, "buy": 20, "hold": 5, "underperform": 3, "sell": 2},
            ],
            "price_targets":{
                "low": "183.86",
                "current": "183.86",
                "average": "183.86",
                "high": "300.00"
            },
        },
        {
            "ticker": "GOOGL",
            "name": "Alphabet Inc.",
            "sector": "Technology",
            "beta": "1.10",
            "current_price": "$2,745.00",
            "pe_ratio": "28.50",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.10"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.12"},
                {"quarter": "Q3 24", "status": "Miss", "eps_change": "-0.02"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.08"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 40, "strong_buy": 15, "buy": 20, "hold": 4, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 48, "strong_buy": 18, "buy": 22, "hold": 5, "underperform": 2, "sell": 1},
                {"month": "Oct", "analyst_num": 35, "strong_buy": 10, "buy": 18, "hold": 6, "underperform": 0, "sell": 1},
                {"month": "Nov", "analyst_num": 50, "strong_buy": 20, "buy": 25, "hold": 4, "underperform": 1, "sell": 0},
            ],
            "price_targets": [
                {"low": "183.86"},
                {"current": "183.86"},
                {"average": "183.86"},
                {"high": "300.00"}
            ],
        },
        {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Technology",
            "beta": "1.25",
            "current_price": "$226.05",
            "pe_ratio": "34.46",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.03"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.05"},
                {"quarter": "Q3 24", "status": "Beat", "eps_change": "+0.04"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.03"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 42, "strong_buy": 10, "buy": 24, "hold": 7, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 50, "strong_buy": 12, "buy": 28, "hold": 8, "underperform": 1, "sell": 1},
                {"month": "Oct", "analyst_num": 38, "strong_buy": 8, "buy": 20, "hold": 7, "underperform": 2, "sell": 1},
                {"month": "Nov", "analyst_num": 45, "strong_buy": 15, "buy": 20, "hold": 5, "underperform": 3, "sell": 2},
            ],
            "price_targets":{
                "low": "183.86",
                "current": "183.86",
                "average": "183.86",
                "high": "300.00"
            },
        },
        {
            "ticker": "GOOGL",
            "name": "Alphabet Inc.",
            "sector": "Technology",
            "beta": "1.10",
            "current_price": "$2,745.00",
            "pe_ratio": "28.50",
            "eps_data": [
                {"quarter": "Q1 24", "status": "Beat", "eps_change": "+0.10"},
                {"quarter": "Q2 24", "status": "Beat", "eps_change": "+0.12"},
                {"quarter": "Q3 24", "status": "Miss", "eps_change": "-0.02"},
                {"quarter": "Q4 24", "status": "-", "eps_change": "+0.08"},
            ],
            "analyst_data": [
                {"month": "Aug", "analyst_num": 40, "strong_buy": 15, "buy": 20, "hold": 4, "underperform": 1, "sell": 0},
                {"month": "Sep", "analyst_num": 48, "strong_buy": 18, "buy": 22, "hold": 5, "underperform": 2, "sell": 1},
                {"month": "Oct", "analyst_num": 35, "strong_buy": 10, "buy": 18, "hold": 6, "underperform": 0, "sell": 1},
                {"month": "Nov", "analyst_num": 50, "strong_buy": 20, "buy": 25, "hold": 4, "underperform": 1, "sell": 0},
            ],
            "price_targets": [
                {"low": "183.86"},
                {"current": "183.86"},
                {"average": "183.86"},
                {"high": "300.00"}
            ],
        },
        
        
    ]
    error_context = {
        'ticker_data': ticker_data
    }
    
    error_html = render_to_string('template-parts/yfinance-ticker-data.html', error_context, request=request)
    return HttpResponse(error_html)