import tkinter
import webbrowser
import pyzbar.pyzbar as pyzbar
from PIL import ImageGrab, Image, ImageEnhance

def handlerAdaptor(fun, **kwds):
    '''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)

def scanBarcode(event, scanType):
    resStr.set("")
    img = ImageGrab.grab()
    #img = Image.open(im)
    #img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
    #img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
    #img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
    #img = img.convert('L')#灰度化
    #img.show()
    barcodes = pyzbar.decode(img)
    barcodeData = []
    for barcode in barcodes:
        barcodeType = barcode.type
        print(barcodeType)
        data = barcode.data.decode("utf-8")
        barcodeData.append(data)
        if barcodeType == 'QRCODE':
            if scanType == '用户指南':
                url = 'https://cs.spon.com.cn/pdf/instruction/' + data + scanType + '.pdf'
            else:
                url = 'https://cs.spon.com.cn/pdf/installinstruction/' + data + scanType + '.pdf'
            webbrowser.open(url, new=0)
    result = ""
    for item in barcodeData:
        result = result + "\n" + item
    resStr.set(result[1:])
    #print(barcodeData)

        
MainForm = tkinter.Tk()
MainForm.wm_attributes('-topmost',1)
MainForm.geometry("330x140")
MainForm.title("二维码识别程序")
MainForm.resizable(width = False, height = False)
MainForm['background']='#f7f9fa'

btnScan = tkinter.Button(MainForm, text="用户指南", fg="white", width="20", bg="#00d1b2", cursor="hand2")
btnScan.bind("<Button-1>", handlerAdaptor(scanBarcode, scanType='用户指南'))

btnScan2 = tkinter.Button(MainForm, text="快速安装指南", fg="white", width="20", bg="#23d160", cursor="hand2")
btnScan2.bind("<Button-1>", handlerAdaptor(scanBarcode, scanType='快速安装指南'))

label1 = tkinter.Label(MainForm, text="识别结果", width="20", fg="black", height="5")

resStr = tkinter.StringVar()
resStr.set("")
label2 = tkinter.Label(MainForm, textvariable=resStr, width="23", fg="black", height="5")

btnScan.place(x=10, y=10)
btnScan2.place(x=170, y=10)

label1.place(x=10, y=50)
label2.place(x=153, y=50)

MainForm.mainloop()









