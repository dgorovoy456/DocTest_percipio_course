class MyOwnObject:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def create_new_MyOwnObject(name, number):
    """
    >>> create_new_MyOwnObject('F O', 1) #doctest: +ELLIPSIS
    <doctest_object.MyOwnObject object at 0x...>
    """
    return MyOwnObject(name, number)
