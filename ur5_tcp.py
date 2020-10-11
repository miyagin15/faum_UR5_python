import socket
import time

HOST = "192.168.10.108"
PORT = 30002

def toBytes(str):
    return bytes(str.encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(toBytes("movej([1.57*2,0,-1.57*1.8,0,-1.57/2,1.57], a=1.40, v=1.04)" + "\n"))
    # ラジアン
    time.sleep(0.5)
    data = s.recv(1024)
    s.close()
    print("Receved", repr(data))
    print("Program finish")

if __name__ == '__main__':
    main()