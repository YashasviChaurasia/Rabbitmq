#!/usr/bin/env python
import pika
import sys
import tut_pb2 as tb

import uuid

unique_id = str(uuid.uuid1())
print(unique_id)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channelRPC = connection.channel()

#sets consumption limit
# channelRPC.basic_qos(prefetch_count=1)
#exchange creation self
channelRPC.exchange_declare(exchange='test_server_ex2',exchange_type='direct')

#declare a queue

#queue name stores as variable

result = channelRPC.queue_declare(queue='test_server_queue1', exclusive=True)
queue_name = result.method.queue
channelRPC.queue_bind(exchange='test_client_ex2', queue=queue_name,routing_key=unique_id)

# count=0
while(True):
    print(' [*] Waiting for client REQ. To exit press CTRL+C')

    # resp='0'
    
    txt=tb.request()
    
    def callback(ch, method, properties, body):
    
        txt.ParseFromString(body)
        print(" [x] %r" % txt.message)
        ch.basic_cancel(consumer_tag)
        


        # print(ch,method,properties)
    consumer_tag=channelRPC.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    #used to register a consumer to a queue
    #also tells queue what fucntion to call when message is received


    #used to start the consumption loop
    channelRPC.start_consuming()



    # print("ARC 2")
    route_back=txt.addr
    # count++
    txt=tb.request()
    txt.message=input("RESPONCE: ")
    f=txt.SerializeToString()
    channelRPC.basic_publish(exchange='test_server_ex2',routing_key=route_back,body=f)

connection.close()