start "" curl -s -G "http://192.168.1.200:8080/action?action=5"
ping 127.0.0.1 -n 2 > nul
start "" curl -s -G "http://192.168.1.200:8080/action?action=7"
ping 127.0.0.1 -n 2 > nul                     
start "" curl -s -G "http://192.168.1.200:8080/action?action=8"
ping 127.0.0.1 -n 2 > nul                     
start "" curl -s -G "http://192.168.1.200:8080/action?action=11"
ping 127.0.0.1 -n 2 > nul                  
start "" curl -s -G "http://192.168.1.200:8080/action?action=12"
ping 127.0.0.1 -n 2 > nul                   
start "" curl -s -G "http://192.168.1.200:8080/action?action=13"
exit
