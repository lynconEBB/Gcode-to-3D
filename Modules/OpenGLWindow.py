import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Modules.ObjLoader import OBJ

class GLWidget(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zMovimentationChanged = pyqtSignal(int)
    xMovimentationChanged = pyqtSignal(int)
    yMovimentationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.paint = False
        self.obj_file = ""
        self.object = 0
        self.xRot = 0
        self.yRot = -1400
        self.zRot = 0
        self.x = 0
        self.y = 0
        self.z = -70
        self.lastPos = QPoint()

        self.trolltechPurple = QColor.fromCmykF(0.40, 0.0, 0.40, 0.0)

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
        glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.xRot/16, 1.0, 0.0, 0.0)
        glRotatef(self.yRot/16, 0.0, 1.0, 0.0)
        glRotatef(self.zRot/16, 0.0, 0.0, 1.0)

        if self.paint :
            self.object = OBJ(self.obj_file, swapyz=True)
            glCallList(self.object.gl_list)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        glViewport((width - side) // 2, (height - side) // 2, side,side)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90.0, width /height, 1, 1000.0)
        glMatrixMode(GL_MODELVIEW)

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

    def set_obj_file(self,obj_file):
        self.obj_file = obj_file
        self.paint = True

    def setClearColor(self, c):
        glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setBottomView(self):
        self.xRot=-1300
        self.yRot=-1400
        self.zRot=0

    def setLeftView(self):
        self.xRot=0
        self.yRot=0
        self.zRot=0

    def setRightView(self):
        self.xRot=0
        self.yRot=3000
        self.zRot=0

    def setTopView(self):
        self.xRot=1300
        self.yRot=-1400
        self.zRot=0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GLWidget()
    window.show()
    sys.exit(app.exec_())

