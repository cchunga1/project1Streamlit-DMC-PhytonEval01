# ==========================================
# OBSERVACIÓN PARA EL ALUMNO:
# La clase TicketRetail ahora incluye atributos vitales de ITIL:
# 'tipo_incidente', 'impacto', 'prioridad' y 'nivel_escalamiento'.
# Se agrega el método 'escalar_ticket' para mover el incidente entre equipos.
# ==========================================

class TicketRetail:
    def __init__(self, id_ticket, tienda, tipo_incidente, impacto, prioridad, escalamiento, estado):
        self.id_ticket = id_ticket
        self.tienda = tienda
        self.tipo_incidente = tipo_incidente
        self.impacto = impacto
        self.prioridad = prioridad
        self.escalamiento = escalamiento
        self.estado = estado

    def actualizar_estado(self, nuevo_estado):
        # Transición del estado del ticket (ej: Abierto -> Resuelto)
        self.estado = nuevo_estado
        
    def escalar_ticket(self, nuevo_nivel):
        # Permite subir el nivel de soporte si no se resuelve a tiempo
        self.escalamiento = nuevo_nivel

    def obtener_diccionario(self):
        # Convierte el objeto en una fila para nuestra tabla visual
        return {
            "ID Ticket": self.id_ticket,
            "Tienda": self.tienda,
            "Tipo de Falla": self.tipo_incidente,
            "Impacto": self.impacto,
            "Prioridad": self.prioridad,
            "Equipo Asignado": self.escalamiento,
            "Estado": self.estado
        }