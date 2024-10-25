from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage


class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x700+200+50")
        self.root.title("STUDENT MANAGEMENT SYSTEM IN QR")
        self.root.resizable(False,False)

        title=Label(self.root,text="STUDENT INFORMATION",font=("goudy old style",25),bg="#043246",fg='white').place(x=0,y=0,relwidth=1)

        #==============student detials entry window============
        #===========variables==============
        self.var_1=StringVar()
        self.var_2=StringVar()
        self.var_3=StringVar()
        self.var_4=StringVar()
        self.var_5=StringVar()
        self.var_6=StringVar()
        self.var_7=StringVar()
        self.var_8=StringVar()
        self.var_9=StringVar()
        self.var_10=StringVar()
        self.var_11=StringVar()
        self.var_12=StringVar()
        self.var_13=StringVar()
        self.var_14=StringVar()
        self.var_15=StringVar()
        self.var_16=StringVar()
        self.var_17=StringVar()
        self.var_18=StringVar()
        self.var_19=StringVar()
        self.var_20=StringVar()
        self.var_21=StringVar()
        self.var_22=StringVar()
        self.var_23=StringVar() 
       # self.var_24=StringVar()
        #self.root_25=Stringvar()
        #self.root_26=Strinvar()

        #=======================secondary frame========================

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=12.5,y=55,width=900,height=630)

        #================insaid title==============================

        emp_title=Label(emp_Frame,text="STUDENT INFORMATION FILLING PAGE",font=("goudy old style",20),bg="#3f51b5",fg='white').place(x=0,y=0,relwidth=1)
#===================================================Entry windows label and entrys==========================================================

