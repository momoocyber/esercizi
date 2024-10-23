import os
import PyPDF2
#IMMISSIONE DEI PARAMETRI
sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
sOutDir = input("Inserisci la dir di output: ")

def CercaStringaInFilename(sFilename,sStringToSearch):
    sFilename1 = sFilename.lower()
    sStringToSearch1 = sStringToSearch.lower()
    print("Cerco {0} in {1} ".format(sStringToSearch1,sFilename1))
    iRet = sFilename1.find(sStringToSearch1)
    if(iRet>-1):
        print("Trovato")
        return True
    return False

def CercaInFilePdf(sFile,sString):
    object = PyPDF2.PdfReader(sFile)
    numPages = len(object.pages)
    for i in range(0, numPages):
        pageObj = object.pages[i]
        text = pageObj.extract_text()
        text = text.lower()
        if(text.find(sString)!=-1):
            return True
    return False


def CercaStringaInFileContent(sFilePathCompleto,sString):
    sOutFileName,sOutFileExt = os.path.splitext(sFilePathCompleto)
    if(sOutFileExt.lower()==".pdf"):
        #print("Riconosciuto file pdf " + sFile)
        return CercaInFilePdf(sFilePathCompleto,sString)
    return False
#NAVIGA NEL FILE SYSTEM
iNumFileTrovati=0
for root, dirs, files in os.walk(sRoot):
    sToPrint = "Dir corrente {0} contenente {1} subdir e {2} files".format(root, len(dirs), len(files))
    print(sToPrint)
    for filename in files:
        iRet = CercaStringaInFilename(filename,sStringaDaCercare)
        if(iRet != True):
            sFilepathCompleto = os.path.join(root,filename)
            iRet = CercaStringaInFileContent(sFilepathCompleto ,sStringaDaCercare)
        if(iRet==True):
            print("Trovato file: ",filename)
            iNumFileTrovati = iNumFileTrovati + 1

