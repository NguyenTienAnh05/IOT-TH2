import json
import random
import time
import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="sensor_data_queue", durable=True)

    while True:
        data = {
            "device_id": "sensor01",
            "temperature": round(random.uniform(20.0, 42.0), 1),
            "humidity": round(random.uniform(30.0, 90.0), 1),
        }

        channel.basic_publish(
            exchange="",
            routing_key="sensor_data_queue",
            body=json.dumps(data),
            properties=pika.BasicProperties(delivery_mode=2),
        )

        print(f"Đã gửi dữ liệu: {data}")
        time.sleep(3)

except KeyboardInterrupt:
    print("\nĐã dừng chương trình bằng Ctrl+C.")

finally:
    try:
        if "connection" in locals() and connection.is_open:
            connection.close()
            print("Đã đóng kết nối RabbitMQ.")
    except Exception:
        pass