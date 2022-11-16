import socket 
socketVar = socket.socket() 
hostName = socket.gethostname() 
port = 8090 
socketVar.bind((hostName, port))
socketVar.listen(1) 
print(hostName) 
print("Waiting for connection...") 
connection, address = socketVar.accept() 
print(address, "Has connected to the server") 
connection.recv(1024) 
fileName = fileName.decode() 
numOfPackets = connection.recv(1024) 
decodedNumOfPackets = numOfPackets.decode() 
numOfPackets = int(decodedNumOfPackets) 
file = open(fileName, 'wb') 
for x in range(1, numOfPackets + 1): 
    numOfPacketsRecv_String = f"Receiving packet #{x} from client..." 
print(numOfPacketsRecv_String) 
data = connection.recv(1024) 
file.write(data) 
connection.close() 
file.close() 
print("\nData has been transmitted successfully!\n") 
