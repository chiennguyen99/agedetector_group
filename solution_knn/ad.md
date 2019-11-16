# Agedetector Group dùng thuật toán KNN để giải
Clone source code và cài đặt python 3.7 để chạy sử dụng câu lệnh sau để cài đặt các module cần thiết
```sh
$ pip install -r requirements.txt
```
Code trong sau khi clone đã config chạy được nên chỉ cần chạy luôn thuật toán KNN để nhận được kết quả
```sh
$ python sk_learn.py
```
Các bước giải khi có tập dữ liệu train như sau 
1. Chuẩn bị dữ liệu
  - Để dữ liệu train vào trong './data/train_1/' đặt tên file là maintrain.txt
  - Để dữ liệu test vào trong './data/test_1/' đặt tên file là main_test.txt
2. Chaỵ chương trình
  - Train dữ liệu run code file main_train.py 
    ```sh
    $ python main_train.py
    ```
  - Chuẩn hóa dữ liệu test bằng cách run file test_create_data.py
    ```sh
    $ python test_create_data.py
    ```
  - Có 2 hướng chạy thuật toán KNN:
    - Nếu chỉ cần đoán dữ liệu thì vào file sk_learn.py comment 1 vài đoạn code như sau:
        ```sh
        target_test = get_target_test()
        print("KNeighbors accuracy score : ", accuracy_score(target_test, pred))
        ```
    - Nếu muốn so sánh dữ liệu đoán được với kết quả thực tế thì tạo file result.txt chứa kết quả theo định dạng mỗi kết quả trên 1 dòng. Lưu file result.txt vào trong folder './data/test_1/'
    - Cuối cùng chỉ cần chạy
    ```sh
    $ python sk_learn.py
    ```
 