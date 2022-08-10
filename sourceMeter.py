#from Servidor import IHerramienta
import subprocess #para mandarle comandos a la consola
import os

from IHerramienta import IHerramienta
"""
class sourceMeter(IHerramienta):
    sourceMeter: str
    projectName: str
    projectBaseDir: str
    resultsDir: str
    runFB: str
    FBFileList: str
    
    def __init__ (self,sourceMeter: str, projectName: str, projectBaseDir: str, resultsDir: str, runFB: str,FBFileList: str):
        self.sourceMeter=sourceMeter
        self.projectName=projectName
        self.projectBaseDir=projectBaseDir
        self.resultsDir=resultsDir
        self.runFB=runFB
        self.FBFileList=FBFileList
        
    def analizar(self):
        subprocess.run([self.sourceMeter, '- projectName =' + self.projectName, '- projectBaseDir ='+self.projectBaseDir,
                        '- resultsDir =' + self.resultsDir, '- runFB =' + self.runFB,'- FBFileList =' + self.FBFileList])

    """
class SourceMeter(IHerramienta):
    def __init__(self, resultsDir: str):
        #self._projectBaseDir = projectBaseDir
        self._resultsDir = resultsDir
        #self._runFB = runFB
        #self._FBFileList = FBFileList

#projectName: str
#projectBaseDir: str
#resultsDir: str
#runFB: str
#FBFileList: str
#SourceMeterJava - projectName = ckjm - 1.9 - projectBaseDir = D:\Celeste\LSI\GICS\ckjm - 1.9\src - resultsDir = Results - runFB = true - FBFileList = filelist.txt
#sourcem= sourceMeter("SourceMeterJava","ckjm - 1.9","D:\Celeste\LSI\GICS\ckjm - 1.9\src","Results","true,"filelist.txt")



    """
    def analizar1(self, source, projectName, dir):
        subprocess.run("cd", dir, shell=True)
        subprocess.run([source,'- projectName =' + projectName, '- projectBaseDir ='+self.projectBaseDir,
                        '- resultsDir =' + self.resultsDir, '- runFB =' + self.runFB,'- FBFileList =' + self.FBFileList])
    """
    #dir = D:/sonar/scripts
    def analizar1(self, source, projectName):
        sep = projectName.split(sep='\\')
        projectKey = sep[4]
        comando = 'cd ' + projectName + ' && ' + source +'- projectName =' + projectKey + '- projectBaseDir ='+projectName +'- resultsDir =' + self.resultsDir, '- runFB = true'+'- FBFileList = filelist.txt'



