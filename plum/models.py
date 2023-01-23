from csv import unregister_dialect
from django.db import models



# Create your models here.
class stform(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    contact=models.IntegerField()
    password=models.CharField(max_length=70)
    
class category(models.Model):
    name=models.CharField(max_length=40)
        
class products(models.Model):
    image=models.ImageField(upload_to='static/uploads/')
    heading= models.CharField(max_length=100)
    category=models.ForeignKey(category, on_delete=models.CASCADE,default=1)
    discription=models.TextField()
   
    def __str__(self):
       return self.heading
      
     
     
class cart(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    quantity=models.IntegerField()
    status=models.BooleanField(default=False)
    added_on=models.DateTimeField( auto_now_add=True,null=True)
    update_on=models.DateTimeField( auto_now=True,null=True)
      
    def __str__(self):
      return self.product.heading
  
class addtocart(models.Model):
    user_id=models.ForeignKey(stform,on_delete=models.CASCADE)
    cat_id=models.ForeignKey(category,on_delete=models.CASCADE)
      
