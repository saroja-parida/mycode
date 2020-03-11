#Write items from dictionaries to xls
import xlsxwriter
class dict:
    def cal_temp(self,d,item):
        aveg=0
        sum1=0
        len1=len(d[item].values())
        print("lenth is %d"%len1)
        for i in d[item].values():
            sum1+=i
        print("Total %s 's temp is %d"%(item,sum1))    
        aveg=sum1/len1
        print("Average temperature of %s is %d"%(item,aveg))    
    def dict_to_xls(self,xls,dictx):
        try:
            workbook1=xlsxwriter.Workbook(xls)
            worksheet1=workbook1.add_worksheet()
        except TypeError as e:
            print("myerror :[%s]"%e)
        row=1
        col=1
        for k in dictx.keys():
            worksheet1.write(row,col,k)
            col+=1
            worksheet1.write(row,col,dictx[k])
            row+=1
            
obj=dict()
dict1={'india':{'pune':30,'mumbai':35,'delhi':40},'aus':{'sydney':20,'mel':25},'japan':{'tokyo':10,'tang':45}}
#obj.cal_temp(dict1,'japan')
obj.dict_to_xls("text.xlsx",dict1)
