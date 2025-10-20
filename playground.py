import warnings
# This line ignores all warnings from the 'urllib3' package
warnings.filterwarnings("ignore", module='urllib3')


import requests
from multiprocessing import Process, Manager # Import Manager



def sendRequest(shared_list): # Function must accept the shared list
    try:
      response = requests.get("http://localhost:2000/")
      # Append to the shared list
      shared_list.append(str(response.text))

    except Exception as e:
        # It's better to print the process ID/name for debugging concurrent errors
        print(f"Process {Process.name} failed: {e}")

if __name__ == "__main__":
    # 1. Create a Manager instance
    with Manager() as manager:
        # 2. Use the manager to create a shared list
        shared_test = manager.list()

        # 3. Pass the shared list as an argument to each process
        sendRe = [
            Process(target=sendRequest, args=(shared_test,))
            for i in range(20000)
        ]

        for s in sendRe:
            s.start()

        for s in sendRe:
            s.join()

        # The length of the shared list will now be correct
        print("Total response len:", len(shared_test))



