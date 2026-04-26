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
st.set_page_config(page_title="Portafolio ITSM Retail", layout="wide")

# ==========================================
# INICIALIZACIÓN DE VARIABLES DE SESIÓN
# Vital para que los datos no se borren al interactuar con los botones.
# ==========================================
if 'movimientos_ej1' not in st.session_state:
    st.session_state.movimientos_ej1 = []

if 'registros_ej2' not in st.session_state:
    st.session_state.registros_ej2 = []

if 'historial_ej3' not in st.session_state:
    st.session_state.historial_ej3 = []

if 'inventario_ej4' not in st.session_state:
    st.session_state.inventario_ej4 = {} 

# ==========================================
# MENÚ DE NAVEGACIÓN
# ==========================================
st.sidebar.title("Menú de Sistemas")
menu = st.sidebar.selectbox(
    "Navegación del Módulo:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ==========================================
# SECCIÓN: HOME
# ==========================================
if menu == "Home":
    st.title("🛠️ Sistema de Gestión TI y Mesa de Ayuda")
    st.subheader("Módulo 1 – Python Fundamentals | Especialización for Analytics")
    
    st.markdown("""
    **Datos del Consultor / Alumno:**
    * **Nombre:** [Tu Nombre Completo]
    * **Perfil Aplicado:** Jefe de Proyectos TI / Service Desk Manager (Retail)
    * **Año:** 2026
    
    **Descripción del Proyecto:**
    Esta aplicación integra los conceptos de Python aplicados a un entorno real de gestión de 
    Servicios de TI (ITSM) en el rubro Retail. 
    
    * **Ej 1:** Gestión del presupuesto del departamento de TI (Listas).
    * **Ej 2:** Inventario de despliegue de hardware en tiendas (NumPy y Pandas).
    * **Ej 3:** Matriz automatizada de escalamiento de incidentes (Funciones).
    * **Ej 4:** Plataforma CRUD para la Mesa de Ayuda (POO).
    """)

# ==========================================
# SECCIÓN: EJERCICIO 1 - FLUJO DE CAJA (PRESUPUESTO TI)
# ==========================================
elif menu == "Ejercicio 1":
    st.title("💸 Ejercicio 1 – Control de Presupuesto TI (Flujo de Caja)")
    st.markdown("Registro de asignaciones presupuestales y gastos operativos (OPEX/CAPEX).")

    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto (Ej: Compra Laptops, Asignación Q1)")
    with col2:
        # Adaptamos Ingreso/Gasto al lenguaje financiero de TI
        tipo = st.selectbox("Tipo de Movimiento", ["Ingreso (Presupuesto Asignado)", "Gasto (Compra/Pago)"])
    with col3:
        valor = st.number_input("Monto ($)", min_value=0.0, step=100.0)

    if st.button("Registrar Movimiento"):
        if concepto != "":
            nuevo_movimiento = {"Concepto": concepto, "Tipo": tipo, "Valor": valor}
            st.session_state.movimientos_ej1.append(nuevo_movimiento)
            st.success("Registro añadido a la contabilidad de TI.")
        else:
            st.error("Por favor, ingresa un concepto válido.")

    if len(st.session_state.movimientos_ej1) > 0:
        st.subheader("Libro Mayor de TI")
        st.dataframe(st.session_state.movimientos_ej1, use_container_width=True)

        # Filtramos por el texto exacto del selectbox para calcular los totales
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos_ej1 if m["Tipo"] == "Ingreso (Presupuesto Asignado)")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos_ej1 if m["Tipo"] == "Gasto (Compra/Pago)")
        saldo_final = total_ingresos - total_gastos

        m1, m2, m3 = st.columns(3)
        m1.metric("Presupuesto Total Asignado", f"${total_ingresos:.2f}")
        m2.metric("Total Ejecutado (Gastos)", f"${total_gastos:.2f}")
        m3.metric("Fondo Disponible (Saldo)", f"${saldo_final:.2f}")

        if saldo_final > 0:
            st.success("🟢 Presupuesto a favor. Hay fondos disponibles para nuevos proyectos.")
        elif saldo_final < 0:
            st.error("🔴 Presupuesto en rojo. Se ha sobregirado la cuenta de TI.")
        else:
            st.warning("🟡 Presupuesto al límite (Saldo cero).")

# ==========================================
# SECCIÓN: EJERCICIO 2 - ARRAYS Y PANDAS (INVENTARIO TI)
# ==========================================
elif menu == "Ejercicio 2":
    st.title("📦 Ejercicio 2 – Despliegue de Hardware (NumPy y Pandas)")
    st.markdown("Registro de equipos tecnológicos enviados a las sucursales.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        producto = st.text_input("Activo TI (Ej: Lector Zebra, PINPAD)")
    with c2:
        categoria = st.selectbox("Categoría", ["Punto de Venta (POS)", "Redes (AP/Switch)", "Servidores", "Backoffice"])
    with c3:
        precio = st.number_input("Costo Unitario ($)", min_value=0.0)
    with c4:
        cantidad = st.number_input("Cantidad enviada", min_value=1, step=1)

    if st.button("Agregar a la Guía de Remisión"):
        if producto:
            total = precio * cantidad
            # Creamos un arreglo matemático de NumPy
            fila_numpy = np.array([producto, categoria, precio, cantidad, total])
            st.session_state.registros_ej2.append(fila_numpy)
            st.success("Activo registrado.")

    if st.session_state.registros_ej2:
        st.subheader("Tabla de Activos Desplegados")
        # Convertimos la matriz de NumPy a un DataFrame de Pandas
        columnas = ["Activo TI", "Categoría", "Costo Unitario", "Cantidad", "Inversión Total"]
        df_registros = pd.DataFrame(st.session_state.registros_ej2, columns=columnas)
        st.dataframe(df_registros, use_container_width=True)

# ==========================================
# SECCIÓN: EJERCICIO 3 - FUNCIONES (ESCALAMIENTO)
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
            # Llamamos a nuestra función importada
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

    tab_cre
