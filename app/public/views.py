from . import public


# create by user

# example
@public.route('/example', methods=['GET', 'POST'])
def example():
    pass
