import time
import urllib
import urllib.request
from functools import lru_cache
@lru_cache(maxsize=20)
def get_url(resource):
    try:
        with urllib.request.urlopen(resource) as s:
            return True
    except Exception as e:
        return False
start = time.time()
get_url("https://cloud.google.com/")
get_url("https://aws.amazon.com/es/")
get_url("https://azure.microsoft.com/es-es/")
get_url("https://www.digitalocean.com/")
get_url("https://cloud.google.com/")
get_url("https://www.ovh.com/")
get_url("https://cloud.google.com/")
get_url("https://cloud.google.com/")
get_url("https://aws.amazon.com/es/")
get_url("https://azure.microsoft.com/es-es/")
get_url("https://aws.amazon.com/es/")
get_url("https://azure.microsoft.com/es-es/")
get_url("https://cloud.google.com/")
get_url("https://aws.amazon.com/es/")
get_url("https://aws.amazon.com/es/")
print(get_url.cache_info())


end = time.time()
print(end - start)
