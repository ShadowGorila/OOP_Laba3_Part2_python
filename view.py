# view.py
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QGroupBox, 
    QSlider, QSpinBox, QLineEdit, QFormLayout
)
from PyQt6.QtCore import Qt
from model import ModelABC
from ui import Ui_Form

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, model: ModelABC):
        super().__init__()
        self.model = model
        self.setupUi(self)
        self.setWindowTitle("Lab 3 Part 2: MVC (A ≤ B ≤ C)")
        self.setMinimumWidth(500)
        
        self.model.dataChanged.connect(self.updateForm)
    
        self.lineEditA.editingFinished.connect(self.updateA)
        self.spinBoxA.editingFinished.connect(self.updateA)
        self.horizontalSliderA.valueChanged.connect(self.updateA)

        self.lineEditB.editingFinished.connect(self.updateB)
        self.spinBoxB.editingFinished.connect(self.updateB)
        self.horizontalSliderB.valueChanged.connect(self.updateB)

        self.lineEditC.editingFinished.connect(self.updateC)
        self.spinBoxC.editingFinished.connect(self.updateC)
        self.horizontalSliderC.valueChanged.connect(self.updateC)    
    
    def updateA(self):
        sender = self.sender()
        if sender is self.lineEditA:
            text = ''.join([d for d in self.lineEditA.text() if d.isdigit()])
            new_a = int(text) if text else 0
        elif sender is self.spinBoxA:
            new_a = int(self.spinBoxA.value())
        else:
            new_a = int(self.horizontalSliderA.value())
        self.model.setA(new_a)
    
    def updateB(self):
        sender = self.sender()
        if sender is self.lineEditB:
            text = ''.join([d for d in self.lineEditB.text() if d.isdigit()])
            new_b = int(text) if text else 0
        elif sender is self.spinBoxB:
            new_b = int(self.spinBoxB.value())
        else:
            new_b = int(self.horizontalSliderB.value())
        self.model.setB(new_b)
    
    def updateC(self):
        sender = self.sender()
        if sender is self.lineEditC:
            text = ''.join([d for d in self.lineEditC.text() if d.isdigit()])
            new_c = int(text) if text else 0
        elif sender is self.spinBoxC:
            new_c = int(self.spinBoxC.value())
        else:
            new_c = int(self.horizontalSliderC.value())
        self.model.setC(new_c)
    
    def updateForm(self):
        a = self.model.getA()
        self.lineEditA.setText(str(a))
        self.spinBoxA.setValue(a)
        self.horizontalSliderA.setValue(a)
        
        b = self.model.getB()
        self.lineEditB.setText(str(b))
        self.spinBoxB.setValue(b)
        self.horizontalSliderB.setValue(b)
        
        
        c = self.model.getC()
        self.lineEditC.setText(str(c))  
        self.spinBoxC.setValue(c)
        self.horizontalSliderC.setValue(c)
    
    def __init__(self, model: ModelABC):
        super().__init__()
        self.model = model
        self.setupUi(self)
        self.setWindowTitle("Lab 3 Part 2: MVC (A ≤ B ≤ C)")
        self.setMinimumWidth(500)
        
        self.model.dataChanged.connect(self.updateForm)
        self.lineEditA.editingFinished.connect(self.updateA)
        self.spinBoxA.editingFinished.connect(self.updateA)
        self.horizontalSliderA.valueChanged.connect(self.updateA) 
        
        self.lineEditB.editingFinished.connect(self.updateB)
        self.spinBoxB.editingFinished.connect(self.updateB) 
        self.horizontalSliderB.valueChanged.connect(self.updateB)   
        
        self.lineEditC.editingFinished.connect(self.updateC)
        self.spinBoxC.editingFinished.connect(self.updateC) 
        self.horizontalSliderC.valueChanged.connect(self.updateC)
        
        self.updateForm()
        
    