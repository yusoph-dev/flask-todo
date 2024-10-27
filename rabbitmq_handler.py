import logging
import pika

class RabbitMQHandler(logging.Handler):
    def __init__(self, rabbitmq_url, exchange, routing_key):
        super().__init__()
        self.rabbitmq_url = rabbitmq_url
        self.exchange = exchange
        self.routing_key = routing_key
        self.connection = pika.BlockingConnection(pika.URLParameters(self.rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='direct')

    def emit(self, record):
        log_entry = self.format(record)
        self.channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=log_entry)

    def close(self):
        self.connection.close()
        super().close()