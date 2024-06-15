from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import csv

window = Tk()

#Thêm tiêu đề & chỉnh kích thước giao diện
window.title("GIAO DIỆN NGƯỜI DÙNG")
window.geometry("500x500")

#Thiết kệ form giao diện nằm ở trung tâm màn hình
def makecenter (root) :
    root.update_idletasks ()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth () // 2) - (width // 2)
    y = (root.winfo_screenheight () // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
makecenter(window)

#Truyền file csv thongtinsinhvien.csv vào
csv_thongtin = pd.read_csv("thongtinsinhvien.csv",header=None, names=["MSSV","Họ và tên","Năm sinh","Khóa học","Lớp học","Ngày cập nhật"])
#Truyền file csv diemsoK204160670.csv vào
csv_K204160670 = pd.read_csv("diemsoK204160670.csv",header=None, names=["STT","Mã Học Phần","Tên Học Phần","Điểm Trung Bình"])
#Truyền file csv diemsoK204160672.csv vào
csv_K204160672 = pd.read_csv("diemsoK204160672.csv",header=None, names=["STT","Mã Học Phần","Tên Học Phần","Điểm Trung Bình"])
#Truyền file csv diemsoK204162002.csv vào
csv_K204162002 = pd.read_csv("diemsoK204162002.csv",header=None, names=["STT","Mã Học Phần","Tên Học Phần","Điểm Trung Bình"])
#Truyền file csv diemsoK204162004.csv vào
csv_K204162004 = pd.read_csv("diemsoK204162004.csv",header=None, names=["STT","Mã Học Phần","Tên Học Phần","Điểm Trung Bình"])
#Truyền file csv diemsoK204162008.csv vào
csv_K204162008 = pd.read_csv("diemsoK204162008.csv",header=None, names=["STT","Mã Học Phần","Tên Học Phần","Điểm Trung Bình"])

#Xuất danh sách sinh vien
def DanhSach(path):
    arr = []
    file = open(path, "r", encoding="utf-8")
    reader = csv.reader(file)
    for row in reader:
        arr.append(row)
    file.close()
    return arr

#Label Thông tin sinh viên
lbl = Label(window, text="Hệ thống nhận diện khuôn mặt " ,bg="Pink"  ,fg="Black"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline'))
lbl.pack()
#Label MSSV
lbl_mssv = Label(window, text=" Nhập_MSSV",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 12, ' bold '))
lbl_mssv.place(x=500, y=160)
txt_mssv = Entry(window,width=30,bg="lightskyblue" ,fg="red",font=('times', 15, ' bold '))
txt_mssv.place(x=700, y=165)
#Label Họ và tên
lbl_ten = Label(window,text = "Họ và tên",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 12, ' bold '))
lbl_ten.place(x=500, y=210)
txt_ten = Entry(window,width=30,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt_ten.place(x=700, y=215)
#Label Năm sinh
lbl_nam_sinh = Label(window,text = "Năm sinh",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 12, ' bold '))
lbl_nam_sinh.place(x=500, y=260)
txt_nam_sinh = Entry(window,width=30,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt_nam_sinh.place(x=700, y=265)
#Label Khóa học
lbl_khoa_hoc = Label(window,text = "Khóa học",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 12, ' bold '))
lbl_khoa_hoc.place(x=500, y=310)
txt_khoa_hoc = Entry(window,width=30,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt_khoa_hoc.place(x=700, y=315)
#Label Lớp sinh viên
lbl_lop = Label(window,text = "Lớp sinh viên",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 12, ' bold '))
lbl_lop.place(x=500, y=360)
txt_lop = Entry(window,width=30,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt_lop.place(x=700, y=365)
#Label Ngày cập nhật
lbl_ngay_cap_nhat= Label(window,text = "Ngày cập nhật",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 12, ' bold '))
lbl_ngay_cap_nhat.place(x=500, y=410)
txt_ngay_cap_nhat = Entry(window,width=30,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt_ngay_cap_nhat.place(x=700, y=415)
#Label Xuất thông báo
# lbl_xuat_thong_bao= Label(window,text = "Xuất thông báo",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold '))
# lbl_xuat_thong_bao.place(x=500, y=480)
# txt_xuat_thong_bao = Entry(window,width=30,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
# txt_xuat_thong_bao.place(x=700, y=465)
#Giao diện nhận dạng được khuôn mặt ==> Có được MSSV ==> Lấy MSSV so sanh với data từ thongtinsinhvien.csv ==> Hiển thị.

#Tiếp tục ==> Thực hiện nhận diện người khác và hiển thị thông tin của người đó.
def TiepTuc():
    pass

#Thực hiện khi thao tác được chọn
def ChonThaoTac(self):
    if cbb_thao_tac.get() == "Xem điểm":
        text = "diemso"+txt_mssv.get()+".csv"
        cbb_thao_tac.bind("<<ComboSelected>>",XuatDiem(text))
    elif cbb_thao_tac.get() == "Xem thông tin":
        cbb_thao_tac.bind("<<ComboSelected>>", XuatThongTinSinhVienTreeView())
    elif cbb_thao_tac.get() == "Cập nhật thông tin":
        cbb_thao_tac.bind("<<ComboSelected>>",CapNhatThongTin())
    elif cbb_thao_tac.get() == "Xóa thông tin":
        cbb_thao_tac.bind("<<ComboSelected>>",XoaThongTin())



#Xuất Thông tin sinh viên được gọi lên Textbox
def XuatThongTinSinhVienTextBox():
    dssv = DanhSach("thongtinsinhvien.csv")
    #Linh hoạt chỗ này để cho ra thông tin sinh viên mong muốn nếu không có thì hiển thị textbox trống
    #txt_mssv.focus()
    arr=dssv[1]
    txt_mssv.insert(0,arr[0])
    txt_ten.insert(0, arr[1])
    txt_nam_sinh.insert(0, arr[2])
    txt_khoa_hoc.insert(0, arr[3])
    txt_lop.insert(0, arr[4])
    txt_ngay_cap_nhat.insert(0, arr[5])
XuatThongTinSinhVienTextBox()


def XuatThongTinSinhVienTreeView():
    def selected_item():
        dssv = DanhSach("thongtinsinhvien.csv")
        arr=dssv[1]
        mssv = arr[0]
        ho_ten = arr[1]
        nam_sinh = arr[2]
        khoa_hoc = arr[3]
        lop_hoc = arr[4]
        ngay_cap_nhat = arr[5]
        tt_tree.insert("", index=END, values=(mssv,ho_ten,nam_sinh,khoa_hoc,lop_hoc,ngay_cap_nhat))

    tt_tree = ttk.Treeview(window, height=50, selectmode='browse',columns=('mssv', 'ho_ten', 'nam_sinh', 'khoa_hoc','lop_hoc','ngay_cap_nhat'))

    tt_tree.column('#0', width=0, stretch=NO)
    tt_tree.column('mssv', anchor=CENTER, width=100, stretch=NO)
    tt_tree.column('ho_ten', anchor=W, width=100, stretch=YES)
    tt_tree.column('nam_sinh', anchor=CENTER, width=100, stretch=NO)
    tt_tree.column('khoa_hoc', anchor=CENTER, width=100, stretch=NO)
    tt_tree.column('lop_hoc', anchor=CENTER, width=100, stretch=NO)
    tt_tree.column('ngay_cap_nhat', anchor=CENTER, width=150, stretch=NO)

    tt_tree.heading('mssv', text='MSSV')
    tt_tree.heading('ho_ten', text='HỌ VÀ TÊN')
    tt_tree.heading('nam_sinh', text='NĂM SINH')
    tt_tree.heading('khoa_hoc', text='KHÓA HỌC')
    tt_tree.heading('lop_hoc', text='LỚP HỌC')
    tt_tree.heading('ngay_cap_nhat', text='NGÀY CẬP NHẬT')

    tt_tree.bind('<ButtonRelease-1>', selected_item())
    tt_tree.place(x=10, y=300)

#Xuất điểm sinh viên được gọi lên TreeView
def XuatDiem(path):
    def selected_item(path):
        dsds = DanhSach(path)
        for arr in dsds:
            for i in range(len(arr)):
                arr[i] = arr[i].strip()
            stt = arr[0]
            mahp = arr[1]
            tenhp = arr[2]
            diemtb = arr[3]
            tree.insert("", index=END, values=(stt,mahp,tenhp,diemtb))

    tree = ttk.Treeview(window, height=100, selectmode='browse',columns=('stt', 'mahp', 'tenhp', 'diemtb'))

    tree.column('#0', width=0, stretch=NO)
    tree.column('stt', anchor=CENTER, width=100, stretch=NO)
    tree.column('mahp', anchor=CENTER, width=150, stretch=NO)
    tree.column('tenhp', anchor=W, width=150, stretch=YES)
    tree.column('diemtb', anchor=CENTER, width=150, stretch=NO)

    tree.heading('stt', text='STT')
    tree.heading('mahp', text='MÃ HỌC PHẦN')
    tree.heading('tenhp', text='TÊN HỌC PHẦN')
    tree.heading('diemtb', text='ĐIỂM TRUNG BÌNH')
    text = "diemso" + txt_mssv.get() + ".csv"
    tree.bind('<ButtonRelease-1>', selected_item(text))

    tree.place(x=50,y=300)

def CapNhatThongTin():
    def CapNhat():
        rep = messagebox.askquestion("CẬP NHẬT","Bạn chắc chắn muốn cập nhật?")
        if rep == "yes":
            mssv = txt_mssv.get()
            ten = txt_ten.get()
            nam_sinh = txt_nam_sinh.get()
            khoa_hoc = txt_khoa_hoc.get()
            lop_hoc = txt_lop.get()
            ngay_cap_nhat = txt_ngay_cap_nhat.get()
            # if (mssv == "X") or (mssv = None):
            csv_thongtin.loc[csv_thongtin["MSSV"] == "", ["MSSV","Họ và tên", "Năm sinh", "Khóa học", "Lớp học", "Ngày cập nhật"]] \
                = mssv,ten, nam_sinh, khoa_hoc, lop_hoc, ngay_cap_nhat
            csv_thongtin.loc[csv_thongtin["MSSV"] == "X", ["MSSV", "Họ và tên", "Năm sinh", "Khóa học", "Lớp học", "Ngày cập nhật"]] \
                = mssv, ten, nam_sinh, khoa_hoc, lop_hoc, ngay_cap_nhat
            csv_thongtin.loc[csv_thongtin["MSSV"]==mssv,["Họ và tên","Năm sinh","Khóa học","Lớp học","Ngày cập nhật"]]\
                =ten,nam_sinh,khoa_hoc,lop_hoc,ngay_cap_nhat
            csv_thongtin.to_csv("thongtinsinhvien.csv",header=False, index=False)
            messagebox.showinfo("THÔNG BÁO","THÔNG TIN ĐÃ ĐƯỢC CẬP NHẬT!")

    btn_save = Button(window, text="UPDATE",command=CapNhat)
    btn_save.place(x=150, y=260)
def XoaThongTin():
    def Xoa():
        rep = messagebox.askquestion("XÓA THÔNG TIN","Bạn chắc chắn muốn xóa?")
        if rep == "yes":
            mssv = txt_mssv.get()
            ten = "X"
            nam_sinh = "X"
            khoa_hoc = "X"
            lop_hoc = "X"
            ngay_cap_nhat = "X"
            csv_thongtin.loc[csv_thongtin["MSSV"]==mssv,["MSSV","Họ và tên","Năm sinh","Khóa học","Lớp học","Ngày cập nhật"]] \
                = "X",ten,nam_sinh,khoa_hoc,lop_hoc,ngay_cap_nhat
            csv_thongtin.to_csv("thongtinsinhvien.csv",header=False, index=False)
            messagebox.showinfo("THÔNG BÁO","THÔNG TIN ĐÃ ĐƯỢC XÓA!")
            txt_mssv.delete(0,END)
            txt_ten.delete(0,END)
            txt_nam_sinh.delete(0,END)
            txt_khoa_hoc.delete(0,END)
            txt_lop.delete(0,END)
            txt_ngay_cap_nhat.delete(0,END)
            XuatThongTinSinhVienTextBox()

    btn_save = Button(window, text="DELETE",command=Xoa)
    btn_save.place(x=200, y=260)
#Button Thoát
btn_thoat = Button(window,text="THOÁT",command=quit,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
btn_thoat.place(x=1400,y=500)
#Button Tiếp tục
btn_tiep_tuc = Button(window,text="TIẾP TỤC",command=TiepTuc,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
btn_tiep_tuc.place(x=1250,y=500)
#Combobox chuỗi các thao tác thực hiện với form thông tin sinh viên
cbb_thao_tac = ttk.Combobox(window,width=15,font="Times 13",state="readonly")
cbb_thao_tac["values"]=("Xem thông tin","Xem điểm","Cập nhật thông tin","Xóa thông tin")
cbb_thao_tac.current(0)
cbb_thao_tac.place(x=150,y=230)
cbb_thao_tac.bind("<<ComboboxSelected>>", ChonThaoTac)
#Label thao tác
lbl_thao_tac = Label(window,text = "Thao tác ==>",fg="black",font=("Arial",12))
lbl_thao_tac.place(x=50, y=230)

window.mainloop()

# # Xóa các treeview, button trong thao tác không cần đến nó
# def XoaTree(tree):
#     for i in tree.get_children():
#         tree.delete(i)
#     window.update()
# def XoaBut(btn):
#     pass


