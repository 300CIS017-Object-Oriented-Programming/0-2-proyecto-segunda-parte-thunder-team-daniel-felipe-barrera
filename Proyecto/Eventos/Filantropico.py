import random
from Evento import Evento 


class Filantropico(Evento):
    def __init__(self):
        # Variables de beneficio
        super().__init__()
       
    # Funciones de configuración de datos del evento
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
    
    def set_stats(self):
        self.event_id = self.number_to_id()


    def show_state(self):
        return self.eventStatus

    def artist_name(self):
        return self.artist

    def show_name(self):
        return self.eventName

    def show_date(self):
        return self.event_date

    def show_aperture(self):
        return self.opening_time

    def show_time(self):
        return self.start_time

    def show_location(self):
        return self.event_location

    def show_address(self):
        return self.address

    def show_city(self):
        return self.city

    def show_type_of_ticket(self):
        return self.type_of_ticket

    def show_event_id(self):
        return self.event_id

    def event_price(self):
        return self.price

    def event_capacity(self):
        return self.max_capacity

    def show_tickets_sold(self, flag):
        if flag:
            self.tickets_sold += 1
        return self.tickets_sold
    
    def number_to_id(self):
        number = str(random.randint(0, 10000))
        return number

    def show_slots(self, show_id): #TODO cambiar para que use la lista de los eventos en la clase Gestor_Eventos, porque no existen esos diccionarios actualmente
        if show_id in self.__filantropic_events:
            avaible_slots = self.__filantropic_events[show_id].max_capacity - self.__filantropic_events[show_id].occupied_slots
        else:
            avaible_slots = 0
        return avaible_slots

    def assign_slot_to_client(self, id):
        if id in self.__filantropicEvents:
            if self.__filantropicEvents[id].occupiedSlots < self.__filantropicEvents[id].maxCapacity:
                self.__filantropicEvents[id].occupiedSlots += 1


    def get_occupied_slots(self, id):
        finalOccupiedSlots = 0
        if id in self.__filantropicEvents:
            finalOccupiedSlots = self.occupiedSlots
        return finalOccupiedSlots
    
    def total_commision(self, show_id):
        return 0