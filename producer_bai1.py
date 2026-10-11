import pika

def main():
    ho_ten = input("Nhập họ và tên: ").strip()
    ma_sinh_vien = input("Nhập mã sinh viên: ").strip()

    if not ho_ten or not ma_sinh_vien:
        print("Họ tên và Mã sinh viên không được để trống!")
        return

    connection_params = pika.ConnectionParameters(host='localhost')
    
    try:
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        print("\nKết nối thành công tới RabbitMQ broker.")
    except Exception as e:
        print(f"Không thể kết nối tới RabbitMQ: {e}")
        return

    queue_name = 'iot_lab_queue'
    channel.queue_declare(queue=queue_name, durable=True)

    noi_dung_chao = "Xin chao tu ung dung Python AMQP"
    message_body = f"{noi_dung_chao} - {ma_sinh_vien} - {ho_ten}"

    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message_body.encode('utf-8'),
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )

    print(f"Đã gửi message thành công tới queue '{queue_name}':")
    print(f"    --> {message_body}")

    connection.close()

if __name__ == '__main__':
    main()