##Author : Aditya Wagholikar
##Date : 9/24/2017
import csv
from math import floor
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
    min_time_gap=0
    prev_ts = 0
    curr_ts = 0
    avg_volume = 0
    avg_price = 0
    max_trade = 0
    min_trade = 999999999999999
    sum_price = 0
    sum_volume = 0
    stock_code_count = 0
    price_range = 0 
    
    def __init__(self, stock_code, timestamp, volume, trading_price, weighted_avg_price):
        
        self.code = stock_code
        self.prev_ts = self.curr_ts
        self.curr_ts = timestamp
        self.avg_volume = volume
        self.avg_volume = volume
        self.max_trade = trading_price
        self.min_trade = trading_price
        self.avg_price = trading_price
        self.sum_price = trading_price
        self.stock_code_count = 1
        self.avg_volume = volume
        self.price_range = self.min_trade - self.max_trade
        
    
    def displayStock(self):
        print("Name : ", self.code,  ", Minimum Time Gap: ", self.min_time_gap, ",  Average Volume : ", self.avg_volume, ", Price Range : ", self.price_range, " , Average Price  : ", self.max_trade)
        
    def updateStock(self, stock_code, timestamp, volume, trading_price, weighted_avg_price):        
        print('****** Inside Update Stock Method ********')
        stock_code_count_old = self.stock_code_count
        self.stock_code_count +=1
        avg_price_old = self.avg_price
        volume_old =self.volume      
        
        print('Updating Stock : ', self.code)
        ##Update Average Price
        print('Old Average Price: ', self.sum_price/stock_code_count_old , ' , Old Average Volume : ',volume_old/stock_code_count_old )
        
        ##Calculate the cumulative share price and cumulative share volume
        self.sum_price += trading_price
        self.sum_volume += volume
        
        ##Update Average Price
        self.avg_price = int(self.sum_price/self.sum_volume)        
        
        print('New Average Price : ', self.avg_price)
        
        ##Update Volume
        self.avg_volume = self.sum_volume/self.stock_code_count
        
        print('New Volume is : ', self.avg_volume)
        
        ##Update Minimum traded price
        if int(self.min_trade) < trading_price:
            self.mix_trade = trading_price
        
        ##Update current and new values of time stamp
        self.prev_ts = self.curr_ts
        self.curr_ts = timestamp
        temp_time_stamp_difference = self.curr_ts - self.prev_ts
        
        if temp_time_stamp_difference < self.min_time_gap:
            self.min_time_gap = temp_time_stamp_difference 
        
        
        
with open('E:\input2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    stock_master = []
    
    
    
    for row in readCSV:
        stock_t = Stock(row[1], int(row[0]), int(row[2]), int(row[3]), int(row[3]))
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
                stock_master[stock_index].updateStock(row[1], int(row[0]), int(row[2]), int(row[3]), int(row[3]))
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

# with open('E:\output.csv', 'w', newline = '') as csvfile:
#     stockwriter = csv.writer(csvfile, quoting = csv.QUOTE_NONE)
#     for j in range(0, len(stock_master),1):
#         stockwriter.writerow([stock_master[j].code,stock_master[j].max_time_gap,stock_master[j].volume,stock_master[j].max_trade,stock_master[j].weighted_avg_price])
#         
