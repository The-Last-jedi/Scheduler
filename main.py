from Scheduler import create_app

app = create_app

#class Task:
 #   def __init__(self, no, priority, dead, diff):
  #      self.no = no
   #     self.p = priority
    #    self.dl = dead
     #   self.diff = diff


if __name__ == "__main__":
    app.run(debug=True)
    
