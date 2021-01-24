from tkinter import *
from matrix_functions import *
from tkinter import messagebox
root=Tk()
root.configure(bg="black")
root.geometry('700x580')
root.title('Matrix and Determinant')
root.iconbitmap('logo.ico')
main_frame=Frame(root,height=700, width=580,bg='BLACK')
result_frame=Frame(root,bg='black')
right_frame=Frame(root,bg='BLACK')
middle_frame=Frame(root,bg='BLACK')
left_frame=Frame(root,bg='black')
matrix_frame=Frame(left_frame,bg='BLACK')
determinant_frame=Frame(left_frame,bg='black')

#MATRIX

################################################################################################################################################

#INPUT MATRIX

def input_row_column():
    global row,col
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=4,column=8,columnspan=3)
    Label(middle_frame,text="Enter number of columns",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=5,column=8,columnspan=3)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=12)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=12)
    Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=input_grid).grid(row=6,column=10,columnspan=3)
    middle_frame.grid(row=5,rowspan=4,column=2,columnspan=4,padx=200,pady=50)


def input_grid():
    global right_frame
    middle_frame.grid_forget()
    right_frame.destroy()
    right_frame=Frame(root,bg='BLACK')
    r=row.get()
    c=col.get()
    global dic
    temp=[]
    dic=[]
    for i in range (r):
        for j in range (c):
            temp.append(IntVar())
        dic.append(temp)
        temp=[]
    Label(right_frame, text="INPUT MATRIX", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=3,padx=10,pady=10)
    for i in range(1,r+1):
        for j in range (1,c+1):            
            ent=Entry(right_frame, width=4,textvariable=dic[i-1][j-1])
            ent.grid(row=i,column=j)

    Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=input_cmd).grid(row=4,column=1,columnspan=3,pady=10)

    right_frame.grid(row=5,rowspan=100,column=50,columnspan=4,padx=200,pady=50)



def input_cmd():
    global mainmatrix
    mainmatrix=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        mainmatrix.append(temp)
        temp=[]
    return mainmatrix


################################################################################################################################################
def frame_destroy():

    global middle_frame
    middle_frame.destroy()
    middle_frame=Frame(root,bg='BLACK')

    global right_frame
    right_frame.destroy()
    right_frame=Frame(root,bg='BLACK')

    global result_frame
    result_frame.destroy()
    result_frame=Frame(root,bg='BLACK')

################################################################################################################################################

#ADDITION

