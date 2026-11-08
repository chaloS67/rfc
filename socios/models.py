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

        numero_socio = models.TextField(
            unique=True,
            
                
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
        super().save(*args, **kwargs)

        if self.estado == 'aprobado' and getattr(self, 'socio', None):
            self.socio.estado = 'activo'

            # --- NUEVA LÓGICA DE ASIGNACIÓN AUTOMÁTICA DE NÚMERO ---
            if not self.socio.numero_socio:
                # Buscamos al socio que tenga el número más alto actualmente
                ultimo_socio = Socio.objects.exclude(numero_socio__isnull=True)\
                                            .exclude(numero_socio__exact='')\
                                            .order_by('-numero_socio').first()
                
                if ultimo_socio and ultimo_socio.numero_socio:
                    nuevo_numero = ultimo_socio.numero_socio + 1
                else:
                    nuevo_numero = 1  # Si es el primer socio histórico del club, arranca en 1

                # Lo guardamos con formato de 3 o 4 dígitos (ej: 001, 002, 145)
                self.socio.numero_socio = str(nuevo_numero).zfill(3)

            # Guardamos todos los cambios en el socio
            self.socio.save()