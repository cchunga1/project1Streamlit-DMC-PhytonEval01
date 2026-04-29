# ==========================================
# Libreria de Clases utilizadas - CC
# ==========================================

class TicketRetail:
    def __init__(self, id_ticket, tienda, tipo_incidente, impacto, prioridad, escalamiento, estado):
        # Atributos de la clase (Características del ticket)
        self.id_ticket = id_ticket
        self.tienda = tienda
        self.tipo_incidente = tipo_incidente
        self.impacto = impacto
        self.prioridad = prioridad
        self.escalamiento = escalamiento
        self.estado = estado

    def actualizar_estado(self, nuevo_estado):
        # Método para cambiar el avance del ticket (ej: Abierto -> Resuelto)
        self.estado = nuevo_estado
        
    def escalar_ticket(self, nuevo_nivel):
        # Método para subir el nivel de soporte si es muy complejo
        self.escalamiento = nuevo_nivel

    def obtener_diccionario(self):
        # Transforma el objeto en un formato fácil de leer para Pandas (Tablas)
        # Campos básicos para generar un ticket
        return {
            "ID Ticket": self.id_ticket,
            "Tienda": self.tienda,
            "Tipo de Falla": self.tipo_incidente,
            "Impacto": self.impacto,
            "Prioridad": self.prioridad,
            "Equipo Asignado": self.escalamiento,
            "Estado": self.estado
        }
