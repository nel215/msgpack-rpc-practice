require 'msgpack/rpc'

c = MessagePack::RPC::Client.new('localhost', 3000)
result = c.call(:sum, 1, 2)
puts(result)
