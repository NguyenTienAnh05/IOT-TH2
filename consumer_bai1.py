import pika
from datetime import datetime

def callback(ch, method, properties, body):
    current_time = datetime.now().strftime("%H:%M:%S")
    message = body.decode('utf-8')
    
    print(f"Da nhan message: {message}")
    print(f"Thoi gian nhan: {current_time}\n")

def main():
    connection_params = pika.ConnectionParameters(host='localhost')
    
    try:
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        print("Kết nối thành công tới RabbitMQ broker.")
    except Exception as e:
        print(f"Không thể kết nối tới RabbitMQ: {e}")
        return

    queue_name = 'iot_lab_queue'
    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    print(f"Dang lang nghe queue '{queue_name}'. Nhan CTRL+C de thoat.\n")
    channel.start_consuming()

if __name__ == '__main__':
    main()