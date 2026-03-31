import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", server.add(a, b))
print("Subtraction:", server.sub(a, b))
print("Multiplication:", server.mul(a, b))
print("Division:", server.div(a, b))