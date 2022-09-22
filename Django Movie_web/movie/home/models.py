from django.db import models

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default="")
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE,null=False,default="")
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length= 200)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



# class user(models.Model):
#     Name = models.CharField(max_length=200)
#     Username = models.CharField(max_length=200)
#     Email =models.EmailField(max_length=200)
#     Phone = models.CharField(max_length=13)
#     Password = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.Name
#
#     def isExists(self):
#         if user.objects.filter(Email = self.Email):
#             return True
#         return False
#     @staticmethod
#     def get_user_by_email(email):
#         try:
#             return user.objects.get(Email=email)
#         except:
#             return False
