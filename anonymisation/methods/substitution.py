def substitute_data(data, substitution_map):
    return ''.join(substitution_map.get(c, c) for c in data)
