def bind(env):
    def bind2env(cls):
        setattr(env, cls.__name__, cls)
        return cls
    return bind2env
