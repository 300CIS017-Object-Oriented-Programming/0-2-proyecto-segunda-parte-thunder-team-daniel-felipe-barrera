import streamlit as st
import random
from Eventos.evento import Evento


class Teatro(Evento):
    def __init__(self):

        super().__init__()
 
        
    def set_data(self, type_of_ticket, price, capacity, status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, occupied_slots, tickets_sold, event_id):
        
        self.type_of_ticket = type_of_ticket
        self.price = price
        self.max_capacity = capacity
        self.event_status = status
        self.artist = artist
        self.event_name = event_name
        self.event_date = event_date
        self.opening_time = opening_time
        self.start_time = start_time
        self.event_location = event_location
        self.address = address
        self.city = city
        self.occupied_slots = occupied_slots
        self.tickets_sold = tickets_sold
        self.event_id = event_id
        
        return self
    

    
        
    def show_state(self): #Estado del evento
        return self.event_status

    def artist_name(self): #Nombre del artista
        return self.artist

    def show_name(self): #Nombre del evento
        return self.event_name

    def show_date(self): #Fecha del evento
        return self.event_date

    def show_aperture(self): #Hora de apertura del evento
        return self.opening_time

    def show_time(self): #Hora de inicio del evento
        return self.start_time

    def show_location(self): #Ubicacion del evento
        return self.event_location

    def show_address(self): #Direccion del evento
        return self.address

    def show_city(self): #Ciudad del evento
        return self.city

    def show_type_of_ticket(self): #Tipo de ticket
        return self.type_of_ticket

    def show_event_id(self): #Id del evento
        return self.event_id

    def event_price(self): #Precio del evento
        return self.price

    def event_capacity(self): #Capacidad del evento
        return self.max_capacity

    def show_slots(self): #Cantidad de slots disponibles
        avaible_slots = self.event_capacity() - self.get_occupied_slots()
        return avaible_slots
    
    def get_occupied_slots(self): #Obtiene los slots ocupados
        return self.occupied_slots
        

    def show_tickets_sold(self): #Muestra la cantidad de tickets vendidos
        return self.tickets_sold
    
    def add_ticket_sold(self): #Agrega un ticket vendido
        self.tickets_sold += 1
        


    def total_commision(self, show_id):
        commision = self.event_price() * 0.93
        return commision
        
    
    def assign_slot_to_client(self):
        
        if self.get_occupied_slots() < self.event_capacity():
            self.occupied_slots += 1
        
        
     
    
    def number_to_id(self): #Id aleatorio para identificar un evento
        number = str(random.randint(0, 10000))
        return number

        

    """
        def add_ticket_sold(self, show_id): #Agrega un ticket vendido
        stop = False
        list_events = self.gestor_eventos.get_events()
        for event in list_events:
            if not stop and isinstance(event, Teatro):
                if event.show_event_id() == show_id:
                    event.tickets_sold += 1
                    stop = True
                    
                    
        def total_commision(self, show_id):
        stop = False
        list_events = self.gestor_eventos.get_events()
        comission = None
        for event in list_events:
            if not stop and isinstance(event, Teatro):
                if event.show_event_id() == self.event_id:
                    comission = event.event_price() * 0.93
                    stop = True
        return comission
        
        
        
        def assign_slot_to_client(self, id):
        stop = False
        list_events = self.gestor_eventos.get_events()
        
        for event in list_events:
            if not stop and isinstance(event, Teatro):
                if event.show_event_id() == id:
                    if event.get_occupied_slots() < event.event_capacity():
                        event.occupied_slots += 1
                        stop = True
    """