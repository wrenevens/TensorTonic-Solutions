from datetime import datetime

def mdl_srt(d : dict):
    return -d['accuracy'], d['latency'], -datetime.strptime(d['timestamp'], '%Y-%m-%d').timestamp()

def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    
    return sorted(models, key=mdl_srt)[0]['name']
    