#from Servidor import IHerramienta
#decidir si dejo constantes o no
from IHerramienta import *
import subprocess #para mandarle comandos a la consola
from subprocess import check_output
from datetime import datetime

"""
class sonarQube(IHerramienta):
    scanner: str
    projectKey: str
    sources: str
    hosturl: str
    login: str
    binaries: str
    dir: str
    
    def __init__ (self,projectKey: str, login: str, binaries: str, dir: str):
        self.scanner="D:\sonar\sonar-scanner-4.7.0.2747-windows\bin\scanner.bat"
        self.projectKey=projectKey
        self.sources="."
        self.hosturl="http://localhost:9000"
        self.login=login
        self.binaries=binaries
        self.dir=dir
"""
#sonar - scanner.bat - D"sonar.projectKey=proyecto" - D"sonar.sources=." - D"sonar.host.url=http://localhost:9000" - D"sonar.login=6d047c32f875ad34e45a6c712cde319c0b9074cd"
#sonar= sonarQube("proyecto","6d047c32f875ad34e45a6c712cde319c0b9074cd","build/bin","D:/sonar/python/venv/proyectos")
#scanner: str
#projectKey: str
#sources: str
#hosturl: str
#login: str
#binaries: str
#dir: str

class SonarQube(IHerramienta):
    def __init__ (self, binaries: str):
        self._sources="."
        self._hosturl="http://localhost:9000"
        #self._login=login
        self._binaries=binaries

#sonar= sonarQube("D:\sonar\sonar-scanner-4.7.0.2747-windows\bin\scanner.bat","proyecto",".","http://localhost:9000","6d047c32f875ad34e45a6c712cde319c0b9074cd","build/bin",carpeta proyecto)

    """
    def __init__ (self,scanner: str, projectKey: str, sources: str, hosturl: str, login: str, binaries: str, dir: str):
        self.scanner=scanner
        self.projectKey=projectKey
        self.sources=sources
        self.hosturl=hosturl
        self.login=login
        self.binaries=binaries
        self.dir=dir    
        
        def analizar1(self,scanner, projectName):
        subprocess.Popen(["cd",projectName], shell=True)
        print('carpeta llolo')
    """

    def analizar1(self,scanner, projectName):
        sep = projectName.split(sep='\\')
        projectKey= sep[4]
        comando = 'cd '+projectName+' && '+scanner+' -Dsonar.projectKey='+projectKey+' -Dsonar.sources='+self._sources+' -Dsonar.host.url='+self._hosturl+' -Dsonar.java.binaries='+self._binaries
        #check_output(comando, shell=True)

        try:
            stdout = subprocess.run(comando, stdout=subprocess.PIPE, universal_newlines=True, check=True, text=True,shell=True).stdout
            if 'EXECUTION SUCCESS' in stdout:
                print("El proyecto " + projectKey + " ha sido analizado con exito!")
        except:
            print("HA OCURRIDO UN ERROR!\n")


        #time = str(datetime.now().time())
        #time = time.replace(":",".")
        #log = open("D:/sonar/scripts/Logs/Log-"+str(datetime.now().date())+"-"+time+".txt","w")
        #str1 = repr(stdout)
        #log.write(str1 + "\n")
        #log.close()

        #print("El proyecto "+projectKey+" ha sido analizado con exito!")
#"D:\sonar\sonar-scanner-4.7.0.2747-windows\bin\sonar-scanner.bat" -D"sonar.projectKey=aoi-2.5.1" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.java.binaries=bin"
        #subprocess.Popen([scanner+' -D"sonar.projectKey='+projectName+'" -D"sonar.sources=." -D"sonar.host.url='+self._hosturl+
                          #'" -D"sonar.binaries='+self._binaries+'"'])
        #subprocess.run("search=$(grep 'EXECUTION SUCCESS' ../../tmp);")


        #Testing if in the output of the analysis it cannot find 'EXECUTION SUCCESS'
        #subprocess.run("if","test","-z","$search")

#s = subprocess.Popen(["cd",projectName,'&&',scanner,'-Dsonar.projectKey=',projectKey,'-Dsonar.sources=. -Dsonar.host.url=',self._hosturl,
        #                  '-Dsonar.binaries=',self._binaries], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        #print(s.stdout.read()+'\n'+s.stderr.read())
        #print('tu')




