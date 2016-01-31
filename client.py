#coding:utf-8

import msgpackrpc

if __name__=="__main__":
    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 3000))
    result = client.call("sum", 1, 2)
    print(result)
