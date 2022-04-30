#!/usr/bin/env python

# coding=UTF-8
from email import message
import os
import sys
import traceback
from operators.op import op
from globalConfig import globalConfig
from db.controllers.ServidorController import ServidorController
serverManager = None


class ServerManager():
    '''

    # Base Server Manager

    Description ::
    ---------- 

    Allows to manage all servers with one class.

    Input ::
    -----

    :attr str serversprotocolClass: Servers default class

    :attr list Servers: List of servers 

    '''

    def __init__(self, serversprotocolClass="server.Server"):
        self.serversprotocolClass = serversprotocolClass
        self.Servers = {}
        self.serverController = ServidorController()
    # ================================================================
    # GET METHODS

    # Method responsible to get Camera by session id
    # (Returns Camera and None if does not exists)
    def getBySocketKey(self, socketkey):
        # If no serverid is passed
        if socketkey == None:
            return None

        for serverid in self.Servers:
            try:
                # Get Camera
                server = self.Servers[serverid]
                # Check if cameraid is the same
                if server.socketkey == socketkey:
                    return server  # Return Camera if not
            except Exception:
                continue  # If the object has no session id

        return None
    
    def db_getBySocketKey(self, socketKey):
        self.serverController.refresh()
        servidor = self.serverController.getBySocketKey(socketKey=socketKey)
        if(servidor == [] or servidor == None):
            return None
        
        return servidor[0]
    
    def db_getByServerId(self, serverid):
        self.serverController.refresh()
        servidor = self.serverController.getByServerId(serverid=serverid)
        if(servidor == [] or servidor == None):
            return None
        
        return servidor[0]  
      
    ### Save in Database Methods
    def saveOrUpdateServer(self,server):
        dbserver = self.db_getByServerId(serverid=server.serverid)
        serverid = server.serverid
        socketKey = server.socketkey
        siglaUni = globalConfig.defaultuniversidad
        
        socketKeyServer = self.db_getBySocketKey(socketKey)
        
        if(dbserver != None and socketKeyServer == None):
            if(self.serverController.update(where="id="+str(dbserver["id"]),serverid=serverid, socketKey=socketKey,siglaUni=siglaUni)):
                op.printLog(logType="INFO", messageStr=f"Server [{serverid}] updated in id [{dbserver['id']}]") 
                return True
            else:
                op.printLog(logType="ERROR", messageStr=f"Was not posible to update Server [{serverid}] in id [{dbserver['id']}]") 
                return False
            
        elif(dbserver != None and socketKeyServer != None):
            if (dbserver["id"] != socketKeyServer["id"]):
                self.serverController.deleteByServerId(serverid = socketKeyServer["serverid"])
            if(self.serverController.update(where="id="+str(dbserver["id"]),serverid=serverid, socketKey=socketKey,siglaUni=siglaUni)):
                op.printLog(logType="INFO", messageStr=f"Server [{serverid}] updated in id [{dbserver['id']}]") 
                return True
            else:
                op.printLog(logType="ERROR", messageStr=f"Was not posible to update Server [{serverid}] in id [{dbserver['id']}]") 
                return False
            
        elif(socketKeyServer != None):
            self.serverController.deleteByServerId(serverid = socketKeyServer["serverid"])
        
        if(self.serverController.add(serverid=serverid, socketKey=socketKey, siglaUni=siglaUni)):
            op.printLog(logType="INFO", messageStr=f"Server [{serverid}] added into DB!") 
            return True
        else:
            op.printLog(logType="ERROR", messageStr=f"Was not posible add Server [{serverid}] in DB!") 
            return False
        
    # Method responsible to get server by server id
    # (Returns Server and None if does not exists)
    def getByServerId(self, serverid):
        # If no serverid is passed
        if serverid == None:
            return None

        # If the server is in servers
        if serverid in self.Servers:
            return self.Servers[serverid]

        return None

    # ================================================================
    # CREATE AND ADD METHODS

    # Adds a new server to the list of servers
    def addServer(self, server):
        self.saveOrUpdateServer(server)
        self.Servers[server.serverid] = server

    # Creates a new server if posible
    # (Returns: None if was not posible to create, Server if yes)
    def new(self, serverid, ip='localhost', port=0, poll_interval=0.5):
        # Create server object dinamically
        tmpServer = op.createClass(
            newClass=self.serversprotocolClass, ip=ip, port=port, poll_interval=poll_interval, serverid=serverid)
        self.addServer(tmpServer)

        return tmpServer

    # Creates and Starts the server
    # (Returns: None if was not posible to create, Server if yes)
    def newAndStart(self, serverid, ip='localhost', port=0, poll_interval=0.5):
        # Create server
        tmpServer = self.new(serverid=serverid, ip=ip,
                             port=port, poll_interval=poll_interval)
        # Start server
        res = tmpServer.start()
        if(res == None):
            op.printLog(
                logType="ERROR", messageStr="Was not posible to create the server in  ip=[" + ip + "], port=[" + str(port) + "]")
            return res

        op.printLog(logType="INFO", messageStr="NEW SERVER CREATED!: serverid=["+tmpServer.serverid+"], ip=[" + ip + "], port=[" + str(
            port) + "], poll_interval=[" + str(poll_interval) + "]. [" + tmpServer.toString() + "].")

        return tmpServer

    # ================================================================
    # PRINT METHODS

    # List all servers added in manager server list
    # (Returns: Number of servers in list)
    def listServers(self):
        num = len(self.Servers)
        if num < 1:
            op.printLog(
                logType="WARNING", messageStr="BaseServersManager.listServers(). None server was found!")
            return 0

        op.printLog(logType="INFO",
                    messageStr="BaseServersManager.listServers():")
        for key in self.Servers:
            tmpServer = self.Servers[key]
            op.printLog(logType="INFO", messageStr="\n-> " +
                        tmpServer.toString()+"\n")
            tmpServer.camerasManager.listCameras()

        return num

    # Prints a menu for cmd server
    def printMenu(self):
        print("\n-------------------------------------")
        print(" 1 -> Start new server")
        print(" 2 -> Start Default Server")
        print(" 3 -> List all servers")
        print(" 4 -> Exit")
        print("-------------------------------------\n")
        print("Choose option:\n")
        return input("[Admin\servers] > ")

    # ================================================================
    # SERVER MANAGER CONNECTION HANDLERS METHODS
    # START AND STOP METHODS

    # Start regular server without CMD
    def startServer(self, serverid, serverip, serverport, serverpollinterval):
        # Set Camera id from arguments
        serverid = str(serverid)
        op.startLog(logFile=f"log/{serverid}/serverStatus.log")
        op.printLog(logType="INFO", messageStr="Trying to start server...")
        # Create and start the server
        server = self.newAndStart(
            serverid=serverid, ip=serverip, port=serverport, poll_interval=serverpollinterval)
        # If was not posible to start
        if(server == None):
            op.printLog(logType="ERROR", messageStr="Was not posible to create server [ip=("+serverip+"), port=("+str(
                serverport)+"), poll_interval=("+str(serverpollinterval)+")]")
            op.printLog(logType="INFO", messageStr="Closing Server...")
            return None

        op.printLog(logType="INFO",
                    messageStr="Server is Opened in Background")
        return server

    # Stop all servers in manager server list
    def stopServers(self):
        for serverid in self.Servers:
            # Get server
            tmpServer = self.Servers[serverid]
            # Stop server
            tmpServer.stop()

    # ================================================================
    # COMMAND LINE METHODS

    # Opens the command line to create the servers
    def commandLine(self, defaultip, defaultport, defaultpollinterval):
        while True:

            # Get menu option
            opt = self.printMenu()

            try:
                numopt = int(opt)

                if (numopt == 1):

                    # Get server id
                    serverid = input("Please insert server id: ")
                    if(serverid == ""):
                        print("\n[ERROR] A Server id needs to be specified!\n")
                        continue

                    # Server Socket Values

                    # Get server ip
                    ip = input("Please insert the IP [Default localhost]: ")
                    ip = ip if not ip == "" else "localhost"

                    # Get server port
                    port = input(
                        "Please insert the PORT [Default ("+str(defaultport)+") auto]: ")
                    try:
                        port = int(port) if not port == "" else defaultport
                        # Get port or set default if empty or invalid
                    except:
                        print("\n[ERROR] The port needs to be a int\n")
                        continue

                    # If invalid
                    if(port < 0 or port > 65535):
                        print(
                            "\n[ERROR] The port needs to be between 1 and 65534\n")
                        continue

                    # Get server poll inverval
                    # Get server port
                    poll_interval = input(
                        "Please insert the POLL INTERVAL [Default "+str(defaultpollinterval)+"]: ")
                    try:
                        poll_interval = int(
                            poll_interval) if not poll_interval == "" else defaultpollinterval
                        # Get port or set default if empty or invalid
                    except:
                        print("\n[ERROR] The pool interval needs to be an int\n")
                        continue

                    # If invalid
                    if(poll_interval < 0):
                        print(
                            "\n[ERROR] The poll interval needs to be a positive int\n")
                        continue

                    try:
                        # Create and Start Server
                        res = self.newAndStart(
                            serverid=serverid, ip=defaultip, port=defaultport, poll_interval=defaultpollinterval)
                        if not res:
                            op.printLog(
                                logType="ERROR", messageStr="Was not possible to add a new server, invalid configuration!\n")
                    except Exception as e:
                        op.printLog(
                            logType="EXCEPTION", e=e, messageStr="in BaseServersManager(). On newAndStart()")
                        traceback.print_exc()

                    continue

                # Default server
                elif (numopt == 2):
                    # SET DEFAULT SERVER CONFIGURATIONS:

                    serverid = "DEFAULT"

                    # ------
                    # Start Server
                    try:
                        # Create and Start Server
                        res = self.newAndStart(
                            serverid=serverid, ip=defaultip, port=defaultport, poll_interval=defaultpollinterval)
                        if not res:
                            op.printLog(
                                logType="ERROR", messageStr="Was not possible to add a new server, invalid configuration!\n")
                            continue
                    except Exception as e:
                        op.printLog(
                            logType="EXCEPTION", e=e, messageStr="in BaseServersManager(). On newAndStart()")
                        traceback.print_exc()
                        op.printLog(
                            logType="ERROR", messageStr="Was not possible to start DEFAULT server, this server already exists!\n")
                    continue

                # List servers
                elif (numopt == 3):
                    self.listServers()

                # Close cmd and close all servers
                elif (numopt == 4):
                    self.stopServers()
                    break

                # If option is no valid
                else:
                    op.printLog(logType="ERROR",
                                messageStr="[ERROR] Option not found!\n")

            except Exception as e:
                op.printLog(logType="EXCEPTION", e=e,
                            messageStr="[ERROR] Option not found!\n")
                traceback.print_exc()
        return 0

