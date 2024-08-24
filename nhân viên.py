# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:13:51 2024

@author: ADMIN
"""

class NVVanPhong:
    def __init__(self, ma_nhan_vien, ho_ten, luong_co_ban, luong_hang_thang, so_ngay):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.luong_hang_thang = luong_hang_thang
        self.so_ngay = so_ngay

    def __str__(self):
        return (f"NVVanPhong({self.ma_nhan_vien}, {self.ho_ten}, {self.luong_co_ban}, "
                f"{self.luong_hang_thang}, {self.so_ngay})")

class NVBanHang:
    def __init__(self, ma_nhan_vien, ho_ten, luong_co_ban, luong_hang_thang, so_san_pham):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.luong_hang_thang = luong_hang_thang
        self.so_san_pham = so_san_pham

    def __str__(self):
        return (f"NVBanHang({self.ma_nhan_vien}, {self.ho_ten}, {self.luong_co_ban}, "
                f"{self.luong_hang_thang}, {self.so_san_pham})")


def create_employee_data():
    employees = []

   
    employees.append(NVVanPhong("NV001", "Nguyễn Văn A", 5000000, 6000000, 22))
    employees.append(NVVanPhong("NV002", "Trần Thị B", 5500000, 6500000, 21))
    employees.append(NVVanPhong("NV003", "Lê Văn C", 5200000, 6200000, 20))
    employees.append(NVVanPhong("NV004", "Phạm Thị D", 5300000, 6300000, 23))
    employees.append(NVVanPhong("NV005", "Hoàng Văn E", 5100000, 6100000, 19))

    
    employees.append(NVBanHang("NV006", "Vũ Thị F", 4000000, 5000000, 30))
    employees.append(NVBanHang("NV007", "Ngô Văn G", 4200000, 5200000, 28))
    employees.append(NVBanHang("NV008", "Đặng Thị H", 4300000, 5300000, 32))
    employees.append(NVBanHang("NV009", "Bùi Văn I", 4100000, 5100000, 29))
    employees.append(NVBanHang("NV010", "Nguyễn Thị J", 4400000, 5400000, 27))

    return employees


def display_employees(employees):
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    employees = create_employee_data()
    display_employees(employees)
