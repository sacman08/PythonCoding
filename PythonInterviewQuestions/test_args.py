# what are *args and ** kwargs?
# * args are for receiving any number of arguments passed into the method/function (tuple)
# **kwargs are for taking keyword arguments passed into the method/function (dict)


def hello_args(*args):
    return f"Hello, {args}!"


def hello_kwargs(**kwargs):
    return f"Howdy, {kwargs}"


print(hello_args('a', 'Aaron', 'George'))
print(hello_kwargs(a='Aaron', b='George', c='Amanda'))
