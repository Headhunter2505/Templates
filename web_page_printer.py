import sys
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', sys.argv[1])

print(r.data)
