import pika

def callback(ch, method, properties, body):
    with open('logs.txt', 'a') as f:
        f.write(body.decode() + '\n')

rabbitmq_url = 'amqp://guest:guest@localhost:5672/'
exchange = 'logs'
routing_key = 'flask_log'
queue = 'flask_log_queue'

connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='direct')
channel.queue_declare(queue=queue)
channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)
channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

print('Waiting for logs. To exit press CTRL+C')
channel.start_consuming()