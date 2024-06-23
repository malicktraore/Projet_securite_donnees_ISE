def mask_data(data, mask_char='*'):
    if isinstance(data, str):
        return mask_char * len(data)
    return data
