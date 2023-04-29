## Assessment - Object-oriented programming
In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.

To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

Run the following code that defines this Server class.

```python
#Begin Portion 1#
import random
    
class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}
    
    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        # Add up the load for each of the connections
        total = 0
        for item in self.connections.values():
            total += item 
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#
```
Now run the following cell to create a Server instance and add a connection to it, then check the load:
```python
server.close_connection("192.168.1.1")
print(server.load)
```
You have successfully coded the `close_connection` method if the cell above prints 0.

Hint: Remember that `del` dictionary[key] removes the item with key key from the dictionary.
