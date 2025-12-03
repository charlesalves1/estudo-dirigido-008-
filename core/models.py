from django.db import models
class Unidade(models.Model):    
    nome = models.CharField(max_length=120)    
    endereco = models.CharField(max_length=200, blank=True)  
    def __str__(self):        
        return self.nome
    
class Sala(models.Model):    
        nome = models.CharField(max_length=120)    
        unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='salas')   
        def __str__(self):        
            return f"{self.nome} - {self.unidade.nome}"
        
class Status(models.Model):    
            nome = models.CharField(max_length=50)    
            def __str__(self):        
                return self.nome
            
class Bem(models.Model):    
        nome = models.CharField(max_length=200)
        tombo = models.CharField(max_length=50, unique=True)
        unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="bens")
        sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True)
        status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True) 

        criando_em = models.DateTimeField(auto_now_add=True)
        atualizado_em = models.DateTimeField(auto_now=True)
        def __str__(self):        
                    return f"{self.nome} ({self.tombo})"
