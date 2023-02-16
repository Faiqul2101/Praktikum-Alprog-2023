# # Studi Kasus
# #         Class Course dan Student
# #         Ada Course jenis Online dan Offline (Inheritance)

# Basic Class
print("\nBasic Class")
class Student:
    jumlah_murid = 0  #Class Atribute
    # def __init__ (self, nama_attribute1, nama_attribute2, nama_attribute3)
    def __init__(self, name, age, grade):
        self.nama = name 
        self.usia = age
        self.nilai = grade
        Student.jumlah_murid += 1

    def get_grade(self):
        return self.nilai

class Course:
    def __init__(self,name , max_student):  # Method init
        self.nama = name
        self.maks_siswa = max_student
        self.murid2 = []
    def add_student(self, student):
        if len(self.murid2) < self.maks_siswa:
            self.murid2.append(student) 
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.murid2:
            value += student.get_grade()
        
        return value / len(self.murid2)

s1 = Student('Faiq', 19, 90) #Membuat Objek dari class Student
print(s1.nama) 
s2 = Student('Sasa', 21, 75)
s3 = Student('Dony', 20, 80)

print(Student.jumlah_murid) #Memanggil atribut Class

course = Course('Science', 2) #Membuat Objek dari class Course
course.add_student(s1) #Menambahkan Murid kedalam class Course dengan Method add_student
course.add_student(s2)
print('murid kedua namanya :' ,course.murid2[1].nama) #Memanggil nama murid dalam class Course
print(course.get_average_grade()) #Menampilkan Nilai rata2 dari Method get_average_grade


# Inheritance
print("\nInheritance")
class Student:
    jumlah_murid = 0
    def __init__(self, name, age, grade):
        self.nama = name
        self.usia = age
        self.nilai = grade
        Student.jumlah_murid += 1

    def get_grade(self):
        return self.nilai
    
class Course:  #Class Parent
    jumlahkelas = 0
    def __init__(self,name , max_student): 
        self.nama = name
        self.maks_siswa = max_student
        self.murid2 = []
        Course.jumlahkelas += 1
    def add_student(self, student):
        if len(self.murid2) < self.maks_siswa:
            self.murid2.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.murid2:
            value += student.get_grade()
        
        return value / len(self.murid2)

class Online(Course): # Class Child dari class Course
    jumlahkelas_online = 0  
    def __init__(self, name, max_student, media):
        super().__init__(name, max_student) # Inheritance
        self.media = media   # Properti Baru
        Online.jumlahkelas_online += 1

class Offline(Course): # Class Child dari class Course
    jumlahkelas_offline = 0
    def __init__(self, name, max_student, ruang_kelas): 
        super().__init__(name, max_student)  # Inheritance
        self.ruang_kelas = ruang_kelas  # Properti Baru
        Offline.jumlahkelas_offline += 1
        
s1 = Student('Faiq', 19, 90)
print(s1.nama)
s2 = Student('Sasa', 21, 75)
s3 = Student('Dony', 20, 80)

course1 = Online('Science', 3, 'Zoom')
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)

course2 = Offline('Math', 1, '3-C')
course2.add_student(s3)

print(Course.jumlahkelas)
print(Online.jumlahkelas_online)
print(Offline.jumlahkelas_offline)
print(course1.get_average_grade())
print('murid kedua namanya :' ,course1.murid2[1].nama) #Memanggil nama murid dalam class Course

# Overriding
print("\nOverriding")
class Student:
    jumlah_murid = 0
    def __init__(self, name, age, grade):
        self.nama = name
        self.usia = age
        self.nilai = grade
        Student.jumlah_murid += 1
    def get_grade(self):
        return self.nilai

class Course:  #Class Parent
    jumlahkelas = 0
    def __init__(self,name , max_student): 
        self.nama = name
        self.maks_siswa = max_student
        self.murid2 = []
        Course.jumlahkelas += 1
    def add_student(self, student):
        if len(self.murid2) < self.maks_siswa:
            self.murid2.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.murid2:
            value += student.get_grade()
        return value / len(self.murid2)
    def keterangan(self):
        return f'Ini Adalah Sebuah Kelas dengan nama {self.nama}, dengan kapasitas maksimum sebanyak {self.maks_siswa} siswa'

class Online(Course): # Class Child dari class Course
    jumlahkelas_online = 0  
    def __init__(self, name, max_student, media):
        super().__init__(name, max_student) # Inheritance
        self.media = media   # Properti Baru
        Online.jumlahkelas_online += 1
    def keterangan(self):  #Override
        return f'Ini Adalah Sebuah Kelas dengan nama {self.nama}, dengan kapasitas maksimum sebanyak {self.maks_siswa} siswa bermediakan {self.media}'

class Offline(Course): # Class Child dari class Course
    def __init__(self, name, max_student, ruang_kelas): 
        super().__init__(name, max_student)  # Inheritance
        self.ruang_kelas = ruang_kelas  # Properti Baru
    def keterangan(self):  #Override
        return f'Ini Adalah Sebuah Kelas dengan nama {self.nama}, dengan kapasitas maksimum sebanyak {self.maks_siswa} di kelas {self.ruang_kelas}'

course = Course('Science', 10)
print(course.keterangan())

course1 = Online('Math', 15, 'Zoom')
print(course1.keterangan())

course2 = Offline('Art', 20, '3-C')
print(course2.keterangan())