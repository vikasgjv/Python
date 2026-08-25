# MultiProcessing

import multiprocessing
import requests


def downloadFile(url, name):
    print(f"Started Downloading {name}")

    response = requests.get(url)

    open(f"files2/file{name}.jpg", "wb").write(response.content)

    print(f"Finished Downloading {name}")


url = "https://picsum.photos/2000/3000"

# Create multiple processes
processes = []

for i in range(5):
    p = multiprocessing.Process(
        target=downloadFile,
        args=[url, i]
    )
    p.start()
    processes.append(p)

# Wait for all processes to finish
for p in processes:
    p.join()


 