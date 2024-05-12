
from Evento import Evento
from Gestores_de_eventos import Boleteria
import random


class Bar(Evento):
    def __init__(self):
        super().__init__()
       

    # Event data configuration functions
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

    def set_bar_id(self):
        self._bar_id = str(self._generate_bar_random_number())


    # Functions to get event information
    def get_bar_id(self):
        return self._bar_id

    def show_state(self):
        return self.event_status

    def artist_name(self):
        return self.artist

    def show_name(self):
        return self.event_name

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
    
    # Utility functions
    def random_number(self):
        return random.randint(0, 10000)

    def show_tickets_sold(self, flag):
        if flag:
            self.tickets_sold += 1
        return self.tickets_sold

    def show_slots(self, show_id):
        if show_id in self._bar_events:
            return self._bar_events[show_id].max_capacity - self._bar_events[show_id].occupied_slots
        

    def assign_slot_to_client(self, id):
        if id in self._bar_events and self._bar_events[id].occupied_slots < self._bar_events[id].max_capacity:
            self._bar_events[id].occupied_slots += 1

    # Profit calculation and management functions
    def total_commision(self, show_id):
        if show_id in self._bar_events:
            return self._bar_events[show_id].price * 0.2
       

    def get_occupied_slots(self, id):
        if id in self._bar_events:
            return self._bar_events[id].occupied_slots
        
    
    def number_to_id(self):
        number = str(random.randint(0, 10000))
        return number