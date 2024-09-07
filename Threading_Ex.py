from threading import Thread

# Hàm square_numbers để tính bình phương của các số từ 0 đến 999. 
def square_numbers():
    for i in range(1000):
        result = i * i
        print("Luồng đã hoàn thành việc tính bình phương.")

# Cú pháp tiêu chuẩn để đảm bảo rằng đoạn mã bên trong khối này chỉ được thực thi khi chương trình được chạy trực tiếp, 
# chứ không phải khi chương trình được import từ một module khác.
if __name__ == "__main__":        
    threads = [] # một danh sách để chứa các luồng (threads) được tạo ra trong chương trình.
    num_threads = 10 # biến được đặt giá trị là 10, nghĩa là sẽ có 10 luồng được tạo ra để chạy song song.

# Vòng lặp này sẽ tạo ra 10 luồng bằng cách sử dụng lớp Thread
    for i in range(num_threads): 
        thread = Thread(target=square_numbers)
        threads.append(thread) # sau khi một luồng được tạo nó sẽ được thêm vào danh sách threads bằng phương thức append().

# Vòng lặp thứ hai sẽ bắt đầu khởi động từng luồng một bằng cách gọi phương thức start() trên mỗi luồng.
    for thread in threads:
        thread.start()

# Vòng lặp cuối cùng sử dụng phương thức join() trên mỗi luồng.
# join() chặn luồng chính lại cho đến khi luồng con tương ứng đã kết thúc công việc của nó.
    for thread in threads:
        thread.join()
        
    print("Tất cả các luồng đã hoàn thành.")