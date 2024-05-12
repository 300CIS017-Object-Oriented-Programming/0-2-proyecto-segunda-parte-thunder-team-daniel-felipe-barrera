
class Cliente:
    def __init__(self, user, id, city, address, payment, email, number, money):
        self.user_name = user
        self.user_id = id
        self.city = city
        self.address = address
        self.method_of_payment = payment
        self.user_email = email
        self.phone_number = number
        self.user_money = money
        self.event = ""

    def get_user_name(self):
        return self.user_name

    # Obtiene el ID de usuario del cliente
    def get_user_id(self):
        return self.user_name

    # Obtiene la ciudad del cliente
    def get_city(self):
        return self.city

    # Obtiene la dirección del cliente
    def get_address(self):
        return self.address

    # Obtiene el método de pago del cliente
    def get_method_of_payment(self):
        return self.method_of_payment

    # Obtiene el correo electrónico del cliente
    def get_email(self):
        return self.user_email

    # Obtiene el número de teléfono del cliente
    def get_phone_number(self):
        return self.phone_number

    # Obtiene el dinero del cliente
    def get_user_money(self):
        return self.user_money