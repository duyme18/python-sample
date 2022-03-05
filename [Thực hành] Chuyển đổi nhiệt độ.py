def trans(f):
    """Hàm chuyển đổi độ Fahrenheit sang độ Celsius
    f - giá trị độ F
    """
    # Vì nhiệt độ đông của nước trong thang đo Fahrenheit là 32
    # và trong thang đo Celsius là 0,
    # bước 1: chuyển đổi giá trị bằng cách lấy độ Fahrenheit trừ 32
    # Khoảng cách từ điểm đông đến điểm sôi của nước trong thang đo Celsius là 0-100,
    # còn trong thang đo Fahrenheit là 32-212.
    # Điều đó có thể hiểu là khoảng cách 180° trong thang đo Fahrenheit
    # tương đương 100° trong thang đo Celsius.
    # Như vậy, bạn sẽ có tỷ lệ 180/100, sau khi tối giản phân số còn 1,8
    # Bước 2: lấy kết quả bước 1 chia cho 1.8, kết quả thu được là độ Celsius
    return (f - 32) / 1.8

print(trans(74))
print(trans(100))
print(trans(32))