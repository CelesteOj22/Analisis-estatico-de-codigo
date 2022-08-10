import subprocess
from subprocess import check_output
from sonarQube import SonarQube
import pathlib
dir="D:/sonar/scripts/proyecto"
sonar = SonarQube("bin")

#subprocess.Popen("cd D:/sonar/scripts",shell=True)
print("Sonar Tumama- Análisis de Sonar Qube con SonarScanner"+"\n"+"La carpeta de proyectos se encuentra en: "+dir+"\n")

directorio = pathlib.Path(dir)
for proyecto in directorio.iterdir():
    sonar.analizar1('D:/sonar/sonar-scanner-4.7.0.2747-windows/bin/sonar-scanner.bat',proyecto.__str__())


