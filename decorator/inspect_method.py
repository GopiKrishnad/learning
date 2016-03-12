"""
The inspect module provides several useful functions to help get information
about live objects such as modules, classes, methods, functions, tracebacks,
frame objects, and code objects. For example, it can help you examine the
contents of a class, retrieve the source code of a method, extract and format
the argument list for a function, or get all the information you need to
display a detailed traceback.

There are four main kinds of services provided by this module:
type checking, getting source code, inspecting classes and functions,
and examining the interpreter stack.
https://docs.python.org/2/library/inspect.html
"""
class function_wrapper(object):
  def __init__(self, wrapped):
    self.wrapped = wrapped
  def __call__(self, * args, **kwargs):
    return self.wrapped(*args, **kwargs)


@function_wrapper
def function():
  pass

if __name__ == "__main__":
  import inspect
  print """There are two types of decorators class decorators and function decorators."""
  print """Lets define a class decorator first"""
  #print "type(function), %s" % (type(function))
  print function.__name__
  print inspect.getargspec(function)
