import clr
clr.AddReference('rpaSupportRJ.dll')
import rpaSupportRJ
import wpf


from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'IronPythonRpa.xaml')
        for i in range(0,100,1):
            rpaSupportRJ.MouseXY.sendMouseDoubleClick(250,250)

    

if __name__ == '__main__':
    Application().Run(MyWindow())
