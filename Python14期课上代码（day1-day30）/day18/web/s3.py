import hashlib

m=hashlib.md5()
#b'fffffff'
#bytes('fffff',encoding='utf-8')
# 'ffffff'.encode('utf-8')
m.update(b'fffffff')
ret=m.hexdigest()
print(ret)