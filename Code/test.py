import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#exchange creation
channel.exchange_declare(exchange='logs',exchange_type='fanout')



#message creation
message = ' '.join(sys.argv[1:]) or "info: Hello World!"


#publishing to the exchange
channel.basic_publish(exchange='logs',routing_key='',body=message)

#declare a queue
result = channel.queue_declare(queue='', exclusive=True)

#inside a channel it picks up a queue and then binds it to a exchange
channel.queue_bind(exchange='logs',queue=result.method.queue)