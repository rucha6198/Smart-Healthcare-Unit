#******************Imports*******************************************************************
from tkinter import *
import paho.mqtt.client as mqtt
import tk_tools
import pandas as pd
import plotly.express as px
import shutil

#*****************Indirect Communication****************************************************
#Subscribing to publisher to retrieve live data from sensors
#mqttBroker = "192.168.1.108"
mqttBroker = "broker.emqx.io"
client = mqtt.Client("Smartphone")

#*****************Creating csv file for creating Graphs***************************************
newPath = shutil.copy('D:\Pub_Sub\IOT_DATA.csv', 'D:\Pub_Sub\Dashboard\IOT_DATA.csv')
df = pd.read_csv('D:\Pub_Sub\Dashboard\IOT_DATA.csv')
df.head()

#****************Creating a window for Dashboard with dimensions*****************************
window = Tk()
window.title("+Smart Healthcare Unit Dashboard+")
window.geometry('1350x800')
window.resizable(True,True)
window.configure(bg="white")

#creating canvas for all actuators
canvas4 = Canvas(window, bg="white", width=100,height=100)
canvas4.place(x=760,y=130)
led = tk_tools.Led(canvas4, size=50)
led.pack()

canvas5 = Canvas(window, bg="white", width=100,height=100)
canvas5.place(x=760,y=270)
led1 = tk_tools.Led(canvas5, size=50)
led1.pack()

canvas6 = Canvas(window, bg="white", width=100,height=100)
canvas6.place(x=760,y=440)
led2 = tk_tools.Led(canvas6, size=50)
led2.pack()

canvas7 = Canvas(window, bg="white", width=100,height=100)
canvas7.place(x=460,y=620)
led3 = tk_tools.Led(canvas7, size=50)
led3.pack()


#************************************* Sensor received data from RPi ***********************************
def on_message(client, userdata, message):
    excel_data = {}
    s = str(message.payload.decode("utf-8"))
    print("Received message: ", s)
    #print(s)
    payload_data = eval(s)
    #payload_data = ast.literal_eval(s)
    print(payload_data)
    excel_data = {'Time': None, 'Temperature': None, 'Humidity': None, 'Pressure' : None, 'Motion' : None, 'Alert' : None, 'Light_int' : None}
    
    
    if 'Time' in payload_data and payload_data['Time'] is not None :
        excel_data['Time'] = payload_data['Time']
        
    if 'Temperature' in payload_data and payload_data['Temperature'] is not None:
        excel_data['Temperature'] = payload_data['Temperature']
        if  excel_data['Temperature'] > 0 :
            label1 = Label(window,text=excel_data['Temperature'],bg="white",fg="grey",font=("Helvetica",20))
            label1.place(x=180,y=170)
            
    if 'Humidity' in payload_data and payload_data['Humidity'] is not None:        
        excel_data['Humidity'] = payload_data['Humidity']
        if  excel_data['Humidity'] > 0 :
            label4 = Label(window,text=excel_data['Humidity'],bg="white",fg="grey",font=("Helvetica",20))
            label4.place(x=180,y=300)

    if 'Motion' in payload_data and payload_data['Motion'] is not None:
        excel_data['Motion'] = payload_data['Motion']

    if 'Pressure' in payload_data and payload_data['Pressure'] is not None:
        excel_data['Pressure'] = payload_data['Pressure']
        if  excel_data['Pressure'] > 10 :
            label7 = Label(window,text=excel_data['Pressure'],bg="white",fg="grey",font=("Helvetica",20))
            label7.place(x=180,y=470)
            label31 = Label(window,text="%",bg="white",fg="grey",font=("Helvetica",20))
            label31.place(x=220,y=470)
        else:
            label30 =Label(window,text="10",bg="white",fg="grey",font=("Helvetica",20))
            label30.place(x=180,y=470)

    if  excel_data['Pressure'] > 100 :
        label29 = Label(window,text="99%",bg="white",fg="grey",font=("Helvetica",20))
        label29.place(x=180,y=470)

    if 'Alert' in payload_data and payload_data['Alert'] is not None:
        excel_data['Alert'] = payload_data['Alert']
        

    if 'Light_int' in payload_data and payload_data['Light_int'] is not None:
        excel_data['Light_int'] = payload_data['Light_int']
    
    #print("Publisher data : , {payload_data}")
    #print("Excel data : , {excel_data}")
    
    #***************Displaying i/p's and o/p's on dashboard window as per required************************************************
    if  excel_data['Temperature'] < 30 :
        label2 = Label(window,text="Heater ON  ",bg="white",fg="grey",font=("Helvetica",20))
        label2.place(x=540,y=130)
        led.to_green()
    else:
        label3 = Label(window,text="Heater OFF",bg="white",fg="grey",font=("Helvetica",20))
        label3.place(x=540,y=130)
        led.to_red()

    if  excel_data['Humidity'] < 40 :
        label5 = Label(window,text="Humidifier ON ",bg="white",fg="grey",font=("Helvetica",20))
        label5.place(x=540,y=260)
        led1.to_green()
    else:
        label6 = Label(window,text="Humidifier OFF",bg="white",fg="grey",font=("Helvetica",20))
        label6.place(x=540,y=260)
        led1.to_red()    

    if  excel_data['Pressure'] < 25 :
        label8 = Label(window,text="Low     Pressure",bg="white",fg="grey",font=("Helvetica",20))
        label8.place(x=540,y=430)
        led2.to_red()
    else:
        label9 = Label(window,text="Normal Pressure",bg="white",fg="grey",font=("Helvetica",20))
        label9.place(x=540,y=430)  
        led2.to_green()

    if  excel_data['Motion'] == 1 :
        label22 = Label(window,text="Motion       Detected",bg="white",fg="grey",font=("Helvetica",20))
        label22.place(x=180,y=620)
        led3.to_green()
    else:
        label23 = Label(window,text="Motion not Detected",bg="white",fg="grey",font=("Helvetica",20))
        label23.place(x=180,y=620)
        led3.to_red()

    if  excel_data['Alert'] == 1 :
        label24 = Label(window,text="FIRE!!!",bg="white",fg="red",font=("Helvetica",80))
        label24.place(x=1000,y=130)
    else:
        label25 = Label(window,text="NORMAL!!!",bg="white",fg="white",font=("Helvetica",80))
        label25.place(x=1000,y=130)

    if  excel_data['Light_int'] > 300 :
        label26 = Label(window,text="Power Saver ON  ",bg="white",fg="grey",font=("Helvetica",20))
        label26.place(x=570,y=620)
    else:
        label27 = Label(window,text="Power Saver OFF",bg="white",fg="grey",font=("Helvetica",20))
        label27.place(x=570,y=620)

