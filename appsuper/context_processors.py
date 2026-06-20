from .models import Sucursal

# 👑 IMPLEMENTACIÓN DEL PATRÓN SINGLETON
class MensajeSingleton:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(MensajeSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instancia.mensaje_exito = None  # Almacén del mensaje en memoria
        return cls._instancia

    def set_mensaje(self, mensaje):
        self.mensaje_exito = mensaje

    def get_and_clear_mensaje(self):
        # Retorna el mensaje y lo limpia de la memoria para que no aparezca de nuevo al recargar
        msg = self.mensaje_exito
        self.mensaje_exito = None
        return msg


def sucursal_context(request):
    """
    Hace que la sede seleccionada esté disponible globalmente limando el domicilio.
    También inyecta el mensaje de éxito del Singleton.
    """
    sucursal_id = request.session.get('sucursal_id')
    sede_limpia = None
    
    if sucursal_id:
        sucursal_actual = Sucursal.objects.filter(id_sucursal=sucursal_id).first()
        if sucursal_actual:
            texto_completo = sucursal_actual.localidad
            
            if " - " in texto_completo:
                sede_limpia = texto_completo.split(" - ")[0].strip()
            elif " (" in texto_completo:
                sede_limpia = texto_completo.split(" (")[0].strip()
            else:
                sede_limpia = texto_completo
                
    # 🔧 LEER SINGLETON: Extraemos el mensaje si existe
    singleton = MensajeSingleton()
    mensaje_verde = singleton.get_and_clear_mensaje()

    return {
        'sede_global': sede_limpia,
        'mensaje_exito_singleton': mensaje_verde  # Disponible en todos los templates
    }
