import PySimpleGUI as sg
import os
import shutil

sg.theme('LightGreen3')

#build the graphic user interface
layout = [
    [sg.Text('File Extraction')],
    [sg.Text('Choice includes all sub directories')],
    [sg.Text('Source Directory'), sg.Input("", key="in"), sg.FolderBrowse()],
    [sg.Text('Type in new folder if it doesnt exist')],
    [sg.Text('Destination Directory'), sg.Input("", key="out"), sg.FolderBrowse()],
    [sg.Button(button_text="Submit", key="sub"), sg.Text('Complete file extraction')],
]

#display the GUI
window = sg.Window('File Extractor', layout)

while True:  # Event Loop to listen for submit click
    event, values = window.Read()

    #window close handler
    if event == sg.WIN_CLOSED:
        break

    if event =="sub":
        dirName = values['in']
        destName = values['out']

        #create destination if it doesnt exist already
        if not os.path.exists(destName):
            os.mkdir(destName)

        # Get the list of all files in directory tree at given path
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(dirName):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]

        # Store all directories in a single folder(destination)
        for elem in listOfFiles:
            origPath = elem
            fileName = os.path.basename(origPath)
            destPath = os.path.join(destName, fileName)
            shutil.copy(origPath, destPath)

        break

window.Close()