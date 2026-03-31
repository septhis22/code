from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8000))
print("Calculator RMI Server running...")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

server.register_function(add)
server.register_function(sub)
server.register_function(mul)
server.register_function(div)

server.serve_forever()