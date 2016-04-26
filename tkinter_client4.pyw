#Το παρών πρόγραμμα είναι ένας client σε γραφικό περιβάλλον
#που καλεί ένα σερβερ με την ip ή hostname, port και username

#Εισάγω τις βιβλιοθήκες
from socket import *
from tkinter import *
from tkinter import ttk
import time
import threading as t

s=socket()#Δημιουργώ ένα socket

#Δίνω αρχικές τιμές στις μεταβλητές μου 
host=''
port=0
name=''

#Η συνάρτηση που στέλνει τα δεδομένα
def send_message(event): 
  str_message= name + ': ' + entry_client.get() + '\n' #Το μύνημα το οποίο περιέχει
  #το όνομα και αυτά που γράψαμε στο entry
  data_send=str_message.encode() #κάνουμε encode
  s.send(data_send) #το στέλνουμε
  entry_client.delete(0,END) #μηδενίζω τα στοιχεία του entry

def receive(): #Η συνάρτηση που λαμβάνει και τυπώνει τα μυνήματα στο text
  while True:  #Τρέχει συνέχεια
    data_recv=s.recv(1024) #λαμβάνει
    data_str_recv=data_recv.decode('utf-8') #κάνει decode
    message_place.config(state=NORMAL) #αλλάζει το status του text για να μπορώ να γράψω
    ora=time.strftime('%H:%M:%S ',time.localtime()) #παίρνω την τρέχουσα όρα
    if data_str_recv.startswith(name): #Αν το μύνημα αρχίζει με το όνομά μου που σημαίνει ότι είναι δικό μου 
      message_place.insert(END,ora+''+data_str_recv,'me') #το τυπώνω με άλλο χρώμα 
    else:
      message_place.insert(END,ora+data_str_recv) #αλλίως το τυπώνω μαύρο	
    message_place.config(state=DISABLED) #ξανα αλλάζω το state του text

# Η συνάρτηση που κάνει τη σύνδεση με το server
def connect():
  global name,host,port,s #Δίνω νέες τιμές στις μεταβλητές μου
  name=entry_name.get()
  win.title(name)
  host=entry_ip.get()  
  server_host=host # Εδώ μπαίνει το hostname ή η IP πχ '127.0.0.1'
  port=entry_port.get()
  port=int(port) 
  s.connect((server_host, port)) #κάνω τη σύνδεση με το tuple (server_host, port)
  a=t.Thread(target=receive) #δημιουργώ thread για τη receive 
  a.start()  #και το ξεκινάω

# Απο εδώ και κάτω το γραφικό περιβάλον
win=Tk()
win.title('CLIENT')
frame1=Frame(win)
frame1.pack(expand=True, fill='both', side='top')
  
# Το Text όπου γράφονται πληροφορίες σύνδεσεις και όλα τα μυνήματα 
message_place=Text(frame1,  wrap=WORD)
message_place.grid(row=0, column=0, columnspan=7,sticky='W', padx=5, pady=5)
message_place.config(state=DISABLED) # Το απενεργοποιώ για να μην μπορώ να γράψω
message_place.tag_configure('me', foreground='blue') #Κάνω tag με άλλο χρώμα για να το 
#χρησιμοποιήσω για τα μυνήματά μου

frame2=Frame(win)
frame2.pack(expand=True, fill='both')
#Μία ταμπέλα 
label_client=Label(frame2, text='Message: ')
label_client.grid(row=0,column=0,sticky='W',padx=5,pady=5)
  
# Το entry για να γράφω τα μυνήματα
entry_client=Entry(frame2, width=60)
entry_client.grid(row=0,column=1, sticky='W',padx=5,pady=5)
entry_client.bind("<Return>", send_message) #Με enter καλώ τη συνάρτηση που στέλνει το μύνημα
  
frame3=Frame(win)
frame3.pack(expand=True, fill='both')
  
label_ip=Label(frame3, text='IP: ', bg='white')
label_ip.pack(side='left',padx=5,pady=5)

entry_ip=Entry(frame3,width=20)
entry_ip.pack(side='left',padx=5,pady=5)

label_port=Label(frame3, text='Port: ', bg='white')
label_port.pack(side='left',padx=5,pady=5)

entry_port=Entry(frame3)
entry_port.pack(side='left',padx=5,pady=5)

label_name=Label(frame3, text='Your name: ', bg='white')
label_name.pack(side='left',padx=5,pady=5)  
  
entry_name=Entry(frame3)
entry_name.pack(side='left',padx=5,pady=5)

rec_button=ttk.Button(frame3, text='connect', command=connect) # Το κουμπί για να λαμβάνω τα μυνήματα
rec_button.pack(side='left', padx=5, pady=5 )
  
win.mainloop()







