# Process: Là lớp trong mô-đun multiprocessing, cho phép tạo và quản lý các tiến trình con.
# os: Mô-đun này được sử dụng để truy cập các thông tin liên quan đến hệ điều hành, 
# ở đây dùng để lấy số lượng lõi CPU thông qua os.cpu_count().

from multiprocessing import Process
import os


def square_numbers():
    for i in range(1000):
        result = i * i
    print(f"Tiến trình {os.getpid()} đã hoàn thành việc tính bình phương.")

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()
        
    print("Tất cả các tiến trình đã hoàn thành.")