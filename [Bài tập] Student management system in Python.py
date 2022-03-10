class Student:
    def __init__(self, student_id, name, doj, address, specialized, classroom):
        self.student_id = student_id
        self.name = name
        self.doj = doj
        self.address = address
        self.specialized = specialized
        self.classroom = classroom

    def add_student(self):
        """
        Hàm thêm sinh viên
        :return:
        """
        print("*** Thêm sinh viên ***")

        global list_student

        infor = {
            'student_id': '',
            'name': '',
            'doj': '',
            'address': '',
            'specialized': '',
            'classroom': ''
        }
        print('Nhập Id:')
        self.student_id = int(input())
        while True:
            for i in range(0, len(list_student)):
                if self.student_id == list_student[i]['student_id']:
                    print('Id đã tồn tại. Nhập lại:')
                    self.student_id = int(input())
            else:
                break

        infor['student_id'] = self.student_id
        print('Nhập tên:')
        self.name = input()
        infor['name'] = self.name
        print('Nhập ngày tháng năm sinh (dd/mm/yyyy):')
        self.doj = input()
        infor['doj'] = self.doj
        print('Nhập địa chỉ:')
        self.address = input()
        infor['address'] = self.address
        print('Nhập chuyên ngành:')
        self.specialized = input()
        infor['specialized'] = self.specialized
        print('Nhập tên lớp:')
        self.classroom = input()
        infor['classroom'] = self.classroom
        list_student.append(infor)
        for i in range(0,len(list_student)):
            print(list_student[i])

    def find_student(self):
        """
        Hàm tìm kiếm sinh viên
        :return:
        """
        print("*** Tìm kiếm sinh viên ***")
        global list_student
        for i in range(0, len(list_student)):
            if self.student_id == list_student[i]['student_id']:
                print([i, list_student[i]])
        print('Không tìm thấy sinh viên với ID trên!!!')

    def delete_student(self):
        """
        Hàm tìm kiếm sinh viên
        :return:
        """
        print("*** Xoá sinh viên ***")
        global list_student
        print('Nhập id sinh viên cần xoá:')
        self.student_id = int(input())

        for i in range(0, len(list_student)):
            if self.student_id == list_student[i]['student_id']:
                print('Xoá thành công!')
                list_student.pop(i)
                for j in range(0, len(list_student)):
                    print(list_student[j])
                break
        print('Không tìm thấy sinh viên với ID trên!!!')

    def get_students(self):
        """
        Hàm lấy danh sách sinh viên
        :return:
        """
        print("*** Danh sách sinh viên ***")
        global list_student
        for i in range(0, len(list_student)):
            print("[", list_student[i]['student_id'], "]", "[", list_student[i]['name'], "]", "[",
                  list_student[i]['doj'], "]", "[", list_student[i]['address'], "]", "[",
                  list_student[i]['specialized'], "]", "[", list_student[i]['classroom'], "]")

    def update_student(self):
        print("*** Cập nhật sinh viên ***")
        global list_student
        print('Nhập id sinh viên cần cập nhật:')
        self.student_id = int(input())

        for i in range(0, len(list_student)):
            if self.student_id == list_student[i]['student_id']:
                print('Nhập tên:')
                self.name = input()
                list_student[i]['name'] = self.name
                print('Nhập ngày tháng năm sinh (dd/mm/yyyy):')
                self.doj = input()
                list_student[i]['doj'] = self.doj
                print('Nhập địa chỉ:')
                self.address = input()
                list_student[i]['address'] = self.address
                print('Nhập chuyên ngành:')
                self.specialized = input()
                list_student[i]['specialized'] = self.specialized
                print('Nhập tên lớp:')
                self.classroom = input()
                list_student[i]['classroom'] = self.classroom
                for j in range(0, len(list_student)):
                    print(list_student[j])
                break
        print('Không tìm thấy sinh viên với ID trên!!!')



list_student = [
    {'student_id': 1, 'name': 'b', 'doj': '13/03/1996', 'address': 'HN', 'specialized': 'IT', 'classroom': 'GEM001'},
    {'student_id': 3, 'name': 'a', 'doj': '27/07/1996', 'address': 'HN', 'specialized': 'IT',
     'classroom': 'GEM002'},
    {'student_id': 2, 'name': 'c', 'doj': '27/07/1996', 'address': 'HN', 'specialized': 'IT',
     'classroom': 'GEM002'}
]
student = Student('', '', '', '', '', '')
action = 0
while action >= 0:
    if action == 1:
        student.add_student()
    elif action == 2:
        student.update_student()
    elif action == 3:
        student.delete_student()
    elif action == 4:
        student.find_student()
    elif action == 5:
        student.get_students()

    print("Chọn chức năng muốn thực hiện:")
    print("1. Thêm sinh viên")
    print("2. Sửa sinh viên")
    print("3. Xóa sinh viên")
    print("4. Tìm kiếm sinh viên")
    print("5. Xem danh sách sinh viên")
    print("0. Thoát.")
    action = int(input("Chọn: "))
    if action == 0:
        break
