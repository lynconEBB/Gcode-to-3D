from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Modules.Main import *
import os
import re

class LayersWindow(QDialog):
    def __init__(self,image_dir):
        super(LayersWindow,self).__init__()
        self.title = "View Layers"
        self.width = 800
        self.height = 800
        self.format_img_name(image_dir)
        self.setFixedSize(self.width,self.height)
        self.setWindowIcon(QIcon("../Icons/layer.png"))
        self.setWindowTitle(self.title)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.init_ui()

    def init_ui(self):
        self.sld = QSlider(Qt.Vertical, self)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.valueChanged[int].connect(self.set_image)
        self.sld.setRange(0, self.layer_max)
        self.sld.setFixedWidth(70)
        self.sld.setTickPosition(QSlider.TicksAbove)
        self.sld.setTickInterval(10)

        self.label = QLabel(self)
        pixmap = QPixmap(self.image+"0.png")
        self.label.setPixmap(pixmap)
        self.layout.addWidget(self.label,0,0)
        self.layout.addWidget(self.sld,0,1)
        self.label.resize(pixmap.width(), pixmap.height())

        self.button = QPushButton("Close",self)
        self.button.clicked.connect(self.close)
        self.layout.addWidget(self.button,1,0)

    def set_image(self,value):
        img_file = self.image+str(value)+".png"
        self.label.setPixmap(QPixmap(img_file))
        print(img_file)

    def format_img_name(self,img):
        path, dirs, files = next(os.walk(img))
        self.layer_max = len(files) - 1
        match = re.findall(r"([A-z]+)(\d+)", files[0], re.I)
        name = match[0][0]
        self.image = path+"/"+str(name)
        print(self.image)


