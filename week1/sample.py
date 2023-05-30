import pandas as pd

def cal():
    for i in range(1, 10, 2):
        for j in range(1, 10):
            #if i%2==0: break
            print(f"{i}*{j}={i*j}")

if __name__ == '__main__':
    cal()