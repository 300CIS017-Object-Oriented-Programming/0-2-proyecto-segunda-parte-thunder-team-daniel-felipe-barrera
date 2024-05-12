
class Boleteria:
    def __init__(self):
        self.__tickets = []
        
    def add_ticket(self, client, type_of_event , event_id ,type_of_ticket, ticket_price, payment_method):
        
        ticket = {
            "Client": client,
            "Event": type_of_event,
            "Event Id": event_id,
            "Type of ticket": type_of_ticket,
            "Ticket price": ticket_price,
            "Payment Method": payment_method,
        }
        self.__tickets.append(ticket)

    def get_type_of_ticket(self):
        return self.__type_of_ticket
    
    def get_ticket_price(self):
        return self.__ticket_price
    
    def get_payment_method(self):
        return self.__payment_method
    
    def get_tickets(self):
        return self.__tickets