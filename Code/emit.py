import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#exchange creation
channel.exchange_declare(exchange='logs',exchange_type='fanout')



#message creation
message = ' '.join(sys.argv[1:]) or "info: Hello World!"#joins elements with ' ' spaces in between
# print(sys.argv)


#publishing to the exchange
channel.basic_publish(exchange='logs',routing_key='',body=message)

#simply prints  
print(" [x] Sent %r" % message)
connection.close()