import streamlit as st

from Eventos.Teatro import Teatro
from Eventos.Bar import Bar
from Eventos.Filantropico import Filantropico
from Gestores_de_eventos.Gestor_Eventos import Gestor_Eventos

class Controlador:
    def __init__(self):

        self.gestor_eventos = Gestor_Eventos()
        self.teatro = Teatro()
        self.barr = Bar()
        self.filantropico = Filantropico()
        
        
    def theater(self):
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
                self.teatro.set_data(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                controlador.gestor_eventos.add_event(self.teatro)
                self.teatro.print_details()
                st.success("The event was succesfully created")
            else:
                st.error("Fill all the blank camps")
        

    def bar(self):
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
        event_id = self.barr.number_to_id()
        
        if st.button("Create event", key = "jkdhbwf"):
            if all([type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city]):
                self.barr.set_data(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                controlador.gestor_eventos.add_event(self.barr)
                
                st.success("El evento fue creado exitosamente!!")
                
                
            else:
                st.error("Por favor complete todos los campos")
        

    def filantropic(self):
        controlador = Controlador()
        
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
                self.filantropico.set_data(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                controlador.gestor_eventos.add_event(self.filantropico)
                
                st.success("El evento fue creado exitosamente!!")
            else:
                st.error("Por favor complete todos los campos")
        