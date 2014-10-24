#!/usr/bin/env python
import csv
import random
import string

class Row:
    def setId(self, nId):
        self.id=nId
    def appendCol(self, col):
        self.cols.append(col)
    def appendHeader(self, header):
        self.headers.append(header)
    def __init__(self):
        self.id = -1
        self.cols = []
        self.headers = []

class RowList:
    rowlist = []
    def setList(self, list):
        self.rowlist=list
    def addRow(self, row):
        self.rowlist.append(row)
    def __init__(self):
        self.rowlist = []

def printline(file, line_list, line):
    line_list.append(line)
    file.write(line+'\n');

def compareIds(x,y):
    if x.id > y.id:
        return 1
    elif x.id == y.id:
        return 0
    else:  #x < y
        return -1

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def convertIt(separator, headers, filename):
    save_file = open("media/"+filename+".ttl", 'w');

    line_list = []
    printline(save_file, line_list,'@prefix c1: <http://localhost:8000/project/' +filename+ '/source> .')
    printline(save_file, line_list,'@prefix c2: <http://localhost:8000/project/' +filename+ '/source#> .')

    ifile  = open('media/'+filename+'.csv', "r")

    #To remove lines with #
    secondReadFile = open('media/'+filename+'.csv', "r", encoding='utf-8')
    totalFileInArray = []
    for line in secondReadFile:
        print(line)
        if(not line.startswith("#") and not line.startswith("\ufeff#")):
            totalFileInArray.append( line )
    secondReadFile.close()


    #Save rows without #
    save_file_without = open("media/"+filename+".csv", 'w');
    for row in totalFileInArray:
        save_file_without.write(str(row));
    save_file_without.close()

    #To know how many columns does it have
    firstReadFile = open('media/'+filename+'.csv', "r", encoding='utf-8')
    cols=1
    firstRead = csv.reader(firstReadFile, delimiter=separator)
    for row in firstRead:
        for col in row:
            cols+=1
        break
    firstReadFile.close()


    print("cols", cols)

    header = []

    for col in range(1,cols):
        seq = id_generator(3)
        unique = (seq in header)
        while(not unique):
            seq = id_generator(3)
            if (not seq in header):
                unique = True
                header.append(seq)
    
    if(not headers):
        reader = csv.DictReader(ifile, fieldnames=header, delimiter=separator)
    else:
        reader = csv.DictReader(ifile, delimiter=separator)
        header = reader.fieldnames

    rowlist = RowList()

    rownum = 0

    for row in reader:
        print(row)
        newRow = Row()
        start = 0
        colnum = 0
        newRow.setId(int(rownum))
        for col in row:
            valueOfCol = row[header[colnum]]
            if valueOfCol:
                if ("URI" in header):
                    uriComplete = valueOfCol.rstrip(' ')
                    uriSplit = uriComplete.split('/');
                    uriNumber = uriSplit[len(uriSplit)-1]
                    newRow.setId(int(float(uriNumber)))
                else:
                    newRow.appendHeader(header[colnum])
                    try:
                        newRow.appendCol(valueOfCol.rstrip(' '))
                    except:
                        newRow.appendCol(valueOfCol)
            colnum += 1 
        rowlist.addRow(newRow)
        rownum += 1

    rowlist.setList(sorted(rowlist.rowlist, key=lambda row: row.id))

    for row in rowlist.rowlist:

        printline(save_file, line_list,'')
        
        row_string = 'c1:'+str(row.id) + ' a c2:' +filename+ ' ;'
        printline(save_file, line_list,row_string)
                
        colnum = 0
        for col in row.cols:
            ending = ';'
            if colnum+1 == len(row.cols):
                ending = '.'
            col = col.rstrip(' ')
            try :
                col.replace('"','')
                if (col.isdigit()):
                    row_string = '\tc2:'+row.headers[colnum] + ' "' +str(col)+ '"^^<http://www.w3.org/2001/XMLSchema#int> '+ending
                else:
                    floating_col = float(col)
                    row_string = '\tc2:'+row.headers[colnum] + ' "' +str(floating_col)+ '"^^<http://www.w3.org/2001/XMLSchema#double> '+ending
                printline(save_file, line_list,row_string)
            except:
                row_string = '\tc2:'+row.headers[colnum] + ' "' +col+ '" '+ending
                printline(save_file, line_list, row_string)
            colnum += 1
    """
    for line in line_list:
        print(line)
    """

    ifile.close()
    save_file.close();

    return line_list

