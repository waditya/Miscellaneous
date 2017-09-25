##Author : Aditya Wagholikar
##Date : 9/24/2017
import csv
import sys
import operator
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from docutils.writers.odf_odt import ToString
from _elementtree import SubElement
from sqlalchemy.sql.expression import true
from pygments.lexers.csound import newline
#from math import floor
#from pandas.io.tests.parser import quoting


stock_lst = []
flag = 0
counter = 0
code_t = ""
min_time_gap_t=999999
# avg_volume_t = 0
# avg_trade_t = 0
# max_trade_t = 0
# min_trade_t = 0
# weighted_avg_price_t = 0
    
class Stock:
    code = ""
    min_time_gap=9999999999999999999999999
    prev_ts = 0
    curr_ts = 0
    avg_volume = 0
    avg_price = 0
    max_trade = 0
    min_trade = 0
    
    sum_price = 0
    sum_volume = 0
    
    stock_code_count = 0
    price_range = 0 
    
    def __init__(self, stock_code, timestamp, volume, trading_price):
        
        self.code = stock_code
        self.prev_ts = self.curr_ts
        self.curr_ts = timestamp
        self.avg_volume = volume
        self.sum_volume = volume
        self.max_trade = trading_price
        self.min_trade = trading_price
        
        self.sum_price = trading_price
        self.stock_code_count = 1
        self.avg_price = int(self.sum_price/self.stock_code_count)
        self.avg_volume = volume
        self.price_range = self.min_trade - self.max_trade
        
    
    def displayStock(self):
        print("Name : ", self.code,  ", Minimum Time Gap: ", self.min_time_gap, ",  Average Volume : ", self.avg_volume,", Max Price :", self.max_trade, " , Minimum Trade : ", self.min_trade, ", Price Range : ", self.price_range,  " , Average Price  : ", self.avg_price)
        
    def updateStock(self, stock_code, timestamp, volume, trading_price):        
        
        
        print('****** Inside Update Stock Method ********')
        stock_code_count_old = int(self.stock_code_count)
        self.stock_code_count +=1
        #avg_price_old = self.avg_price
        volume_old =self.sum_volume      
        print('Checkpoint - US-01')
        print('Updating Stock : ', self.code)
        ##Update Average Price
        print('Old Average Price: ', self.sum_price/stock_code_count_old , ' , Old Average Volume : ',volume_old/stock_code_count_old )
        
        ##Calculate the cumulative share price and cumulative share volume
        self.sum_price += trading_price
        self.sum_volume += volume
        
        ##Update Average Price
        self.avg_price = int(self.sum_price/self.stock_code_count)        
        
        print('New Average Price : ', self.avg_price)
        
        ##Update Volume
        self.avg_volume = int(self.sum_volume/self.stock_code_count)
        
        print('New Average Volume is : ', self.avg_volume)
        
        ##Update Minimum traded price
        if int(self.min_trade) < trading_price:
            self.mix_trade = trading_price
        
        ##Update current and new values of time stamp
        self.prev_ts = self.curr_ts
        self.curr_ts = timestamp
        temp_time_stamp_difference = self.curr_ts - self.prev_ts
        print('Code : ',self.code, ' has Current TimeStamp as :', self.curr_ts,' Previous Timestamp as :', self.prev_ts, ' temporary time difference : ', temp_time_stamp_difference)
        
        if temp_time_stamp_difference < self.min_time_gap: 
            print('Checkpoint - US - 03')
            self.min_time_gap = temp_time_stamp_difference 
        
        #Update Mimimum Trading Price
        if self.min_trade > trading_price:
            self.min_trade = trading_price
        
        ##Update Maximum Trading Price
        if self.max_trade < trading_price:
            self.max_trade = trading_price
            
        #Update Price Range
        self.price_range = self.max_trade - self.min_trade
        
with open("E:\\06 Summer Internship\\01 Quantlab\\QL-02-Wagholikar\\input.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    stock_master = []
    
    
    
    for row in readCSV:
        stock_t = Stock(row[1], int(row[0]), int(row[2]), int(row[3]))
        counter = counter + 1
        print('Counter  is : ', counter)
        if flag== 0:
            stock_lst.append(row[1])            
            stock_master.append(stock_t)
            flag = 1
            print(stock_master[0].displayStock())
        else:
            print("Next item traversal starts...")
            try:
                stock_index = stock_lst.index(row[1])
                print('Stock index of ', row[1], ' is :', stock_index)                               
                stock_master[stock_index].updateStock(row[1], int(row[0]), int(row[2]), int(row[3]))
                print(stock_master[stock_index].displayStock())
                
            except:
                print('New Stock node is being added..')
                stock_lst.append(row[1])
                print('The given stock : ', row[1] ,' is being updated')
                stock_master.append(stock_t)
                stock_master[-1].displayStock() 
    
                        
    print(stock_lst)
    
#     for i in range(0,len(stock_master),1):
#         stock_master[i].weighted_avg_price = floor(stock_master[i].weighted_avg_price)
        
    stock_master.sort(key= lambda x: x.code, reverse=False)
    for item in stock_master:
        print(item.displayStock())    

with open("E:\\06 Summer Internship\\01 Quantlab\\QL-02-Wagholikar\\output.csv", 'w', newline = '') as csvfile:
    stockwriter = csv.writer(csvfile, quoting = csv.QUOTE_NONE)
    for j in range(0, len(stock_master),1):
        stockwriter.writerow([stock_master[j].code,stock_master[j].min_time_gap,stock_master[j].avg_volume,stock_master[j].price_range,stock_master[j].avg_price])
        
    root = Element('symbols')
# tree = ElementTree(root)
# name = Element('symbol')
    tag1 = 'symbol'
    subtag1 = "name"
    subtag2 = "MinTimeGap"
    subtag3 = "AverageVolume" 
    subtag4 = "PriceRange"
    subtag5 = "AveragePrice"
    
    

    for k in range(0, len(stock_master), 1):
        subvalue1 = stock_master[k].code
        subvalue2 = str(stock_master[k].min_time_gap)
        subvalue3 = str(stock_master[k].avg_volume)
        subvalue4 = str(stock_master[k].price_range)
        subvalue5 = str(stock_master[k].avg_price)
        my_dict={subtag1:subvalue1, subtag2:subvalue2, subtag3:subvalue3, subtag4:subvalue4, subtag5:subvalue5}
        #my_dict.sor
        #sorted(my_dict, 1 , reversed = true)
        #sorted_my_dict= sorted(my_dict.items(), key = operator.itemgetter(0))
        print(my_dict)
        value= 'value'+str(k)
        value=SubElement(root, tag1, my_dict)
        
    
    
    print(etree.tostring(root))
    orig_stdout = sys.stdout
    f = open("E:\\06 Summer Internship\\01 Quantlab\\QL-02-Wagholikar\\output.xml", 'w', newline = '')
    sys.stdout = f
    print(etree.tostring(root))
    sys.stdout = orig_stdout
    f.close()
    #tree= Element('masternode')
    #tree = ElementTree(root)
    #tree.append(root)
    #tree.write(open("E:\\06 Summer Internship\\01 Quantlab\\QL-02-Wagholikar\\xml_output_test001.csv", 'w'))          
    
