from pythonping import ping

class Server:
    """Represents severs provided for the server viablilty application"""
    def __init__(self, ipAddress: str, name: str) -> None:
       self._ipAddress = ipAddress
       self._name = name
      
    def setResponse(self, min, avg, max, success):
      self._min = min
      self._max = max
      self._avg = avg
      self._success = success
    
    @property
    def ipAddress(self) -> str:
      return self._ipAddress
  
    @property
    def name(self) -> str:
      return self._name
    
    @property
    def min(self) -> str:
      return self._min
    
    @property
    def avg(self) -> str:
      return self._avg
    
    @property
    def max(self) -> str:
      return self._max
    
    @property
    def success(self) -> bool:
      return self._success
    
# 1200 payload size is relatable to average game payalods
emptyPaylod = bytearray(1200)

servers = [
  Server("96.7.137.208", "United States East"),
  Server("70.191.189.99", "United States West"),
  Server("77.74.193.94", "United Kingdom"),
  Server("45.235.47.246", "Brazil"),
  Server("185.238.200.7", "Russia"),
  Server("92.173.162.22", "France")
]

for server in servers:
  print(server.name)
  result = ping(server.ipAddress, payload=emptyPaylod, count=5, interval=1, verbose=True)

  server.setResponse(result.rtt_min_ms, result.rtt_avg_ms, max=result.rtt_max_ms, success=result.success(option=3))
  print(f'Min: {server.min}')
  print(f'Avg: {server.avg}')
  print(f'Max: {server.max}')
  print(f'Success: {server.success}')
  print('---------------')
  print('\n')

