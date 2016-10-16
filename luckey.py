# Luckey ticket 

"""
Check if number num is luckey
"""
def sum_ok(num, n):
	splited_num = tuple((num % 10**n - num % 10**(n-1))/ 10**(n-1) for n in range(1, 2*n+1))
	return sum(splited_num[:n]) == sum(splited_num[-n:])

luckey_count = 0

def main():
	import threading
	import time
	from Queue import Queue
	
	q = Queue()
	lock = threading.Lock()

	n = 6
	parts = 10
	
	threads = 2
	
	def count_on_interval(interval):
		global luckey_count
		for i in range(*interval):
			if sum_ok(i, int(n/2)):
				with lock:
					#print threading.current_thread().name, 'found: ', i, 'on ', interval
					luckey_count += 1
	
	def threader():
		while True:
			interval = q.get()
			count_on_interval(interval)
			q.task_done()
	
	# threads initialization
	for x in range(threads):
		 t = threading.Thread(target=threader)
	
		 # classifying as a daemon, so they will die when the main dies
		 t.daemon = True
	
		 # begins, must come after daemon definition
		 t.start()
	
	# start of calculation
	start = time.time()

	part = 10**n / parts
	incremet_sum = 0
	
	for i in range(parts):
		q.put((incremet_sum, incremet_sum + part))
		incremet_sum += part
	
	# wait until the thread terminates.
	q.join()

	print 'Entire job took:', time.time() - start, 'probability:', (1.0 * luckey_count) / 10**n

if __name__ == "__main__":
	main()