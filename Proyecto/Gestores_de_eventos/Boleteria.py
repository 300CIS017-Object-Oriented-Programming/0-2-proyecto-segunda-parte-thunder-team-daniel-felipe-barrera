import streamlit as st

from Eventos.cliente import Cliente
from Gestores_de_eventos import generar_boleta
from Gestores_de_eventos.gestor_eventos import Gestor_Eventos


class Boleteria:
    def __init__(self):
        if "tickets" not in st.session_state:
            st.session_state["tickets"] = []
        if "clients" not in st.session_state:
            st.session_state["clients"] = []
        
        self.tickets = st.session_state["tickets"]
        self.clients = st.session_state["clients"]

        self.client = ""
        self.client_id = ""
        self.type_of_event = ""
        self.event_id = ""
        self.type_of_ticket = ""
        self.payment_method = ""
        self.attendance = None
        
        
    def set_data(self, client, client_id, type_of_event, event_id, type_of_ticket, payment_method):
        
        self.client = client
        self.client_id = client_id
        self.type_of_event = type_of_event
        self.event_id = event_id
        self.type_of_ticket = type_of_ticket
        self.payment_method = payment_method
        self.attendance = False
        
        
        return self #Se retorna un obejto de tipo Boleteria (el ticket)
        
        
    def add_ticket(self, client, client_id, type_of_event , event_id ,type_of_ticket, payment_method):
        
        ticket = self.set_data(client, client_id, type_of_event, event_id, type_of_ticket, payment_method)
        self.tickets.append(ticket)
        st.session_state["tickets"] = self.tickets
        
    
    def add_client(self,client):
        self.clients.append(client)
        st.session_state["clients"] = self.clients
        
    def get_client(self):
        return self.client
    
    def get_client_id(self):
        return self.client_id

    def get_type_of_event(self):
        return self.type_of_event
    
    def get_event_id(self):
        return self.event_id
    
    def get_type_of_ticket(self):    
        return self.type_of_ticket
    
    def get_payment_method(self):
        return self.payment_method

    def get_attendance(self):
        return self.attendance
    
    def get_client_data(self, client_id):
        found = False
        for client in self.clients:
            if isinstance(client, Cliente) and client.get_user_id() == client_id:
                found = True
        if not found:
            st.error("Client not found")
        if found:
            return client        
        
            
    def register_attendance(self, client_id):
        found = False
        for ticket in self.tickets:
            if isinstance(ticket, Boleteria) and ticket.get_event_id() == client_id:
                ticket.attendance = True
                found = True
                
        return found

    def get_tickets(self):
        return self.tickets
    
    def create_pdf(self, client_id):
        events_instance = Gestor_Eventos()
        boleteria_instance = Boleteria()
        tickets = self.get_tickets()
        generar_boleta.generate_ticket_pdf(boleteria_instance, tickets, client_id, events_instance)
        
            
                
        
        