def get_filter_params(request):
    temp = {p: v for p, v in request.GET.copy().items() if p != 'page'}
    if any([not not v for v in temp.values()]):
        return ''.join([f'&{p}={v}' for p, v in temp.items() if v])
    else:
        return None