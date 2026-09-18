from django.db import models

class Socio(models.Model):

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
        estado = models.CharField(
                max_length=20,
                default= "pendiente"
        )

        fecha_reg = models.DateTimeField(
                auto_now_add=True
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
            {"pendiente","Pendiente"},
            {"aprobado", "Aprobado"},
            {"rechazado","Rechazado"}
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

      def __str__(self):
        return f"Pago de {self.socio}"