# current_thread: Dùng để lấy tên của luồng hiện tại.
from threading import Thread, Lock, current_thread
from queue import Queue

# Tham số q và lock. q là hàng đợi, nơi các nhiệm vụ được lấy ra và xử lý. 
# lock là khóa dùng để tránh việc nhiều luồng in thông tin ra màn hình cùng một lúc
def worker(q, lock):
    while True:
        value = q.get()  # chặn cho đến khi có mặt hàng đó

        with lock:
            # ngăn chặn việc in cùng lúc với khóa này
            print(f"in {current_thread().name} got {value}")

        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

# Vòng lặp tạo ra 10 threads, mỗi luồng sẽ thực hiện hàm worker.
    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # Đặt mỗi luồng là "daemon", nghĩa là các luồng sẽ tự động kết thúc khi chương trình chính kết thúc.
        t.start()

    # Vòng lặp for x in range(20) sẽ thêm 20 nhiệm vụ (các giá trị từ 0 đến 19) vào hàng đợi.
    for x in range(20):
        q.put(x)

    q.join()  # Chặn lại chương trình chính cho đến khi tất cả các nhiệm vụ trong hàng đợi đã được xử lý xong.

    print('main done')