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
  print "type(function), %s" % (type(function))
  #print function.__name__
  print inspect.getargspec(function)
