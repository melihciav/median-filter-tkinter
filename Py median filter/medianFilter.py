from tempfile import tempdir
from tkinter import *
from random import seed
from random import randint

root = Tk()

width = 450 
height = 450 
 
screen_width = root.winfo_screenwidth()  
screen_height = root.winfo_screenheight() 

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root['bg'] = '#0059b3'
root.title("Median Filter")
root.iconbitmap(r'mellon.ico')
root.resizable(width=FALSE, height=FALSE)
array = []
geciciDizi=[0,0,0]
medianArray=[0,0,0,0,0,0,0,0]
def CreateArray(): #10 elemanlık değerleri çıkartır ve ekrana yazdırır
    array.clear()
    OutputArray.delete('1.0', END)
    for i in range(0,10):
        sayi = randint(10, 100)
        array.append(sayi)
    OutputArray.insert(END,array)
       
def MedianFilter():# girilen değerleri filtreleyerek ekrana yazdırır
    
    medianArray1.delete('1.0', END)
    temp = 0
    n = 0
    
    a=0
    
    for i in range(0,len(array)-2):
        a = i + 1
        b = a + 1 
        
        geciciDizi[0] = array[i]
        geciciDizi[1] = array[a]
        geciciDizi[2] = array[b]
        
        for m in range(0,(len(geciciDizi))):
            j = m
            for j in range(0,len(geciciDizi)):
                if (geciciDizi[m] > geciciDizi[j]):
                    temp = geciciDizi[j]
                    geciciDizi[j] = geciciDizi[m]
                    geciciDizi[m] = temp
        medianArray[n] = geciciDizi[1]
        n = n + 1
        
        
    
    medianArray1.insert(END,medianArray)

Button1 = Button(root, text="Rastgele değerler oluştur",command=CreateArray,bg='#81DAF5')
Button1.place(x=150,y=60)
Button2 = Button(root, text="Değerleri filtrele",command=MedianFilter,bg='#81DAF5')
Button2.place(x=170,y=260)

def clear():# girdi ve filtreleme kutusunu temizler
    OutputArray.delete('1.0', END)
    medianArray1.delete('1.0', END)
    
#root.geometry("450x450")

OutputArray = Text(root, width= 29, height = 1)
OutputArray.place(x=100,y=100)

medianArray1 = Text(root, width= 29, height = 1)
medianArray1.place(x=100,y=300)

clear_button = Button(root, text ='Resetle', command=clear,bg='#FA5858')
clear_button.place(x=380,y=200)

root.mainloop()