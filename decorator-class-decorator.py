class DangerDecorClass:
  def __init__(self, func):
    self.func = func

  def __call__(self, *args):
    print('I am not in danger, I am the danger', args[0])
    self.func(*args)
    print('End of the story')

@DangerDecorClass
def sayMyName(name):
  print('I am the danger')

sayMyName('hygenberg')
