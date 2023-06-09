import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from django.db import models




class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    preco = models.IntegerField(null=False)
    url = models.TextField(max_length=99999)
    qrcode_image = models.ImageField(upload_to='qr_code_images', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.preco} - {self.url}"

    def generate_qrcode(self):
       qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
       )
       qr.add_data(str(self.nome))
       qr.make(fit=True)

       img = qrcode.make(str(self.nome), box_size=20)
       stream = BytesIO()
       img.save(stream, format='PNG')
       stream.seek(0)
       self.qrcode_image.save(f"{self.nome}.png", InMemoryUploadedFile(
            stream, None, f"{self.nome}.png", 'image/png', img.tell, None
        ), save=False)

    def save(self, *args, **kwargs):
        if not self.id:  # Executa apenas ao criar um novo objeto
            self.generate_qrcode()
        super().save(*args, **kwargs)
         


class ProdutoCarrinho(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    preco = models.IntegerField(null=False)
    img = models.TextField(max_length=99999)
