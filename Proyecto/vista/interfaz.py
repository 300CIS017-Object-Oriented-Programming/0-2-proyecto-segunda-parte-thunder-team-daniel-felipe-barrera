import streamlit as st


from Gestores_de_eventos.Controlador import Controlador


class Interfaz:
    def __init__(self):
        # Crea un estado de sesión
        if 'user_type' not in st.session_state:
            st.session_state['user_type'] = None
        self.controlador = Controlador()
        

    def interfaz_funcion(self):
        # Crea dos columnas
        col1, col2 = st.columns(2)

        # En la primera columna, muestra la imagen y el botón de 'Usuario'
        with col1:
            st.image("./imagenes_decorativas/fondo_usuario.jpg", use_column_width=True)
            if st.button('Usuario', key="button_usuario"):
                st.write('Has seleccionado Usuario.')
                st.session_state['user_type'] = 'Usuario'  # Guarda el tipo de usuario en el estado de la sesión
        # En la segunda columna, muestra la imagen y el botón de 'Administrador'
        with col2:
            st.image("./imagenes_decorativas/fondo_administrador.jpg", use_column_width=True)
            if st.button('Administrador', key="button_administrador"):
                st.session_state['user_type'] = 'Administrador'  # Guarda el tipo de usuario en el estado de la sesión
                self.admin_interfaz()  # Llama a la función admin_interfaz
                
                    
    def user_interfaz(self):
        # Si el tipo de usuario es 'Usuario', muestra la interfaz de usuario
        if st.session_state['user_type'] == 'Usuario':
            st.write('Bienvenido Usuario')
            activity = st.selectbox("¿Qué quieres hacer?", ["Registrarse a un evento", "Ver mi información"], key = "jkabawdbjawjnawd")
            if activity == "Registrarse a un evento":
                event_type = st.selectbox("Selecciona el tipo de evento", ["Teatro", "Bar", "Filantropico"], key="bawdbhawawuhawuduwiaw")
                # Aquí puedes agregar el código para manejar el registro del usuario al evento seleccionado
            elif activity == "Ver mi información":
                pass
    
    def admin_interfaz(self):
        if st.session_state['user_type'] == 'Administrador':
            password = st.text_input("Introduce la contraseña", type="password", key="padjwannfjdjuejeefewefwef")
            if password == "admin":  # Reemplaza "contraseña_correcta" con la contraseña real
                st.write('Has seleccionado Administrador.')
                st.session_state['user_type'] = 'Administrador'  # Guarda el tipo de usuario en el estado de la sesión
                self.admin_actions()  # Llama a la función admin_actions
            else:
                st.write('Contraseña incorrecta.')

    def admin_actions(self):
        action = st.selectbox("¿Qué acción quieres realizar?", ["Crear un evento", "Eliminar un evento", "Ver estadísticas"],key="admin_action")
        if action == "Crear un evento":
            event_type = st.selectbox("¿Qué tipo de evento quieres crear?", ["Teatro", "Bar", "Filantropico"], key="event_type")
            if event_type == "Teatro":
                self.controlador.theater()
            elif event_type == "Bar":
                self.controlador.bar()
            elif event_type == "Filantropico":
                self.controlador.filantropic()
        elif action == "Eliminar un evento":
        
            pass
        elif action == "Ver estadísticas":
            
            pass