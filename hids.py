import psutil

def run_hids():
    """
    Monitors the host system for suspicious activity (e.g., abnormal CPU or memory usage).
    This is a simplified version; real HIDS would look for more complex patterns.
    """
    # Example: Detect abnormal CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    flagged = False
    
    # If CPU or memory usage is abnormally high, flag it
    if cpu_usage > 90 or memory_usage > 90:
        flagged = True

    return {'cpu_usage': cpu_usage, 'memory_usage': memory_usage, 'flagged': flagged}
