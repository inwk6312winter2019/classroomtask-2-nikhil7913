import math
import copy
 
class Network:
   
   
   
     
    def __init__(self, ip, prefix):
       
        self.net_addr = []
        self.copy_addr = []
        self.prefix = prefix
        ip = ip.split(".")
        ad = "1"*prefix + "0"*(32-prefix)
        octet = [ad[0:8], ad[8:16], ad[16:24], ad[24:32]]
 
        for p in range(len(ip)):
            a = int(ip[p])
            b = int(octet[p], 2)
            self.net_addr.append(a&b)
        #print "Network Address:", self.net_addr
 
    def subnet(self, count):
       
         
       
        d = int(math.log(count, 2))
 
       
        target = self.prefix + d
         
       
        ad = "1"*target + "0"*(32-target)
        octet = [ad[0:8], ad[8:16], ad[16:24], ad[24:32]]
       
         
       
        move = math.ceil( target / 8.0 )
        host = (move*8) - target
         
       
        jump = 2**host
 
       
        self.copy_addr = copy.deepcopy(self.net_addr)
        for i in range(count):
            print ("#%d %-15s /%d") % (i+1, ".".join(map(str, self.copy_addr)), target)
            self.add(move, jump)
             
        print ("Every subnet has %d usable IP addresses") % (2**(32-target)-2)
 
    def add(self, octet, value):
       
        octet = int(octet)
     
        self.copy_addr[octet-1] = self.copy_addr[octet-1] + int(value)
         
       
        for i in range(octet-1, -1, -1):
            if self.copy_addr[i] >= 256:
                self.copy_addr[i] = 0
                self.copy_addr[i-1] = self.copy_addr[i-1] + 1
     
if __name__ == "__main__":
    net = input("Enter Network (d.d.d.d): ")
    pre = int(input("Enter Prefix: "))
     
   
    n = Network(net, pre)
     
    sub = int(input("Enter Number of Subnets (powers of 2 only): "))
     
   
    n.subnet(sub)
