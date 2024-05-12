import streamlit as st
import random
from Evento import Evento
from Gestores_de_eventos.Boleteria import Boleteria

class Teatro(Evento):
    def __init__(self):
        super().__init__()
 
        
    def set_data(self, typeOfTicket, price, capacity, status, artist, eventName, eventDate, openingTime, startTime, eventLocation, address, city, occupiedSlots, ticketsSold, event_id):
        self.type_of_ticket = typeOfTicket
        self.price = price
        self.max_capacity = capacity
        self.event_status = status
        self.artist = artist
        self.event_name = eventName
        self.event_date = eventDate
        self.opening_time = openingTime
        self.start_time = startTime
        self.event_location = eventLocation
        self.address = address
        self.city = city
        self.occupied_slots = occupiedSlots
        self.tickets_sold = ticketsSold
        self.event_id = event_id
    

    def get_occupied_slots(self, id): #Obtiene los slots ocupados
        if id in self._events:
            return self._events[id].occupied_slots
        


    def assign_slot_to_client(self, id): #Asigna un slot a un cliente
        if id in self._events:
            self._events[id].occupied_slots += 1

    def show_state(self): #Estado del evento
        return self.status

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
        return self.capacity

    def show_slots(self, show_id): #Cantidad de slots disponibles
        if show_id in self._events:
            return self._events[show_id].capacity - self._events[show_id].occupied_slots
        

    def show_tickets_sold(self, flag): #Muestra la cantidad de tickets vendidos
        if flag:
            self.tickets_sold += 1
        return self.tickets_sold

   

    def total_commision(self, show_id): #Calcula la comision del evento para obtener las ganancias
        if show_id in self._events:
            return self._events[show_id].price * 0.93
     
    
    def number_to_id(self): #Id aleatorio para identificar un evento
        number = str(random.randint(0, 10000))
        return number

    def print_details(self): #Funcion temporarl para probar si se gaurdan los eventos
        st.write(f"ID del evento: {self.show_event_id()}")
        st.write(f"Nombre del evento: {self.show_name()}")
        st.write(f"Fecha del evento: {self.show_date()}")
        st.write(f"Hora de apertura: {self.show_aperture()}")
        
        

   