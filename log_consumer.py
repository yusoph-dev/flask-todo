import pika

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")
    with open('logs.txt', 'a') as f:
        f.write(body.decode() + '\n')

rabbitmq_url = 'amqp://guest:guest@localhost:5672/'
exchange = 'logs'
routing_key = 'flask_log'
queue = 'flask_log_queue'

connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='direct')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind to multiple routing keys for different log levels
log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
for severity in log_levels:
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=f'flask_log.{severity.lower()}'
    )

print(' [*] Waiting for logs. To exit press CTRL+C')

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
