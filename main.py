from tkinter import *
from tkinter import filedialog

canvasCollection = {}
entryCollection = {}
buttonCollection = {}
mainWindow = Tk()

currentFileParams = {
    "input1": "",
    "input2": ""
}

Label(mainWindow, text="A simple program to generate files based on user input dynamically.").grid(row=0)


def getAndProcessInput():
    input1 = entryCollection['entry1'].get()
    input2 = entryCollection['entry2'].get()
    input3 = entryCollection['entry3'].get()
    print([input1, input2, input3])
    currentFileParams["input1"] = input1
    currentFileParams["input2"] = input2

    folder_selected = filedialog.askdirectory()
    generateFiles(folder_selected, input1, input3, input2)


def createNewEntry(entryName, root, row, column):
    entryRef = Entry(root)
    entryRef.grid(row=row, column=column)
    entryCollection[entryName] = entryRef


def createNewCanvas(canvasName, root, width, height, row):
    canvasRef = Canvas(root, width=width, background='red', height=height)
    canvasCollection[canvasName] = canvasRef
    canvasRef.grid(row=row)


def createNewButton(buttonName,  text, row, column):
    buttonRef = Button(text=text, command=getAndProcessInput).grid(
        row=row, column=column)
    buttonCollection[buttonName] = buttonRef


# createNewCanvas("canvas1", mainWindow, 400, 100, 1)
# createNewCanvas("canvas2", mainWindow, 400, 100, 2)
# createNewCanvas("canvas3", mainWindow, 400, 100, 3)


Label(mainWindow,
      text="Enter file name with extension and iterables wrapped by '*' (mina*2**1*) :").grid(row=1, column=0)
createNewEntry(
    "entry1", mainWindow, 1, 1)
Label(mainWindow,
      text="Enter the iterables iteration differences seperated by ',' (3,5):").grid(row=2, column=0)
createNewEntry(
    "entry2", mainWindow, 2, 1)
Label(mainWindow,
      text="Enter number of files to generate :").grid(row=3, column=0)
createNewEntry(
    "entry3", mainWindow, 3, 1)

createNewButton(
    "button1", 'Generate', 4, 0)


def generateFiles(fileDir, fileNameFormat, numberOfFiles, iterationDiff):
    fileName = fileNameFormat.split('*')
    filenameIterableDiffs = iterationDiff.split(',')
    iterables = []
    iterableDiffs = []
    for it in filenameIterableDiffs:
        if (it.isdigit()):
            iterableDiffs.append(int(it))

    for it in fileName:
        if (it.isdigit()):
            iterables.append(int(it))

    for itFile in range(int(numberOfFiles)):
        reformedFileName = ''
        iterableIt = 0
        for it in fileName:
            if (it.isdigit()):
                iterables[iterableIt] += iterableDiffs[iterableIt]
                if (itFile < 1):
                    iterables[iterableIt] -= iterableDiffs[iterableIt]

                reformedFileName += str((iterables[iterableIt]))
                iterableIt += 1
            else:
                reformedFileName += str(it)

        new = open(fileDir+"/"+reformedFileName, 'w')


mainWindow.mainloop()