class HelpWindow(object):
    def setupUi(self, GecodeConverterHelper):
        GecodeConverterHelper.setObjectName("GecodeConverterHelper")
        GecodeConverterHelper.setFixedSize(770, 753)
        self.verticalLayoutWidget = QWidget(GecodeConverterHelper)
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 871, 751))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.label = QLabel(self.tab)
        self.label.setGeometry(QRect(170, 30, 371, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.tab)
        self.label_2.setGeometry(QRect(10, 100, 951, 121))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.tab)
        self.label_3.setGeometry(QRect(50, 190, 631, 191))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.tab)
        self.label_4.setGeometry(QRect(20, 350, 671, 101))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QFrame(self.tab)
        self.line.setGeometry(QRect(20, 60, 701, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QLabel(self.tab)
        self.label_6.setGeometry(QRect(20, 490, 711, 151))
        self.label_6.setMaximumSize(QSize(1677721, 1677721))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QRect(20, 10, 731, 701))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 729, 699))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QWidget()
        self.widget.setObjectName("widget")
        self.scrollArea_2 = QScrollArea(self.widget)
        self.scrollArea_2.setGeometry(QRect(20, 10, 731, 701))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 729, 699))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.widget, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(GecodeConverterHelper)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(GecodeConverterHelper)

    def retranslateUi(self, GecodeConverterHelper):
        _translate = QCoreApplication.translate
        GecodeConverterHelper.setWindowTitle(_translate("GecodeConverterHelper", "Gecode Converter Helper"))
        self.label.setText(_translate("GecodeConverterHelper", "Gcode Converter Helper"))
        self.label_2.setText(_translate("GecodeConverterHelper", "     Gcode Converter its a pretty simple to use software, there are many functions\n"
"that can be very useful, such as:"))
        self.label_3.setText(_translate("GecodeConverterHelper", "-STL file reconstruction\n"
"\n"
" -Capture information while printing a 3d object\n"
"\n"
" -Generate Print Report\n"
"\n"
" - Detect print failures"))
        self.label_4.setText(_translate("GecodeConverterHelper", "    The way to use all these functions is written in this helper, you can acess all\n"
"this information passing through these tabs:"))
        self.label_6.setPixmap(QPixmap("../Images/Capturar.PNG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("GecodeConverterHelper", "Main"))
        self.label_5.setText(_translate("GecodeConverterHelper", "STL Reconstructor"))
        self.label_7.setText(_translate("GecodeConverterHelper", "   The STL Reconstructor is a function capable of receiving a gcode file\n"
"and returning an STL file to be exported, this can be useful on\n"
"occasions when you lose the STL file that generated this Gcode"))
        self.label_8.setText(_translate("GecodeConverterHelper", "       1) First of all, you need to import a gcode file, you can do this by clicking on File -> Import Gcode\n"
"  in the menu bar or just clicking on the import icon in the tool bar  "))
        self.label_11.setText(_translate("GecodeConverterHelper", "      2) A Preview Window will appear and you can confirm if this the gcode file that you choose, in addition\n"
"  you can see how many layers and how many printing commands your file has "))
        self.label_9.setText(_translate("GecodeConverterHelper", "      3) Then you need to click on Tool -> Remesh Gcode on the menu bar or just click on the remes\n"
"   icon in the tool bar"))
        self.label_10.setText(_translate("GecodeConverterHelper", "       4) In the Remesh Window you must specify some things: first you need to specify the skirt heigth\n"
"  of your gcode, if your gcode don\'t have skirt just put 0, next you need to specify the infill density of \n"
"  your gcode, gcode Converter works way better with 100% gcodes, and finally you need to mark the\n"
"   check box if you want to save the image of all layers of your gcode, this images will be saved on\n"
"   the directory specified in the configuration window "))
        self.label_12.setText(_translate("GecodeConverterHelper", "      5) Now that you should see a preview of your new STL, all you have to do is export this file, this can\n"
"   be done by clicking on File -> Export STL in the menu bar or just clicking on the export file on the Tool Bar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("GecodeConverterHelper", "STL Reconstruction"))
        self.label_13.setText(_translate("GecodeConverterHelper", "Get Differences Between Two STLs"))
        self.label_14.setText(_translate("GecodeConverterHelper", "This function generates an OBJ file with a texture that indicates to the parts\n"
"where the 2 files are similar and where they are more different, the colors follow\n"
"from blue to red being blue the nearest and red the farthest"))
        self.label_15.setText(_translate("GecodeConverterHelper", "     1) To start using this function, you must perform the STL recryption function so that this file is in the\n"
"   program\'s memory"))
        self.label_16.setText(_translate("GecodeConverterHelper", "     2)Next you need to click on Tool -> Compare STL on the menu bar or in the icon of the tool bar"))
        self.label_17.setText(_translate("GecodeConverterHelper", "      3) Choose the original STL to compare with the generated STL, and click on Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("GecodeConverterHelper", "Get Diferences"))


class InformationWindow(QDialog):
    def __init__(self):
        super(InformationWindow, self).__init__()
        self.title = "GCode Converter Information"
        self.width = 300
        self.height = 300
        self.setWindowIcon(QIcon("../Icons/GSTicon.png"))
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.create_text()
        self.center()

    def create_text(self):
        title_font = QFont("Times",20,QFont.Bold)
        text_font = QFont("Times",10)

        lb_title = QLabel("Software Information",self)
        lb_title.setFont(title_font)
        lb_title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        lb_title.setAlignment(Qt.AlignCenter)
        lb_text1 = QLabel("     <b>Version:</b> 1.55",self)
        lb_text1.setFont(text_font)
        lb_text2 = QLabel( "     <b>Python Packages: </b>MatPlotLib, PyOpenGL, PyQt5, Python-OpenCV, Numpy",self)
        lb_text2.setFont(text_font)
        lb_text3 = QLabel("     <b>Python Version: </b>3.7", self)
        lb_text3.setFont(text_font)
        lb_text4 = QLabel("     <b>Last Update: </b>27/08/2018", self)
        lb_text4.setFont(text_font)
        lb_text5 = QLabel("     <b>Author: </b>Lyncon Estevan Bernardo Baez", self)
        lb_text5.setFont(text_font)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(25)
        self.layout.addWidget(lb_title)
        self.layout.addWidget(lb_text1,alignment=Qt.AlignCenter)
        self.layout.addWidget(lb_text2,alignment=Qt.AlignCenter)
        self.layout.addWidget(lb_text3,alignment=Qt.AlignCenter)
        self.layout.addWidget(lb_text4,alignment=Qt.AlignCenter)
        self.layout.addWidget(lb_text5,alignment=Qt.AlignCenter)

        self.button = QPushButton("Close", self)
        self.button.setToolTip("Close Gcode Converter Information Window")

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.close)
        self.setLayout(self.layout)
        self.layout.addStretch(5)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class ConfigurationWindow(QDialog):
    def __init__(self,ply_default,output_default,image_dir_default,texture_file):
        super(ConfigurationWindow, self).__init__()
        self.resize(550, 200)
        self.setWindowTitle("Configurations")
        self.setMinimumWidth(350)
        self.setWindowIcon(QIcon("../Icons/config.png"))
        self.center()

        title_font = QFont("Times", 20, QFont.Bold)
        lb_title = QLabel("Configurations", self)
        lb_title.setFont(title_font)
        lb_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lb_title.setAlignment(Qt.AlignCenter)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.ply = QLineEdit()
        self.ply.setText(ply_default)
        self.output = QLineEdit()
        self.output.setText(output_default)
        self.image = QLineEdit()
        self.image.setText(image_dir_default)
        self.texture = QLineEdit()
        self.texture.setText(texture_file)
        self.ply_button = QPushButton("Browse", self)
        self.ply_button.clicked.connect(self.browse_ply)
        self.obj_button = QPushButton("Browse", self)
        self.obj_button.clicked.connect(self.browse_obj)
        self.image_button = QPushButton("Browse", self)
        self.image_button.clicked.connect(self.browse_image_dir)
        self.texture_button = QPushButton("Browse", self)
        self.texture_button.clicked.connect(self.browse_texture_file)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox1.addWidget(self.ply)
        hbox1.addWidget(self.ply_button)
        hbox2.addWidget(self.output)
        hbox2.addWidget(self.obj_button)
        hbox3.addWidget(self.image)
        hbox3.addWidget(self.image_button)
        hbox4.addWidget(self.texture)
        hbox4.addWidget(self.texture_button)
        layout = QFormLayout()
        layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        layout.addRow(lb_title)
        layout.addRow("<b>Path to save Ply File</b>",hbox1)
        layout.addRow("<b>Path to save OBJ file</b>", hbox2)
        layout.addRow("<b>Directory to save layer Images</b>", hbox3)
        layout.addRow("<b>Path to save OBJ file with texture</b>", hbox4)
        layout.addWidget(self.button_box)
        layout.setSpacing(20)

        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def browse_ply(self):
        diag = QFileDialog()
        ply_name = diag.getOpenFileName(self,"Ply File",self.ply.text(),"Point Cloud(*.ply)")
        if ply_name[0] != "":
            self.ply.setText(ply_name[0])

    def browse_obj(self):
        diag = QFileDialog()
        obj_name =diag.getOpenFileName(self,"Obj File",self.output.text(),"3d Object(*.obj)")
        if obj_name[0] != "":
            self.output.setText(obj_name[0])

    def browse_image_dir(self):
        diag = QFileDialog()
        image_name = diag.getExistingDirectory(self, "Images Directory", self.output.text())
        if image_name != "":
            self.output.setText(image_name)

    def browse_texture_file(self):
        diag = QFileDialog()
        texture_name =diag.getOpenFileName(self,"Obj File",self.texture.text(),"3d Object(*.obj)")
        if texture_name[0] != "":
            self.texture.setText(texture_name[0])

class RemeshWindow(QDialog):

    save = pyqtSignal(bool)

    def __init__(self):
        super(RemeshWindow, self).__init__()
        self.title = "Remesh"
        self.width = 300
        self.height = 240
        self.setWindowIcon(QIcon("../Icons/remesh.png"))
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.init_ui()
        self.center()

    def init_ui(self):
        title_font = QFont("Times",20,QFont.Bold)
        text_font = QFont("Times",10)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        lb_title = QLabel("Configurations", self)
        lb_title.setFont(title_font)
        lb_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lb_title.setAlignment(Qt.AlignCenter)

        self.skirt_h = QSpinBox()
        self.skirt_h.setValue(0)
        self.skirt_h.setFixedWidth(50)
        hbox1= QHBoxLayout()
        self.density = QSpinBox()
        self.density.setMaximum(100)
        self.density.setValue(100)
        self.density.setFixedWidth(50)
        self.percent = QLabel("%",self)
        hbox1.addWidget(self.density)
        hbox1.addWidget(self.percent)
        self.check = QCheckBox()
        self.check.stateChanged.connect(lambda :self.save.emit(self.check.isChecked()))

        layout = QFormLayout()
        layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        layout.setAlignment(Qt.AlignCenter)
        layout.addRow(lb_title)
        layout.addRow("<b>Skirt height: </b>",self.skirt_h )
        layout.addRow("<b>Fill density</b> ",hbox1)
        layout.addRow("<b>Save all layer Images</b>",self.check)
        layout.addWidget(self.button_box)
        layout.setSpacing(20)
        self.resize(200, 200)
        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class MainThread(QThread):

    finish = pyqtSignal(str)
    finish2 = pyqtSignal(str)
    finish3 = pyqtSignal(str)

    def __init__(self,gcode_file,obj_file,ply_file,image_dir,save_img,skirt_h):
        QThread.__init__(self)
        self.obj_file = obj_file
        self.gcode_file = gcode_file
        self.ply_file = ply_file
        self.image_dir = image_dir
        self.save_imgs = save_img
        self.skirt_h = skirt_h

    def run(self):
        main = Main(self.gcode_file, self.obj_file, self.ply_file, self.image_dir,save_img = self.save_imgs,skirt_height=self.skirt_h)
        main.convert()
        self.finish.emit("hi")
        self.finish2.emit("hi")
        self.finish3.emit("finished")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LayersWindow("/home/lyncon/3d-printer-parser/Images")
    ui.show()
    sys.exit(app.exec_())