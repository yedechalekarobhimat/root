import socket 
import tkinter as tk 
import time


def transmitFile(hostAddress, fileName):
    open(fileName, 'rb')
    fileToSend.seek(0, 2) 
    fileLength = fileToSend.tell() 
    numOfPackets = int(fileLength /1024) + 1 
    fileToSend.seek(0, 0) 
    print(fileLength) 
    print(fileName)
    print(numOfPackets)
 # encodes the fileName and numOfPackets and sends it to the server 
    encodedFileName =fileName.encode()
    socketVar.send(encodedFileName)
    time.sleep(1)  # delays by 1 second 
    stringNumOfPackets =str(numOfPackets) 
    encodedStringNumOfPackets =stringNumOfPackets.encode() 
    socketVar.send(encodedStringNumOfPackets)

    range(1, numOfPackets + 1)
    numOfPacketsSend_String = f"Sending packetserver..." 
    print(numOfPacketsSend_String) 
    data = fileToSend.read(1024)
    socketVar.send(data) 
    fileToSend.close()

    print("\nData has been sentsuccessfully!")
    return 

def closeProgram(event):  # closesthe program 
    window.quit()
    return 

def sendFile(event):
    ent_destination.get() 
    fileName=ent_fileName.get() 
    print(fileName)
 # close the window and send the file 
    window.destroy()
    transmitFile(hostAddress, fileName)
 # Display the confirmation the file sent
    lbl_FileSent=tk.Label(text = "The file has been sent.") 
    lbl_FileSent.pack()
    btn_confirmExit=tk.Button(text = "Click to exit.", width = 16, height = 2)
    btn_confirmExit.pack() 
    btn_confirmExit.bind('<Button-1>', closeProgram)
    return

defaultServerName=socket.gethostname()
window=tk.Tk()
# introductory message
lbl_introduction=tk.Label(text = "Computer Network") 
lbl_introduction.pack()
# get the destination name from the user, default to defaultServerName 
ent_destination =tk.Entry() 
ent_destination.pack() 
ent_destination.insert(0, defaultServerName)
# get the file name from the user. Default to adventuretime.jpg 
lbl_getFileName =tk.Label(text = "\n Enter the name the file should have at the destination") 
ent_fileName=tk.Entry() 
lbl_getFileName.pack() 
ent_fileName.pack() 
ent_fileName.insert(0, "cute.mp3")

btn_confirmEntry=tk.Button(text = "Transmit File", height = 2, width = 10)
btn_confirmEntry.pack() 
btn_confirmEntry.bind('<Button-1>', sendFile)
window.mainloop()
