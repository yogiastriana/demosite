from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
from .models import Run
from demosite.views import process_form, process_stats_data, transform_metric, format_strategy_name, format_table_value, generate_optimization_summary_html_table
# from m4.views import process_form
from rebalancing.views import process_f1_input_form
from django.http import Http404
import json
import time

# Create your views here.
def runs_view(request):

    if request.user.userprofile.role == 'admin':
        runs = Run.objects.all()
    else:
        runs = Run.objects.filter(user=request.user.id)

    context = {
        "runs": runs
    }

    return render(request, 'runs_mvoh.html',  context)


def f1_runs_view(request):

    if request.user.userprofile.role == 'admin':
        runs = Run.objects.filter(model_name='f1')
    else:
        runs = Run.objects.filter(user=request.user.id, model_name='f1')

    context = {
        "runs": runs
    }

    return render(request, 'rebalancing/runs_f1.html',  context)


def     m2_runs_view(request):

    if request.user.userprofile.role == 'admin':
        runs = Run.objects.filter(model_name='m2')
    else:
        runs = Run.objects.filter(user=request.user.id, model_name='m2')

    context = {
        "runs": runs
    }

    return render(request, 'runs_m2.html',  context)


def get_single_saved_run(request):
    run_id = request.GET.get('run_id')  
    run_data = Run.objects.filter(id=run_id).first()  


    runs = Run.objects.filter(user_id=request.user.id)
    
    context = {
        'run_data': run_data,
        'runs': runs,
    }

    return render(request, 'mvoh/input_form.html',  context)


def get_single_saved_run_m2(request):
    run_id = request.GET.get('run_id')  
    run_data = Run.objects.filter(id=run_id).first()  


    runs = Run.objects.filter(user_id=request.user.id)
    
    context = {
        'run_data': run_data,
        'runs': runs,
    }

    return render(request, 'm2/input_form.html',  context)


def get_single_saved_run_m3(request):
    run_id = request.GET.get('run_id')  
    run_data = Run.objects.filter(id=run_id).first()  


    runs = Run.objects.filter(user_id=request.user.id)
    
    context = {
        'run_data': run_data,
        'runs': runs,
    }

    return render(request, 'm3/input_form.html',  context)


def get_single_saved_run_m4(request):
    run_id = request.GET.get('run_id')  
    run_data = Run.objects.filter(id=run_id).first()  


    runs = Run.objects.filter(user_id=request.user.id)
    
    context = {
        'run_data': run_data,
        'runs': runs,
    }

    return render(request, 'm4/input_form.html',  context)


def run_detail_view(request, run_id):
    run = get_object_or_404(Run, id=run_id)
    return render(request, 'run_detail.html', {'run': run})


def m4_run_detail_view(request, run_id):
    run = get_object_or_404(Run, id=run_id)
    return render(request, 'runs/m4_run_detail.html', {'run': run})


def f1_run_detail_view(request, run_id):
    run = get_object_or_404(Run, id=run_id)
    return render(request, 'runs/f1_run_detail.html', {'run': run})


def save_run_view(request):
    if request.method == 'POST':
        user_id = request.user.id 
        title = request.POST.get('title')
        description = request.POST.get('description')
        if request.POST.get('model_name') and request.POST.get('model_name') == 'f1':
            input_data = process_f1_input_form(request)
            model_name = 'f1'
        else:
            input_data = process_form(request)
            model_name = 'f1'

        new_run = Run(
            user_id=user_id,
            title=title,
            description=description,
            model_name=model_name,
            input_data=input_data
        )
        new_run.save()

        # Render the new row as HTML
        if request.user.userprofile.role == 'admin':
            runs = Run.objects.filter(model_name='f1')
        else:
            runs = Run.objects.filter(user=request.user.id, model_name='f1')
        
        return render(request, 'template-parts/run-list.html', {'runs': runs})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_run(request):
    run_id = request.POST.get('run_id')
    run = Run.objects.get(id=run_id)
    run.delete()
    
    runs = Run.objects.all()  # Fetch the remaining runs
    
    return render(request, 'template-parts/run-list.html', {'runs': runs})  


