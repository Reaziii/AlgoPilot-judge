import psutil
def is_processor_free(threshold_percentage=80):
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage < threshold_percentage

def check_processor_availability():
    if is_processor_free():
        print("Processor is available.")
    else:
        print("Processor is busy.")
