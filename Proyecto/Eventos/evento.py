from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self):
 
        self.event_status = ""         # Estado del evento
        self.artist = ""               # Nombre del artista
        self.event_name = ""           # Nombre del evento
        self.event_date = ""           # Fecha
        self.opening_time = ""         # Hora de apertura
        self.start_time = ""           # Hora de inicio
        self.event_location = ""       # Lugar
        self.address = ""              # Dirección
        self.city = ""                 # Ciudad
        self.type_of_ticket = ""       # Tipo de ticket (regular o preventa)
        self.event_id = ""             # ID del evento
        self.occupied_slots = 0         # Espacios ocupados
        self.price = 0.0               # Precio del evento
        self.max_capacity = 0           # Capacidad máxima
        self.tickets_sold = 0           # Número de tickets vendidos
        self.comission = 0.0           # Comisión por venta

    @abstractmethod
    def set_data(self, type_of_ticket, price, aforo, status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, occupied_slots, tickets_sold, event_id):
        pass

    @abstractmethod
    def show_state(self):
        pass

    @abstractmethod
    def artist_name(self):
        pass

    @abstractmethod
    def show_name(self):
        pass

    @abstractmethod
    def show_date(self):
        pass

    @abstractmethod
    def show_aperture(self):
        pass

    @abstractmethod
    def show_time(self):
        pass

    @abstractmethod
    def show_location(self):
        pass

    @abstractmethod
    def show_address(self):
        pass

    @abstractmethod
    def show_city(self):
        pass

    @abstractmethod
    def show_type_of_ticket(self):
        pass

    @abstractmethod
    def show_event_id(self):
        pass

    @abstractmethod
    def event_price(self):
        pass

    @abstractmethod
    def event_capacity(self):
        pass

    @abstractmethod
    def show_slots(self):
        pass

    @abstractmethod
    def show_tickets_sold(self):
        pass

    @abstractmethod
    def total_commision(self, show_id):
        pass
    
    @abstractmethod
    def number_to_id(self):
        pass