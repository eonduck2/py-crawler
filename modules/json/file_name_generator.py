from datetime import datetime

def generate_file_name(input_data):
    now = datetime.now()
    return input_data + now.strftime("%Y-%m-%d_%H-%M-%S") + '.json'
