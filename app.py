import streamlit as st
import pandas as pd

# =====================================================================
# OBSERVACIÓN 1: CONFIGURACIÓN Y CLASES (POO)
# Se define la configuración base de la página. Además, definimos una
# clase 'Producto' aquí arriba para cumplir con el requisito de uso 
# de programación orientada a objetos. Esta clase encapsula atributos 
# y un método de cálculo que usaremos en el Ejercicio 3.
# =====================================================================
st.set_page_config(page_title="Proyecto 1 - Streamlit", page_icon="💻", layout="centered")

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total_inventario(self):
        return self.precio * self.cantidad

# =====================================================================
# OBSERVACIÓN 2: MANEJO DE ESTADO (SESSION STATE)
# Streamlit recarga todo el script con cada interacción. Para mantener
# estructuras de datos vivas entre clics (como listas o diccionarios),
# debemos inicializarlas en el st.session_state.
# =====================================================================
if 'lista_tareas' not in st.session_state:
    st.session_state.lista_tareas = []

# =====================================================================
# OBSERVACIÓN 3: FUNCIONES MODULARES PARA CADA SECCIÓN
# En lugar de tener código "espagueti", creamos una función para cada 
# vista. Esto demuestra buenas prácticas de programación y lógica.
# =====================================================================

def mostrar_home():
    """Renderiza la página de inicio."""
    st.title("🏠 Home")
    st.markdown("""
    ### Bienvenido a la Aplicación Interactiva
    Este proyecto es el MVP (Producto Mínimo Viable) del primer módulo. 
    
    **Objetivos demostrados en esta app:**
    * Uso de estructuras de datos (Listas, Diccionarios).
    * Implementación de diversos Widgets interactivos.
    * Creación y consumo de Funciones.
    * Programación Orientada a Objetos (Clases).
    * Lógica de control de flujo.
    
    👈 *Usa el menú lateral para navegar por los ejercicios.*
    """)

def mostrar_ejercicio_1():
    """Ejercicio 1: Estructuras de datos y Widgets básicos."""
    st.title("📝 Ejercicio 1: Gestión de Tareas")
    st.write("Demostración de **Estructuras de Datos (Listas)** y **Widgets (Inputs, Botones)**.")
    
    # Widget de entrada de texto
    nueva_tarea = st.text_input("Ingresa una nueva tarea para el backlog:")
    
    # Lógica: Si se presiona el botón y hay texto, se agrega a la lista
    if st.button("Agregar Tarea"):
        if nueva_tarea:
            st.session_state.lista_tareas.append(nueva_tarea)
            st.success(f"Tarea '{nueva_tarea}' agregada exitosamente.")
        else:
            st.warning("Por favor, escribe una tarea antes de agregar.")
            
    # Mostrar la estructura de datos
    st.write("### Lista Actual:")
    if len(st.session_state.lista_tareas) > 0:
        for i, tarea in enumerate(st.session_state.lista_tareas):
            st.info(f"{i + 1}. {tarea}")
    else:
        st.write("La lista está vacía.")

def procesar_texto(texto):
    """Función de apoyo para el Ejercicio 2."""
    palabras = texto.split()
    caracteres = len(texto)
    return len(palabras), caracteres

def mostrar_ejercicio_2():
    """Ejercicio 2: Funciones y Lógica de Programación."""
    st.title("⚙️ Ejercicio 2: Analizador de Texto")
    st.write("Demostración de **Funciones personalizadas** y **Lógica de control**.")
    
    # Widget de área de texto
    texto_usuario = st.text_area("Pega aquí un texto para analizar:")
    
    if st.button("Analizar"):
        if texto_usuario.strip() != "":
            # Llamada a la función
            num_palabras, num_caracteres = procesar_texto(texto_usuario)
            
            # Lógica condicional simple
            categoria = "Corto" if num_palabras < 20 else "Largo"
            
            # Mostrar resultados usando columnas (layout)
            col1, col2, col3 = st.columns(3)
            col1.metric("Palabras", num_palabras)
            col2.metric("Caracteres", num_caracteres)
            col3.metric("Categoría", categoria)
        else:
            st.error("El texto no puede estar vacío.")

def mostrar_ejercicio_3():
    """Ejercicio 3: Programación Orientada a Objetos."""
    st.title("📦 Ejercicio 3: Calculadora de Inventario (POO)")
    st.write("Demostración de **Clases y Objetos**.")
    
    st.write("Ingresa los datos del producto para instanciar un objeto de la clase `Producto`:")
    
    # Widgets de entrada numérica y de texto
    nombre_prod = st.text_input("Nombre del Producto:", value="Laptop Pro Max")
    precio_prod = st.number_input("Precio Unitario ($):", min_value=0.0, value=1500.0, step=50.0)
    stock_prod = st.number_input("Cantidad en Stock:", min_value=0, value=10, step=1)
    
    if st.button("Calcular Valorización"):
        # Instanciamos el objeto con los datos de los widgets
        producto_obj = Producto(nombre_prod, precio_prod, stock_prod)
        
        # Consumimos el método de la clase
        valor_total = producto_obj.calcular_total_inventario()
        
        st.success("¡Objeto instanciado correctamente!")
        st.write(f"**Producto:** {producto_obj.nombre}")
        st.write(f"**Valor total en almacén:** ${valor_total:,.2f}")

def mostrar_ejercicio_4():
    """Ejercicio 4: Integración y Visualización."""
    st.title("📊 Ejercicio 4: Visualización de Datos")
    st.write("Integración de **Diccionarios** convertidos a **DataFrames** y **Gráficos interactivos**.")
    
    # Usamos un diccionario como estructura de datos base
    datos_ventas = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
        "Ventas": [120, 150, 180, 130, 210]
    }
    
    # Widget de slider para modificar dinámicamente un valor
    ajuste_mayo = st.slider("Ajustar proyección de ventas para Mayo:", min_value=0, max_value=400, value=210)
    datos_ventas["Ventas"][4] = ajuste_mayo
    
    # Convertimos a DataFrame (muy común en Streamlit)
    df = pd.DataFrame(datos_ventas)
    
    st.write("**Tabla de Datos:**")
    st.dataframe(df, use_container_width=True)
    
    st.write("**Gráfico de Barras:**")
    # Streamlit permite graficar directamente un DataFrame
    st.bar_chart(df.set_index("Mes"))

# =====================================================================
# OBSERVACIÓN 4: FUNCIÓN PRINCIPAL Y NAVEGACIÓN (SIDEBAR)
# Aquí estructuramos el control de flujo principal de la aplicación.
# Cumplimos con el requisito de usar st.sidebar.selectbox().
# =====================================================================
def main():
    st.sidebar.title("Menú de Navegación")
    
    # Creación del menú desplegable en la barra lateral
    opciones_menu = ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    seleccion = st.sidebar.selectbox("Selecciona una sección:", opciones_menu)
    
    st.sidebar.markdown("---")
    st.sidebar.info("Proyecto 1 - Módulo de Python")
    
    # Lógica de enrutamiento según la selección del usuario
    if seleccion == "Home":
        mostrar_home()
    elif seleccion == "Ejercicio 1":
        mostrar_ejercicio_1()
    elif seleccion == "Ejercicio 2":
        mostrar_ejercicio_2()
    elif seleccion == "Ejercicio 3":
        mostrar_ejercicio_3()
    elif seleccion == "Ejercicio 4":
        mostrar_ejercicio_4()

# Punto de entrada de ejecución del script
if __name__ == "__main__":
    main()
