from django.urls import path
from . import views

urlpatterns = [
    # --- Autenticación ---
    path('', views.login_view, name='login_raiz'),       
    path('login/', views.login_view, name='login'),      
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),

    path('cambiar-contrasenia/', views.cambiar_contrasenia, name='cambiar_contrasenia'), # 👈 Tenías 'cambiar_contraseña' con Ñ
    
    # --- NUEVO: Selección de Sucursal Obligatoria ---
    path('seleccionar-sucursal/', views.seleccionar_sucursal, name='seleccionar_sucursal'),

    # --- Páginas Generales ---
    path('inicio/', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),

    # --- Módulo Productos ---
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/nuevo/', views.producto, name='producto'),

    # Rutas lógicas para las acciones de los 3 botones de las tarjetas
    path('productos/modificar/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('productos/vender/<int:pk>/', views.vender_producto, name='vender_producto'),
    path('productos/rellenar/<int:pk>/', views.rellenar_stock_producto, name='rellenar_stock'),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),

    # --- Módulo Ventas ---
    path('venta/', views.registrar_venta, name='venta'),
    path('ventas/historial/', views.lista_ventas, name='lista_ventas'),
    path('venta/eliminar/<int:pk>/', views.eliminar_Venta, name='eliminar_Venta'),

    # --- Módulo Empleados y Clientes Individuales ---
    path('empleado/<int:pk>/', views.detalle_empleado, name='detalle_empleado'),
    path('cliente/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),

    # Módulo Empleados y Clientes - Edición
    path('empleado/<int:pk>/editar/', views.editar_empleado, name='editar_empleado'),
    path('cliente/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),

    # 🌟 CORREGIDO: Módulo Empleados y Clientes - Eliminación (Unificado a 'pk')
    path('empleado/<int:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
    path('cliente/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    # 🌟 CORREGIDO: Cambio de sucursal del empleado (Unificado a 'pk')
    path('empleado/<int:pk>/cambiar-sucursal/', views.seleccionar_sucursal_empleado, name='seleccionar_sucursal_empleado'),
    path('empleado/<int:pk>/guardar-sucursal/<int:id_sucursal>/', views.guardar_sucursal_empleado, name='guardar_sucursal_empleado'),

    # --- Módulo General de Usuarios ---
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/empleado/nuevo/', views.empleado, name='empleado'),
    path('usuarios/cliente/nuevo/', views.cliente, name='cliente'),
    
    # 👑 RUTAS JEFES: Ver Detalle y Editar
    path('usuarios/jefe/<int:pk>/', views.detalle_jefe, name='detalle_jefe'),
    path('usuarios/jefe/<int:pk>/editar/', views.editar_jefe, name='editar_jefe'),

    # --- Módulo Estadísticas ---
    path('estadisticas/', views.ranking_productos_mas_vendidos, name='ranking_productos'),
    path('estadisticas/reiniciar/', views.reiniciar_estadisticas_sucursal, name='reiniciar_estadisticas'),

]
