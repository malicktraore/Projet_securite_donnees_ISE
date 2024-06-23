import random

def randomize_data(data):
    if isinstance(data, str):
        data = list(data)
        random.shuffle(data)
        return ''.join(data)
    return data
