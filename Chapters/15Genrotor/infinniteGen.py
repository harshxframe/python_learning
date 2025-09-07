# Learn about infinite generator

def infinite_send():
    count = 1
    while True:
        yield f"Refill {count}"
        count += 1



refill = infinite_send()

for _  in range(3):
    print(next(refill))