# Telnet
Used for login remotely in another systems. This can be used for transfering files from one system to another.

# How to use 

         To run it as a Server (or Receiver), execute command -
         
                        python telnet.py -r

         To run it as a Client (or Sender), execute command -

                        python telnet.py -s 192.168.10.10 (server_ip)

         Login credentials
                        Username = root
                        Password = redhat

         For help -
                        python telnet.py -h
                       
                  
# File Sharing

         Receiver Command -
                           
                        python telnet.py -g
                        
         Sender Command -
                           
                        python telnet.py -f /file_path/file_name -i 192.168.10.10 -d /file_destination_path/file_name
