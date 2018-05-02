import redis
try: 
    r = redis.StrictRedis(host='quay.quaylab.lan', port=6379, db=0)
    print "Proxy Test: {}".format(r.ping())
except:
    print "Proxy Test: {}".format(False)
try:
    r = redis.StrictRedis(host='quay.quaylab.lan', port=6380, db=0)
    print "Pod Test: {}".format(r.ping())
except:
    print "Pod Test: {}".format(False)
