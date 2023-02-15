# we will be implementing discord servers basic implementation
# we have 3 types of nodes registry, servers and client
# Registry server is like central server and maintains information of all servers.
# server, on deployment it registers itself to a particular address, server just broadcasts input to it to all the clients
# so its like 



# server----- exchange ------queue---- A and all of them connect back to server.
#                                 ---- B
#                                 ---- C


# clients connect to registry server first and then requests list of all active server and then connects to server it is interested in
# clients can request subset of articles and also publish articles to server
# topic based exchange for clients

# communication happens in form of protos 

# have separate files for each type of communication via protos
# for each communication each side should print what they receive.





import test_pb2 as tb
import sys

person= tb.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = tb.Person.HOME
#use serialize to get to string
f=person.SerializeToString()
print(f)
p2=tb.Person()

#and this to decode it from string
u=p2.ParseFromString(f)
print(p2.name)
