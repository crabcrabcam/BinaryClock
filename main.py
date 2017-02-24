#Gotta do those imports!
from datetime import datetime
import tkinter as tk
import converters



#Functions for creating circles
                #Takes x coord, y coord and radius
                #Also takes the fill colour, outline colour and width of outline
def create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)



def create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)

def setHour():
    time = list(converters.DecToBinStringHour(datetime.now().hour))
    for i in range(0,6):
        if list[i] == '0':
            hourArray[i] = canvas.create_circle(15 * i, 20, 10, fill="#000", outline="#FF11FF", width=4)
        else:
            hourArray[i] = canvas.create_circle(15 * i, 20, 10, fill="#FF11FF", outline="#FF11FF", width=4)

def updateScreen():
    setHour()

#Makes the window
root = tk.Tk()
#Sets the size of the window
canvas = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
#Sets up a grid for the canvas
canvas.grid()

#Adds the functions to the canvas so we can use them
tk.Canvas.create_circle_arc = create_circle_arc
tk.Canvas.create_circle = create_circle

#Hour, minute and second arrays
#Circle base is an array for the details in cirlces
circleBase = [15, 20, 10, fill="#000", outline="#FF11FF", width=4]
hourArray = [circleBase, circleBase, circleBase, circleBase, circleBase]
minuteArray = [circleBase, circleBase, circleBase, circleBase, circleBase, circleBase]
secondArray = [circleBase, circleBase, circleBase, circleBase, circleBase, circleBase]

#Creates some circles
#canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
#canvas.create_circle_arc(100, 120, 48, fill="green", outline="", start=45, end=140)
#canvas.create_circle_arc(100, 120, 48, fill="green", outline="", start=275, end=305)
#canvas.create_circle_arc(100, 120, 45, style="arc", outline="white", width=6, start=270-25, end=270+25)
#canvas.create_circle(150, 40, 20, fill="#BBB", outline="")

#Sets the title of the window
root.wm_title("Binary Clock")

updateScreen()

print(datetime.now().hour)
print(converters.DecToBinStringHour(datetime.now().hour))
print(datetime.now().minute)
print(converters.DecToBinStringMinuteSecond(datetime.now().minute))
print(datetime.now().second)
print(converters.DecToBinStringMinuteSecond(datetime.now().second))