def addition_input_row_column():

    frame_destroy()
    global row1,col1
    Label(middle_frame,text="Enter number of rows of first matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=4,column=8,columnspan=5)
    Label(middle_frame,text="Enter number of columns of first matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=5,column=8,columnspan=5)
    row1=IntVar()
    Entry(middle_frame,width=4,textvariable=row1, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=14)
    col1=IntVar()
    Entry(middle_frame,width=4,textvariable=col1, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=14)

    global row2,col2
    Label(middle_frame,text="Enter number of rows of second matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=8,column=8,columnspan=5)
    Label(middle_frame,text="Enter number of columns of second matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=9,column=8,columnspan=5)
    row2=IntVar()
    Entry(middle_frame,width=4,textvariable=row2, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=8,column=14)
    col2=IntVar()
    Entry(middle_frame,width=4,textvariable=col2, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=9,column=14)

    Label(middle_frame, text="""
""", bg="black").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    Submit_btn=Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=addition_input_grid)
    Submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(row=5,rowspan=10,column=2,columnspan=4,padx=200,pady=50)


def addition_input_grid():

    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()

    if r1==r2 and c1==c2 and r1!=0 and r2!=0 and c1!=0 and c2!=0:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        
        global dic1
        temp=[]
        dic1=[]
        for i in range (r1):
            for j in range (c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp=[]
        Label(right_frame, text="   INPUT MATRIX 1", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c1+c2,padx=10,pady=10)
        for i in range(1,r1+1):
            for j in range (1,c1+1):            
                ent=Entry(right_frame, width=4,textvariable=dic1[i-1][j-1])
                ent.grid(row=i,column=j+2,padx=5,pady=5)

        global dic2
        temp=[]
        dic2=[]
        for i in range (r2):
            for j in range (c2):
                temp.append(IntVar())
            dic2.append(temp)
            temp=[]
        Label(right_frame, text="   INPUT MATRIX 2", fg="white", bg="black",font=('ariel', 15)).grid(row=r1+1,column=1,columnspan=c1+c2,padx=10,pady=10)
        for i in range(1,r2+1):
            for j in range (1,c2+1):            
                ent=Entry(right_frame, width=4,textvariable=dic2[i-1][j-1])
                ent.grid(row=i+r1+2,column=j+2,padx=5,pady=5)

        Button(right_frame,text='Submit',font=('ariel', 15),bg="black", fg="white", width=5,command=addition_input_cmd).grid(row=r1+r2+4,column=2,columnspan=c1+c2,pady=10)
        right_frame.grid(row=5,rowspan=100,column=50,columnspan=40)

    elif r1==0 or r2==0 or c1==0 or c2==0:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")
    else:
        messagebox.showerror("Input Error","Number of rows and columns should be equal.")


def addition_input_cmd():
    
    global addm1
    addm1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        addm1.append(temp)
        temp=[]

    global addm2
    addm2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        addm2.append(temp)
        temp=[]

    addition_result=addition_of_matrix(addm1,addm2)
    Label(result_frame, text='RESULT',fg="white", bg="black",font=('Ariel',15)).grid(row=0,column=0,columnspan=len(addition_result[0]))
    for i in range (len(addition_result)):
        for j in range (len(addition_result[0])):
            Label(result_frame,text=addition_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
          


################################################################################################################################################

################################################################################################################################################
#SUBTRACTION

def subtraction_input_row_column():

    frame_destroy()

    global row1,col1
    Label(middle_frame,text="Enter number of rows of first matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=4,column=8,columnspan=5)
    Label(middle_frame,text="Enter number of columns of first matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=5,column=8,columnspan=5)
    row1=IntVar()
    Entry(middle_frame,width=4,textvariable=row1, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=14)
    col1=IntVar()
    Entry(middle_frame,width=4,textvariable=col1, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=14)

    global row2,col2
    Label(middle_frame,text="Enter number of rows of second matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=8,column=8,columnspan=5)
    Label(middle_frame,text="Enter number of columns of second matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=9,column=8,columnspan=5)
    row2=IntVar()
    Entry(middle_frame,width=4,textvariable=row2, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=8,column=14)
    col2=IntVar()
    Entry(middle_frame,width=4,textvariable=col2, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=9,column=14)

    Label(middle_frame, text="""
""", bg="black").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=subtraction_input_grid).grid(row=11,column=14,columnspan=3)
    middle_frame.grid(row=5,rowspan=10,column=2,columnspan=4,padx=200,pady=50)


def subtraction_input_grid():


    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()

    if r1==r2 and c1==c2 and r1!=0 and r2!=0 and c1!=0 and c2!=0:   
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        
        global dic1
        temp=[]
        dic1=[]
        for i in range (r1):
            for j in range (c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp=[]
        Label(right_frame, text="   INPUT MATRIX 1", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c1+c2,padx=10,pady=10)
        for i in range(1,r1+1):
            for j in range (1,c1+1):            
                ent=Entry(right_frame, width=4,textvariable=dic1[i-1][j-1])
                ent.grid(row=i,column=j+2,padx=5,pady=5)

        global dic2
        temp=[]
        dic2=[]
        for i in range (r2):
            for j in range (c2):
                temp.append(IntVar())
            dic2.append(temp)
            temp=[]
        Label(right_frame, text="   INPUT MATRIX 2", fg="white", bg="black",font=('ariel', 15)).grid(row=r1+1,column=1,columnspan=c1+c2,padx=10,pady=10)
        for i in range(1,r2+1):
            for j in range (1,c2+1):            
                ent=Entry(right_frame, width=4,textvariable=dic2[i-1][j-1])
                ent.grid(row=i+r1+2,column=j+2,padx=5,pady=5)

        Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=subtraction_input_cmd).grid(row=r1+r2+4,column=2,columnspan=c1+c2,pady=10)
        right_frame.grid(row=5,rowspan=100,column=50,columnspan=40)

    elif r1==0 or r2==0 or c1==0 or c2==0:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")

    else:
        messagebox.showerror("Input Error","Number of rows and columns should be equal.")


def subtraction_input_cmd():
    
    global subm1
    subm1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        subm1.append(temp)
        temp=[]

    global subm2
    subm2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        subm2.append(temp)
        temp=[]

    subtraction_result=subtraction_of_matrix(subm1,subm2)
    Label(result_frame, text='RESULT',bg="black", fg="white",font=('Ariel',15)).grid(row=0,column=0,columnspan=len(subtraction_result[0]))
    for i in range (len(subtraction_result)):
        for j in range (len(subtraction_result[0])):
            Label(result_frame,text=subtraction_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
          

          


################################################################################################################################################
#PRODUCT 

def product_input_row_column():

    frame_destroy()

    global row1,col1
    Label(middle_frame,text="Enter number of rows of first matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=4,column=8,columnspan=5)
    Label(middle_frame,text="Enter number of columns of first matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=5,column=8,columnspan=5)
    row1=IntVar()
    Entry(middle_frame,width=4,textvariable=row1, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=14)
    col1=IntVar()
    Entry(middle_frame,width=4,textvariable=col1, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=14)

    global row2,col2
    Label(middle_frame,text="Enter number of rows of second matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=8,column=8,columnspan=5)
    Label(middle_frame,text="Enter number of columns of second matrix",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=35).grid(row=9,column=8,columnspan=5)
    row2=IntVar()
    Entry(middle_frame,width=4,textvariable=row2, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=8,column=14)
    col2=IntVar()
    Entry(middle_frame,width=4,textvariable=col2, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=9,column=14)

    Label(middle_frame, text="""
""", bg="black").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=product_input_grid).grid(row=11,column=14,columnspan=3)
    middle_frame.grid(row=5,rowspan=10,column=2,columnspan=4,padx=200,pady=50)


def product_input_grid():

    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()
    
    if c1==r2 and r1!=0 and r2!=0 and c1!=0 and c2!=0:  
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        
        global dic1
        temp=[]
        dic1=[]
        for i in range (r1):
            for j in range (c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp=[]
        Label(right_frame, text="   INPUT MATRIX 1", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c1+c2,padx=10,pady=10)
        for i in range(1,r1+1):
            for j in range (1,c1+1):            
                ent=Entry(right_frame, width=4,textvariable=dic1[i-1][j-1])
                ent.grid(row=i,column=j+2,padx=5,pady=5)

        global dic2
        temp=[]
        dic2=[]
        for i in range (r2):
            for j in range (c2):
                temp.append(IntVar())
            dic2.append(temp)
            temp=[]
        Label(right_frame, text="   INPUT MATRIX 2", fg="white", bg="black",font=('ariel', 15)).grid(row=r1+1,column=1,columnspan=c1+c2,padx=10,pady=10)
        for i in range(1,r2+1):
            for j in range (1,c2+1):            
                ent=Entry(right_frame, width=4,textvariable=dic2[i-1][j-1])
                ent.grid(row=i+r1+2,column=j+2,padx=5,pady=5)

        Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=product_input_cmd).grid(row=r1+r2+4,column=2,columnspan=c1+c2,padx=20,pady=10)
        right_frame.grid(row=5,rowspan=100,column=50,columnspan=40)

    elif r1==0 or r2==0 or c1==0 or c2==0:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")
    else:
        messagebox.showerror("Input Error","Number of columns of first matrix \n should be equal to number \n of rows of second matrix.")


def product_input_cmd():
    
    global pdm1
    pdm1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        pdm1.append(temp)
        temp=[]

    global pdm2
    pdm2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        pdm2.append(temp)
        temp=[]

    product_result=product_of_matrix(pdm1,pdm2)
    Label(result_frame, text='RESULT',bg="black", fg="white",font=('Ariel',15)).grid(row=0,column=0,columnspan=len(product_result[0]))
    for i in range (len(product_result)):
        for j in range (len(product_result[0])):
            Label(result_frame,text=product_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
          

          


################################################################################################################################################


#ADJOINT OF MATRIX
          

def adjoint_input_row_column():

    frame_destroy()

    global row,col
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=4,column=8,columnspan=3)
    Label(middle_frame,text="Enter number of columns",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=5,column=8,columnspan=3)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=12)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=12)
    Submit_btn=Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=adjoint_input_grid)
    Submit_btn.grid(row=6,column=10,columnspan=3)
    middle_frame.grid(row=5,rowspan=4,column=2,columnspan=4,padx=200,pady=50)


def adjoint_input_grid():
    r=row.get()
    c=col.get()
    
    if r!=0 and c!=0: 
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        
        global dic
        temp=[]
        dic=[]
        for i in range (r):
            for j in range (c):
                temp.append(IntVar())
            dic.append(temp)
            temp=[]
        Label(right_frame, text="INPUT MATRIX", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c,padx=10,pady=10)
        for i in range(1,r+1):
            for j in range (1,c+1):            
                ent=Entry(right_frame, width=4,textvariable=dic[i-1][j-1])
                ent.grid(row=i,column=j,padx=5,pady=5)

        Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=adjoint_input_cmd).grid(row=r+2,column=1,columnspan=c,pady=10)

        right_frame.grid(row=5,rowspan=100,column=50,columnspan=4,padx=20,pady=50)

    else:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")
        


def adjoint_input_cmd():
    global adjointmatrix
    adjointmatrix=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        adjointmatrix.append(temp)
        temp=[]

    adjoint_result=adjoint_matrix(adjointmatrix)
    Label(result_frame, text='RESULT',font=('Ariel',15)).grid(row=0,column=0,columnspan=len(adjoint_result[0]))
    for i in range (len(adjoint_result)):
        for j in range (len(adjoint_result[0])):
            Label(result_frame,text=adjoint_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)


################################################################################################################################################

#INVERSE OF A MATRIX

def inverse_input_row_column():

    frame_destroy()

    global row,col
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=4,column=8,columnspan=3)
    Label(middle_frame,text="Enter number of columns",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=5,column=8,columnspan=3)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=12)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=12)
    Submit_btn=Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=inverse_input_grid)
    Submit_btn.grid(row=6,column=10,columnspan=3)
    middle_frame.grid(row=5,rowspan=4,column=2,columnspan=4,padx=200,pady=50)


def inverse_input_grid():

    r=row.get()
    c=col.get()

    if r==c and r!=0 and c!=0:        
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        
        global dic
        temp=[]
        dic=[]
        for i in range (r):
            for j in range (c):
                temp.append(IntVar())
            dic.append(temp)
            temp=[]
        Label(right_frame, text="INPUT MATRIX", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c,padx=10,pady=10)
        for i in range(1,r+1):
            for j in range (1,c+1):            
                ent=Entry(right_frame, width=4,textvariable=dic[i-1][j-1])
                ent.grid(row=i,column=j,padx=5,pady=5)

        btn=Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=inverse_input_cmd)
        btn.grid(row=r+2,column=c-1,columnspan=c,pady=10)

        right_frame.grid(row=5,rowspan=100,column=50,columnspan=4,padx=20,pady=50,sticky='nsew')

    elif r==0 or c==0:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")

    else:
        messagebox.showerror("Input Error","Number of rows and columns should be equal.")
        


def inverse_input_cmd():
    global inversematrix
    inversematrix=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        inversematrix.append(temp)
        temp=[]

    if main_determinant(inversematrix) !=0:
        inverse_result=inverse_of_matrix(inversematrix)
        Label(result_frame, text='RESULT',font=('Ariel',15)).grid(row=0,column=0,columnspan=len(inverse_result[0]))
        for i in range (len(inverse_result)):
            for j in range (len(inverse_result[0])):
                Label(result_frame,text=inverse_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
        result_frame.grid(row=7,column=300,padx=100)

    else:
        messagebox.showerror("Input Error","Inverse is not possible as \n determinant is Zero.")
        


################################################################################################################################################

#COFACTOR OF MATRIX

def cofactor_input_row_column():

    frame_destroy()

    global row,col
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=4,column=8,columnspan=3)
    Label(middle_frame,text="Enter number of columns",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=5,column=8,columnspan=3)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=12)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=12)
    Submit_btn=Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=cofactor_input_grid)
    Submit_btn.grid(row=6,column=10,columnspan=3)
    middle_frame.grid(row=5,rowspan=4,column=2,columnspan=4,padx=200,pady=50)


