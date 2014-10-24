from csvtordfconverter import convertIt, RowList, Row

separator = ";"
headers=False
line_list = convertIt(separator,headers,"output.2001c")

"""

separator = "\t"
headers=True
line_list = convertIt(separator,headers,"countries")


rowlist = RowList()

row1 = Row()
row1.setId(1)
rowlist.addRow(row1)
row2 = Row()
row2.setId(15)
rowlist.addRow(row2)
row3 = Row()
row3.setId(13)
rowlist.addRow(row3)
row4 = Row()
row4.setId(2)
rowlist.addRow(row4)
row5 = Row()
row5.setId(14)
rowlist.addRow(row5)

print(sorted(rowlist.rowlist, key=id))

"""