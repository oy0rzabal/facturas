from django.db import models

class E_Propiedades(models.Model):
    m2_terreno= models.FloatField(default=0)
    m2_construccion = models.FloatField(default=0)
    estatus_legal_propiedad=models.CharField(max_length=100, unique=True)
    tipo_inmubele = models.CharField(max_length=100, unique=True, primary_key=True)
    antiguedad = models.CharField(max_length=100, unique=True)
    etapa=models.FloatField(default=0)
    ingresos = models.FloatField(default=0)
    gastos_general =models.FloatField(default=0)
    precio_evaluo_estimacion_mercado = models.FloatField(default=0)
    precio_m2_mercado = models.FloatField(default=0)
    ganancias_totales = models.FloatField(default=0)

    def __str__(self):
        texto= "{0}{1}"
        return texto.format(self.m2_terreno,
                            self.m2_construccion,
                            self.estatus_legal_propiedad,
                            self.tipo_inmubele,
                            self.antiguedad,
                            self.etapa,
                            self.ingresos,
                            self.gastos_general,
                            self.precio_evaluo_estimacion_mercado,
                            self.precio_m2_mercado,
                            self.ganancias_totales,
                            )