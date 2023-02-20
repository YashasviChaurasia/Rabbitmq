import pika
import tut_pb2 as tb
import sys

import uuid

unique_id = str(uuid.uuid1())
print(unique_id)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channelRPC = connection.channel()

# channelRPC.basic_qos(prefetch_count=1)


channelRPC.exchange_declare(exchange='test_client_ex2',exchange_type='direct')
# msg creation


result = channelRPC.queue_declare(queue='test_client_queue1-2', exclusive=True)
queue_name = result.method.queue
channelRPC.queue_bind(exchange='test_server_ex2', queue=queue_name,routing_key=unique_id)



while(True):
    routing_id=input("Enter Routing for server id: ")
    print(routing_id)
    txt=tb.request()
    txt.message=input("REQUEST: ")
    txt.addr=unique_id
    f=txt.SerializeToString()

    #exchange creation not needed here as exchange is already theri on connection
    # channel.exchange_declare(exchange='logs',exchange_type='fanout')

    #publishing to the exchange
    channelRPC.basic_publish(exchange='test_client_ex2',routing_key=routing_id,body=f)

    #simply prints  
    # print(" [x] Sent %r" % txt.message)


    # print("ARC 2")




    print(' [*] Waiting for client message. To exit press CTRL+C')


    def callback(ch, method, properties, body):
        txt.ParseFromString(body)
        print(" [x] %r" % txt.message)
        ch.basic_cancel(consumer_tag)
        # print(ch,method,properties)
    consumer_tag=channelRPC.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    #used to register a consumer to a queue
    #also tells queue what fucntion to call when message is received


    channelRPC.start_consuming()



connection.close()