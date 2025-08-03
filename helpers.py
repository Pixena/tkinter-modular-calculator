
def safe_eval(expr):
    if '__' in expr:
        raise Exception('Недопустимо')
    allowed = set('0123456789+-*/().% ')
    for c in expr:
        if c not in allowed:
            raise Exception('Недопустимо')
    return eval(expr)