

import subprocess
import datetime
import csv

before_query_time_memcache = datetime.datetime.utcnow()

tme=[]
with open('/home/ubuntu/flaskapp/states.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        tme.append(row)
print tme
nmapp=tme[0]
print nmapp
# nr=nmapp.replace(",","")
# nr1=nr.replace('[','')
nomapp=''.join(nmapp)
print  nomapp
nofred=tme[1]
noofred=''.join(nofred)
print noofred

mapno=5
redno=2
if mapno < int(nomapp) and redno < int(noofred):
    subprocess.call(['$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapred.map.tasks="%s" -D mapred.reduce.tasks="%s" -file  /home/ubuntu/mapp/mapper.py -mapper  /home/ubuntu/mapp/mapper.py -file /home/ubuntu/mapp/reducer.py -reducer /home/ubuntu/mapp/reducer.py -input /input -output /out7'%(mapno,redno)],shell=True)

    after_query_time_memcacahe = datetime.datetime.utcnow()
    differrnce1 = str(after_query_time_memcacahe - before_query_time_memcache)


    writeintocsv = open("timetaken.csv", 'wb')
    writeobj = csv.writer(writeintocsv, quoting=csv.QUOTE_ALL)
    writeobj.writerow(differrnce1 )
else :
    print "Invalid mappers and reducers "
