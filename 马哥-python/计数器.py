def counter(base):
    def inc(step=1):
        nonlocal base
        base = base + step
        return base
    return inc
foo = counter(10)
foo1 = counter(10)
if foo == foo1:
    print(True)
else:
    print(False)
foo()