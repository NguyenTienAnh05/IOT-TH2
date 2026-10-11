import random
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Khai báo Direct Exchange
channel.exchange_declare(exchange="iot_alert_exchange", exchange_type="direct")

severities = ["info", "warning", "critical"]
messages = {
    "info": "He thong hoat dong binh thuong info",
    "warning": "Nhiet do phong may chuot muc warning",
    "critical": "Cam bien kho lanh mat ket noi critical",
}

print("Producer đang chạy gửi dữ liệu... (Nhấn Ctrl + C để dừng)")

try:
  while True:
    severity = random.choice(severities)
    message = messages[severity]

    channel.basic_publish(
        exchange="iot_alert_exchange", routing_key=severity, body=message
    )
    print(f"Da gui [{severity}]: {message}")

    time.sleep(3)
except KeyboardInterrupt:
  print("\nProducer đã dừng hoạt động.")
finally:
  if connection.is_open:
    connection.close()