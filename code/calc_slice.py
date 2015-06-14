import ptb; ptb.enable(context=5)


def validate_step(step):

    reverse = False

    if step == 0:
        raise Exception("Step cannot be zero.")
    if step < 0:
        reverse = True
    if step is None:
        step = 1

    return (step, reverse)


def slice_object(obj, start=None, stop=None, step=None):

    length = len(obj)
    step, reverse = validate_step(step)
    if s and not e:
        sliced = []
        _len = n - s  # [3:]
        if s < 0:
            _len = abs(s)
        elif s >= n:
            _len = n - s % n
        for i in range(0, _len, stp):
            index = (i + s) % n
            sliced.append(_self[index])
            print(ss)


slice_object('a')