def cofactor_input_grid():

    r=row.get()
    c=col.get()

    if r!=0 and c!=0 :
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        global dic
        temp=[]
        dic=[]
        for i in range (r):
            for j in range (c):
                temp.append(IntVar())
            dic.append(temp)
            temp=[]
        Label(right_frame, text="INPUT MATRIX", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c,padx=10,pady=10)
        for i in range(1,r+1):
            for j in range (1,c+1):            
                ent=Entry(right_frame, width=4,textvariable=dic[i-1][j-1])
                ent.grid(row=i,column=j,padx=5,pady=5)

        Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=cofactor_input_cmd).grid(row=r+1,column=c-1,columnspan=c,pady=10)
        right_frame.grid(row=5,rowspan=100,column=50,columnspan=4,padx=20,pady=50)

    else:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")


def cofactor_input_cmd():
    global cofactormatrix
    cofactormatrix=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        cofactormatrix.append(temp)
        temp=[]
    
    cofactor_result=cofactor_matrix(cofactormatrix)
    Label(result_frame, text='RESULT',font=('Ariel',15)).grid(row=0,column=0,columnspan=len(cofactor_result[0]))
    for i in range (len(cofactor_result)):
        for j in range (len(cofactor_result[0])):
            Label(result_frame,text=cofactor_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)

