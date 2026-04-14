# model.py
import json
import os
from PyQt6.QtCore import QObject, pyqtSignal

class ModelABC(QObject):
    dataChanged = pyqtSignal(int, int, int)
    
    CONFIG_FILE = "config.json"
    MIN_VAL = 0
    MAX_VAL = 100

    def __init__(self):
        super().__init__()
        self._A = 0
        self._B = 50
        self._C = 100
        self.load()

    def getA(self) -> int: return self._A
    def getB(self) -> int: return self._B
    def getC(self) -> int: return self._C

    def setA(self, val):
        """Разрешающее поведение для A"""
        val = max(self.MIN_VAL, min(self.MAX_VAL, val))
        
        new_A = val
        new_B = max(self._B, new_A)
        new_C = max(self._C, new_B)

        if new_A != self._A or new_B != self._B or new_C != self._C:
            self._A, self._B, self._C = new_A, new_B, new_C
            self.save()
            print(f"[Model] setA({val}) -> A={self._A}, B={self._B}, C={self._C}")
            self.dataChanged.emit(self._A, self._B, self._C)

    def setB(self, val):
        """Ограничивающее поведение для B"""
        val = max(self.MIN_VAL, min(self.MAX_VAL, val))
        new_B = max(self._A, min(self._C, val))
        
        if new_B != self._B or val != self._B:
            self._B = new_B
            self.save()
            print(f"[Model] setB({val}) -> B={self._B} (ограничено [{self._A}, {self._C}])")
            self.dataChanged.emit(self._A, self._B, self._C)

    def setC(self, val):
        """Разрешающее поведение для C"""
        val = max(self.MIN_VAL, min(self.MAX_VAL, val))
        
        new_C = val
        new_B = min(self._B, new_C)
        new_A = min(self._A, new_B)

        if new_A != self._A or new_B != self._B or new_C != self._C:
            self._A, self._B, self._C = new_A, new_B, new_C
            self.save()
            print(f"[Model] setC({val}) -> A={self._A}, B={self._B}, C={self._C}")
            self.dataChanged.emit(self._A, self._B, self._C)

    def save(self):
        try:
            with open(self.CONFIG_FILE, "w") as f:
                json.dump({"A": self._A, "B": self._B, "C": self._C}, f)
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

    def load(self):
        if os.path.exists(self.CONFIG_FILE):
            try:
                with open(self.CONFIG_FILE, "r") as f:
                    data = json.load(f)
                self.setA(data.get("A", 0))
                self.setB(data.get("B", 0))
                self.setC(data.get("C", 0))
            except Exception as e:
                print(f"Ошибка загрузки: {e}")