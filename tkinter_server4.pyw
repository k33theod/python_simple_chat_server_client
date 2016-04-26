# Το παρών πρόγραμμα είναι ένας απλός server 
# Εισάγω τις απαραίτητες βιβλιοθήκες
from socket import *
import threading as t

# Αυτή η συνάρτηση λαμβάνει και στέλνει δεδομένα 
# Τρέχει ξεχωριστά ως thread για κάθε connection (con)
def receive_send(con):
# Το πρώτο μύνημα που στέλνει μετά από τη σύνδεση
    connection_message='Καλωσήρθατε '+ str(len(connections))+' συνδεδεμένοι χρήστες\n' 
    con.send(connection_message.encode('utf-8'))# Το κωδικοποιώ και το στέλνω    
    while True: #βρόγχος που τρέχει πάντα 
        data_recv=con.recv(1024) #ότι δεδομένα λαμβάνει
        for i in connections: #τα στέλνει σε όλους 
            i.send(data_recv)        
    con.close()		
 
def connector(): #Η συνάρτηση που κάνει τις συνδέσεις
    while True: # Τρέχει συνέχεια
        con, address = s.accept() #κάνει accept και επιστρέφει το con, address
        connections.append(con) # Βάζει το κάθε νέο con στον πίνακα των συνδέσεων
		#δημιουργώ thread για τη receive_send 
        a=t.Thread(target=receive_send, args=(con,))  
        a.start()# Το ξεκινάω 

connections=[] # πίνακας συνδέσεων

host='' # κενό 
port=8000 #port 0 έως 65535
s=socket() #normal socket μπορώ να παραλείψω τις παραμέτρους
s.bind((host, port)) # Το κάνω bind με το tuple(host, port)
s.listen(5)
# Τρέχω τη συνάρτηση connector
connector()