################################################################################################################################################

#DETERMINANT
def determinant_input_row_column():

    frame_destroy()

    global row,col
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=4,column=8,columnspan=3)
    Label(middle_frame,text="Enter number of columns",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=5,column=8,columnspan=3)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=12)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=12)
    Submit_btn=Button(middle_frame,text='Submit',bg="black", fg="white", width=5,command=determinant_input_grid)
    Submit_btn.grid(row=6,column=10,columnspan=3)
    middle_frame.grid(row=15,rowspan=4,column=2,columnspan=4,padx=200,pady=50)


def determinant_input_grid():

    r=row.get()
    c=col.get()
    
    if r==c and r!=0 and c!=0:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        
        global dic
        temp=[]
        dic=[]
        for i in range (r):
            for j in range (c):
                temp.append(IntVar())
            dic.append(temp)
            temp=[]
        Label(right_frame, text="INPUT MATRIX", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c,padx=10,pady=10)
        for i in range(1,r+1):
            for j in range (1,c+1):            
                ent=Entry(right_frame, width=4,textvariable=dic[i-1][j-1])
                ent.grid(row=i,column=j,padx=5,pady=5)

        Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=determinant_input_cmd).grid(row=r+1,column=c-1,columnspan=c,pady=10)

        right_frame.grid(row=5,rowspan=100,column=50,columnspan=4,padx=20,pady=50)

    elif r==0 or c==0:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")

    else:
        #Instead of else the condition should be *elif r!=c
        messagebox.showerror("Input Error","The rows and columns can't be zero.")


