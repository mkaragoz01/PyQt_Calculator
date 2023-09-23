import sys
from ui_hes_mak import Ui_MainWindow
from random import choice
from PyQt5 import QtWidgets

class Window(QtWidgets.QMainWindow):
    
    ilksayi = None
    ikincisayi = False
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton_1.clicked.connect(self.frakam_basma)
        self.ui.pushButton_2.clicked.connect(self.frakam_basma)
        self.ui.pushButton_3.clicked.connect(self.frakam_basma)
        self.ui.pushButton_4.clicked.connect(self.frakam_basma)
        self.ui.pushButton_5.clicked.connect(self.frakam_basma)
        self.ui.pushButton_6.clicked.connect(self.frakam_basma)
        self.ui.pushButton_7.clicked.connect(self.frakam_basma)
        self.ui.pushButton_8.clicked.connect(self.frakam_basma)
        self.ui.pushButton_9.clicked.connect(self.frakam_basma)
        self.ui.pushButton_0.clicked.connect(self.frakam_basma)
        
        self.ui.pushButton_nokta.clicked.connect(self.fondalik)
        
        self.ui.pushButton_degis.clicked.connect(self.fisaret_yuzde)
        self.ui.pushButton_yuzde.clicked.connect(self.fisaret_yuzde)
        
        self.ui.pushButton_art.clicked.connect(self.faritmetik)
        self.ui.pushButton_eksi.clicked.connect(self.faritmetik)
        self.ui.pushButton_carp.clicked.connect(self.faritmetik)
        self.ui.pushButton_bolme.clicked.connect(self.faritmetik)
        
        self.ui.pushButton_art.setCheckable(True) # Aynı butona tekrar tekrar tıklamasını engellemek için!!!
        self.ui.pushButton_eksi.setCheckable(True)
        self.ui.pushButton_carp.setCheckable(True)
        self.ui.pushButton_bolme.setCheckable(True)
        
        self.ui.pushButton_esittir.clicked.connect(self.fsonuc)
        self.ui.pushButton_esittir.setCheckable(True)
        
        self.ui.pushButton_C.clicked.connect(self.fsil)

    def frakam_basma(self):
        buton = self.sender() # Bastığın butonun üstündeki text bilgisini almaya yarıyor!!!
        
        if ((self.ikincisayi)and(self.ui.pushButton_esittir.isChecked())):
            self.ui.label.setText(format(float(buton.text()) ,'.15g'))
            self.ikincisayi = True
            self.ui.pushButton_esittir.setChecked(False)
        elif ((self.ui.pushButton_art.isChecked() or self.ui.pushButton_eksi.isChecked() or self.ui.pushButton_carp.isChecked() or self.ui.pushButton_bolme.isChecked())and (not self.ikincisayi)):
            self.ui.label.setText(format(float(buton.text()) ,'.15g')) # str değerleri sayıya çevirip baştaki sıfırı atmaya yarar.
            self.ikincisayi = True
        else: # if bloğu tuş kontrolü için
            if(('.'in self.ui.label.text()) and buton.text() =="0"):
                self.ui.label.setText(format(float(self.ui.label.text() + buton.text()),'.15'))
            else:
                self.ui.label.setText(format(float(self.ui.label.text()+buton.text()) ,'.15g'))
            
        
    def fondalik(self):
        if '.' not in self.ui.label.text():
            self.ui.label.setText(self.ui.label.text()+".")
            

    def fisaret_yuzde(self):
        buton = self.sender()
        deger = float(self.ui.label.text())
        if buton.text() == "+/-":
            deger = deger * (-1)
        else:
            deger = deger * (0.01)
        self.ui.label.setText(str(format(float(deger) ,'.15g')))
        
    def faritmetik(self):
        buton = self.sender()
        self.ilksayi = float(self.ui.label.text())
        buton.setChecked(True)
        
        
    def fsonuc(self):
        try:
        
            ikincideger= float(self.ui.label.text())
            if self.ui.pushButton_art.isChecked():
                yenideger = self.ilksayi + ikincideger
                
                self.ui.label.setText(format(yenideger, '.15g'))
                self.ui.pushButton_art.setChecked(False)
            elif self.ui.pushButton_eksi.isChecked():
                yenideger = self.ilksayi - ikincideger
                
                self.ui.label.setText(format(yenideger, '.15g'))
                self.ui.pushButton_eksi.setChecked(False)
            elif self.ui.pushButton_carp.isChecked():
                yenideger = self.ilksayi * ikincideger
                
                self.ui.label.setText(format(yenideger, '.15g'))
                self.ui.pushButton_carp.setChecked(False)
            elif self.ui.pushButton_bolme.isChecked():
                yenideger = self.ilksayi / ikincideger
                
                self.ui.label.setText(format(yenideger, '.15g'))
                self.ui.pushButton_bolme.setChecked(False)
            
            self.ilksayi = yenideger
            self.ui.pushButton_esittir.setChecked(True)
        except:
            self.fsil()

    def fsil(self):
        self.ui.label.setText('0')
        self.ilksayi = 0
        self.ikincisayi = False
        self.ui.pushButton_art.setChecked(False)
        self.ui.pushButton_eksi.setChecked(False)
        self.ui.pushButton_carp.setChecked(False)
        self.ui.pushButton_bolme.setChecked(False)
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()