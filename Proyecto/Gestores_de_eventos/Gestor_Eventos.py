import streamlit as st

class Gestor_Eventos:
    def __init__(self):
        if 'events' not in st.session_state:
            st.session_state['events'] = []
        if 'events_stats' not in st.session_state:
            st.session_state['events_stats'] = {}

    def add_event(self, event):
        st.session_state['events'].append(event)
    
    def add_event_stats(self, event_id, event_stats):
        st.session_state['events_stats'][event_id] = event_stats

    def show_all_artist_tickets_sold(self, artist):
        found = False
        for event in st.session_state['events']:
            if event.artist_name() == artist:
                st.write(f"Artist name: {artist}\nEvent name: {event.show_name()}\nDate: {event.show_date()}\nAddress: {event.show_addres()}\nRemaining slots: {event.show_slots()} of {event.event_capacity()}\n")
                found = True
        if not found:
            st.write("The specified artist doesn't exist in any event")

    def show_payment_methods(self):
        for event_id, stats in st.session_state['events_stats'].items():
            st.write(f"Event ID: {event_id}\nType of payment: {stats['payment_type']}\nProfit: {stats['profit']}\n")

    def delete_a_event(self, event_ID):
        for i, event in enumerate(st.session_state['events']):
            if event.show_event_id() == event_ID:
                if event.show_state() == "Realizado":
                    st.write("Sorry, the event has already taken place")
                elif event.get_occupied_slots() > 0:
                    st.write("Sorry, you can't delete this event because there's at least one ticket sold")
                else:
                    del st.session_state['events'][i]
                    del st.session_state['events_stats'][event_ID]
                    st.write("Event deleted successfully")
    
        st.write("We can't found an event with that ID")
        
    def show_all_events(self):
        for event in st.session_state['events']:
            st.write(f"Event id: {event.show_event_id()}")
            st.write(f"Event name: {event.show_name()}")
            
        if not st.session_state['events']:
            st.write("There's no events available")