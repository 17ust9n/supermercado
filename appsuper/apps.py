from django.apps import AppConfig

class AppsuperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appsuper'

    def ready(self):
        # Activación de los Observers (Señales) al iniciar el servidor
        import appsuper.signals 
