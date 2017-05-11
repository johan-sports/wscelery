def exclude_keys(d, keys):
    """Return a new dictionary excluding all `keys`."""
    return {k: v for k, v in d.items() if k not in keys}
