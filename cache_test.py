import time
from cache import Cache

def get_data(key):
    time.sleep(.003)
    return hash(str(key))

"""
for i in xrange(1000000):
    print "Getting data of person "+str(i)
    print get_data(i)
"""

def cache_get_data(c, key):
    """If key in cache, return value from cache.
    Else, get value from db and store key,value in cache."""
    value = c.get_value(key)
    hit = True
    if value is None:
        value = get_data(key)
        c.cache(key, value)
        hit = False
    return (value, hit)


c = Cache(20)
times = []
hit_count = 0
miss_count = 0
for key in [76, 25, 79, 14, 66, 13, 8, 65, 28, 25, 76, 80, 77, 70, 64, 79, 40, 26, 86, 64, 17, 14, 94, 75, 47, 41, 5, 31, 47, 81, 14, 8, 71, 77, 42, 90, 84, 10, 67, 32, 36, 85, 62, 28, 29, 25, 17, 63, 88, 24, 26, 40, 39, 4, 35, 70, 47, 26, 56, 22, 66, 100, 56, 93, 76, 9, 58, 29, 74, 96, 81, 66, 16, 19, 27, 28, 77, 73, 78, 23, 35, 94, 83, 41, 63, 82, 52, 15, 62, 73, 76, 31, 19, 82, 24, 28, 95, 33, 63, 13, 10, 14, 58, 28, 6, 13, 50, 3, 25, 12, 98, 7, 29, 91, 20, 30, 77, 5, 43, 95, 55, 19, 32, 27, 61, 55, 89, 63, 33, 63, 64, 97, 43, 31, 7, 61, 31, 44, 46, 71, 39, 27, 96, 30, 94, 64, 43, 39, 92, 41, 83, 6, 21, 7, 30, 45, 31, 29, 46, 45, 94, 59, 2, 26, 76, 84, 63, 52, 23, 31, 14, 28, 78, 88, 75, 91, 10, 49, 34, 54, 34, 5, 91, 34, 76, 48, 76, 4, 89, 22, 27, 72, 42, 91, 98, 100, 64, 49, 66, 6, 20, 16, 91, 8, 12, 68, 45, 35, 24, 70, 68, 52, 26, 19, 72, 69, 47, 20, 6, 22, 55, 59, 1, 100, 45, 10, 24, 34, 44, 95, 86, 24, 56, 82, 89, 87, 54, 93, 24, 57, 68, 18, 92, 69, 55, 54, 36, 79, 63, 28, 33, 31, 10, 67, 84, 42, 78, 63, 45, 41, 86, 17, 18, 88, 94, 58, 61, 46, 95, 1, 21, 94, 74, 29, 61, 97, 8, 27, 95, 39, 81, 64, 32, 61, 41, 8, 19, 52, 71, 58, 30, 94, 21, 75, 61, 74, 32, 27, 95, 98, 82, 43, 6, 11, 79, 58, 49, 87, 19, 29, 35, 54, 28, 64, 51, 77, 64, 34, 22, 76, 55, 19, 57, 74, 52, 71, 86, 1, 34, 46, 86, 48, 57, 35, 23, 65, 27, 91, 88, 55, 10, 78, 39, 80, 3, 55, 34, 76, 30, 61, 29, 100, 1, 25, 95, 60, 47, 94, 22, 12, 8, 37, 14, 82, 38, 88, 29, 2, 52, 21, 4, 73, 92, 89, 88, 72, 70, 25, 45, 50, 82, 7, 55, 76, 98, 21, 57, 26, 7, 89, 81, 35, 99, 99, 25, 6, 10, 2, 11, 93, 29, 29, 63, 76, 4, 88, 91, 63, 82, 63, 31, 92, 77, 60, 72, 4, 41, 80, 26, 57, 59, 26, 54, 41, 39, 45, 20, 82, 91, 25, 5, 14, 92, 30, 38, 5, 24, 96, 97, 83, 24, 98, 4, 23, 71, 19, 60, 13, 25, 60, 3, 47, 69, 24, 56, 48, 38, 60, 73, 39, 29, 61, 33, 65, 14, 47, 67, 40, 27, 56, 70, 75, 69, 6, 52, 79, 89, 81, 69, 21, 12, 2, 35, 37, 78, 59, 79, 18, 86, 3, 67, 65, 2, 62, 97, 1, 82, 33, 83, 25, 96, 48, 100, 57, 57, 94, 61, 38, 19, 69, 58, 36, 6, 20, 26, 82, 50, 59, 12, 69, 55, 95, 35, 95, 91, 57, 42, 6, 20, 77, 53, 70, 9, 2, 60, 71, 72, 69, 3, 54, 67, 86, 78, 25, 6, 71, 81, 41, 12, 68, 53, 94, 9, 32, 70, 59, 76, 49, 4, 42, 50, 74, 72, 15, 39, 91, 83, 49, 40, 61, 14, 59, 58, 40, 68, 46, 11, 29, 23, 48, 87, 92, 44, 61, 1, 85, 71, 90, 62, 29, 8, 50, 21, 94, 83, 17, 70, 73, 3, 29, 97, 32, 21, 20, 60, 31, 42, 99, 30, 32, 16, 58, 21, 56, 67, 53, 75, 36, 90, 22, 11, 1, 67, 57, 86, 24, 69, 40, 80, 73, 7, 48, 81, 70, 88, 51, 90, 70, 70, 4, 50, 32, 79, 26, 83, 99, 45, 67, 92, 36, 16, 54, 93, 30, 83, 18, 54, 46, 55, 20, 29, 25, 64, 27, 30, 97, 91, 70, 39, 44, 25, 89, 29, 89, 51, 4, 48, 87, 44, 44, 31, 99, 5, 46, 23, 94, 26, 26, 53, 15, 35, 1, 6, 97, 21, 87, 95, 55, 50, 98, 83, 93, 16, 37, 8, 69, 7, 45, 77, 61, 33, 59, 58, 18, 51, 50, 53, 90, 38, 82, 60, 4, 44, 38, 40, 96, 89, 61, 73, 15, 19, 54, 77, 8, 10, 86, 8, 41, 73, 58, 36, 13, 9, 91, 87, 69, 77, 37, 50, 64, 61, 19, 70, 91, 3, 7, 93, 68, 85, 22, 98, 7, 94, 28, 20, 22, 56, 94, 53, 25, 26, 3, 57, 31, 5, 36, 4, 20, 4, 62, 11, 36, 20, 78, 12, 5, 100, 96, 66, 53, 22, 28, 46, 30, 94, 69, 83, 20, 78, 45, 44, 80, 26, 36, 68, 80, 16, 71, 72, 15, 78, 71, 15, 77, 72, 74, 54, 27, 28, 98, 17, 91, 43, 84, 55, 51, 79, 45, 82, 9, 83, 64, 7, 25, 85, 25, 13, 4, 25, 46, 37, 84, 76, 49, 7, 87, 12, 53, 71, 44, 71, 27, 45, 13, 43, 61, 70, 51, 13, 26, 99, 59, 63, 51, 15, 70, 74, 12, 26, 27, 87, 2, 66, 61, 95, 85, 57, 43, 14, 78, 10, 55, 56, 28, 56, 18, 78, 97, 15, 8, 49, 84, 71, 61, 80, 1, 73, 68, 54, 14, 1, 76, 77, 58, 10, 18, 22, 98, 4, 23, 93, 28, 2, 76, 19, 3, 73, 25, 64, 13, 43, 38, 69, 9, 13, 52, 9, 43, 1, 32, 40, 55, 80, 22, 5, 88, 42, 53, 92, 93, 72, 10, 28, 93, 28, 52, 98, 60, 22, 44, 62, 74, 23, 94, 17, 55, 56, 26, 77, 93, 87, 78, 88, 82, 19, 75, 57, 45, 26, 44, 93, 69, 53, 83, 48, 27, 53, 51, 67, 53, 15, 89, 69, 61, 88, 64, 49, 12, 37, 90, 57, 31, 69, 56, 52, 99, 52, 8, 54, 36]:
    t0 = time.time()
    value, hit = cache_get_data(c, key)
    assert value == hash(str(key)), "Value for %d was %d, expected %d" % (key, value, hash(str(key)))
    tf = time.time()
    times.append(tf-t0)
    if hit:
        hit_count += 1
    else:
        miss_count += 1

print "Average access time: ", sum(times)/ float(len(times))
print "Hits: ", hit_count
print "Misses: ", miss_count



