from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

"""
class Noh:
    def __init__(self):
        self.visitado = False
        self.profundidade = 0
        self.nohPai = ''

    def setVisitado(self, visitado):
        self.visitado = visitado

    def getVisitado(self):
        return self.visitado

    def setProfundidade(self, profundidade):
        self.profundidade = profundidade
        
    def getProfundidade(self):
        return self.profundidade

    def setPai(self, nohPai):
        self.nohPai = nohPai

    def getPai(self):
        return self.nohPai
"""

grafo = [
    
    {
        'noh': 'A',
        'visitado': False,
        'vizinhanca': ['C']
    },
    {
        'noh': 'B',
        'visitado': False,
        'vizinhanca': ['C']
    },
    {
        'noh': 'C',
        'visitado': False,
        'vizinhanca': ['A','B','G','D','H']
    },
    {
        'noh': 'D',
        'visitado': False,
        'vizinhanca': ['F','E','C']
    },
    {
        'noh': 'E',
        'visitado': False,
        'vizinhanca': ['D']
    },
    {
        'noh': 'F',
        'visitado': False,
        'vizinhanca': ['D']
    },
    {
        'noh': 'G',
        'visitado': False,
        'vizinhanca': ['C','H']
    },
    {
        'noh': 'H',
        'visitado': False,
        'vizinhanca': ['C','G','I','J','M','N']
    },
    {
       'noh': 'I',
       'visitado': False,
       'vizinhanca': ['H']
    },
    {
        'noh': 'J',
        'visitado': False,
        'vizinhanca': ['H','K','L']
    },
    {
        'noh': 'K',
        'visitado': False,
        'vizinhanca': ['J']
    },
    {
        'noh': 'L',
        'visitado': False,
        'vizinhanca': ['J']
    },
    {
        'noh': 'M',
        'visitado': False,
        'vizinhanca': ['H']
    },
    {
        'noh': 'N',
        'visitado': False,
        'vizinhanca': ['H']
    }

]

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Trabalho Final de Lógica e Matemática Discreta - Prof. Edgard Lamounier - Chrystian R. Campos - 11721ECP006"
        self.top = 50
        self.left = 100
        self.width = 1200
        self.height = 1200

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.combo = QComboBox(self)
        self.combo.setGeometry(QtCore.QRect(10, 650, 100, 22))
        self.combo.addItem("Largura")
        self.combo.addItem("Profundidade")
        self.line = QLineEdit(self)
        self.line.setGeometry(QtCore.QRect(150, 650, 50, 22))
        self.button = QPushButton(self)
        self.button.setGeometry(QtCore.QRect(250, 650, 100, 22))
        self.button.setText("Buscar")
        self.button.clicked.connect(self.buscar)   
        self.colorA = QColor(Qt.white)
        self.colorB = QColor(Qt.white)
        self.colorC = QColor(Qt.white)
        self.colorD = QColor(Qt.white)
        self.colorE = QColor(Qt.white)
        self.colorF = QColor(Qt.white)
        self.colorG = QColor(Qt.white)
        self.colorH = QColor(Qt.white)
        self.colorI = QColor(Qt.white)
        self.colorJ = QColor(Qt.white)
        self.colorK = QColor(Qt.white)
        self.colorL = QColor(Qt.white)
        self.colorM = QColor(Qt.white)
        self.colorN = QColor(Qt.white)
        labelA = QtWidgets.QLabel(self)
        labelA.setText('A')
        labelA.move(135, 280)
        labelB = QtWidgets.QLabel(self)
        labelB.setText('B')
        labelB.move(235, 200)
        labelC = QtWidgets.QLabel(self)
        labelC.setText('C')
        labelC.move(335, 280)
        labelD = QtWidgets.QLabel(self)
        labelD.setText('D')
        labelD.move(160, 430)
        labelE = QtWidgets.QLabel(self)
        labelE.setText('E')
        labelE.move(235, 580)
        labelF = QtWidgets.QLabel(self)
        labelF.setText('F')
        labelF.move(85, 580)
        labelG = QtWidgets.QLabel(self)
        labelG.setText('G')
        labelG.move(435, 180)
        labelH = QtWidgets.QLabel(self)
        labelH.setText('H')
        labelH.move(535, 280)
        labelI = QtWidgets.QLabel(self)
        labelI.setText('I')
        labelI.move(635, 180)
        labelJ = QtWidgets.QLabel(self)
        labelJ.setText('J')
        labelJ.move(735, 280)
        labelK = QtWidgets.QLabel(self)
        labelK.setText('K')
        labelK.move(1035, 220)
        labelL = QtWidgets.QLabel(self)
        labelL.setText('L')
        labelL.move(1035, 330)
        labelM = QtWidgets.QLabel(self)
        labelM.setText('M')
        labelM.move(835, 430)
        labelN = QtWidgets.QLabel(self)
        labelN.setText('N')
        labelN.move(635, 580)
        self.show()

    def paintEvent(self, event=None):
        
        paint = QPainter(self)
        paint.setPen(QPen(QColor(Qt.black),4,Qt.SolidLine))
        ac = [QPoint(135,235),QPoint(335,235)]
        paint.drawPolyline(QPolygon(ac))
        bc = [QPoint(235,165),QPoint(335,235)]
        paint.drawPolyline(QPolygon(bc))
        gc = [QPoint(435,135),QPoint(335,235)]
        paint.drawPolyline(QPolygon(gc))
        dc = [QPoint(160,385),QPoint(335,235)]
        paint.drawPolyline(QPolygon(dc))
        hc = [QPoint(535,235),QPoint(335,235)] 
        paint.drawPolyline(QPolygon(hc))
        df = [QPoint(160,385),QPoint(85,535)]
        paint.drawPolyline(QPolygon(df))
        de = [QPoint(160,385),QPoint(235,535)]
        paint.drawPolyline(QPolygon(de))
        gh = [QPoint(435,135),QPoint(535,235)]
        paint.drawPolyline(QPolygon(gh))
        nh = [QPoint(635,535),QPoint(535,235)]
        paint.drawPolyline(QPolygon(nh))
        ih = [QPoint(635,135),QPoint(535,235)]
        paint.drawPolyline(QPolygon(ih))
        jh = [QPoint(735,235),QPoint(535,235)]
        paint.drawPolyline(QPolygon(jh))
        mh = [QPoint(835,385),QPoint(535,235)]
        paint.drawPolyline(QPolygon(mh))
        jk = [QPoint(735,235),QPoint(1035,185)]
        paint.drawPolyline(QPolygon(jk))
        jl = [QPoint(735,235),QPoint(1035,285)]
        paint.drawPolyline(QPolygon(jl))
        paint.setBrush(self.colorF)
        paint.drawEllipse(50,500, 70, 70)
        paint.setBrush(self.colorE)
        paint.drawEllipse(200,500, 70, 70)
        paint.setBrush(self.colorN)
        paint.drawEllipse(600,500, 70, 70)
        paint.setBrush(self.colorD)
        paint.drawEllipse(125,350, 70, 70)
        paint.setBrush(self.colorM)
        paint.drawEllipse(800,350, 70, 70)
        paint.setBrush(self.colorA)
        paint.drawEllipse(100,200, 70, 70)
        paint.setBrush(self.colorC)
        paint.drawEllipse(300,200, 70, 70)
        paint.setBrush(self.colorH)
        paint.drawEllipse(500,200, 70, 70)
        paint.setBrush(self.colorJ)
        paint.drawEllipse(700,200, 70, 70)
        paint.setBrush(self.colorK)
        paint.drawEllipse(1000,150, 70, 70)
        paint.setBrush(self.colorL)
        paint.drawEllipse(1000,250, 70, 70)
        paint.setBrush(self.colorB)
        paint.drawEllipse(200,125, 70, 70)
        paint.setBrush(self.colorG)
        paint.drawEllipse(400,100, 70, 70)
        paint.setBrush(self.colorI)
        paint.drawEllipse(600,100, 70, 70)
                
        paint.end()

    def buscar(self):
        if self.combo.currentText() == "Largura":
            self.largura(self.line.text())
            self.update()
            for vertice in grafo:
                vertice['visitado'] = False
        elif self.combo.currentText() == "Profundidade":
            self.profundidade(self.line.text())
            self.update()
            for vertice in grafo:
                vertice['visitado'] = False

    def largura(self,noh):
        fila = []

        nohInicial = noh

        for vertice in grafo:
            if vertice['noh'] == nohInicial:
                vertice['visitado'] = True
                print('Nó visitado: ', nohInicial)
                fila.append(nohInicial)

        while(len(fila)):
            for vertice in grafo:
                if vertice['noh'] == fila[0]:
                    vizinhanca = vertice['vizinhanca']
                    for vizinho in vizinhanca:
                        for v in grafo:
                            if v['noh'] == vizinho and v['visitado'] == False:
                                v['visitado'] = True
                                if nohInicial == 'A':
                                    self.colorA = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'B':
                                    self.colorB = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'C':
                                    self.colorC = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'D':
                                    self.colorD = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'E':
                                    self.colorE = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'F':
                                    self.colorF = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'G':
                                    self.colorG = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'H':
                                    self.colorH = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'I':
                                    self.colorI = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'J':
                                    self.colorJ = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'K':
                                    self.colorK = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'L':
                                    self.colorL = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'M':
                                    self.colorM = QColor(Qt.red)
                                    self.update()
                                elif nohInicial == 'N':
                                    self.colorN = QColor(Qt.red)
                                    self.update()
                                print('Nó visitado: ', vizinho)
                                fila.append(vizinho)

            fila.pop(0)
    
    def profundidade(self,noh):

        pilha = []

        nohInicial = noh

        for vertice in grafo:
            if vertice['noh'] == nohInicial:
                vertice['visitado'] = True
                print('Nó visitado: ', nohInicial)

        for vertice in grafo:
                if vertice['noh'] == noh:
                    vizinhanca = vertice['vizinhanca']
                    for vizinho in vizinhanca:
                        for v in grafo:
                            if v['noh'] == vizinho and v['visitado'] == False:
                                print('Saindo de: ' + noh + ' Indo para: ' + vizinho)
                                self.profundidade(vizinho)

    #profundidade('C')

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())