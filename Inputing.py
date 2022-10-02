import os

dir_path = r'./corpus/'

def read_file(file_name):
    import PyPDF2
  
    # creating a pdf file object
    pdfFileObj = open(dir_path + file_name, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    
    
    paper_content = ""
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(0)
        paper_content += pageObj.extractText()
    pdfFileObj.close()

    return paper_content

def read_corpus():
    files = {}
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if path[-3:].lower() == "pdf" or path[-4:] == ".pdf":
                files[path] = read_file(path)

    return files

