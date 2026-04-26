# ==========================================
# OBSERVACIÓN PARA EL ALUMNO:
# Esta función actúa como el "Cerebro" de nuestra Mesa de Ayuda.
# Evalúa el tipo de incidente del catálogo de servicios y su impacto
# para determinar automáticamente qué tan urgente es (Prioridad) 
# y a qué equipo técnico debe derivarse (Nivel de Escalamiento).
# ==========================================

def determinar_atencion_y_escalamiento(tipo_incidente, impacto):
    """
    Determina la prioridad y el nivel de escalamiento de un incidente en tienda.
    """
    # Asignamos un peso numérico al impacto para facilitar la lógica de control de flujo
    pesos_impacto = {"Alto": 3, "Medio": 2, "Bajo": 1}
    peso = pesos_impacto.get(impacto, 1)

    # Matriz de decisión basada en el Catálogo de Servicios
    if tipo_incidente == "Error de la aplicación del sistema de ventas":
        if peso == 3:
            return "Crítica (Afecta Facturación)", "Nivel 3 (Soporte de Desarrollo/Vendor)"
        elif peso == 2:
            return "Alta (Falla Parcial de Cajas)", "Nivel 2 (Soporte Sistemas Interno)"
        else:
            return "Media (Lentitud en sistema)", "Nivel 1 (Mesa de Ayuda)"
            
    elif tipo_incidente == "Conectividad":
        if peso >= 2: # Alto o Medio
            return "Alta (Tienda sin red/internet)", "Nivel 3 (Telecomunicaciones/ISP)"
        else:
            return "Baja (Intermitencia leve)", "Nivel 1 (Mesa de Ayuda)"
            
    elif tipo_incidente == "Infraestructura":
        if peso == 3:
            return "Crítica (Riesgo físico/Eléctrico)", "Nivel 2 (Mantenimiento/Infraestructura Local)"
        else:
            return "Media (Avería de hardware menor)", "Nivel 1 (Soporte Técnico en Sitio)"
    
    # Valor por defecto en caso de un error
    return "No Definida", "Nivel 1"
