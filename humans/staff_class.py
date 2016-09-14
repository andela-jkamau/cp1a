from .person_class import Person


class Staff(Person):

    """
            This is a sub-class of the `Person` class.
            It holds information about a Staff.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