#=========================================label=====================================
        lbl_1=Label(emp_Frame,text="BATCH",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_2=Label(emp_Frame,text="ROLL NO",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_3=Label(emp_Frame,text="NAME",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_4=Label(emp_Frame,text="DATE OF BIRTH",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        lbl_5=Label(emp_Frame,text="GENDER",font=("times new roman",15,'bold'),bg='white').place(x=20,y=220)
        lbl_6=Label(emp_Frame,text="BLOOD GROUP",font=("times new roman",15,'bold'),bg='white').place(x=20,y=260)
        lbl_7=Label(emp_Frame,text="WEIGHT(KG's)",font=("times new roman",15,'bold'),bg='white').place(x=20,y=300)
        lbl_8=Label(emp_Frame,text="HEIGHT(CM)",font=("times new roman",15,'bold'),bg='white').place(x=20,y=340)
        lbl_9=Label(emp_Frame,text="IDENTIFICATION\nMARK",font=("times new roman",15,'bold'),bg='white').place(x=20,y=380)
        lbl_10=Label(emp_Frame,text="NATIONALITY",font=("times new roman",15,'bold'),bg='white').place(x=20,y=430)
        lbl_11=Label(emp_Frame,text="RELIGION",font=("times new roman",15,'bold'),bg='white').place(x=20,y=465)
        lbl_12=Label(emp_Frame,text="COMMUNITY",font=("times new roman",15,'bold'),bg='white').place(x=20,y=505)
        lbl_13=Label(emp_Frame,text="FATHER NAME",font=("times new roman",16,'bold'),bg='white').place(x=430,y=60)
        lbl_14=Label(emp_Frame,text="MOTHER NAME",font=("times new roman",16,'bold'),bg='white').place(x=430,y=100)
        lbl_15=Label(emp_Frame,text="FATHER'S\nOCCUPATION",font=("times new roman",15,'bold'),bg='white').place(x=430,y=130)
        lbl_16=Label(emp_Frame,text="ANNUAL INCOME",font=("times new roman",14,'bold'),bg='white').place(x=430,y=185)
        lbl_17=Label(emp_Frame,text="10TH MARK",font=("times new roman",14,'bold'),bg='white').place(x=430,y=225)
        lbl_18=Label(emp_Frame,text="12TH MARK",font=("times new roman",15,'bold'),bg='white').place(x=430,y=265)
        lbl_19=Label(emp_Frame,text="LANGUAGE KNOWN",font=("times new roman",15,'bold'),bg='white').place(x=430,y=305)
        lbl_20=Label(emp_Frame,text="DEPARTMENT",font=("times new roman",15,'bold'),bg='white').place(x=430,y=345)
        lbl_21=Label(emp_Frame,text="ADDRESS",font=("times new roman",15,'bold'),bg='white').place(x=430,y=385)
        lbl_22=Label(emp_Frame,text="PHONE NUMBER",font=("times new roman",15,'bold'),bg='white').place(x=430,y=425)
        lbl_23=Label(emp_Frame,text="WHATSAPP NUMBER",font=("times new roman",14,'bold'),bg='white').place(x=430,y=465)

        #==================================data entry box=================================

        txt_1=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_1,bg='lightyellow').place(x=210,y=60)
        txt_2=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_2,bg='lightyellow').place(x=210,y=100)
        txt_3=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_3,bg='lightyellow').place(x=210,y=140)
        txt_4=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_4,bg='lightyellow').place(x=210,y=180)
        txt_5=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_5,bg='lightyellow').place(x=210,y=220)
        txt_6=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_6,bg='lightyellow').place(x=210,y=260)
        txt_7=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_7,bg='lightyellow').place(x=210,y=300)
        txt_8=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_8,bg='lightyellow').place(x=210,y=340)
        txt_9=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_9,bg='lightyellow').place(x=210,y=385)
        txt_10=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_10,bg='lightyellow').place(x=210,y=430)
        txt_11=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_11,bg='lightyellow').place(x=210,y=467)
        txt_12=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_12,bg='lightyellow').place(x=210,y=505)
        txt_13=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_13,bg='lightyellow').place(x=640,y=60)
        txt_14=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_14,bg='lightyellow').place(x=640,y=100)
        txt_15=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_15,bg='lightyellow').place(x=640,y=140)
        txt_16=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_16,bg='lightyellow').place(x=640,y=185)
        txt_17=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_17,bg='lightyellow').place(x=640,y=225)
        txt_18=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_18,bg='lightyellow').place(x=640,y=265)
        txt_19=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_19,bg='lightyellow').place(x=640,y=305)
        txt_20=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_20,bg='lightyellow').place(x=640,y=345)
        txt_21=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_21,bg='lightyellow').place(x=640,y=385)
        txt_22=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_22,bg='lightyellow').place(x=640,y=425)
        txt_23=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_23,bg='lightyellow').place(x=640,y=465)


        #==========To Create button============
        
        btn_generate=Button(emp_Frame,text='CONVERT_QR',command=self.generate,font=("times new roman",18,'bold'),bg='#00FF00',fg='white').place(x=545,y=580,width=200,height=40)        
        btn_clear=Button(emp_Frame,text='CLEAR',command=self.clear,font=("times new roman",18,'bold'),bg='red',fg='white').place(x=755,y=580,width=120,height=40)

        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",18),bg='white',fg='green')
        self.lbl_msg.place(x=12.5,y=580,width=535,height=30)
       

        #========student qr_code check window==================
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=920,y=55,width=270,height=630)

        emp_title=Label(qr_Frame,text="CHECK YOUR QR HERE",font=("goudy old style",15),bg="#3f51b5",fg='white').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text='NO QR\n\n AVAILABLE',font=('times new roman',15),bg='#3f51b5',fg='white',relief=RIDGE)
        self.qr_code.place(x=20,y=60,width=220,height=220)

        #================================================================>
      #  btn_check=Button(qr_Frame,text='Check_QR',command=self.check,font=("times new roman",18,'bold'),bg='blue',fg='white').place(x=20,y=580,width=150,height=30)

        #====================D.DETIALS==============
        self.qr_code_1=Label(qr_Frame,text='DEVALOPED BY:',font=('times new roman',15),bg='#F5F5F5',fg='black',relief=RIDGE)
        self.qr_code_1.place(x=20,y=350,width=220,height=30)    
        self.qr_code_1=Label(qr_Frame,text='Swathi & Team',font=('times new roman',18),bg='#F5F5F5',fg='black',relief=RIDGE)
        self.qr_code_1.place(x=10,y=400,width=240,height=30)

        self.msg1=''
        self.lbl_msg1=Label(qr_Frame,text=self.msg1,font=("times new roman",18),bg='white',fg='green')
        self.lbl_msg1.place(x=20,y=300,width=220,height=30)


