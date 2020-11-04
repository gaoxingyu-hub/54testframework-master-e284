class FlagEntry(object):
    def __init__(self, enum_name, name, value):
        self.enum_name = enum_name
        self.name = name
        self.value = value

    def __str__(self):
        return '{}.{}'.format(self.enum_name, self.name)

    def __or__(self, other):
        if not isinstance(other, FlagEntry):
            raise TypeError('Expect type {}, but got {}'.format(FlagEntry, type(other)))

        if self.enum_name != other.enum_name:
            raise TypeError('Expect enum type {}, but got {}'.format(self.enum_name, other.enum_name))

        if self.name == other.name:
            return FlagEntry(self.enum_name, self.name, self.value)
        else:
            return FlagEntry(self.enum_name, '{}|{}'.format(other.name, self.name), other.value | self.value)

    def __and__(self, other):
        if not isinstance(other, FlagEntry):
            raise TypeError('Expect type {}, but got {}'.format(FlagEntry, type(other)))

        if self.enum_name != other.enum_name:
            raise TypeError('Expect enum type {}, but got {}'.format(self.enum_name, other.enum_name))

        return self.value & other.value

    def __ior__(self, other):
        if not isinstance(other, FlagEntry):
            raise TypeError('__ior__ expect type {}, but got {}'.format(FlagEntry, type(other)))

        if self.enum_name != other.enum_name:
            raise TypeError('__ior__ expect enum type {}, but got {}'.format(self.enum_name, other.enum_name))

        if self.name != other.name:
            self.name =  '{}|{}'.format(other.name, self.name)
            self.value |= other.value

        return self


class FlagMeta(type):
    def __new__(mcs, name, bases, members):
        if name == 'None':
            return None

        new_members = {}
        _name_to_members = {}
        _value_to_members = {}
        for n, v in members.items():
            if n.startswith('__'):
                continue

            if not isinstance(v, int):
                raise TypeError('Expect type {}, but got {}'.format(int, type(v)))

            if v in _value_to_members:
                raise KeyError('Value {} already exist'.format(v))

            flag_entry = FlagEntry(name, n, v)
            new_members[n] = flag_entry
            _name_to_members[n] = flag_entry
            _value_to_members[v] = flag_entry

        new_members['_name_to_members'] = _name_to_members
        new_members['_value_to_members'] = _value_to_members

        return type.__new__(mcs, name, bases, new_members)

    def __iter__(self):
        return self._name_to_members.values().__iter__()

    def __setattr__(self, key, value):
        """
        We don't allow change any attribute of a flag enum
        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError('FlagMeta does not support __setattr__')

    def __call__(cls, value):
        """
        This implementation is different from official version.
        In official version, if there is enum value 1 and 2, 3 is a valid value of this enum too;
        However, in Renix version, only 1 and 2 is treated as valid.
        :param value: value of the flag enum
        :return:
        """
        if value in cls._value_to_members:
            return cls._value_to_members[value]
        else:
            raise KeyError('Invalid enum value {}'.format(value))

    def __getitem__(self, item):
        if item in self._name_to_members:
            return self._name_to_members[item]
        else:
            raise KeyError('Invalid enum name {}'.format(item))

    def __setitem__(self, item, value):
        raise NotImplementedError('FlagMeta does not support __setitem__')


class Flag(object):
    __metaclass__ = FlagMeta

