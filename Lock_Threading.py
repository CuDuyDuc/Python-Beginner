from threading import Thread, Lock
import time

# database_value là biến toàn cục mà cả hai luồng sẽ cố gắng thay đổi.
database_value = 0

# Hàm này nhận một đối tượng Lock để đảm bảo rằng chỉ có một luồng thay đổi biến database_value tại một thời điểm.
def increase(lock):
    global database_value 

    # Khóa biến dùng chung, nghĩa là chỉ cho phép một luồng thực hiện việc thay đổi database_value trong khi các luồng khác phải đợi.
    lock.acquire()

    # Sao chép database_value sang biến cục bộ
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1) # Dừng lại 0,1 giây để mô phỏng một tác vụ mất thời gian.
    database_value = local_copy

    # Mở khóa, cho phép các luồng khác tiếp tục.
    lock.release()


if __name__ == "__main__":

    # Tạo một đối tượng Lock. Đối tượng này sẽ được truyền vào hàm increase để điều khiển việc khóa và mở khóa dữ liệu.
    lock = Lock()

    print('Start value: ', database_value)

    # Chuyển khóa cho chức năng đích
    t1 = Thread(target=increase, args=(lock,)) # chú ý dấu phẩy sau khóa vì args phải là một tuple
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('End main')