from tkinter import *
root = Tk()
root.title('ООП Лабораторная работа №4')
root.resizable(False,False)

class Circle:
    def __init__(self,x,y,Bool = True):
        self.x = x
        self.y = y
        self.r = r
        self.chocen = Bool
        print('Круг создан')
        
    def YEPchoce(self):
        self.chocen = True
        
    def NOPEchoce(self):
        self.chocen = False
        
    def print_circle(self):
        if self.chocen:
            canv.create_oval(self.x-self.r/2,self.y-self.r/2,self.x+self.r/2,self.y+self.r/2,
                         fill='black', outline='black')
        else: canv.create_oval(self.x-self.r/2,self.y-self.r/2,self.x+self.r/2,self.y+self.r/2,
                         fill='white', outline='black')
    def delete_circle(self):pass
        
        
class Node:
    def __init__(self,obj=None, next = None):
        self.obj = obj
        self.next = next

class Storage:
    def __init__(self):
        self.first = None
    def add(self,shape):
        if self.first == None:
            self.first = Node(shape,None)
            return
        current = self.first
        while 1:
            if current.next == None:
                current.next = Node(shape,None)
                return
            current=current.next

    def length(self):
        length = 0
        if self.first == None:
            return 0
        current = self.first
        while current.next != None:
            current = current.next
            length += 1
        return length + 1
    
    def get_object(self,n):
        count = 0
        current = self.first
        while 1:
            if count == n:
                return current.obj
            current = current.next
            count+=1
        


width = 800
height = width/2
r = int(width/12)
print(r)
s = Storage()
def check(event):
    for i in range(s.length()):
        s.get_object(i).NOPEchoce()
    s.add(Circle(event.x,event.y))
    for i in range(s.length()):
        s.get_object(i).print_circle()
    
          
 



canv = Canvas(root,width=width,height=height,bg='white')


root.bind('<Button-1>', check)
canv.pack()
root.mainloop()

        
            
            
        
            
    
    

