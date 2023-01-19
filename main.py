import os,time,sys
list=[]  

 
def add():
  time.sleep(2)
  os.system("clear")
  task=input("What is the task?> ")
  due=input("When is the task due?> ")
  priority=input("High, medium or low priority task?> ").lower()
  row=[task,due,priority]
  list.append(row)
  print()
  print(f"{space:^18}Task added to list")

  
def view():
  time.sleep(2)
  os.system("clear")
  viewList=input("1. View all\n2. View by priority\n>> ").lower()
  if viewList=="1" or viewList=="view all":
    for row in list:
      for item in row:
        print(item, end=" | ")
      print()  
    print()
      
  elif viewList=="2" or viewList=="view by priority":
    priority=input("High, medium or low priority task>>").lower()
    for row in list:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
      
def edit():
  time.sleep(2)
  os.system("clear")
  change=input("Which task do you want to edit? \n>>\n ")
  for row in list:
    if change in row:
      list.remove(row)
  task=input("What is the task?> ")
  due=input("When is the task due?> ")
  priority=input("High, medium or low priority task?> ").lower()
  row=[task,due,priority]
  list.append(row)
  print()
  print("\033[32mUpdate complete! ")

def remove():
  time.sleep(2)
  os.system("clear")
  remTask=input("Which task is done? ")
  for row in list:
    if remTask in row:
      list.remove(row)
      print()
      print("\033[32mWohooo! Task completed! ")
    elif remTask not in row:
      print("\033[31mTask not in list")

while True:      
  space=""
  print(f"{space:^18}\033[1;33mMy To Do List")
  
  print("Select an option: ")
  
  options=input("1. Add to do list\n2. View my list\n3. Edit to do list\n4. Remove my list\n>> ").lower()
  
 
  if options=="1" or options=="add":
    add()
    
  elif options=="2" or options=="view":
    view()
   
  elif options=="3" or options=="edit":
    edit()
    
  elif options=="4" or options=="remove":
    remove()
    
    time.sleep(2)
    os.system("clear")