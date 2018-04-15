from . import auth


# create by user

# example
@auth.route('/example', methods=['GET', 'POST'])
def example():
    pass
