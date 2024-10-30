class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MultitonByFirstArg(Singleton):

    def __call__(cls, *args, **kwargs):
        instance_name = cls.__name__ + (args[0] if len(args) else 'None')
        if instance_name not in cls._instances:
            cls._instances[instance_name] = super(MultitonByFirstArg, cls).__call__(*args, **kwargs)
        return cls._instances[instance_name]