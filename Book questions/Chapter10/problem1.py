import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        duration = self.end - self.start
        print(f"Execution took {duration:.2f} seconds")

with Timer():
    for i in range(1000000):
        pass