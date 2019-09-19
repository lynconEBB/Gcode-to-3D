import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Modules.Treatment import *

class GcodePreviewWidget(QMainWindow):

    ok = pyqtSignal(str)
    cancel = pyqtSignal(str)
    def __init__(self,parent =None):
        super(GcodePreviewWidget,self).__init__(parent)
        self.win_opengl = GcodePreview(self)
        self.setCentralWidget(self.win_opengl)
        self.title = "Gcode Extrusion Preview"
        self.width = 800
        self.height = 500
        self.icon = QIcon("../Icons/import.png")
        self.dock =QDockWidget("Gcode Information",self)
        self.listWidget = QListWidget()
        self.text_font = QFont("Times", 10, QFont.Bold)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,self)
        self.button_box.accepted.connect(self.emit_ok)
        self.button_box.rejected.connect(self.close)

        self.init_ui()

    def init_ui(self):
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)

        self.button_box.setGeometry(50, 350, 100, 100)
        self.button_box.resize(QSize(300,200))

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.listWidget.setFont(self.text_font)
        self.dock.setWidget(self.listWidget)
        self.dock.setFloating(False)

    def emit_ok(self):
        self.ok.emit(self.win_opengl.gcode_file)

    def update_list(self):
        self.listWidget.takeItem(0)
        self.listWidget.insertItem(0, "Layers: "+str(self.win_opengl.layers_num))
        self.listWidget.takeItem(1)
        self.listWidget.insertItem(1, "Print Commands: "+str(len(self.win_opengl.vertices)))

class GcodePreview(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zMovimentationChanged = pyqtSignal(int)
    xMovimentationChanged = pyqtSignal(int)
    yMovimentationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GcodePreview, self).__init__(parent)
        self.paint = False
        self.xRot = 0
        self.yRot = -1400
        self.zRot = 0
        self.gcode_file = ""
        self.x = 0
        self.y = 0
        self.z = -70
        self.lastPos = QPoint()
        self.vertices, self.edges = [],[]
        self.layers_num = 0

        self.trolltechPurple = QColor.fromCmykF(0.0, 0.0, 0.40, 0.0)

    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(400, 400)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)

            self.update()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)

            self.update()

    def setXMovimentation(self,position):
        if position > 0:
            self.x += abs(position)
        else:
            self.x -= abs(position)

        self.xMovimentationChanged.emit(position)
        self.update()

    def setYMovimentation(self, position):
        if position < 0:
            self.y += abs(position)
        else:
            self.y -= abs(position)

        self.yMovimentationChanged.emit(position)
        self.update()

    def initializeGL(self):
        self.setClearColor(self.trolltechPurple.darker())
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.xRot/16, 1.0, 0.0, 0.0)
        glRotatef(self.yRot/16, 0.0, 1.0, 0.0)
        glRotatef(self.zRot/16, 0.0, 0.0, 1.0)
        if self.paint == True:
            self.makeObject()
            self.update()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return
        glViewport((width - side) // 2, (height - side) // 2, side,side)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90.0, width /height, 1, 1000.0)
        glMatrixMode(GL_MODELVIEW)

    def makeObject(self):
        i=0
        for layer in self.vertices:
            glBegin(GL_LINES)
            for edge in self.edges[i]:
                for v in edge:
                    glVertex3fv(layer[v])
            i+=1
            glEnd()

    def set_gcode_file(self,file):
        self.gcode_file = file
        self.vertices,self.edges,self.layers_num = Treatment.gcode_preview(self.gcode_file)
        self.paint = True

    def wheelEvent(self, event):

        wheel_move = event.angleDelta().y()
        if wheel_move<0:
            self.z += 10
        else:
            self.z -= 10

        self.zMovimentationChanged.emit(wheel_move)
        self.update()

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setYMovimentation(dy * 0.1)
            self.setXMovimentation(dx * 0.1)

        self.lastPos = event.pos()


    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def setClearColor(self, c):
        glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GcodePreviewWidget()
    window.show()
    sys.exit(app.exec_())

