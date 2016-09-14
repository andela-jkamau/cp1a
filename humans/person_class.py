class Person(object):

    """
    This class accepts `name` as its argument.
    name=Person's name
    """

    def __init__(self, name, identifier=0, office_allocated=False):
        self.name = name
        self.identifier = identifier
        self.office_allocated = office_allocated
