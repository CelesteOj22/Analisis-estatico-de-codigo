import subprocess
from subprocess import check_output
from sonarQube import SonarQube
from sourceMeter import SourceMeter
import pathlib
dir="D:/sonar/scripts/proyecto"
sonar = SonarQube("bin")
source= SourceMeter("SMResults")
#subprocess.Popen("cd D:/sonar/scripts",shell=True)
print("Análisis de lote de proyectos"+"\n"+"La carpeta de proyectos se encuentra en: "+dir+"\n")

directorio = pathlib.Path(dir)
for proyecto in directorio.iterdir():
    #sonar.analizar1('D:/sonar/sonar-scanner-4.7.0.2747-windows/bin/sonar-scanner.bat',proyecto.__str__())
    #print(proyecto.__str__())
    source.analizar1('D:\sonar\SourceMeter-10.0.0-x64-Windows\Java\SourceMeterJava.exe',proyecto.__str__())

