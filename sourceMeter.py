import subprocess #para mandarle comandos a la consola
import os
from subprocess import check_output
from IHerramienta import *

class SourceMeter(IHerramienta):
    def __init__(self, resultsDir: str):
        #self._projectBaseDir = projectBaseDir
        self._resultsDir = resultsDir
        self._runFB = 'true'
        self._FBFileList = 'filelist.txt'

#SourceMeterJava - projectName = ckjm - 1.9 - projectBaseDir = D:\Celeste\LSI\GICS\ckjm - 1.9\src - resultsDir = Results - runFB = true - FBFileList = filelist.txt




    """
    def analizar1(self, source, projectName, dir):
        subprocess.run("cd", dir, shell=True)
        subprocess.run([source,'- projectName =' + projectName, '- projectBaseDir ='+self.projectBaseDir,
                        '- resultsDir =' + self.resultsDir, '- runFB =' + self.runFB,'- FBFileList =' + self.FBFileList])
    """
    #dir = D:/sonar/scripts
    def analizar1(self, source, projectName):
        sep = projectName.split(sep='\\')
        projectKey= sep[4]
        comando = 'cd ' +projectName+' && '+source+' -projectName='+projectKey+' -projectBaseDir='+projectName+' -resultsDir='+self._resultsDir+' -runFB='+self._runFB+' -FBFileList='+self._FBFileList
        #check_output(comando, shell=True)
        #stdout = subprocess.run(comando, stdout=subprocess.PIPE, universal_newlines=True, check=True, text=True,shell=True).stdout
        #print(stdout)

        try:
            stdout = subprocess.run(comando, stdout=subprocess.PIPE, universal_newlines=True, check=True, text=True,shell=True).stdout
            print("El proyecto " + projectKey + " ha sido analizado con exito!")
        except:
            print("Ha ocurrido un error durante el analisis del proyecto "+projectKey)

