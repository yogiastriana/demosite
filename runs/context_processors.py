# context_processors.py
def mvoh_runs_in_session(request):
    # Fetch 'runs' from the session if it exists
    mvoh_runs = request.session.get('mvoh_runs', [])
    
    return {
        'session_mvoh_runs': mvoh_runs
    }


def m2_runs_in_session(request):
    # Fetch 'runs' from the session if it exists
    m2_runs = request.session.get('m2_runs', [])
    
    return {
        'session_m2_runs': m2_runs
    }


def m3_runs_in_session(request):
    # Fetch 'runs' from the session if it exists
    m3_runs = request.session.get('m3_runs', [])
    
    return {
        'session_m3_runs': m3_runs
    }

def m4_runs_in_session(request):
    # Fetch 'runs' from the session if it exists
    m4_runs = request.session.get('m4_runs', [])
    
    return {
        'session_m4_runs': m4_runs
    }


def f1_runs_in_session(request):
    # Fetch 'runs' from the session if it exists
    f1_runs = request.session.get('f1_runs', [])
    
    return {
        'session_f1_runs': f1_runs
    }