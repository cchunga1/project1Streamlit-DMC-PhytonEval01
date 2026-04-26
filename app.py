# ==========================================
# SECCIÓN: EJERCICIO 3 - USO DE FUNCIONES EXTERNAS
# Perfil: Mesa de Ayuda (Matriz de Escalamiento)
# ==========================================
elif menu == "Ejercicio 3":
    st.title("🔀 Ejercicio 3 – Funciones Externas")
    st.markdown("Matriz automatizada de Prioridades y Niveles de Escalamiento.")

    func_seleccionada = st.selectbox("Selecciona la herramienta:", ["Calculadora de Escalamiento ITSM"])

    if func_seleccionada == "Calculadora de Escalamiento ITSM":
        
        st.write("Configura los parámetros del incidente reportado:")
        c1, c2 = st.columns(2)
        with c1:
            tipo_inc = st.selectbox("Catálogo de Servicio (Tipo)", [
                "Error de la aplicación del sistema de ventas", 
                "Conectividad", 
                "Infraestructura"
            ])
        with c2:
            impacto_inc = st.selectbox("Impacto en la Tienda", ["Alto", "Medio", "Bajo"])

        if st.button("Evaluar Prioridad"):
            # Invocamos la función que nos devuelve dos textos
            prioridad_res, escalamiento_res = determinar_atencion_y_escalamiento(tipo_inc, impacto_inc)
            
            st.error(f"🚨 **Prioridad de Atención:** {prioridad_res}")
            st.info(f"👨‍💻 **Derivar a:** {escalamiento_res}")
            
            # Guardamos el registro
            st.session_state.historial_ej3.append({
                "Incidente": tipo_inc,
                "Impacto": impacto_inc,
                "Prioridad Calculada": prioridad_res,
                "Nivel Asignado": escalamiento_res
            })

    if st.session_state.historial_ej3:
        st.write("### Historial de Evaluaciones")
        st.dataframe(pd.DataFrame(st.session_state.historial_ej3), use_container_width=True)

# ==========================================
# SECCIÓN: EJERCICIO 4 - CLASES EXTERNAS Y CRUD
# Perfil: Mesa de Ayuda Retail (Gestión Integrada)
# ==========================================
elif menu == "Ejercicio 4":
    st.title("🎫 Ejercicio 4 – Clases y CRUD")
    st.markdown("Sistema de Tickets con enrutamiento automático.")

    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear Ticket", "Bandeja de Entradas", "Gestionar", "Cerrar Ticket"])

    # --- CREATE ---
    with tab_crear:
        st.subheader("Apertura de Incidente")
        col_a, col_b = st.columns(2)
        with col_a:
            id_tk = st.text_input("N° Ticket (Ej: TK-500)")
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
                    # Usamos la función del Ejercicio 3 para autocompletar la lógica de la Clase!
                    prioridad_calc, escala_calc = determinar_atencion_y_escalamiento(tipo_tk, impacto_tk)
                    
                    nuevo_ticket = TicketRetail(id_tk, tienda_tk, tipo_tk, impacto_tk, prioridad_calc, escala_calc, estado_tk)
                    st.session_state.inventario_ej4[id_tk] = nuevo_ticket
                    st.success(f"Ticket generado exitosamente. Asignado a: {escala_calc}")
            else:
                st.warning("Debe ingresar el ID del Ticket y la Tienda.")

    # --- READ ---
    with tab_leer:
        st.subheader("Bandeja de Incidentes Activos")
        if st.session_state.inventario_ej4:
            lista_tickets = [obj.obtener_diccionario() for obj in st.session_state.inventario_ej4.values()]
            st.dataframe(pd.DataFrame(lista_tickets), use_container_width=True)
        else:
            st.info("Sin incidentes reportados.")

    # --- UPDATE ---
    with tab_actualizar:
        st.subheader("Actualizar Estado o Escalar")
        if st.session_state.inventario_ej4:
            ids_tickets = list(st.session_state.inventario_ej4.keys())
            id_a_modificar = st.selectbox("Selecciona el Ticket a gestionar", ids_tickets)
            
            c_upd1, c_upd2 = st.columns(2)
            with c_upd1:
                nuevo_estado = st.selectbox("Actualizar Estado a:", ["Abierto", "En Revisión", "Escalado", "Resuelto"])
            with c_upd2:
                nuevo_escala = st.selectbox("Modificar Nivel de Escalamiento:", ["Nivel 1 (Mesa de Ayuda)", "Nivel 2 (Especialistas)", "Nivel 3 (Vendor/Proveedores)"])
            
            if st.button("Guardar Cambios"):
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
            
            if st.button("Eliminar Ticket"):
                del st.session_state.inventario_ej4[id_a_eliminar]
                st.success(f"El ticket {id_a_eliminar} ha sido cerrado del sistema.")
        else:
            st.write("Bandeja vacía.")
