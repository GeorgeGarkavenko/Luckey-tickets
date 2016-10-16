# Luckey ticket 

"""
Check if number num is luckey
"""
def sum_ok(num, n):
	splited_num = tuple((num % 10**n - num % 10**(n-1))/ 10**(n-1) for n in range(1, 2*n+1))
	return sum(splited_num[:n]) == sum(splited_num[-n:])

n = 4

def count_on_interval(interval):
		luckey_count = 0
		for i in range(*interval):
			if sum_ok(i, int(n/2)):
					luckey_count += 1
		return luckey_count

if __name__ == "__main__":
	
	import time
	from multiprocessing.pool import Pool
	
	parts = 50
	workers = 8
	
	# start of calculation
	start = time.time()

	part = 10**n / parts
	incremet_sum = 0
	
	intervals = []
	for i in range(parts):
		intervals.append((incremet_sum, incremet_sum + part))
		incremet_sum += part
	
	pool = Pool(workers)
	luckey_count = pool.map(count_on_interval, intervals)
	print luckey_count

	print 'Entire job took:', time.time() - start, 'probability:', (1.0 * sum(luckey_count)) / 10**n
