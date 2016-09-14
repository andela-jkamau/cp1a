from .person_class import Person


class Fellow(Person):

    """
            This is a sub-class of the `Person` class.
                It holds information about a Fellow.
            The class extends the `Person` class by giving it
                a `livingspace_allocated` property.
                `livingspace_allocated`
                    defaults to False.
            livingspace_allocated = The ID of the living space
                the Fellow has been allocated to.
    """

    def __init__(
        self,
        livingspace_allocated=False,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.livingspace_allocated = livingspace_allocated
