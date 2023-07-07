from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Technician(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Technician'
    
    def __str__(self):
        return self.name


class Product_name(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name

class Product_code(models.Model):
    Product_name = models.ForeignKey(Product_name, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
   
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Serial no.'

    def __str__(self):
        return self.name

# class Product_code(models.Model):
#     NAME = Product_name.objects.all()
#     name = models.CharField(max_length=255)
#     Choice = models.ForeignKey(Product_name, verbose_name="Category", on_delete=models.CASCADE, blank=True, null=True)
#     class Meta:
#         ordering = ('name',)
#         verbose_name_plural = 'Product Code'
    
#     def __str__(self):
#         return self.name
     

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    Product_name = models.ForeignKey(Product_name, related_name='items', on_delete=models.CASCADE)
    Technician = models.ForeignKey(Technician, null=True, related_name='items', on_delete=models.CASCADE)
    Patient_name = models.CharField(max_length=255)
    Product_code = models.ForeignKey(Product_code, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Serial no.")
    
    Address = models.TextField(blank=True, null=True)
    Amount = models.FloatField(null=True)
    Contact = PhoneNumberField(blank=True)
    Issue_date = models.DateField(null=True)
    Rent_start_date = models.DateField(null=True)
    Rent_end_date = models.DateField(null=True)
    is_sold = models.BooleanField('Paid', default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Reference = models.TextField(blank=True, null=True)
    Vendor = models.TextField(blank=True, null=True)
     
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Patients '

    def __str__(self):
        return self.Patient_name