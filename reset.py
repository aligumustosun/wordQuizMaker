targetDifference=2

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num-1] = text
    out = open(file_name, 'w')
   # print("it is replaced")
    out.writelines(lines)
    out.close()

def read_line(file_name,line_num):
    lines=open(file_name, 'r').readlines()
    return lines[line_num-1]
def lineLength(adres):
    lines=open(adres, 'r').readlines()
    return len(lines)


i=1
while (i<lineLength('words.txt')+1):
    a,b,c,d = read_line('words.txt',i).split(',')
    replace_line('words.txt',i,b+","+a+",0,"+str(int((targetDifference)*-1))+"\n")
    print(i)
    i+=1
    
