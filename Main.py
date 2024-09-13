# List: là một tập hợp được sắp xếp (có chỉ mục) và có thể thay đổi. Cho phép các thành viên trùng lặp.

thislist = ["banana", "chery", "apple", "orange"]
fruits = ["mango", "pineapple", "papaya"]

# insert(): chèn một mục list mới mà không thay thế bất kỳ giá trị hiện có nào.
thislist.insert(2, "watermelon")

# sử dụng append(): để thêm 1 mục vào cuối list
thislist.append("corn")

# sử dụng remove() loại bỏ mục đã chỉ định. remove() chỉ xóa được 1 mục đầu tiên trong ds nếu ds có nhiều hơn 1 mục   
thislist.remove("banana")

# sử dụng pop() loại bỏ chỉ mục đã chỉ định
thislist.pop(1)

#  sử dụng extend() để thêm các phần tử từ list khác vào list hiện tại
thislist.extend(fruits)

# sử dụng del() cũng xóa chỉ mục đã chỉ định.
del thislist[1] 
print(thislist)

# sử dụng clear()làm trống list
# thislist.clear()

# Trích	xuất mảng con [start:end] 	
print(thislist[None: 3]) 
print(thislist[1:4])

# Lặp qua một list sử dụng for
for x in thislist:
  print(x)
  
# In tất cả các mục bằng cách tham chiếu đến số chỉ mục của chúng
for i in range(len(thislist)):
  print(thislist[i])
  
# Lặp qua một list sử dụng while. Sử dụng hàm len() này để xác định độ dài của list
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Sắp xếp list 
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numList.sort()
print(numList)

# Sắp xếp list (giảm dần) reverse = True
numList.reverse()
print(numList)

# Lấy phần tử thông qua bước nhảy
newNumList = numList[::1]
print(newNumList)

newNumList = numList[::2] 
print(newNumList)

newNumList = numList[::-1] # đảo ngược list vs chỉ mục âm
print(newNumList)

# /=============================================================/
# Tuple là một tập hợp được sắp xếp (có chỉ mục) và không thể thay đổi. Cho phép các thành viên trùng lặp.
# Note: Khi tạo một tuple chỉ có một phần tử, thêm dấu phẩy sau phần tử đó, nếu không nó sẽ không được xác định là một tuple.
numTuple = (1,)

tup = (i for i in range(10) if (i % 2 == 0))
newtuple = tuple(tup)
print(newtuple)

# Thay đổi giá trị của tuple: chuyển đổi tuple thành list, thay đổi list và chuyển đổi list trở lại thành tuple.
x = ("orange", "apple", "kiwi")
y = list(x)
y[1] = "cherry"
x = tuple(y)

print(x)

# khi chuyển tuple thành list thì có thể sử dụng phương thức append() để thêm 1 mục vào tuple
thistuple = ("orange", "apple", "watermelon")
mylist = list(thistuple)
mylist.append("kiwi")
thistuple = tuple(mylist)

# thêm tuple vào tuple
newtuple = ("banana",)
thistuple += newtuple

print(thistuple)

# giải nén tuple
thistuple1 = ("orange", "apple", "watermelon")
(a, b, c) = thistuple1
print(a)
print(b)
print(c)

# sử dụng Asterisk*
fruitstuple = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruitstuple

print(green)
print(yellow)
print(red)

# Chuyển đổi tuple thành một list, xóa remove() và chuyển đổi nó trở lại thành tuple
y = list(fruitstuple)
y.remove("apple")
fruitstuple = tuple(y)

print(fruitstuple)

#  /=============================================================/
# Set là một tập hợp không được sắp xếp, không thể thay đổi và không được lập chỉ mục. Không có thành viên trùng lặp.
# Set chỉ có thể chứa hashable object nhưng chính nó không phải là 1 hashable object. Do đó không thể chứa 1 set trong 1 set

thisSet = {"orange", "apple", "banana"}
fruitsSet = {"watermelon", "banana", "cherry", "strawberry"}

# Lặp qua một set: 
for x in thisSet:
  print(x)

# Để thêm một mục vào set, sử dụng add():
thisSet.add("corn")
print(thisSet)

# Để thêm các mục từ tập hợp khác vào tập hợp hiện tại, sử dụng phương update()
thisSet.update(fruitsSet)
print(thisSet)

# Chỉ giữ lại các bản sao: intersection()
result = thisSet.intersection(fruitsSet)
print(result)

# Giữ lại các phần tử từ set đầu tiên không có trong set khác: difference()
result = thisSet.difference(fruitsSet)
print(result)

# Giữ lại tất cả các mục trừ các mục trùng lặp: symmetric_difference()
result = fruitsSet.symmetric_difference(thisSet)
print(result)

# Để xóa một mục trong một tập hợp, sử dụng phương thức remove(), hoặc discard()
# Lưu ý: Nếu mục cần xóa không tồn tại, remove() sẽ xảy ra lỗi, còn discard() thì không

thisSet.remove("orange")

thisSet.discard("corn")

# Phương pháp union() trả về một tập hợp mới với tất cả các mục từ cả hai tập hợp
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
# hoặc cũng có thể sử dụng dấu |
# set3 = set1 | set2
print(set3)

#  /=============================================================/
# Dictionary là một bộ sưu tập được sắp xếp và có thể thay đổi. Không có thành viên trùng lặp.
# Các giá trị trùng lặp sẽ ghi đè lên các giá trị hiện có
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "color": ["red", "yellow"]
}
 
for x in thisdict:
  print(x)
  
# Trả về danh sách tất cả các khóa trong dictionary: keys()
keyDict = thisdict.keys()
print(keyDict)

# Trả về danh sách tất cả các giá trị trong dictionary: values()
keyDict = thisdict.values()
print(keyDict)

# Các giá trị trong các mục Dictionary có thể thuộc bất kỳ kiểu dữ liệu nào
# Có thể thay đổi giá trị của một mục cụ thể bằng cách tham chiếu đến tên khóa của mục đó
thisdict["year"] = 2018

# Phương pháp update() sẽ cập nhật từ điển bằng các mục từ đối số đã cho
thisdict.update({"year": 2021})

# cập nhật color thêm màu green
thisdict.update({"color": ["green", "white"]})

# Phương pháp popitem() xóa mục được chèn cuối cùng
thisdict.popitem()

print(thisdict)




