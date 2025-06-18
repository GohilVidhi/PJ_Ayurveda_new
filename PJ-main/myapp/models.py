from django.db import models
from django_mysql.models import ListTextField
# Create your models here.


#======================Disease=============================    
class disease(models.Model):
    disease_name = models.CharField(max_length=255,blank=True,null=True)
    image=models.ImageField(upload_to="image",blank=True,null=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updatedAt=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.disease_name


#=======================Medicine============================   
class medicine(models.Model):
    disease_data= models.ForeignKey(disease, on_delete=models.CASCADE, blank=True, null=True)
    medicine_name= models.CharField(max_length=255, blank=True, null=True)
    price= models.IntegerField(blank=True, null=True)
    description= models.TextField(blank=True, null=True)
    image1= models.ImageField(upload_to='image', blank=True, null=True)
    image2= models.ImageField(upload_to='image', blank=True, null=True)
    image3= models.ImageField(upload_to='image', blank=True, null=True)
    how_work= models.TextField(blank=True, null=True)
    inside= models.TextField(blank=True, null=True)
    createdAt= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt=models.CharField(max_length=255,blank=True,null=True)
   
    def __str__(self):
        return self.medicine_name


#====================Health_Parameters===============================  
      
class health_parameters(models.Model):
    disease_data = models.ForeignKey(disease,on_delete=models.CASCADE,blank=True,null=True)
    parameter_name=models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self):
        return self.parameter_name

#=======================Sub_Health_Parameters============================



class sub_health_parameters(models.Model):
    disease_data = models.ForeignKey(disease,on_delete=models.CASCADE,blank=True,null=True)
    parameter_data = models.ForeignKey(health_parameters,on_delete=models.CASCADE,blank=True,null=True)
    sub_parameter_name=models.JSONField(default=list)
    createdAt= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt=models.CharField(max_length=255,blank=True,null=True)




# ======================= Ask To Expert ============================


class ask_to_expert(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    mobile_no = models.CharField(max_length=15,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    weight = models.FloatField(blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)
    blood_group = models.CharField(max_length=5,blank=True,null=True)
    health_condition = models.CharField(max_length=50,blank=True,null=True)
    disease = models.ForeignKey(disease,on_delete=models.CASCADE,blank=True,null=True)
    healthparameter = models.ManyToManyField(health_parameters,blank=True,null=True)
    subhealthparameter=models.JSONField(default=list,blank=True,null=True)
    dietary = models.CharField(max_length=100,blank=True,null=True)
    allergies = models.CharField(max_length=255,blank=True,null=True)
    exercise = models.CharField(max_length=100,blank=True,null=True)
    sleep = models.CharField(max_length=50,blank=True,null=True)
    stress_level = models.CharField(max_length=50,blank=True,null=True)
    prescription = models.FileField(upload_to='image/', blank=True, null=True)
    productId = models.CharField(max_length=100, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updatedAt = models.CharField(max_length=150,blank=True,null=True)

#======================= User ============================
class user(models.Model):
    user_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    membership=models.BooleanField(default=False)
    email = models.EmailField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user_id


#======================= Order ============================

class order(models.Model):
    user_data = models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    product_data = models.ForeignKey(medicine,on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(max_length=50, default="Pending")
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    delivery_time_preference = models.CharField(max_length=100)
    delivery_time = models.CharField(max_length=100, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.CharField(max_length=255, blank=True, null=True)

#======================= Advertisement ============================

class advertisement(models.Model):
    image = models.ImageField(upload_to='image', blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.CharField(max_length=255, blank=True, null=True)

#======================= Contact Us ============================
    
class contact_us(models.Model):
    user_data = models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    messages = models.JSONField(default=list)
    read = ListTextField(base_field=models.IntegerField(), size=None, blank=True, null=True)
    def __str__(self):
        return self.user_data.user_id


#======================= Plan ============================
class plan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    disease_data = models.ForeignKey(disease, on_delete=models.CASCADE,blank=True, null=True)
    product_data = models.ForeignKey(medicine, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title
    
#======================= Membership ============================

class user_membership(models.Model):
    user_data = models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    plan_data = models.ForeignKey(plan, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    paymentmethod = models.CharField(max_length=255, blank=True, null=True)
    paymentDate = models.CharField(max_length=255, blank=True, null=True)
    endDate = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.user_data.user_id


#============== Admin Login Code  ==========================

class admin_login(models.Model):
    email=models.EmailField(max_length=255,blank=True,null=True)
    password=models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.email







"""

1 : user                    ----
2 : disease                 -----
3 : health_parameters       -----
4 : sub_health_parameters   -----
5 : medicine                -----
6 : ask_to_expert           -----
7 : advertisement           -----
8 : contact_us              -----
9 : membership
10 : plan
11 : order                  ----- 


"""    