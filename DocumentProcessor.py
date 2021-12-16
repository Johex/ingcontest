try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

class DocumentProcessor:

    def retrieveContractNumber(self, filename):
        ocrText = pytesseract \
            .image_to_string(Image.open(filename)) \
            .split('\n')
        # _lineWithContractNumber = self.__findLineContractNumber(ocrText)
        _contractNumber = self.__findLineContractNumber(ocrText)
        # _contractNumber =  self.__filterContractNumberFromLine(_lineWithContractNumber)
        print(_contractNumber)
        return _contractNumber

    def __findLineContractNumber(self,stringList):
        print("fineLine")
        # Gwn splitten op spaces en dan 2de??? nope want veel lines
        # regex die kijke voor string van veel cijfers??

        for line in stringList:
            contr_number = re.search('[0-9]{5,}', line)
            # contr_number = re.search('^[a-zA-Z]{1,4}[0-9]+$', line)
            if contr_number:
                # print(contr_number.group())
                words = line.split(' ')
                indices = [i for i, s in enumerate(words) if contr_number.group() in s]
                result = words[indices[0]].replace('.', '')
                return result
        return "not found"

    def __filterContractNumberFromLine(self,line):
        line = line.replace("Contractnummer", "")
        line = line.strip()
        return line


# dp = DocumentProcessor()
# dp.retrieveContractNumber('inputfiles/docu-041.png')