###### MAIN PROGRAM ######################################################################################################################################################
# Main program help


def showHelp():
    print(
        "\n\n***************************************"
        + "\n\nDEFAULT PROTOCOL = ["+defaultprotocol+"]"
        + '\n\n-> IF YOU NEED HELP: '
        + '\n\n\tpy BaseServersManager.py -h'
        + '\n\n-> IF YOU WANT TO USE CMD: '
        + '\n\n\tpy BaseServersManager.py -cmd\n'
        + '\n\n-> IF YOU WANT TO OPEN DEFAULT SERVER: '
        + '\n\n\tpy BaseServersManager.py --default\n'
        + '\n\n-> ARGUMENTS DESCRIPTION: '
        + '\n\n\t-n [serverid] [MANDATORY]: Server unique identificator, can be alfanumeric.'
        + '\n\n\t-ip [ip]: IP from server to connect to.'
        + '\n\n\t-port [port]: PORT from server to connect to.'
        + '\n\n\t-poll [poll interval]: Server poll interval, time in seconds to check if server needs to shutdown.'
        + '\n\n-> REQUIREMENTS: '
        + '\n\n\t[serverid] Must be filled to open server.'
        + '\n\n\tDefault Values if empty:'
        + '\n\n\t-----------------------------------------'
        + '\n\t| [-ip] = '+defaultip+'\t\t\t|'
        + '\n\t| [-port] = '+str(defaultport)+'\t\t\t|'
        + '\n\t| [-poll] = '+str(defaultpollinterval)+'\t\t\t\t|'
        + '\n\t| Other Arguments = None\t\t|'
        + '\n\t-----------------------------------------\n'
    )

