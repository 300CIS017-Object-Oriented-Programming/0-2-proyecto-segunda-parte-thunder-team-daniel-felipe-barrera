import streamlit as st
from Eventos.teatro import Teatro
from Eventos.bar import Bar
from Eventos.filantropico import Filantropico  

#Ajustes, que no todo quede en session_states, los nombres de los archivos con minusculas
#Cambiar los nombres de la funciones para que sean más descriptivos

class Gestor_Eventos:
    def __init__(self):
        if 'events' not in st.session_state:
            st.session_state['events'] = []
        if 'events_stats' not in st.session_state:
            st.session_state['events_stats'] = {}

        self.events = st.session_state['events']
        self.events_stats = st.session_state['events_stats']
        self.teatro = Teatro()
        self.bar = Bar()
        self.filantropico = Filantropico()
        
        
    def add_event(self, event):
        self.events.append(event)
        st.session_state['events'] = self.events
    
    def add_event_stats(self, event_id, event_stats):
        self.events_stats[event_id] = event_stats
        st.session_state['events_stats'] = self.events_stats

    def show_all_artist_tickets_sold(self, artist): #TODO
        found = False
        for event in st.session_state['events']:
            if event.artist_name() == artist:
                st.write(f"Artist name: {artist}\nEvent name: {event.show_name()}\nDate: {event.show_date()}\nAddress: {event.show_addres()}\nRemaining slots: {event.show_slots()} of {event.event_capacity()}\n")
                found = True
        if not found:
            st.write("The specified artist doesn't exist in any event")

    def show_payment_methods(self): #TODO
        for event_id, stats in st.session_state['events_stats'].items():
            st.write(f"Event ID: {event_id}\nType of payment: {stats['payment_type']}\nProfit: {stats['profit']}\n")


    def delete_a_event(self, event_ID): #Hecho
        found = False #banderas para evitar el uso de break
        stop_list = False
        #La función enumerate obtiene el índice y el valor de la lista
        #Esto se hace debido a que los eventos se guardan en una lista, se tiene que acceder tanto al indice como al objeto que guarda la información dl evento
        for i, event in enumerate(self.events): 
            #Si no se ha encontrado el evento y el evento es de tipo Teatro, Bar o Filantropico y el id del evento es igual al id del evento que se quiere eliminar
            #Primero verifica que no tenga espacios ocupados o que el estado no sea realizado, para eliminarlo
            if not found and isinstance(event, (Teatro, Bar, Filantropico)) and event.show_event_id() == event_ID:
                if event.get_occupied_slots() > 0:
                    st.write("You can't delete an event with occupied slots")
                    found = True
                    stop_list = True
                elif event.show_state() == "Realizado":
                    st.write("You can't delete an event that has already been done")
                    found = True
                    stop_list = True
                else: 
                    
                    del self.events[i]
                    if not stop_list:
                        for j, session_event in enumerate(st.session_state['events']): #Se hace el mismo procedimiento con la lista que se guarda en la session de streamlit
                            if session_event.show_event_id() == event_ID:
                                del st.session_state['events'][j]
                                stop_list = True
                    found = True
    
    def show_event(self, selected_event): #Hecho
        
        event_found = False
        for event in self.events:
 
            if selected_event == "Teatro" and isinstance(event, Teatro):
                
                st.write("Type of event: Teatro")
                st.write(f"Artist: {event.artist_name()}")
                st.write(f"Event id: {event.show_event_id()}")  # Aquí estás accediendo a los atributos de la instancia
                st.write(f"Event name: {event.show_name()}")
                st.write(f"Event price: {event.event_price()}")
                st.write(f"Event date: {event.show_date()}")
                st.write(f"Event location: {event.show_location()}")
                st.write(f"Event address: {event.show_address()}")
                st.write(f"Event city: {event.show_city()}")
                st.write(f"Event status: {event.show_state()}")
                st.write(f"Avaible slots: {event.show_slots()}")
                
                    
            elif selected_event == "Bar" and isinstance(event, Bar):
                event_found = True
                st.write("Type of event: Bar")
                st.write(f"Artist: {event.artist_name()}")
                st.write(f"Event id: {event.show_event_id()}")
                st.write(f"Event name: {event.show_name()}")
                st.write(f"Event price: {event.event_price()}")
                st.write(f"Event date: {event.show_date()}")
                st.write(f"Event location: {event.show_location()}")
                st.write(f"Event address: {event.show_address()}")
                st.write(f"Event city: {event.show_city()}")
                st.write(f"Event status: {event.show_state()}")
                st.write(f"Avaible slots: {event.show_slots()}")
                
            
                    
            elif selected_event == "Filantropico" and isinstance(event, Filantropico):
                    event_found = True
                    st.write("Type of event: Filantropico")
                    st.write(f"Event id: {event.show_event_id()}")
                    st.write(f"Event name: {event.show_name()}")
                    st.write(f"Event price: {event.event_price()}")
                    st.write(f"Event date: {event.show_date()}")
                    st.write(f"Event location: {event.show_location()}")
                    st.write(f"Event address: {event.show_address()}")
                    st.write(f"Event city: {event.show_city()}")
                    st.write(f"Event status: {event.show_state()}")
                    st.write(f"Artist: {event.artist_name()}")
                    st.write(f"Avaible slots: {event.show_slots()}")
        if not event_found:
            st.write("Event not found")  
                    
    def find_event(self, event_id): #Hecho
        found_event = None
        
        for event in self.events:
            if isinstance(event, (Teatro, Bar, Filantropico)) and event.show_event_id() == event_id:
                found_event = event
            else:
                st.error("Sorry, the event was not found")  
        return found_event   
            
    def get_events(self):
        return self.events
    
    def get_events_stats(self):
        return self.events_stats
    