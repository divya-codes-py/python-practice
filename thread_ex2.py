import threading
import time

def download_file(filename, size):
    print(f"⬇️ Downloading {filename}...")
    time.sleep(size)
    print(f"✅ {filename} download complete!")

thread1 = threading.Thread(target=download_file, args=("file1.txt", 1))
thread2 = threading.Thread(target=download_file, args=("file2.txt", 2))
thread3 = threading.Thread(target=download_file, args=("file3.txt", 3))

start = time.time()

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

end = time.time()
print(f"\n⏱️ Total time: {round(end - start, 2)} seconds")
