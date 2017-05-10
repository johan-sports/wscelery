import functools


def multi(dispatch_fn):
    @functools.wraps(dispatch_fn)
    def _inner(*args, **kwargs):
        return _inner.__multi__.get(
            dispatch_fn(*args, **kwargs),
            _inner.__multi_default__
        )(*args, **kwargs)

    _inner.__multi__ = {}
    _inner.__multi_default__ = lambda *args, **kwargs: None  # Default default
    return _inner


def method(dispatch_fn, dispatch_key=None):
    def apply_decorator(fn):
        if dispatch_key is None:
            # Default case
            dispatch_fn.__multi_default__ = fn
        else:
            dispatch_fn.__multi__[dispatch_key] = fn
        return dispatch_fn

    return apply_decorator


def select_keys(d, keys):
    """Return a new dictionary containing only the items that
    have a `key` in keys."""
    return {k: v for k, v in d.items() if k in keys}
