from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f'{self.nome} {self.uf}'
    
class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete= models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
            return self.nome
    
class Leitor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nome} {self.email} {self.cpf}'
    
class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    preco = models.FloatField()
    data_publicacao = models.DateField()
    def __str__(self):
        return f'{self.nome} {self.autor} {self.editora} {self.genero} {self.preco} {self.data_publicacao}'
    

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    data_devolucao = models.DateField()
    def __str__(self):
        return f'{self.data_emprestimo} {self.livro} {self.leitor} {self.data_devolucao}'
    

