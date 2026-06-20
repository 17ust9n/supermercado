from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import Venta

# El decorador @receiver registra esta función como un OBSERVER (Sujeto: Venta)
@receiver(post_save, sender=Venta)
def ejecutar_observadores_de_venta(sender, instance, created, **kwargs):
    """
    Este es el despachador del Observer. 
    Se ejecuta automáticamente CADA VEZ que se guarda una Venta.
    """
    if created:
        # Se ejecuta de forma segura una vez confirmada la transacción en la vista
        transaction.on_commit(lambda: actualizar_stock_y_billetera(instance))

def actualizar_stock_y_billetera(venta):
    """Ejecuta las acciones de los observadores de forma segura."""
    # 🔌 IMPORTACIÓN LOCAL: Evita la importación circular y permite que el servidor arranque
    from .views import calcular_precio_composite_manual 

    producto = venta.producto
    cliente = venta.cliente
    
    # 👁️ Observador 1: Inventario
    producto.stock -= venta.cantidad
    producto.save()
    
    # 👁️ Observador 2: Billetera (Aplicando el Composite corregido)
    # Reutilizamos la lógica del árbol para obtener el precio real estructurado
    precio_unitario = calcular_precio_composite_manual(producto)
    costo_total = precio_unitario * venta.cantidad
    
    cliente.dinero -= costo_total
    cliente.save()
