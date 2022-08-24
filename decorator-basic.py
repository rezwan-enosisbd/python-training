
def mydecor(func):
  def insideFunc():
    print('First')
    func()
    print('Last')
  return insideFunc

@mydecor
def greetings():
  print('Hello What\'s up ? ')


greetings()

