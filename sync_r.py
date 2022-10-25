from unittest import result
import requests
import time


def get_r(num, results):
    for i in range(num):
        r = requests.get("https://google.com")
        results.append(r.status_code)


start_time = time.time()
results = []
get_r(15, results)
print(results)
print(f"Duration: {time.time() - start_time}")
