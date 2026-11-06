from django.db import models
from django.contrib.auth.models import User

class Socio(models.Model):
        
        ESTADOS_SOCIO = [       
                    ('pendiente','Pendiente'),
                    ('activo', 'Activo'),
                    ('inactivo','Inactivo'),
              ]
        usuario = models.OneToOneField(
             User,
             on_delete=models.CASCADE,
             related_name="socio",
             null=True,
             blank=True,
             default='pendiente',
             help_text="Cuenta de usuario para inicio de sesion en la web"
        )
        nombre = models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        dni = models.CharField(
                max_length=20,
                unique=True
        )
        fecha_nac = models.DateField()
        telefono = models.CharField(max_length=30)
        email = models.EmailField(blank=True)
        responsable = models.CharField(
                max_length=100,
                blank=True                       )

        telefono_responsable = models.CharField(
                max_length=30,
                blank=True
        )
        
        fecha_reg = models.DateTimeField(
                auto_now_add=True
        )

        estado = models.CharField(
        max_length=20,
        choices=ESTADOS_SOCIO,
        default='pendiente'
        )

        numero_socios = models.PositiveIntegerField(
            unique=True,
            null=True,
            blank=True
                
        )

        def __str__(self):
            return f"{self.nombre} {self.apellido}"

class Pagos(models.Model):
      
      ESTADOS = [       
            ('pendiente','Pendiente'),
            ('aprobado', 'Aprobado'),
            ('rechazado','Rechazado'),
      ]

      socio = models.ForeignKey(
            Socio,on_delete=models.CASCADE,
            related_name="pagos"
      )

      comprobante = models.FileField(
        upload_to="comprobante/"
      )

      estado = models.CharField(
           max_length=20,
           choices=ESTADOS,
           default="pendiente"
      )

      fecha_envio= models.DateField(
            auto_now_add=True
      )

      def save(self, *args, **kwargs):
        # 1. Guardamos el pago en la base de datos
        super().save(*args, **kwargs)

        # 2. Si el pago fue aprobado, cambiamos el estado del Socio a 'activo'
        if self.estado == 'aprobado' and self.socio:
            self.socio.estado = 'activo'
            self.socio.save()

      def __str__(self):
        return f"Pago de {self.socio}"