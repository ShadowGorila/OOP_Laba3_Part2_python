# main.py
import sys
from PyQt6.QtWidgets import QApplication
from model import ModelABC
from view import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Создаём модель (она сама загрузит сохранённые значения)
    model = ModelABC()
    
    # Создаём и показываем окно
    window = MainWindow(model)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()