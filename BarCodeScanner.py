import tkinter
import base64
import webbrowser
import pyzbar.pyzbar as pyzbar
from PIL import ImageGrab, Image, ImageEnhance

def handlerAdaptor(fun, **kwds):
    '''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)

def scanBarcode(event, scanType):
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
        data = barcode.data.decode("utf-8")
        dataStr = (base64.b64decode(data)).decode()
        barcodeData.append(dataStr)
        url = 'https://cs.spon.com.cn/pdf/instruction/' + dataStr + scanType + '.pdf'
        webbrowser.open(url, new=0)
    #print(barcodeData)

        
MainForm = tkinter.Tk()
MainForm.wm_attributes('-topmost',1)
MainForm.geometry("300x80")
MainForm.title("二维码识别程序")
MainForm.resizable(width = False, height = False)
MainForm['background']='LightSlateGray'
btnScan = tkinter.Button(MainForm, text="用户指南", fg="black", width="15")
btnScan.pack(side="left", pady="5m", padx="5m")
btnScan.bind("<Button-1>", handlerAdaptor(scanBarcode, scanType='用户指南'))

btnScan2 = tkinter.Button(MainForm, text="快速安装手册", fg="black", width="20")
btnScan2.pack(side="left", pady="5m", padx="5m")
btnScan2.bind("<Button-1>", handlerAdaptor(scanBarcode, scanType='快速安装手册'))

MainForm.mainloop()









