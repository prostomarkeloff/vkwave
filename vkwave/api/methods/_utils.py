def get_params(func_locals: dict):
    params = {}
    for key, value_ in func_locals.items():
        if key not in ["self", "return_raw_response"] and value_ is not None:
            if isinstance(value_, list):
                value_ = ",".join(str(item) for item in value_)
            params[key] = value_
    return params
