class User:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello " + self.name)

p1 = User("Username")
p1.greet()