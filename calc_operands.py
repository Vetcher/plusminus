import math


def add_(left, right):
    return left.calc() + right.calc()


def sub_(left, right):
    return left.calc() - right.calc()


def mul_(left, right):
    return left.calc() * right.calc()


def div_(left, right):
    try:
        return left.calc() / right.calc()
    except ZeroDivisionError:
        return float('Inf')


def pow_(left, right):
    try:
        return left.calc() ** right.calc()
    except OverflowError:
        return float('Inf')


def abs_(left, right=None):
    if right is not None: raise ValueError("Right in abs is not None")
    return abs(left.calc())


def ln_(left, right=None):
    if right is not None: raise ValueError("Right in ln is not None")
    return math.log(left.calc())


def log_(left, right):
    return math.log(right.calc(), left.calc())


def lg_(left, right=None):
    if right is not None: raise ValueError("Right in lg is not None")
    return math.log(left.calc(), 10)


def sin_(left, right=None):
    if right is not None: raise ValueError("Right in sin is not None")
    return math.sin(left.calc())


def cos_(left, right=None):
    if right is not None: raise ValueError("Right in sin is not None")
    return math.cos(left.calc())


def tan_(left, right=None):
    if right is not None: raise ValueError("Right in sin is not None")
    return math.tan(left.calc())


def ctan_(left, right=None):
    if right is not None: raise ValueError("Right in sin is not None")
    return 1.0 / math.tan(left.calc())


mapoffunc = {
    '+': add_,
    '-': sub_,
    '*': mul_,
    '\u00D7': mul_,
    '/': div_,
    '^': pow_,
    'abs': abs_,
    'ln': ln_,
    'log': log_,
    'e': math.e,
    'lg': lg_,
    'pi': math.pi,
    '\u03C0': math.pi,
    'sin': sin_,
    'cos': cos_,
    'tan': tan_,
    'tg': tan_,
    'ctg': ctan_,
    'ctan': ctan_,
    'cot': ctan_,
}

amount_of_args = {
    add_: 2,
    sub_: 2,
    mul_: 2,
    div_: 2,
    pow_: 2,
    abs_: 1,
    ln_: 1,
    log_: 2,
    lg_: 1,
    sin_: 1,
    cos_: 1,
    tan_: 1,
    ctan_: 1,
}

signarr = [add_, sub_, mul_, div_, pow_]
funcarr = [abs_, ln_, log_, lg_, sin_, cos_, tan_, ctan_]
