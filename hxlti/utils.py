import logging

def unpack_paramaters(params, params_map):
    request_params = {}

    for key in params_map:
        pvalue = params(key, '')

        if pvalue:
            if params_map[key]['ptype'] == "list":
                if pvalue:
                    value = [x.strip() for x in pvalue.split(';')]
                else:
                    value = []
            else:
                value = pvalue
            request_params[params-map[key]['mapto']] = value

    retur
