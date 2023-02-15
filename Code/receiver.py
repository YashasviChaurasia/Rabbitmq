#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#exchange creation
channel.exchange_declare(exchange='logs',exchange_type='fanout')

#declare a queue
result = channel.queue_declare(queue='', exclusive=True)

#queue name stores as variable
queue_name = result.method.queue

#inside a channel it picks up a queue and then binds it to a exchange
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

#used to register a consumer to a queue
#also tells queue what fucntion to call when message is received
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

#used to start the consumption loop
channel.start_consuming()