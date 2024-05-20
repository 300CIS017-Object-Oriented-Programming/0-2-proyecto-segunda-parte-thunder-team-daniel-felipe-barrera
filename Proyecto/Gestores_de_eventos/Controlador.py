import streamlit as st
import random
from Eventos.teatro import Teatro
from Eventos.bar import Bar
from Eventos.filantropico import Filantropico
from Gestores_de_eventos.gestor_eventos import Gestor_Eventos
from Eventos.cliente import Cliente
from Gestores_de_eventos.boleteria import Boleteria

#En este archivo se piden todos los datos necesarios, se llaman a las funciones, entre otros.


class Controlador:
    def __init__(self):
        

        self.gestor_eventos = Gestor_Eventos() #Objeto de la clase Gestor_Eventos
        self.teatro = Teatro() # objeto de la clase Teatro
        self.bar = Bar() # objeto de la clase Bar
        self.filantropico = Filantropico() # objeto de la clase Filantropico
        self.boleteria = Boleteria() # objeto de la clase Boleteria
        
        
    def create_event_theater(self):
        controlador = Controlador()
        
        st.title("Welcome administrator, please input the next values")
        ticket_option = st.selectbox("The ticket is", options=[1, 2], format_func=lambda x: "Regular" if x == 1 else "Presale", key="ticket_option")
        type_of_ticket = "Regular" if ticket_option == 1 else "Presale"
        event_price = st.number_input("Please input the price of the ticket", key="wddw")

        aforo = st.number_input("Capacity of the theatre",key="aforo")
        event_status = st.text_input("State of the event",key="event_status")
        artist = st.text_input("Artist name", key = "artist")
        event_name = st.text_input("Event name", key ="event_name")
        event_date = st.text_input("Event date", key = "event_date")
        opening_time = st.text_input("Opening time",key = "opening_time")
        start_time = st.text_input("Start time", key = "start_time")
        event_location = st.text_input("Event location", key = "event_location")
        address = st.text_input("Address", key = "address")
        city = st.text_input("City", key = "city")
        event_id = self.teatro.number_to_id()
        
        if st.button("Create event", key = "dauwyduawd"):
            if all([type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city]):
                object_theater = self.teatro.set_data(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                controlador.gestor_eventos.add_event(object_theater)
                
                st.success("The event was succesfully created")
            else:
                st.error("Fill all the blank camps")
        

    def create_event_bar(self):
        controlador = Controlador()
        
        st.title("Welcome administrator, please input the next values")
        
        ticket_option = st.selectbox("The ticket is", options=[1, 2], format_func=lambda x: "Regular" if x == 1 else "Presale", key = "jkawhdvidhopke")
        type_of_ticket = "Regular" if ticket_option == 1 else "Presale"
        event_price = st.number_input("Please input the price of the ticket", key = "dwadwadw")

        aforo = st.number_input("Capacity of the bar", key = "daawdwad")
        event_status = st.text_input("State of the event", key ="w")
        artist = st.text_input("Artist name", key = "wdwadwadwa")
        event_name = st.text_input("Event name", key = "jadawhbda")
        event_date = st.text_input("Event date", key = "kjawdbahdwad")
        opening_time = st.text_input("Opening time", key = "kladabdadwd")
        start_time = st.text_input("Start time", key = "89371bnkm")
        event_location = st.text_input("Event location", key = "kldjhwvqd")
        address = st.text_input("Address", key = "ioiruf3ygq2eow")
        city = st.text_input("City", key = "jlkadhcawvdi")
        event_id = self.bar.number_to_id()
        
        if st.button("Create event", key = "jkdhbwf"):
            if all([type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city]):
                object_bar = self.bar.set_data(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                controlador.gestor_eventos.add_event(object_bar)
                
                st.success("El evento fue creado exitosamente!!")
                
                
            else:
                st.error("Por favor complete todos los campos")
        

    def create_event_filantropic(self):
        controlador = Controlador()
        type_of_event = "Filantropico"
        st.title("Welcome administrator, please input the next values")
        ticket_option = st.selectbox("The ticket is", options=[1, 2], format_func=lambda x: "Regular" if x == 1 else "Presale", key = "jwhduvadhw")
        type_of_ticket = "Regular" if ticket_option == 1 else "Presale"
        sponsor = st.text_input("Please input the sponsor name", key = "j213123")
        event_price = st.number_input("Hi {}, please input the amount of money you want to spend in this event".format(sponsor), key = "jdawhdwk")
        aforo = st.number_input("Capacity of the filantropic event", key = "891238t124")
        event_status = st.text_input("State of the event", key = "idahbmawfe")
        artist = st.text_input("Artist name", key = "jkdabwada")
        event_name = st.text_input("Event name", key = "akjdbhawjdbaw")
        event_date = st.text_input("Event date", key = "jhfvaydnaw")
        opening_time = st.text_input("Opening time", key = "uidaywbna")
        start_time = st.text_input("Start time", key = "jdvagwdh")
        event_location = st.text_input("Event location", key = "kfjgvahbjdk")
        address = st.text_input("Address", key = "KLhjadvjbnk")
        city = st.text_input("City", key = "jkadyuybwa")
        event_id = self.filantropico.number_to_id()
        
        if st.button("Create event", key = "dawjdhgawdva"):
            if all([type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city]):
                filantropic = self.filantropico.set_data(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                controlador.gestor_eventos.add_event(filantropic)
                
                st.success("The event was succesfully created")
            else:
                st.error("Please complete the blank camps")
        

    
    def register_user_to_event(self):
        no_more_slots = False
        controller = Controlador()
        user_id = str(random.randint(0, 10000))
      
        
        st.title("Welcome user, please select the type of event you want to attend or mark attend to the event you want to attend")
        selected_event_type = st.selectbox("Select event type", options=["Teatro", "Bar", "Filantropico", "Register attendance"], key="event_type")
        if(selected_event_type == "Register attendance"):
            self.register_attend()
        else:
            
            ticket_type = st.selectbox("Select ticket type", options=["Presale", "Regular"], key="ticket_type")
            
            controller.gestor_eventos.show_event(selected_event_type)
                
            st.title("Welcome user, please input the next values")
            name = st.text_input("Name", key = "name")
            email = st.text_input("Email", key = "email")
            phone = st.text_input("Phone", key = "phone")
            address = st.text_input("Address", key = "address")
            city = st.text_input("City", key = "city")
            payment = st.text_input("Payment method", key = "payment")
            money = st.number_input("Money", key = "money")
            event_id = st.text_input("Write the ID of the event you want to enter", key = "awdwdawd")
                
            if st.button("Register", key = "register"):
                event = controller.gestor_eventos.find_event(event_id)
                if(event.get_occupied_slots() == event.event_capacity()):
                    st.error("Sorry, there's no more slots available for this event")
                    no_more_slots = True
                    
                elif (money < event.event_price()):
                    st.error("You don't have enough money to attend this event")
                        
                elif all([name, email, phone, address, city, payment, money, event_id]) and not no_more_slots:
                    st.success("The user was succesfully registered")
                    st.write(f"This is your ID, don't forget it!! {user_id}")
                    client = Cliente(name, user_id, city, address, payment, email, phone, money, selected_event_type)
                    controller.boleteria.add_client(client)
                    controller.boleteria.add_ticket(name, user_id, selected_event_type, event_id, ticket_type, payment)
                    event.add_ticket_sold()
                    event.assign_slot_to_client()
                        
                        
                        
                else:
                    st.error("Fill all the blank camps")
                    
    def register_attend(self):
        controller = Controlador()
        
        st.write("Welcome user, please input the next values to register your attendance") 
        event_id = st.text_input("Write the ID of the event you want to attend", key = "event_id")
        if (st.button("Register attendance", key = "register")):
            register = controller.boleteria.register_attendance(event_id)
            if not register:
                st.error("The event was not found or you're not in the list")
            else:
                st.success("You were succesfully registered")
        
            
    
                    
    def delete_event(self):
        controller = Controlador()
        st.title("Welcome administrator, please select the type of event you want to delete")
        selected_event_type = st.selectbox("Select event type", options=["-- Select a event --", "Teatro", "Bar", "Filantropico"], key="event_type")
        event_id = st.text_input("Write the ID of the event you want to delete", key = "event_id")
        
        if st.button("Delete event", key = "delete"):
            controller.gestor_eventos.delete_a_event(event_id)
            st.success("The event was succesfully deleted")
            
    def generate_ticket(self):
        controller = Controlador()
        st.title("Welcome admin, please input the next values to generate your ticket")
        client_id = st.text_input("Write the ID of the client", key = "client_id")
        if st.button("Generate ticket", key = "generate"):
            controller.boleteria.create_pdf(client_id)
            st.success("The ticket was succesfully generated")
        
        