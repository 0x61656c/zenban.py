from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    #kanbandata
    data.Kanban = {
        "Personal" : ["Test1", "Test1.5"],
        "Work" : ["Test2"],
        "School" : ["Test3"]
    }
        
    data.max_len = len(data.Kanban)

    #window data
    data.height = 768
    data.width = 1360
    data.displayMargin = 100

    #state data
    data.state = "display"

    #menu data
    data.menu_margin = (data.height / 3) - 50

    #display data

    #plus button data
    data.plus_button_margin = 10
    data.plus_button_size = 30

    #testblock
    data.xpos = 50
    data.ypos = 50
    data.xsize = 150
    data.ysize = 100
    data.blockmargin = data.ysize + 20
    

def newEvent(data, input):
    """
    Var input must be a tuple of category and event text
        Example: ("Personal", "Get a job")
    """
    data.Kanban[input[0]].append(input[1])
    
def newBlockCheck(event, data):
    return event.x in range(
        data.plus_button_margin,
        data.plus_button_margin + data.plus_button_size) and event.y in range(
        data.plus_button_margin,
        data.plus_button_margin + data.plus_button_size)

def mousePressed(event, data):
    #print(newBlockCheck(event, data))
    if data.state == "display":
        if newBlockCheck(event, data):
            data.state = "new"
            data.Kanban["Personal"].append("Hello")

    elif data.state == "new":
        if newBlockCheck(event,data):
            data.state = "display"

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def drawButton(canvas, data):
    if data.state == "display":
        new_button = canvas.create_rectangle(
            data.plus_button_margin,
            data.plus_button_margin,
            data.plus_button_margin + data.plus_button_size,
            data.plus_button_margin + data.plus_button_size)
        text = canvas.create_text(
            data.plus_button_margin + data.plus_button_size / 2,
            data.plus_button_margin + data.plus_button_size / 2,
            text = "+",
            )

    elif data.state == "new":
        new_button = canvas.create_rectangle(
            data.plus_button_margin,
            data.plus_button_margin,
            data.plus_button_margin + data.plus_button_size,
            data.plus_button_margin + data.plus_button_size)
        text = canvas.create_text(
            data.plus_button_margin + data.plus_button_size / 2,
            data.plus_button_margin + data.plus_button_size / 2,
            text = "x",
            )

def drawBlocks(canvas, data):
    xcurrent = 0
    for key in data.Kanban:
        xcurrent += 1
        ycurrent = 0
        for element in range(len(data.Kanban[key])):
            canvas.create_rectangle(
                xcurrent * data.width / (data.max_len + 1), 
                ycurrent * data.blockmargin + data.displayMargin,
                xcurrent * data.width/ (data.max_len +1) + data.xsize,
                ycurrent * data.blockmargin + data.ysize + data.displayMargin
                )

            ycurrent += 1


def drawMenu(canvas, data):
    drawButton(canvas, data)

def drawDisplay(canvas, data):
    drawButton(canvas, data)
    drawBlocks(canvas, data)

def redrawAll(canvas, data):
    if data.state == "display":
        drawDisplay(canvas, data)
    elif data.state == "new":
        drawMenu(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
run(1000, 1000)
