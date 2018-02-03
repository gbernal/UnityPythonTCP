Unity TCP Network Client
========================

This is a simple TCP client for the Unity 3D platform, written in C# using .NET sockets.

What is it for?
---------------

This is just a starter script for more complex networking applications.

How does it work?
-----------------

The package comes with a simple echo server, written in python.
The server runs on port 50002, it will echo back packets received and will close the connection when receiving a "quit" command.Just type quit and press space bar in the public string in the hierchi tab

Execute the server, load the network prefab to the scene 

The program will send any strings typed in the public string space, and when pressed space bar will send the string to the server.
When received, the server will reply accordingly.

All the string transactions can be monitored in the Unity console window, since no GUI is present.

If a "quit" command is submitted, the server will close the connection, and further packet requests will return an exception (the socket has been closed)