def determinant_input_cmd():
    global determinant
    determinantmatrix=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        determinantmatrix.append(temp)
        temp=[]

    determinant_result=main_determinant(determinantmatrix)
    Label(result_frame, text='RESULT',font=('Ariel',15)).grid(row=10,column=0,columnspan=2,rowspan=10)
    Label(result_frame,text=determinant_result,font=('ariel',15)).grid(row=20,column=0,columnspan=1,pady=10)
    result_frame.grid(row=7,column=300,padx=100)
    

################################################################################################################################################

#TRANSPOSE	

def transpose_input_row_column():

    frame_destroy()

    global row,col
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=4,column=8,columnspan=3)
    Label(middle_frame,text="Enter number of columns",bg='black',fg='white', borderwidth=3, relief="groove",font=('ariel', 10),width=21).grid(row=5,column=8,columnspan=3)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=4,column=12)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col, borderwidth=3,bg='gray64',fg='black', relief="solid").grid(row=5,column=12)
    Submit_btn=Button(middle_frame,text='Submit',bg="black", fg="white",width=5,command=transpose_input_grid)
    Submit_btn.grid(row=6,column=10,columnspan=3)
    middle_frame.grid(row=5,rowspan=4,column=2,columnspan=4,padx=200,pady=50)


def transpose_input_grid():

    r=row.get()
    c=col.get()

    if r!=0 and c!=0:
        
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame=Frame(root,bg='BLACK')
        global dic
        temp=[]
        dic=[]
        for i in range (r):
            for j in range (c):
                temp.append(IntVar())
            dic.append(temp)
            temp=[]
        Label(right_frame, text="INPUT MATRIX", fg="white", bg="black",font=('ariel', 15)).grid(row=0,column=1,columnspan=c,padx=10,pady=10,sticky='nsew')
        for i in range(1,r+1):
            for j in range (1,c+1):            
                ent=Entry(right_frame, width=4,textvariable=dic[i-1][j-1])
                ent.grid(row=i,column=j,padx=5,pady=5)

        Button(right_frame,text='Submit',bg="black", fg="white",font=('ariel', 15),width=5,command=transpose_input_cmd).grid(row=r+1,column=c-1,columnspan=c,pady=10)
        right_frame.grid(row=5,rowspan=100,column=50,columnspan=4,padx=20,pady=50)

    else:
        messagebox.showerror("Input Error","The rows and columns can't be zero.")

