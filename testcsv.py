import csv

fd = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(fd,delimiter=',')
wr.writerow(['name','temperature','check'])

f = open('temperature.txt', 'r')
i=1
while True:
    name = 'name'+str(i)
    i+=1
    temperature = f.readline()
    if not temperature: break
    check='T'
    if float(temperature)>=37.5 :
        check = 'F'
    row=[str(name),str(temperature),str(check)]
    wr.writerow(row)
f.close()
