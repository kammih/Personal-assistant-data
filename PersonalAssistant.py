class PersonalAssistant:
  def __init__(self, todos):

        self.todos = todos

  def get_contact(self, name):
    if name in self.contacts:
      return self.get_contacts[name]
    else:
      return "No contact with that name!"
    
    
 
  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
      return f'{todo_item} was removed'
    else:
      print("To-do is not in list!")

    
  def get_todos(self):
    return self.todos
  

  def get_birthday(self, name):
    if name == "Rubi":
      return "Birthday is 03/13/23!"
    elif name == "Tyler":
      return "Birthday is 01/03/95!"
    elif name == "Truitt":
      return "Birthday is 01/06/25!"
    else:
      return "Can't find birthday for this person..."
  
  



