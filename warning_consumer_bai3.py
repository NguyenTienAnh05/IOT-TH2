import pika


def callback(ch, method, properties, body):
  print(f"[warning_queue] Da nhan: {body.decode('utf-8')}")
  ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="iot_alert_exchange", exchange_type="direct")

channel.queue_declare(queue="warning_queue", durable=True)
channel.queue_bind(
    exchange="iot_alert_exchange", queue="warning_queue", routing_key="warning"
)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="warning_queue", on_message_callback=callback)

print("Warning Consumer đang chờ cảnh báo mức warning...")
channel.start_consuming()