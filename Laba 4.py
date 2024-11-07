import sys
import math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
QVBoxLayout, QHBoxLayout, QMessageBox, QTabWidget, QComboBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def calculate_v(x, y, z, f):
try:
func = math.cos
numerator = 1 + math.sin(x + y)**2
denominator = abs(x - (2 * y / (1 + x**2 * y**2)))
term1 = numerator / denominator * x**abs(y)
term2 = func(math.atan(1/z))**2
v = term1 + term2
return f"Результат v: {v:.4f}"
except Exception as e:
return f"Ошибка при расчете v: {e}"

def calculate_c(x, y, f):
try:
if f == 'cos':
func = math.cos
elif f == 'exp':
func = math.exp
elif f == 'sin':
func = math.sin
else:
return "Неверная функция"

if x * y > 12:
c = func(x**3 + 1/math.tan(y))
elif x * y < 7:
c = math.sinh(x**3) + y**2
else:
c = math.cos(x - x**3)
return f"Результат c: {c:.4f}"
except Exception as e:
return f"Ошибка при расчете c: {e}"

class FormulaApp(QWidget):
def __init__(self):
super().__init__()

self.initUI()

def initUI(self):
self.setWindowTitle('Практическая работа №6')
self.setGeometry(100, 100, 500, 500)

self.tabs = QTabWidget()
self.tab1 = QWidget()
self.tab2 = QWidget()

self.tabs.addTab(self.tab1, "Вычисление v")
self.tabs.addTab(self.tab2, "Вычисление c")

self.create_tab1_ui()

self.create_tab2_ui()

main_layout = QVBoxLayout()
main_layout.addWidget(self.tabs)
self.setLayout(main_layout)

def create_tab1_ui(self):
layout = QVBoxLayout()

img1_label = QLabel(self)
img1_pixmap = QPixmap("1.png")  # Путь к первой картинке
img1_label.setPixmap(img1_pixmap.scaled(379, 64))

layout.addWidget(img1_label, alignment=Qt.AlignCenter)

# Поля ввода для X, Y и Z
self.x_input = QLineEdit(self)
self.x_input.setPlaceholderText("Введите значение X")
layout.addWidget(self.x_input)

self.y_input = QLineEdit(self)
self.y_input.setPlaceholderText("Введите значение Y")
layout.addWidget(self.y_input)

self.z_input = QLineEdit(self)
self.z_input.setPlaceholderText("Введите значение Z")
layout.addWidget(self.z_input)

self.v_button = QPushButton('Вычислить v', self)
self.v_button.clicked.connect(self.on_calculate_v)
layout.addWidget(self.v_button)

self.result_label_tab1 = QLabel('Здесь будет выводиться результат', self)
layout.addWidget(self.result_label_tab1)

self.tab1.setLayout(layout)

def create_tab2_ui(self):
layout = QVBoxLayout()

img2_label = QLabel(self)
img2_pixmap = QPixmap("2.png")  # Путь ко второй картинке
img2_label.setPixmap(img2_pixmap.scaled(280, 93))

layout.addWidget(img2_label, alignment=Qt.AlignCenter)

self.x_input_tab2 = QLineEdit(self)
self.x_input_tab2.setPlaceholderText("Введите значение X")
layout.addWidget(self.x_input_tab2)

self.y_input_tab2 = QLineEdit(self)
self.y_input_tab2.setPlaceholderText("Введите значение Y")
layout.addWidget(self.y_input_tab2)

self.f_combo_tab2 = QComboBox(self)
self.f_combo_tab2.addItems(['cos', 'exp', 'sin'])
layout.addWidget(self.f_combo_tab2)

self.c_button = QPushButton('Вычислить c', self)
self.c_button.clicked.connect(self.on_calculate_c)
layout.addWidget(self.c_button)

self.result_label_tab2 = QLabel('Здесь будет выводиться результат', self)
layout.addWidget(self.result_label_tab2)

self.tab2.setLayout(layout)

def get_inputs(self, tab=1):
try:
if tab == 1:
x = float(self.x_input.text())
y = float(self.y_input.text())
z = float(self.z_input.text())
f = self.f_combo_tab1.currentText()
else:
x = float(self.x_input_tab2.text())
y = float(self.y_input_tab2.text())
z = 0  # Вкладка 2 не использует z
f = self.f_combo_tab2.currentText()
return x, y, z, f
except ValueError:
QMessageBox.warning(self, 'Ошибка', 'Введите корректные числовые значения!')
return None, None, None, None

def on_calculate_v(self):
x, y, z, f = self.get_inputs(tab=1)
if x is not None and y is not None and z is not None:
result = calculate_v(x, y, z, f)
self.result_label_tab1.setText(result)

def on_calculate_c(self):
x, y, _, f = self.get_inputs(tab=2)
if x is not None and y is not None:
result = calculate_c(x, y, f)
self.result_label_tab2.setText(result)

if __name__ == '__main__':
app = QApplication(sys.argv)
ex = FormulaApp()
ex.show()
sys.exit(app.exec_())