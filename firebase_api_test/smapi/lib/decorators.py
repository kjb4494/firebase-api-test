from functools import wraps
from rest_framework.exceptions import ParseError


def requires_params(params):
    def require_params(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            for param in params:
                if args[1].GET.get(param) is None:
                    raise ParseError(
                        'No value given for one or more required parameters error.(' + ', '.join(params) + ')'
                    )
            order = func(*args, **kwargs)
            return order
        return decorator
    return require_params
