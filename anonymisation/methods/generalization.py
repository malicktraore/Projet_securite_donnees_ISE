def generalize_data(data, level):
    if isinstance(data, int):
        return (data // level) * level
    return data
