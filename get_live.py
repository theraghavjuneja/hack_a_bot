from datetime import datetime
import json
from datetime import datetime
import json

def get_live_indices(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    date_time_list = data['starting_dates']
    current_date_time = datetime.now()

    converted_date_time_list = [
        [datetime.strptime(date_str.split(': ')[1], '%b %d, %Y, %I:%M %p') for date_str in sublist]
        for sublist in date_time_list
    ]

    indices_to_print = [index for index, sublist in enumerate(converted_date_time_list) if any(date_time > current_date_time for date_time in sublist)]

    return indices_to_print