#commands==========================    
    def clear(self):
        self.var_1.set('')
        self.var_2.set('')
        self.var_3.set('')
        self.var_4.set('')
        self.var_5.set('')
        self.var_6.set('')
        self.var_7.set('')
        self.var_8.set('')
        self.var_9.set('')
        self.var_10.set('')
        self.var_11.set('')
        self.var_12.set('')
        self.var_13.set('')
        self.var_14.set('')
        self.var_15.set('')
        self.var_16.set('')
        self.var_17.set('')
        self.var_18.set('')
        self.var_19.set('')
        self.var_20.set('')
        self.var_21.set('')
        self.var_22.set('')
        self.var_23.set('')
       #self.var_24.set('')
       #self.var_25.set('')
       #self.var_26.set('')    
        
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.msg1=''
        self.lbl_msg1.config(text=self.msg)
        self.qr_code.config(image='')
            #=================================qr generate button commands=================================================
            #========================True or false statement=============================
    def generate(self):
        if self.var_1.get()=="" or self.var_2.get()=="" or self.var_3.get()==""  or self.var_4.get()=="" or self.var_5.get()=="" or self.var_6.get()=="" or self.var_7.get()=="" or self.var_8.get()=="" or self.var_9.get()=="" or self.var_10.get()=="" or self.var_11.get()=="" or self.var_12.get()=="" or self.var_13.get()=="" or self.var_14.get()=="" or self.var_15.get()=="" or self.var_16.get()=="" or self.var_17.get()=="" or self.var_18.get()=="" or self.var_19.get()=="" or self.var_20.get()=="" or self.var_21.get()=="" or self.var_22.get()=="" or self.var_23.get()=="":
       # if self.var_1.get()=="" or self.var_2.get()=="" :
             
            self.msg='All Fileds are required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
            self.lbl_msg.place(y=580)
            
            
            

            #======================importing data in qr====================

        else:
            qr_data=(f" BATCH :{self.var_1.get()}\n ROLL NO :{self.var_2.get()}\n NAME :{self.var_3.get()}\n DATE OF BIRTH :{self.var_4.get()}\n GENDER :{self.var_5.get()}\n BLOOD GROUP :{self.var_6.get()}\n WEIGHT(KGs):{self.var_7.get()}\n HEIGHT(CM) :{self.var_8.get()}\n IDENTIFICATION MARK :{self.var_9.get()}\n NATIONALITY :{self.var_10.get()}\n RELIGION :{self.var_11.get()}\n COMMUNITY :{self.var_12.get()}\n FATHER NAME :{self.var_13.get()}\n MOTHER NAME :{self.var_14.get()}\n FATHER'S OCCUPATION :{self.var_15.get()}\n ANNUAL INCOME :{self.var_16.get()}\n 10TH MARK :{self.var_17.get()}\n 12TH MARK :{self.var_18.get()}\n LANGUAGE KNOWN :{self.var_19.get()}\n DEPARTMENT :{self.var_20.get()}\n ADDRESS :{self.var_21.get()}\n PHONE NUMBER :{self.var_22.get()}\n WHATSAPP NUMBER :{self.var_23.get()}\n\n\t\t<<<=========================================>>>")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[220,220])
            qr_code.save(str(self.var_2.get()+'.png'))
            #==========qr code image update============
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            #==========updating Notificaton============
            self.msg="QR Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg,fg='green')
            self.lbl_msg.place(y=580)
            #==============================================================
            self.msg1="you have a qr"
            self.lbl_msg1.config(text=self.msg1,fg='green')
            self.lbl_msg1.place(y=300)

            with open(self.var_2.get()+".txt","w") as aj:
                aj.write(qr_data)
#=======================mainloop funtion===========================         
    
root=Tk()
obj=Qr_Generator(root)
root.mainloop()