# Main function of the program


def main(serverManager, arguments):
    # Calculate the number of arguments
    lenArguments = len(arguments)
    # Pass all arguments to a dictionary
    # Get by key and argument [-key argument]
    args = {}
    for i in range(0, lenArguments, 2):
        try:
            args[arguments[i]] = arguments[i+1]
        except:
            args[arguments[i]] = None

    # If user want to see the help docs
    if '-h' in args:
        # Print help
        showHelp()
        return 2

    # If the user wants to open a comand line for the ServerManager
    if "-cmd" in args:
        return serverManager.commandLine(defaultip=defaultip, defaultport=defaultport, defaultpollinterval=defaultpollinterval)

    # If user want to open default server
    if "--default" in args:
        serverid = "DEFAULT"
        serverManager.startServer(serverid=serverid, serverip=defaultip,
                                  serverport=defaultport, serverpollinterval=defaultpollinterval)
        return 0

    # If user does not introduces the serverid
    if ("-n" not in args):
        # Show error message
        op.printLog(
            logType="ERROR", messageStr="Please introduce at least the serverid argument to execute the server with default values.\n")
        # Print help
        showHelp()
        return 2

    # Get Arguments
    serverid = args["-n"]  # Get serverid
    # Get ip or set default if empty
    ip = args["-ip"] if("-ip" in args) else defaultip

    # Get port or set default if empty or invalid
    try:
        port = int(args["-port"]) if("-port" in args) else defaultport
    except:
        port = defaultport

    # If invalid
    if(port < 0 or port > 65535):
        port = defaultport

    # Get pollinteval or set default if empty or invalid
    try:
        pollinterval = int(
            args["-pool"]) if("-pool" in args) else defaultpollinterval
    except:
        pollinterval = defaultpollinterval

    # If invalid
    if(pollinterval < 0):
        pollinterval = defaultpollinterval

    # START Server
    serverManager.startServer(
        serverid=serverid, serverip=ip, serverport=port, serverpollinterval=pollinterval)
    return 0


if __name__ == '__main__':
    # SET DEFAULT SERVER CONFIGURATIONS:
    # DEFAULT server configuration
    defaultip = globalConfig.defaultip
    defaultport = globalConfig.defaultport
    defaultpollinterval = globalConfig.defaultpollinterval
    defaultprotocol = globalConfig.defaultserverprotocol

    serverManager = ServerManager(serversprotocolClass=defaultprotocol)

    exitCode = main(serverManager=serverManager, arguments=sys.argv[1:])

    sys.exit(0)
