import urllib
import time
count = 1
folder = "/home/zzheng/coding/pics/"
with open("/home/zzheng/coding/nsfw_data_scrapper-master/raw_data/neutral/urls_neutral.txt",'r') as f:
    for line in f:
        print "get "+str(count)+"pics now..."
        filename = folder+str(count)+'.jpg'
        print str(count )+ " :: "+line
        try:
            _,header = urllib.urlretrieve(line, filename)
            print "download "+str(count)+" pics now"
        except:
            print " cant not download "+str(count)+" pic"
        time.sleep(0.01)
        count += 1
f.close()