#********************creating canvas for all images used in dashboard************************************************
canvas = Canvas(window, bg="white", width=150,height=150)
canvas.place(x=0,y=100)
img = PhotoImage(file="temp.png")
canvas.create_image(0,0,anchor=NW,image=img)

canvas2 = Canvas(window, bg="white", width=150,height=150)
canvas2.place(x=0,y=260)
img2 = PhotoImage(file="humidity.png")
canvas2.create_image(0,0,anchor=NW,image=img2)

canvas3 = Canvas(window, bg="white", width=150,height=150)
canvas3.place(x=0,y=420)
img3 = PhotoImage(file="pressure.png")
canvas3.create_image(0,0,anchor=NW,image=img3)

canvas8 = Canvas(window, bg="white", width=150,height=150)
canvas8.place(x=0,y=580)
img4 = PhotoImage(file="motion.png")
canvas8.create_image(0,0,anchor=NW,image=img4)

canvas9 = Canvas(window, bg="white", width=65,height=65)
canvas9.place(x=275,y=15)
img5 = PhotoImage(file="sign.png")
canvas9.create_image(0,0,anchor=NW,image=img5)

canvas10 = Canvas(window, bg="white", width=65,height=65)
canvas10.place(x=1220,y=15)
img6 = PhotoImage(file="sign.png")
canvas10.create_image(0,0,anchor=NW,image=img6)

canvas11 = Canvas(window, bg="white", width=350,height=350)
canvas11.place(x=1000,y=400)
img7 = PhotoImage(file="hospital.png")
canvas11.create_image(0,0,anchor=NW,image=img7)

#*******************creating label texts for all images used in dashboard***************************************   
label10 = Label(window,text="Smart Healthcare Unit",bg="white",fg="black",font=("Helvetica",65))
label10.place(x=350,y=0)

label11 = Label(window,text="Temperature:",bg="white",fg="grey",font=("Helvetica",20))
label11.place(x=180,y=130)

label12 = Label(window,text="Setpoint:",bg="white",fg="grey",font=("Helvetica",20))
label12.place(x=360,y=130)

label13 = Label(window,text="30",bg="white",fg="grey",font=("Helvetica",20))
label13.place(x=360,y=170)

label14 = Label(window,text="Humidity:",bg="white",fg="grey",font=("Helvetica",20))
label14.place(x=180,y=260)

label15 = Label(window,text="Setpoint:",bg="white",fg="grey",font=("Helvetica",20))
label15.place(x=360,y=260)

label17 = Label(window,text="40",bg="white",fg="grey",font=("Helvetica",20))
label17.place(x=360,y=300)

label18 = Label(window,text="Pressure:",bg="white",fg="grey",font=("Helvetica",20))
label18.place(x=180,y=430)

label19 = Label(window,text="Setpoint:",bg="white",fg="grey",font=("Helvetica",20))
label19.place(x=360,y=430)

label20 = Label(window,text="25%",bg="white",fg="grey",font=("Helvetica",20))
label20.place(x=360,y=470)

#****************Creating graph from live data**************************************************************
fig = px.line(df, x = 'Time', y = 'Temperature', title='Temperature in °C')
fig.show()

fig1 = px.line(df, x = 'Time', y = 'Humidity', title='Humidity in %')
fig1.show()

fig2 = px.line(df, x = 'Time', y = 'Pressure', title='Pressure in %')
fig2.show()

#****************Running the dashboard and Subscriber till stopped******************************************
client.connect(mqttBroker)

client.loop_start()

client.subscribe("HEALTH")
client.on_message = on_message
#time.sleep(2)

window.mainloop()
client.loop_forever()
