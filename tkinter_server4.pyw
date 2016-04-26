# Το παρών πρόγραμμα είναι ένας απλός server.  A simple python server 
# There are alot of issues to be solved to make this server reliable and stabile.
# Complete lack of error handling, client disconnection handling and other importan things
# However it runs fast well end sufficient for people want a siple communication tool. 

# Εισάγω τις απαραίτητες βιβλιοθήκες. Modules to import
from socket import *
import threading as t

# Αυτή η συνάρτηση λαμβάνει και στέλνει δεδομένα .Receive_send function receives and sends data to connections 
# Τρέχει ξεχωριστά ως thread για κάθε connection (con). Runs as a thread seperately for each connection 
def receive_send(con):
# Το πρώτο μύνημα που στέλνει μετά από τη σύνδεση. 1st message to each connection
    connection_message='Καλωσήρθατε '+ str(len(connections))+' συνδεδεμένοι χρήστες\n' 
    con.send(connection_message.encode('utf-8'))# Το κωδικοποιώ και το στέλνω. Encode and send. All data travel as binary streams    
    while True: #βρόγχος που τρέχει πάντα . This runs forever
        data_recv=con.recv(1024) #ότι δεδομένα λαμβάνει. Receives data
        for i in connections: #τα στέλνει σε όλους . Send them to all connections
            i.send(data_recv)        
    con.close()		
 
def connector(): #Η συνάρτηση που κάνει τις συνδέσεις. This function makes the connections
    while True: # Τρέχει συνέχεια. Runs forever
        con, address = s.accept() #κάνει accept και επιστρέφει το con, address. Accept connection at socket s and produces socket con
        connections.append(con) # Βάζει το κάθε νέο con στον πίνακα των συνδέσεων. Appends new socket at connections list
		#δημιουργώ thread για τη receive_send. Makes a Thread to receive_send function passing con as argument. 
        a=t.Thread(target=receive_send, args=(con,))  
        a.start()# Το ξεκινάω . Starts thread

connections=[] # πίνακας συνδέσεων. Connections list

host='' # κενό. It works, we dont need a hostname 
port=8000 #port 0 έως 65535. Port number to open.
s=socket() #normal socket μπορώ να παραλείψω τις παραμέτρους. Creates a normal socket s, same as s=socket(AF_INET, SOCK_STREAM)
s.bind((host, port)) # Το κάνω bind με το tuple(host, port). Binds s socket to tuple (host,port)
s.listen(5)#Listens
# Τρέχω τη συνάρτηση connector
connector()# Run the connector function


