#coding:utf-8

import msgpackrpc

class TestServer(object):
    def sum(self, x, y):
        print("called")
        return x + y

if __name__=="__main__":
    server = msgpackrpc.Server(TestServer())
    server.listen(msgpackrpc.Address("localhost", 3000))
    server.start()
