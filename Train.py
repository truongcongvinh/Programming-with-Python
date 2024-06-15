import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
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
# csv_thongtin = pd.read_csv("thongtinsinhvien.csv",header=None, names=["MSSV","Họ và tên","Năm sinh","Khóa học","Lớp học","Ngày cập nhật"])
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


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
def TakeImages():
    mssv = txt_mssv.get()
    ho_ten = txt_ten.get()
    nam_sinh = txt_nam_sinh.get()
    khoa_hoc = txt_khoa_hoc.get()
    lop_hoc = txt_lop.get()
    ngay_cap_nhat = txt_ngay_cap_nhat.get()
    if (is_number(mssv) and ho_ten.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #incrementing sample number
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+ho_ten +"."+mssv +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds
            # Nhấn q để đừng quá trình thêm ảnh
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + mssv +" Name : "+ ho_ten
        row = [mssv,ho_ten,nam_sinh,khoa_hoc,lop_hoc,ngay_cap_nhat]
        with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        messagebox.showinfo("THÔNG BÁO", res)
    else:
        if(is_number(mssv)):
            res = "Enter Alphabetical Name"
            messagebox.showinfo("THÔNG BÁO", res)
        if(ho_ten.isalpha()):
            res = "Enter Numeric Id"
            messagebox.showinfo("THÔNG BÁO", res)


def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    # Tạo một facelist
    lstface = []
    # Tạo một list MSSV
    lstmssv = []
    # Run các path để tải mssv và image
    for imagePath in imagePaths:
        # tải hình ảnh và chuyển nó thành grayscale
        pilImage = Image.open(imagePath).convert('L')
        #Chuyển tất cả PIL image sang dạng numpy array
        imageNp = np.array(pilImage, 'uint8')
        # Lấy mssv từ image
        mssv = int(os.path.split(imagePath)[-1].split(".")[1])
        # Trích xuất các face có trong Image sample
        lstface.append(imageNp)
        lstmssv.append(mssv)
    return lstface, lstmssv

def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"
    messagebox.showinfo("THÔNG BÁO", res)

# def TrackImages():
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.read("TrainingImageLabel\Trainner.yml")
#     harcascadePath = "haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(harcascadePath);
#     df=pd.read_csv("StudentDetails\StudentDetails.csv")
#     cam = cv2.VideoCapture(0)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     col_names =  ['Id','Name','Date','Time']
#     attendance = pd.DataFrame(columns = col_names)
#     while True:
#         ret, im =cam.read()
#         gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#         faces=faceCascade.detectMultiScale(gray, 1.2,5)
#         for(x,y,w,h) in faces:
#             cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
#             Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
#             if(conf < 50):
#                 ts = time.time()
#                 date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#                 aa=df.loc[df['Id'] == Id]['Name'].values
#                 tt=str(Id)+"-"+aa
#                 attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
#             else:
#                 Id='Unknown'
#                 tt=str(Id)
#             if(conf > 75):
#                 noOfFile=len(os.listdir("ImagesUnknown"))+1
#                 cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])
#             cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)
#         attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
#         cv2.imshow('im',im)
#         # Nhấn Nút Q để thoát quá trình kiểm tra
#         if (cv2.waitKey(1)==ord('q')):
#             break
#     ts = time.time()
#     date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#     timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#     Hour,Minute,Second=timeStamp.split(":")
#     fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
#     attendance.to_csv(fileName,index=False)
#     cam.release()
#     cv2.destroyAllWindows()
#     #print(attendance)
#     res=attendance
#     message2.configure(text= res)


takeImg = Button(window, text="Thêm ảnh sinh viên \n (nhấn q để dừng thêm) ", command=TakeImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=200, y=500)
trainImg = Button(window, text="Học ảnh \n (nhấn q để dừng học) ", command=TrainImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=500, y=500)
trackImg = Button(window, text="Kiểm tra sinh viên \n (nhấn q để dừng học) ",fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trackImg.place(x=800, y=500)
quitWindow = Button(window, text="Thoát ", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)
window.mainloop()