
from feed.core.base import Stream
from feed.core.methods import Methods
from feed.core.mixins import DataTypeMixin


@Stream.register_accessor(name="bool")
class BooleanMethods(Methods):
    ...


@Stream.register_mixin(dtype="bool")
class BooleanMixin(DataTypeMixin):
    ...


class Boolean:

    @classmethod
    def register(cls, names):
        def wrapper(func):
            BooleanMethods.register_method(func, names)
            BooleanMixin.register_method(func, names)
            return func
        return wrapper
