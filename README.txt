# IOT-TH2: LẬP TRÌNH PYTHON VỚI GIAO THỨC AMQP

## 1. Yêu cầu môi trường
- Python 3.x
- Cài đặt thư viện: `pip install pika`

## 2. Cấu hình MQTT Broker
Các chương trình sử dụng **RabbitMQ**, một message broker nội bộ giao tiếp bằng giao thức **AMQP**. Thư viện Python `pika` mở kết nối tới `localhost` với cấu hình mặc định của RabbitMQ (cổng AMQP `5672`, tài khoản mặc định `guest/guest`). Các script không truyền username/password riêng, nên RabbitMQ cần cho phép kết nối mặc định trên máy đang chạy chương trình.

Bạn cần cài đặt và khởi động RabbitMQ trước khi chạy các script. Nếu dùng Docker trên máy local, chạy lệnh sau để mở cổng AMQP và cho phép tài khoản `guest` kết nối từ host:
docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS="-rabbit loopback_users []" rabbitmq:management

## 3. Cách chạy chương trình
- Mỗi chương trình được chạy trên các cửa sổ terminal / command prompt riêng biệt để quan sát quá trình giao tiếp qua RabbitMQ.

### Bài 1: Gửi và nhận message cơ bản qua queue
- Chạy Consumer: 'python consumer_bai1.py'
- Chạy Producer: 'python producer_bai1.py'
- Gõ Họ tên và MSV

### Bài 2: Mô phỏng cảm biến IoT gửi dữ liệu môi trường

- Chạy Monitoring consumer: 'python monitoring_consumer_bai2.py'
- Chạy Sensor producer: 'python sensor_producer_bai2.py'
- Nhấn Ctrl + C để dừng

### Bài 3: Mô phỏng hệ thống điều phối cảnh báo IoT với exchange
- Chạy Warining consumer: 'python warning_consumer_bai3.py'
- Chạy Critical consumer: 'python critical_consumer_bai3.py'
- Chạy Alert producer: 'python alert_producer_bai3.py'
- Nhấn Ctrl+C để dừng

## 4. Kết quả

### Bài 1: Gửi và nhận message cơ bản qua queue

Testcase 1:
Bên Producer:

Nhập họ và tên: Nguyen Tien Anh
Nhập mã sinh viên: B23DCCN037

Kết nối thành công tới RabbitMQ broker.
Đã gửi message thành công tới queue 'iot_lab_queue':
  --> Xin chao tu ung dung Python AMQP - B23DCCN037 - Nguyen Tien Anh

Bên Consumer:

Kết nối thành công tới RabbitMQ broker.
Dang lang nghe queue 'iot_lab_queue'. Nhan CTRL+C de thoat.

Da nhan message: Xin chao tu ung dung Python AMQP - B23DCCN037 - Nguyen Tien Anh
Thoi gian nhan: 21:22:06

Testcase 2:
Bên Producer:

Nhập họ và tên: Nguyen Van Quang
Nhập mã sinh viên: B23DCCN690

Kết nối thành công tới RabbitMQ broker.
Đã gửi message thành công tới queue 'iot_lab_queue':
  --> Xin chao tu ung dung Python AMQP - B23DCCN690 - Nguyen Van Quang

Bên Consumer:

Kết nối thành công tới RabbitMQ broker.
Dang lang nghe queue 'iot_lab_queue'. Nhan CTRL+C de thoat.

Da nhan message: Xin chao tu ung dung Python AMQP - B23DCCN690 - Nguyen Van Quang
Thoi gian nhan: 21:23:12

### Bài 2: Mô phỏng cảm biến IoT gửi dữ liệu môi trường
Bên Sensor producer:

Đã gửi dữ liệu: {'device_id': 'sensor01', 'temperature': 35.2, 'humidity': 82.1}
Đã gửi dữ liệu: {'device_id': 'sensor01', 'temperature': 40.0, 'humidity': 79.1}
Đã gửi dữ liệu: {'device_id': 'sensor01', 'temperature': 41.4, 'humidity': 43.7}
Đã gửi dữ liệu: {'device_id': 'sensor01', 'temperature': 21.8, 'humidity': 82.5}
Đã gửi dữ liệu: {'device_id': 'sensor01', 'temperature': 40.0, 'humidity': 87.0}

Đã dừng chương trình bằng Ctrl+C.
Đã đóng kết nối RabbitMQ.

Bên Monitoring_consumer:

Monitoring Consumer đang chờ dữ liệu qua AMQP...
Device: sensor01
Temperature: 35.2
Humidity: 82.1
CANH BAO: Nhiet do cao
------------------------------
Device: sensor01
Temperature: 40.0
Humidity: 79.1
CANH BAO: Nhiet do cao
------------------------------
Device: sensor01
Temperature: 41.4
Humidity: 43.7
CANH BAO: Nhiet do cao
------------------------------
Device: sensor01
Temperature: 21.8
Humidity: 82.5
------------------------------
Device: sensor01
Temperature: 40.0
Humidity: 87.0
CANH BAO: Nhiet do cao
------------------------------

### Bài 3: Mô phỏng hệ thống điều phối cảnh báo IoT với exchange
Bên Alert producer:

Producer đang chạy gửi dữ liệu... (Nhấn Ctrl + C để dừng)
Da gui [info]: He thong hoat dong binh thuong info
Da gui [warning]: Nhiet do phong may chuot muc warning
Da gui [info]: He thong hoat dong binh thuong info
Da gui [warning]: Nhiet do phong may chuot muc warning
Da gui [warning]: Nhiet do phong may chuot muc warning
Da gui [warning]: Nhiet do phong may chuot muc warning
Da gui [info]: He thong hoat dong binh thuong info
Da gui [critical]: Cam bien kho lanh mat ket noi critical

Producer đã dừng hoạt động.

Bên Critical consumer:
[critical_queue] Da nhan: Cam bien kho lanh mat ket noi critical
[critical_queue] Da nhan: Cam bien kho lanh mat ket noi critical
[critical_queue] Da nhan: Cam bien kho lanh mat ket noi critical
[critical_queue] Da nhan: Cam bien kho lanh mat ket noi critical

Consumer đã dừng hoạt động.

Bên Warning consumer:
Warning Consumer dang cho canh bao muc warning...
[warning_queue] Da nhan: Nhiet do phong may chuot muc warning
[warning_queue] Da nhan: Nhiet do phong may chuot muc warning
[warning_queue] Da nhan: Nhiet do phong may chuot muc warning
[warning_queue] Da nhan: Nhiet do phong may chuot muc warning
[warning_queue] Da nhan: Nhiet do phong may chuot muc warning
[warning_queue] Da nhan: Nhiet do phong may chuot muc warning
[warning_queue] Da nhan: Nhiet do phong may chuot muc warning

