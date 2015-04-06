# Trivial Service Locator pattern in python

Full library source code:

**bind.py**

	def bind(env):
	    def bind2env(cls):
	        setattr(env, cls.__name__, cls)
	        return cls
	    return bind2env
	    
## Example usage

module **serviceA.py**

```
def defs(env_):

@bind(env_)
class ServiceA:
	
	...

```

module **serviceB.py**

```
def defs(env_):

@bind(env_)
class ServiceB:
	
	TheServiceA = env_.TheServiceA
	
	...

```

module **runtime.py**

```
import serviceA
import serviceB

class Env:

	TheServiceA = ServiceA()
	TheServiceB = ServiceB()

	def __init__(self): 
		serviceA.defs(self)
		serviceB.defs(self)

env = Env()

```
## Circular dependencies

When ServiceA and ServiceB both depend on each other the previous code fails. To fix it, it is enough to use properties:

module **serviceA.py**

```
def defs(env_):

@bind(env_)
class ServiceA:
	
	TheServiceB = property(lambda self: env_.TheServiceB)

```

module **serviceB.py**

```
def defs(env_):

@bind(env_)
class ServiceB:
	
	TheServiceA = property(lambda self: env_.TheServiceA)	
	...

```
