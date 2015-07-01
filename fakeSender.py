import pika
import json
from data.configuration import config

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=config['sms_queue'])

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print "Got payload ", payload
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=config['sms_queue'])

print "Consuming"
channel.start_consuming()