def delete_f1_run(request):
    run_id = request.POST.get('run_id')
    run = Run.objects.get(id=run_id)
    run.delete()
    
    if request.user.userprofile.role == 'admin':
        runs = Run.objects.filter(model_name='f1')
    else:
        runs = Run.objects.filter(user=request.user.id, model_name='f1')
    
    return render(request, 'template-parts/run-list.html', {'runs': runs})  
    

def session_mvoh_run(request, id):

    runs = request.session.get('mvoh_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == id), None)

    tciker_data = run.get('form_data').get('ticker_data')
    
    sector_data = {}
 
    for item in tciker_data:
        sector = item['sector']
        if sector in sector_data:
            sector_data[sector] += 1
        else:
            sector_data[sector] = 1

    # Convert the sector_data dictionary into the desired format (list of dictionaries)
    sector_data_list = [{'name': sector, 'value': count} for sector, count in sector_data.items()]

    if run is None:
        raise Http404("Run not found")
    
    saved_runs_with_output = Run.objects.filter(user_id=request.user.id).exclude(output_data__isnull=True).exclude(output_data__exact='').count()

    context = {
        'run': run,
        'sector_data': sector_data_list,
        'saved_runs_with_output': saved_runs_with_output
    }

    # Render the run data in a template, for example
    return render(request, 'mvoh_run_template.html', context)


def session_m2_run(request, id):

    runs = request.session.get('m2_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == id), None)

    tciker_data = run.get('form_data').get('ticker_data')
    
    sector_data = {}
 
    for item in tciker_data:
        sector = item['sector']
        if sector in sector_data:
            sector_data[sector] += 1
        else:
            sector_data[sector] = 1

    # Convert the sector_data dictionary into the desired format (list of dictionaries)
    sector_data_list = [{'name': sector, 'value': count} for sector, count in sector_data.items()]

    if run is None:
        raise Http404("Run not found")
    
    saved_runs_with_output = Run.objects.filter(user_id=request.user.id).exclude(output_data__isnull=True).exclude(output_data__exact='').count()

    context = {
        'run': run,
        'sector_data': sector_data_list,
        'saved_runs_with_output': saved_runs_with_output
    }

    # Render the run data in a template, for example
    return render(request, 'm2/m2_run_template.html', context)


def session_m3_run(request, id):

    runs = request.session.get('m3_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == id), None)

    tciker_data = run.get('form_data').get('ticker_data')
    
    sector_data = {}
 
    for item in tciker_data:
        sector = item['sector']
        if sector in sector_data:
            sector_data[sector] += 1
        else:
            sector_data[sector] = 1

    # Convert the sector_data dictionary into the desired format (list of dictionaries)
    sector_data_list = [{'name': sector, 'value': count} for sector, count in sector_data.items()]

    if run is None:
        raise Http404("Run not found")
    
    saved_runs_with_output = Run.objects.filter(user_id=request.user.id).exclude(output_data__isnull=True).exclude(output_data__exact='').count()

    context = {
        'run': run,
        'sector_data': sector_data_list,
        'saved_runs_with_output': saved_runs_with_output
    }

    # Render the run data in a template, for example
    return render(request, 'm3/m3_run_template.html', context)


def session_m4_run(request, id):

    runs = request.session.get('m4_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == id), None)


    ticker_data = run.get('form_data').get('ticker_data')
    
    sector_data = {}
 
    for item in ticker_data:
        sector = item['sector']
        if sector in sector_data:
            sector_data[sector] += 1
        else:
            sector_data[sector] = 1

    # Convert the sector_data dictionary into the desired format (list of dictionaries)
    sector_data_list = [{'name': sector, 'value': count} for sector, count in sector_data.items()]

    if run is None:
        raise Http404("Run not found")
    
    saved_runs_with_output = Run.objects.filter(user_id=request.user.id).exclude(output_data__isnull=True).exclude(output_data__exact='').count()

    context = {
        'run': run,
        'sector_data': sector_data_list,
        'saved_runs_with_output': saved_runs_with_output
    }

    # Render the run data in a template, for example
    return render(request, 'm4/m4_run_template.html', context)


def session_f1_run(request, id):

    runs = request.session.get('f1_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == id), None)
    # print("Run form data: ", run.get('form_data'))


    if run is None:
        raise Http404("Run not found")
    
    saved_runs_with_output = Run.objects.filter(user_id=request.user.id).exclude(output_data__isnull=True).exclude(output_data__exact='').count()

    context = {
        'run': run,
        'saved_runs_with_output': saved_runs_with_output
    }

    # Render the run data in a template, for example
    return render(request, 'f1/f1_session_run_template.html', context)


def save_session_run_view(request):
    user_id = request.user.id 
    title = request.POST.get('title')
    description = request.POST.get('description')
    input_data = process_form(request)
    session_run_id = request.POST.get('session_run_id')

    model_name = 'mvoh'

    runs = request.session.get('mvoh_runs', [])
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == int(session_run_id)), None)

    new_run = Run(
        user_id=user_id,
        title=title,
        description=description,
        model_name=model_name,
        input_data=input_data 
    )
    if(request.POST.get('save_output') != None and request.POST.get('save_output') == 'on' ):
        output_data=run.get('output')
        new_run.output_data=output_data
    new_run.save()

    new_runs = [r for r in runs if r['run_id'] != int(session_run_id)]
    request.session['mvoh_runs'] = new_runs

    saved_runs = Run.objects.filter(user_id=request.user.id)

    context = {
        "runs": saved_runs
    }
    return render(request, 'runs_mvoh.html', context)


def save_session_m2_run_view(request):
    user_id = request.user.id 
    title = request.POST.get('title')
    description = request.POST.get('description')
    input_data = process_form(request)
    session_run_id = request.POST.get('session_run_id')

    runs = request.session.get('m2_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == int(session_run_id)), None)


    new_run = Run(
        user_id=user_id,
        title=title,
        description=description,
        model_name='m2',
        input_data=input_data
    )
    if(request.POST.get('save_output') != None and request.POST.get('save_output') == 'on' ):
        output_data=run.get('output')
        new_run.output_data=output_data
    new_run.save()

    new_runs = [r for r in runs if r['run_id'] != int(session_run_id)]
    request.session['m2_runs'] = new_runs

    saved_runs = Run.objects.filter(user_id=request.user.id)

    context = {
        "runs": saved_runs
    }
    return render(request, 'runs_mvoh.html', context)


def save_session_m3_run_view(request):
    user_id = request.user.id 
    title = request.POST.get('title')
    description = request.POST.get('description')
    input_data = process_form(request)
    session_run_id = request.POST.get('session_run_id')

    runs = request.session.get('m3_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == int(session_run_id)), None)


    new_run = Run(
        user_id=user_id,
        title=title,
        description=description,
        model_name='m3',
        input_data=input_data
    )
    if(request.POST.get('save_output') != None and request.POST.get('save_output') == 'on' ):
        output_data=run.get('output')
        new_run.output_data=output_data
    new_run.save()

    new_runs = [r for r in runs if r['run_id'] != int(session_run_id)]
    request.session['m3_runs'] = new_runs

    saved_runs = Run.objects.filter(user_id=request.user.id)

    context = {
        "runs": saved_runs
    }
    return render(request, 'runs_mvoh.html', context)


def save_session_m4_run_view(request):
    user_id = request.user.id 
    title = request.POST.get('title')
    description = request.POST.get('description')
    input_data = process_m4_form(request)
    session_run_id = request.POST.get('session_run_id')

    runs = request.session.get('m4_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == int(session_run_id)), None)


    new_run = Run(
        user_id=user_id,
        title=title,
        description=description,
        model_name='m4',
        input_data=input_data
    )
    if(request.POST.get('save_output') != None and request.POST.get('save_output') == 'on' ):
        output_data=run.get('output')
        new_run.output_data=output_data
    new_run.save()

    new_runs = [r for r in runs if r['run_id'] != int(session_run_id)]
    request.session['m4_runs'] = new_runs

    saved_runs = Run.objects.filter(user_id=request.user.id)

    context = {
        "runs": saved_runs
    }
    return render(request, 'runs_mvoh.html', context)


def save_session_f1_run_view(request):
    user_id = request.user.id 
    title = request.POST.get('title')
    description = request.POST.get('description')
    input_data = process_f1_input_form(request)
    session_run_id = request.POST.get('session_run_id')

    runs = request.session.get('f1_runs', [])
    
    # Find the run with the specified ID
    run = next((run for run in runs if run['run_id'] == int(session_run_id)), None)


    new_run = Run(
        user_id=user_id,
        title=title,
        description=description,
        model_name='f1',
        input_data=input_data
    )
    if(request.POST.get('save_output') != None and request.POST.get('save_output') == 'on' ):
        output_data=run.get('output')
        new_run.output_data=output_data
    new_run.save()

    new_runs = [r for r in runs if r['run_id'] != int(session_run_id)]
    request.session['f1_runs'] = new_runs

    # saved_runs = Run.objects.filter(user_id=request.user.id)

    # if request.user.userprofile.role == 'admin':
    #     saved_runs = Run.objects.filter(model_name='f1')
    # else:
    #     saved_runs = Run.objects.filter(user=request.user.id, model_name='f1')

    # context = {
    #     "runs": saved_runs
    # }
    # return render(request, 'rebalancing/runs_f1.html',  context)
    return redirect('runs_f1')


def run_output_view(request, id):
    run = Run.objects.get(id=id)

    start_time = time.perf_counter()
    model_output = run.output_data

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


def calculate_ticker_correlation_view(request):
    if request.method == 'POST':
        try:
            # Attempt to parse the request body as JSON
            body = json.loads(request.body)
            list_tickers = body.get('data', [])

            # Initialize an empty list to hold the processed data
            list_data = []
            for ticker in list_tickers:
                dict_ticker_info = {
                    "ticker": ticker.get('Symbol', ''),
                    "company": ticker.get('Shortname', ''),
                    "sector": ticker.get('Sector', ''),
                    "industry": ticker.get('Industry', ''),
                    "market_cap": ticker.get('Marketcap', ''),
                    "previous_close": "12345678",
                    "beta": "Beta",
                    "benchmark": 0,
                    "amin": 0,
                    "amax": 1,
                    "correlation": "afddsaf"  # Placeholder
                }
                list_data.append(dict_ticker_info)
            print(list_data)
            return JsonResponse(list_data, safe=False)
        
        except json.JSONDecodeError:
            # Handle JSON decode error if the body is not a valid JSON
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def calculate_m4_ticker_correlation_view(request):
    if request.method == 'POST':
        try:
            # Attempt to parse the request body as JSON
            body = json.loads(request.body)
            list_tickers = body.get('data', [])

            # Initialize an empty list to hold the processed data
            list_data = []
            for ticker in list_tickers:
                dict_ticker_info = {
                    "ticker": ticker.get('Symbol', ''),
                    "company": ticker.get('Shortname', ''),
                    "pw": 'pw',
                    "pda": 'pda',
                    "sector": ticker.get('Sector', ''),
                    "market_cap": ticker.get('Marketcap', ''),
                }
                list_data.append(dict_ticker_info)
            print(list_data)
            return JsonResponse(list_data, safe=False)
        
        except json.JSONDecodeError:
            # Handle JSON decode error if the body is not a valid JSON
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
