# Luckey ticket 

"""
Check if number num is luckey
"""

n = 3

# n = 4
# 
# time 490.384 sec
# p = 0.0481603

def count_on_interval(interval):
		# intitialize
		luckey_count = 0
		
		a = bytearray(('{:0'+ str(2*n)+'d}').format(interval[0])[-2*n:])
		b = bytearray(('{:0'+ str(2*n)+'d}').format(interval[1])[-2*n:])
		print '(', a, b, ')'
		
		# count
		while a != b:
			# check
			# print a
			if sum(map(lambda x: x-48, a[:n])) == sum(map(lambda x: x-48, a[-n:])):
				# print '!'
				luckey_count += 1
			
			# next value
			for i in range(2*n, 0, -1):
				if a[i-1] == 57:
					a[i-1] = 48
					continue
				else:
					a[i-1] += 1
					break
			
		# print luckey_count
		return luckey_count

if __name__ == "__main__":
	
	import time
	from multiprocessing.pool import Pool
	
	parts = 1000
	workers = 100
	
	# start of calculation
	start = time.time()

	part = 10**(n*2) / parts
	incremet_sum = 0
	
	intervals = []
	for i in range(parts):
		intervals.append((incremet_sum, incremet_sum + part))
		incremet_sum += part
	
	
	# # with 1 process
	# luckey_count = map(count_on_interval, intervals)
	# print luckey_count
	
	# with a pool of processes
	pool = Pool(workers)
	luckey_count = pool.map(count_on_interval, intervals)
	print luckey_count
	
	print 'Entire job took:', time.time() - start, 'probability:', (1.0 * sum(luckey_count)) / 10**(n*2)
