def my_decorator(func): # hàm decorator nó nhận một hàm khác func làm đối số.
    def wrapper(): #  Đây là hàm bọc, thực hiện các hành động trước và sau khi gọi hàm func().
        print("Trước khi gọi hàm.")
        func()
        print("Sau khi gọi hàm.")
    return wrapper

@my_decorator
def say_hello():
    print("Xin chào. Tôi là Dmon's!")

# Gọi hàm say_hello
say_hello()
