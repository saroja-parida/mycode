#!/bin/usr/python
import xlrd
sheet_no=raw_input("enter sheet num: ")
xd=xlrd.open_workbook("sample.xlsx",'r')
sh=xd.sheet_by_index(int(sheet_no))
header=[sh.cell(0,i) for i in range(sh.ncols)]
hostdetail_l=[]
hostdetail_d={}
for row in range(1,sh.nrows):
	new_d={}
 	row_value=sh.row_values(row)
#	print row_value
#	print "="*20
	for coln in range(1,sh.ncols):
		hostdetail_d[header[coln]]=row_value[coln]
print "--"*50
print "host details"
print "--"*50			
print hostdetail_d			
#print header 
