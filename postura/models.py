from django.db import models

class RegistrosPostura(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    estado_postura = models.CharField(max_length=255)
    nivel_respaldo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registros_postura'


class HistoricoPostura(models.Model):
    id = models.AutoField(primary_key=True)
    registro = models.ForeignKey(RegistrosPostura, on_delete=models.CASCADE, db_column='registro_id')
    timestamp = models.DateTimeField()
    postura_anterior = models.CharField(max_length=255)
    postura_actual = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'historico_postura'


class Alertas(models.Model):
    id = models.AutoField(primary_key=True)
    registro = models.ForeignKey(RegistrosPostura, on_delete=models.CASCADE, db_column='registro_id')
    nombre = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alertas'


class CorreccionesTipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correcciones_tipo'


class Correcciones(models.Model):
    id = models.AutoField(primary_key=True)
    registro = models.ForeignKey(RegistrosPostura, on_delete=models.CASCADE, db_column='registro_id')
    correccion_tipo = models.ForeignKey(CorreccionesTipo, on_delete=models.CASCADE, db_column='correccion_tipo_id')
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'correcciones'


class Estadisticas(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(unique=True)
    tiempo_correcto_total = models.IntegerField(default=0)
    tiempo_incorrecto_total = models.IntegerField(default=0)
    tiempo_sin_sentarse = models.IntegerField(default=0)
    total_alertas = models.IntegerField(default=0)
    total_correcciones = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'estadisticas'
