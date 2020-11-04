from .renix_common_api import *


def rom(cls):
    from .core import Core
    if not issubclass(cls, Core):
        raise Exception('meta.rom.on_decorator', str(cls), 'subclass of core.Core')

    ROMManager.register_cls(cls)

    return cls


class ROMManager:
    # All registered ROM class. The key is the name of the ROM class before decorated by meta.rom
    _class_depot = {}

    # All ROM class instances. The key is the handle of the object
    _object_depot = {}

    @classmethod
    def register_cls(cls, rom_cls):
        if rom_cls.cls_name() in cls._class_depot:
            renix_debug('{} has already been register.'.format(rom_cls.cls_name()))
            return

        cls._class_depot[rom_cls.cls_name()] = rom_cls

    @classmethod
    def get_cls(cls, name):
        return cls._class_depot[name] if name in cls._class_depot else None

    @classmethod
    def get_all_objects(cls):
        return ROMManager._object_depot

    @classmethod
    def get_object(cls, handle, update_child=True):
        if handle in ROMManager._object_depot:
            obj = ROMManager._object_depot[handle]
            obj.get(update_child=update_child)
            return obj
        else:
            separate = handle.rfind('_')
            if separate > 0:
                relative_class_name = handle[:separate]
                cls_obj = ROMManager.get_cls(relative_class_name)
                if cls_obj:
                    try:
                        relative = cls_obj(handle=handle)
                        return relative
                    except:
                        return None
                else:
                    raise NotImplementedError('Cannot find an ROM class with name: {}'.format(relative_class_name))
            else:
                renix_error('This is not a valid handle: {}'.format(handle))
            return None

    @classmethod
    def add_object(cls, handle, obj):
        ROMManager._object_depot[handle] = obj

    @classmethod
    def remove_object(cls, handle):
        if handle in ROMManager._object_depot:
            ROMManager._object_depot.pop(handle)
