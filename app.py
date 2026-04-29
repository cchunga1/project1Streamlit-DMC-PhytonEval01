# ==========================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================
import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import determinar_atencion_y_escalamiento
from libreria_clases_proyecto1 import TicketRetail

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="Mesa de Ayuda Retail", layout="wide")

# ==========================================
# INICIALIZACIÓN DE VARIABLES DE SESIÓN
# ==========================================
if 'caja_chica_ej1' not in st.session_state:
    st.session_state.caja_chica_ej1 = []

if 'repuestos_ej2' not in st.session_state:
    st.session_state.repuestos_ej2 = []

if 'historial_ej3' not in st.session_state:
    st.session_state.historial_ej3 = []

if 'inventario_ej4' not in st.session_state:
    st.session_state.inventario_ej4 = {} 

# ==========================================
# MENÚ DE NAVEGACIÓN
# ==========================================
st.sidebar.title("Menú Help Desk")
menu = st.sidebar.selectbox(
    "Selecciona un módulo:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ==========================================
# SECCIÓN: HOME
# ==========================================
if menu == "Home":
    st.title("🎧 Titulo del Proyecto : Portal de Mesa de Ayuda - Retail")
    st.subheader("Curso : Módulo 1 - Python Fundamentals | Especialización for Analytics")
    
    st.markdown("""
    * **Nombre:** JOSE CHRISTIAN CHUNGA MARTINEZ
    * **Nombre del Módulo :** Módulo 1 - Python Fundamentals | Especialización for Analytics
    * **Información general del estudiante :** Ingeniero de Sistemas
    * **Año:** 2026
    
    **Descripción del Proyecto:**
    Esta plataforma simula las herramientas diarias utilizadas por una Mesa de Ayuda en una empresa de Retail, 
    aplicando los fundamentos de programación en Python:
    
    * **Ejercicio 1:** Control de Caja Chica para emergencias de soporte (Listas y Control de Flujo).
    * **Ejercicio 2:** Inventario de repuestos de primera línea (NumPy y DataFrames).
    * **Ejercicio 3:** Matriz de priorización de incidentes en tiendas (Funciones).
    * **Ejercicio 4:** Plataforma de registro y enrutamiento de Tickets (POO y CRUD).
    """)

# URL Raw de GitHub
url_imagen = "https://github.com/cchunga1/project1Streamlit-DMC-PhytonEval01/blob/main/Logo%20Python.png"

# Mostrar la imagen en la interfaz
st.image(url_imagen, caption="Descripción de la imagen", use_column_width=True)

# ==========================================
# SECCIÓN: EJERCICIO 1 - FLUJO DE CAJA (CAJA CHICA SOPORTE)
# ==========================================
elif menu == "Ejercicio 1":
    st.title("💵 Ejercicio 1 – Control de Caja Chica (Help Desk)")
    st.markdown("Registro de fondos para movilidad de técnicos a tiendas y compras menores de urgencia.")

    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto (Ej: Taxi a Tienda San Isidro, Compra de Patch Cord)")
    with col2:
        tipo = st.selectbox("Tipo de Movimiento", ["Ingreso (Reembolso/Asignación)", "Gasto (Salida de dinero)"])
    with col3:
        valor = st.number_input("Monto (S/)", min_value=0.0, step=10.0)

    if st.button("Registrar en Caja Chica"):
        if concepto != "":
            nuevo_movimiento = {"Concepto": concepto, "Tipo": tipo, "Monto": valor}
            st.session_state.caja_chica_ej1.append(nuevo_movimiento)
            st.success("Movimiento registrado en la caja chica de soporte.")
        else:
            st.error("Por favor, ingresa el concepto del gasto o ingreso.")

    if len(st.session_state.caja_chica_ej1) > 0:
        st.subheader("Registro de Movimientos")
        st.dataframe(st.session_state.caja_chica_ej1, use_container_width=True)

        total_ingresos = sum(m["Monto"] for m in st.session_state.caja_chica_ej1 if m["Tipo"] == "Ingreso (Reembolso/Asignación)")
        total_gastos = sum(m["Monto"] for m in st.session_state.caja_chica_ej1 if m["Tipo"] == "Gasto (Salida de dinero)")
        saldo_final = total_ingresos - total_gastos

        m1, m2, m3 = st.columns(3)
        m1.metric("Fondo Asignado", f"S/ {total_ingresos:.2f}")
        m2.metric("Gastos Ejecutados", f"S/ {total_gastos:.2f}")
        m3.metric("Efectivo Disponible", f"S/ {saldo_final:.2f}")

        if saldo_final > 0:
            st.success("🟢 Hay efectivo disponible para atención de emergencias en tienda.")
        elif saldo_final < 0:
            st.error("🔴 ¡Alerta! La caja chica está sobregirada. Solicitar reembolso urgente.")
        else:
            st.warning("🟡 Caja chica en cero. No se pueden autorizar más pasajes o compras.")

# ==========================================
# SECCIÓN: EJERCICIO 2 - ARRAYS Y PANDAS (INVENTARIO DE REPUESTOS)
# ==========================================
elif menu == "Ejercicio 2":
    st.title("🔌 Ejercicio 2 – Stock de Repuestos Nivel 1")
    st.markdown("Control rápido de periféricos y partes para envío inmediato a sucursales.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        producto = st.text_input("Repuesto (Ej: Lector de Código de Barras, Mouse, Cable HDMI)")
    with c2:
        categoria = st.selectbox("Categoría", ["Periféricos POS", "Cables/Conectividad", "Energía", "Redes"])
    with c3:
        precio = st.number_input("Costo Unitario Aprox (S/)", min_value=0.0)
    with c4:
        cantidad = st.number_input("Cantidad en Almacén HD", min_value=1, step=1)

    if st.button("Agregar a Stock"):
        if producto:
            total = precio * cantidad
            # Uso de NumPy para estructurar los datos matemáticos
            fila_numpy = np.array([producto, categoria, precio, cantidad, total])
            st.session_state.repuestos_ej2.append(fila_numpy)
            st.success("Repuesto ingresado al inventario de Mesa de Ayuda.")

    if st.session_state.repuestos_ej2:
        st.subheader("Inventario Disponible en Mesa de Ayuda")
        columnas = ["Descripción", "Categoría", "Costo Ref.", "Stock", "Valor Total inmovilizado"]
        df_registros = pd.DataFrame(st.session_state.repuestos_ej2, columns=columnas)
        st.dataframe(df_registros, use_container_width=True)

# ==========================================
# SECCIÓN: EJERCICIO 3 - FUNCIONES (MESA DE AYUDA RETAIL)
# ==========================================
elif menu == "Ejercicio 3":
    st.title("🔀 Ejercicio 3 – Funciones (Escalamiento ITSM)")
    st.markdown("Matriz automatizada de Prioridades y Niveles de Soporte ITIL.")

    func_seleccionada = st.selectbox("Selecciona la herramienta:", ["Calculadora de Escalamiento ITSM"])

    if func_seleccionada == "Calculadora de Escalamiento ITSM":
        st.write("Configura los parámetros del incidente reportado desde tienda:")
        c1, c2 = st.columns(2)
        with c1:
            tipo_inc = st.selectbox("Catálogo de Servicio (Falla reportada)", [
                "Error de la aplicación del sistema de ventas", 
                "Conectividad", 
                "Infraestructura"
            ])
        with c2:
            impacto_inc = st.selectbox("Nivel de Impacto Operativo", ["Alto", "Medio", "Bajo"])

        if st.button("Evaluar Prioridad SLA"):
            prioridad_res, escalamiento_res = determinar_atencion_y_escalamiento(tipo_inc, impacto_inc)
            
            st.error(f"🚨 **Prioridad de Atención:** {prioridad_res}")
            st.info(f"👨‍💻 **Derivar a:** {escalamiento_res}")
            
            st.session_state.historial_ej3.append({
                "Incidente": tipo_inc,
                "Impacto": impacto_inc,
                "Prioridad Calculada": prioridad_res,
                "Nivel Asignado": escalamiento_res
            })

    if st.session_state.historial_ej3:
        st.write("### Historial de Evaluaciones de Triage")
        st.dataframe(pd.DataFrame(st.session_state.historial_ej3), use_container_width=True)

# ==========================================
# SECCIÓN: EJERCICIO 4 - CLASES (MESA DE AYUDA)
# ==========================================
elif menu == "Ejercicio 4":
    st.title("🎫 Ejercicio 4 – Clases y CRUD (Mesa de Ayuda)")
    st.markdown("Sistema Central de Tickets con enrutamiento automático.")

    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear Ticket", "Bandeja de Entradas", "Gestionar", "Cerrar Ticket"])

    # --- CREATE ---
    with tab_crear:
        st.subheader("Apertura de Incidente")
        col_a, col_b = st.columns(2)
        with col_a:
            id_tk = st.text_input("N° Ticket (Ej: INC-1020)")
            tienda_tk = st.text_input("Tienda Afectada")
            estado_tk = st.selectbox("Estado Inicial", ["Abierto", "En Revisión"])
        with col_b:
            tipo_tk = st.selectbox("Tipo de Incidente", [
                "Error de la aplicación del sistema de ventas", 
                "Conectividad", 
                "Infraestructura"
            ])
            impacto_tk = st.selectbox("Nivel de Impacto", ["Alto", "Medio", "Bajo"])

        if st.button("Generar e Integrar Ticket"):
            if id_tk and tienda_tk:
                if id_tk in st.session_state.inventario_ej4:
                    st.error("El número de ticket ya existe.")
                else:
                    prioridad_calc, escala_calc = determinar_atencion_y_escalamiento(tipo_tk, impacto_tk)
                    
                    nuevo_ticket = TicketRetail(id_tk, tienda_tk, tipo_tk, impacto_tk, prioridad_calc, escala_calc, estado_tk)
                    st.session_state.inventario_ej4[id_tk] = nuevo_ticket
                    st.success(f"Ticket generado exitosamente. Asignado automáticamente a: {escala_calc}")
            else:
                st.warning("Debe ingresar el ID del Ticket y la Tienda.")

    # --- READ ---
    with tab_leer:
        st.subheader("Bandeja de Incidentes Activos")
        if st.session_state.inventario_ej4:
            lista_tickets = [obj.obtener_diccionario() for obj in st.session_state.inventario_ej4.values()]
            st.dataframe(pd.DataFrame(lista_tickets), use_container_width=True)
        else:
            st.info("No hay incidentes reportados en la red de tiendas.")

    # --- UPDATE ---
    with tab_actualizar:
        st.subheader("Actualizar Estado o Escalar Ticket")
        if st.session_state.inventario_ej4:
            ids_tickets = list(st.session_state.inventario_ej4.keys())
            id_a_modificar = st.selectbox("Selecciona el Ticket a gestionar", ids_tickets)
            
            c_upd1, c_upd2 = st.columns(2)
            with c_upd1:
                nuevo_estado = st.selectbox("Actualizar Estado a:", ["Abierto", "En Revisión", "Escalado", "Resuelto"])
            with c_upd2:
                nuevo_escala = st.selectbox("Modificar Nivel de Soporte:", ["Nivel 1 (Mesa de Ayuda)", "Nivel 2 (Especialistas)", "Nivel 3 (Vendor/Proveedores)"])
            
            if st.button("Guardar Cambios de Gestión"):
                ticket_obj = st.session_state.inventario_ej4[id_a_modificar]
                ticket_obj.actualizar_estado(nuevo_estado)
                ticket_obj.escalar_ticket(nuevo_escala)
                st.success(f"Ticket {id_a_modificar} actualizado con éxito.")
        else:
            st.write("No hay tickets abiertos.")

    # --- DELETE ---
    with tab_eliminar:
        st.subheader("Cerrar y Eliminar Ticket")
        if st.session_state.inventario_ej4:
            ids_borrar = list(st.session_state.inventario_ej4.keys())
            id_a_eliminar = st.selectbox("Selecciona el Ticket finalizado", ids_borrar)
            
            if st.button("Cerrar Ticket Definitivamente"):
                del st.session_state.inventario_ej4[id_a_eliminar]
                st.success(f"El ticket {id_a_eliminar} ha sido cerrado del sistema.")
        else:
            st.write("Bandeja vacía.")