def transpose_input_cmd():
    global transposematrix
    transposematrix=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        transposematrix.append(temp)
        temp=[]
    transpose_result=transpose(transposematrix)
    Label(result_frame, text='RESULT',font=('Ariel',15)).grid(row=0,column=0,columnspan=len(transpose_result[0]))
    for i in range (len(transpose_result)):
        for j in range (len(transpose_result[0])):
            Label(result_frame,text=transpose_result[i][j],padx=6,pady=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)

################################################################################################################################################

def back_btn():
    back.grid_forget()
    matrix_frame.grid_forget()
    determinant_frame.grid_forget()
    middle_frame.grid_forget()
    right_frame.grid_forget()
    result_frame.grid_forget()
    main_frame.grid()

def matrix_cmd():
    global back
    main_frame.grid_remove()
    lbl=Label(matrix_frame, text='MATRIX',font=('Ariel',20), bg='black', fg='white')
    lbl.grid(row=0,column=0, ipadx=20,ipady=10)
    button1=Button(matrix_frame,text="Addition",bg="black",fg="white",padx=10,pady=10,command=addition_input_row_column)
    button1.grid(row=5,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Subtraction",bg="black",fg="white",padx=10,pady=10,command=subtraction_input_row_column)
    button1.grid(row=6,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Product",bg="black",fg="white",padx=10,pady=10,command=product_input_row_column)
    button1.grid(row=7,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Inverse",bg="black",fg="white",padx=10,pady=10,command=inverse_input_row_column)
    button1.grid(row=8,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Adjoint",bg="black",fg="white",padx=10,pady=10,command=adjoint_input_row_column)
    button1.grid(row=9,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Cofactor",bg="black",fg="white",padx=10,pady=10,command=cofactor_input_row_column)
    button1.grid(row=10,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Transpose",bg="black",fg="white",padx=10,pady=10,command=transpose_input_row_column)
    button1.grid(row=11,column=0,padx=10,pady=10,sticky="nsew")
    back=Button(matrix_frame, bg='black',fg='white',text='Home',padx=10,pady=10, width=10,command=back_btn)
    back.grid(row=12,column=0, padx=10, pady=10, sticky="nsew")
    matrix_frame.grid(row=0,column=0,columnspan=2,rowspan=6,sticky=W)
    
def determinant_cmd():
    global back
    main_frame.grid_remove()
    back=Button(determinant_frame, bg='black',fg='white',text='Home',padx=10,pady=10,command=back_btn)
    back.grid(row=2,column=0, padx=10, pady=10, sticky="nsew")
    lbl=Label(determinant_frame, text='DETERMINANT',font=('Ariel',15), bg='black', fg='white')
    lbl.grid(row=0,column=0, ipadx=20,ipady=20,columnspan=4)
    button1=Button(determinant_frame,text="Value of determinant",bg="black",fg="white",padx=10,pady=10,command=determinant_input_row_column)
    button1.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
    determinant_frame.grid(row=0,column=0,columnspan=2,rowspan=6,sticky=W)
    matrix_frame=Frame(left_frame,bg='BLACK')

def close_main(event=None):
    if messagebox.askokcancel("Quit","Do you really want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW",close_main)

Label(main_frame, text="""
""", bg="black").grid(row=6,columnspan=2,padx=80,pady=2,sticky=EW)
Label(main_frame, text="""




""", bg="black").grid(row=0,columnspan=2,padx=80,pady=2,sticky=EW)
Label(main_frame, text="", bg="black").grid(row=8,columnspan=2,padx=80,pady=2,sticky=EW)
Label(main_frame, text="                            Choose an option to work on",font=('Ariel', 16),bg='black',fg='white').grid(row=5,columnspan=6,sticky=EW)
Button(main_frame, text="Matrix",bg='black',fg='white', font=('Ariel', 18),width=10,command=matrix_cmd).grid(row=7,column=1,columnspan=2,padx=80,pady=2,sticky=EW)
Label(main_frame, text="     ", bg="black").grid(row=7,padx=80,pady=2,sticky=EW)
Button(main_frame, text="Determinant",bg='black',fg='white', font=('Ariel', 18),width=10,command=determinant_cmd).grid(row=9,column=1,columnspan=2,padx=80,pady=2,sticky=EW)
left_frame.grid(row=4,column=0,columnspan=3,rowspan=7,sticky=W)
main_frame.grid(row=0,column=0,rowspan=3,columnspan=3,sticky="nesw")

root.mainloop()
