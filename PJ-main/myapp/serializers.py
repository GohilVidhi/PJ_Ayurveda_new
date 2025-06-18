
from rest_framework import serializers
from .models import*
import pytz


#======================Disease Code =============================    
    
class disease_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    disease_name = serializers.CharField(max_length=255, required=True)
    image = serializers.ImageField(required=False)
    description = serializers.CharField(max_length=1000, required=True)
    createdAt = serializers.SerializerMethodField()
    updatedAt=serializers.CharField(max_length=255, required=False)
    class Meta:
        model = disease
        fields = "__all__"
        read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
        
    def create(self, validated_data):
        return disease.objects.create(**validated_data)
    
    def validate_disease_name(self, value):
        """Ensure the disease name is unique for both creation and updates."""
        query = disease.objects.filter(disease_name=value)
        if self.instance:  # Exclude the current instance during update
            query = query.exclude(id=self.instance.id)
        
        if query.exists():
            raise serializers.ValidationError("A disease with this name already exists.")
        
        return value
    
    def update(self, instance, validated_data):
        instance.disease_name=validated_data.get('disease_name',instance.disease_name)
        instance.image=validated_data.get('image',instance.image)
        instance.description=validated_data.get('description',instance.description)
        instance.updatedAt=validated_data.get('updatedAt',instance.updatedAt)
    
        instance.save()   
        return instance    

#======================Disease Code End=============================    



#====================== Medicine Code ============================
    
class disease_serializer_show(serializers.ModelSerializer):
    
    class Meta:
        model = disease
        fields =['id','disease_name','image','description']


class medicine_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    disease_data = serializers.SlugRelatedField(slug_field='id', queryset=disease.objects.all(), required=True)
    medicine_name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField()
    image1 = serializers.ImageField(required=False,)
    image2 = serializers.ImageField(required=False, allow_null=True)
    image3 = serializers.ImageField(required=False, allow_null=True)
    how_work = serializers.CharField()
    inside = serializers.CharField()
    createdAt = serializers.SerializerMethodField()
    updatedAt=serializers.CharField(max_length=255, required=False)
   
    
    class Meta:
        model = medicine
        fields = "__all__"
        read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return medicine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.disease_data = validated_data.get('disease_data', instance.disease_data)
        instance.medicine_name = validated_data.get('medicine_name', instance.medicine_name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.image1 = validated_data.get('image1', instance.image1)
        instance.image2 = validated_data.get('image2', instance.image2)
        instance.image3 = validated_data.get('image3', instance.image3)
        instance.how_work = validated_data.get('how_work', instance.how_work)
        instance.inside = validated_data.get('inside', instance.inside)
        instance.updatedAt=validated_data.get('updatedAt',instance.updatedAt)
        instance.save()
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["disease_data"] = disease_serializer_show(instance.disease_data).data 
        return representation  


#====================== Medicine Code End============================


#====================== Health Parameter Code ============================

class health_parameters_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    disease_data = serializers.SlugRelatedField(slug_field='id', queryset=disease.objects.all(), required=True)
    parameter_name = serializers.CharField(max_length=255,required=True)
 
    
    class Meta:
        model = health_parameters
        fields = "__all__"


    def create(self, validated_data):
        return health_parameters.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.disease_data = validated_data.get('disease_data', instance.disease_data)
        instance.parameter_name = validated_data.get('parameter_name', instance.parameter_name)

        instance.save()
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["disease_data"] = disease_serializer_show(instance.disease_data).data 
        return representation  


#====================== Health Parameter Code End ============================


#====================== Sub Health Parameter Code ============================


class sub_health_parameters_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    disease_data = serializers.SlugRelatedField(slug_field='id', queryset=disease.objects.all(), required=True)
    parameter_data = serializers.SlugRelatedField(slug_field='id', queryset=health_parameters.objects.all(), required=True)
    sub_parameter_name=serializers.JSONField(required=False) 
    createdAt = serializers.SerializerMethodField()
    updatedAt=serializers.CharField(max_length=255, required=False)
    class Meta:
        model = sub_health_parameters
        fields = "__all__"
        read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')


    def create(self, validated_data):
        sub_names = validated_data.get("sub_parameter_name", [])
        if sub_names and isinstance(sub_names, list) and all(isinstance(i, str) for i in sub_names):
            validated_data["sub_parameter_name"] = [
                {"id": index + 1, "name": name} for index, name in enumerate(sub_names)
            ]
        return sub_health_parameters.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.disease_data = validated_data.get('disease_data', instance.disease_data)
        instance.parameter_data = validated_data.get('parameter_data', instance.parameter_data)
        sub_names = validated_data.get("sub_parameter_name")
    
        if sub_names is not None:
            if isinstance(sub_names, list) and all(isinstance(i, str) for i in sub_names):
                instance.sub_parameter_name = [
                    {"id": index + 1, "name": name} for index, name in enumerate(sub_names)
                ]
            elif isinstance(sub_names, list) and all(isinstance(i, dict) for i in sub_names):
                # If it's already in correct format, accept directly
                instance.sub_parameter_name = sub_names
            else:
                instance.sub_parameter_name = [] 
        instance.save()
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["disease_data"] = disease_serializer_show(instance.disease_data).data 
        representation["parameter_data"] = health_parameters_serializer(instance.parameter_data).data 
        return representation  

#====================== Ask To Expert Code ============================
    
class ask_to_expert_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    mobile_no = serializers.CharField(max_length=15)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    gender = serializers.CharField(max_length=10)
    blood_group = serializers.CharField(max_length=5)
    health_condition = serializers.CharField(max_length=50)
    disease = serializers.SlugRelatedField(slug_field='id', queryset=disease.objects.all(), required=True)
    healthparameter = serializers.SlugRelatedField(slug_field='id', queryset=health_parameters.objects.all(),many=True, required=True)
    subhealthparameter = serializers.ListField(
        child=serializers.CharField(), required=False
    )
    dietary = serializers.CharField()
    allergies = serializers.CharField()
    exercise = serializers.CharField()
    sleep = serializers.CharField()
    stress_level = serializers.CharField()

    prescription = serializers.FileField(allow_null=True, required=False)
    productId = serializers.CharField(allow_null=True, required=False)
    
    createdAt = serializers.SerializerMethodField()
    updatedAt=serializers.CharField(max_length=255, required=False)

    class Meta:
        model = ask_to_expert
        fields = "__all__"
        read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    
    def create(self, validated_data):
        healthparameters = validated_data.pop('healthparameter', [])
        instance = ask_to_expert.objects.create(**validated_data)
        instance.healthparameter.set(healthparameters)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.age = validated_data.get('age', instance.age)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        instance.health_condition = validated_data.get('health_condition', instance.health_condition)
        instance.disease = validated_data.get('disease', instance.disease)
        instance.subhealthparameter = validated_data.get('subhealthparameter', instance.subhealthparameter)
        instance.dietary = validated_data.get('dietary', instance.dietary)
        instance.allergies = validated_data.get('allergies', instance.allergies)
        instance.exercise = validated_data.get('exercise', instance.exercise)
        instance.sleep = validated_data.get('sleep', instance.sleep)
        instance.stress_level = validated_data.get('stress_level', instance.stress_level)
        instance.prescription = validated_data.get('prescription', instance.prescription)
        instance.productId = validated_data.get('productId', instance.productId)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)

        instance.save()

        if 'healthparameter' in validated_data:
            instance.healthparameter.set(validated_data['healthparameter'])

        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["disease"] = disease_serializer_show(instance.disease).data 
        representation["healthparameter"] = health_parameters_serializer(instance.healthparameter,many=True).data 

        return representation  


#====================== Ask To Expert Code End ============================
    

#====================== Order Code ============================

class user_serializer_show(serializers.ModelSerializer):
    
    class Meta:
        model = user
        fields =['id','name','email','user_id']


class order_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_data = serializers.SlugRelatedField(slug_field='user_id', queryset=user.objects.all(), required=True)
    product_data = serializers.SlugRelatedField(slug_field='id', queryset=medicine.objects.all(), required=True)
    status = serializers.CharField()
    address = serializers.CharField()
    mobile = serializers.CharField()
    delivery_time_preference = serializers.CharField()
    delivery_time = serializers.CharField(allow_null=True, required=False)
    createdAt = serializers.SerializerMethodField()
    updatedAt=serializers.CharField(max_length=255, required=False)


    class Meta:
        model = order
        fields = "__all__"
        read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    def create(self, validated_data):
        return order.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user_data = validated_data.get('user_data', instance.user_data)
        instance.product_data = validated_data.get('product_data', instance.product_data)
        instance.status = validated_data.get('status', instance.status)
        instance.address = validated_data.get('address', instance.address)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.delivery_time_preference = validated_data.get(
            'delivery_time_preference', instance.delivery_time_preference
        )
        instance.delivery_time = validated_data.get('delivery_time', instance.delivery_time)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)

        instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_serializer_show(instance.user_data).data
        representation["product_data"] = medicine_serializer_show(instance.product_data).data
        return representation
    
#====================== Order Code End ============================


#====================== User Code ============================

class user_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField(max_length=255, required=False, allow_blank=True)
    name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    membership = serializers.BooleanField(default=False)
    email = serializers.EmailField(max_length=255, required=False, allow_blank=True)
    createdAt = serializers.SerializerMethodField()
    updatedAt=serializers.CharField(max_length=255, required=False)



    class Meta:
        model = user
        fields = "__all__"
        read_only_fields = ['createdAt']
    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    
    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
   
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.name = validated_data.get('name', instance.name)
        instance.membership = validated_data.get('membership', instance.membership)
        instance.email = validated_data.get('email', instance.email)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        instance.save()
        return instance
    
#====================== User Code End ============================


#====================== Advertisement Code ============================
class advertisement_serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    createdAt = serializers.SerializerMethodField()
    updatedAt=serializers.CharField(max_length=255, required=False)
    
    class Meta:
        model = advertisement
        fields = "__all__"
        read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
        
    def create(self, validated_data):
        return advertisement.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.updatedAt = validated_data.get('updatedAt', instance.updatedAt)
        instance.save()
        return instance

#====================== Advertisement Code End============================

#====================== Contact Us Code  ============================

from datetime import datetime
class contact_us_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_data = serializers.SlugRelatedField(slug_field='user_id', queryset=user.objects.all(), required=True)
    messages = serializers.ListField(
        child=serializers.DictField(),  # Each message is a dictionary
        required=True
    )
    read=serializers.ListField(
        child=serializers.IntegerField(),  # Assuming read is a list of integers (IDs)
        required=False,
        allow_empty=True
    )
    class Meta:
        model = contact_us
        fields = "__all__"
    def validate_messages(self, new_messages, existing_messages=None):
        current_max_id = 0
        if existing_messages:
            current_max_id = max([int(msg.get('id', 0)) for msg in existing_messages])  # Ensure IDs are integers

       
        for message in new_messages:
            current_max_id += 1
            message['id'] = current_max_id
            message['createdAt'] = message.get('createdAt', datetime.now().isoformat())

        return new_messages

    def create(self, validated_data):
       
        messages = self.validate_messages(validated_data.pop('messages'))
        validated_data['messages'] = messages
        read = validated_data.pop('read', [])
        if read:
            validated_data['read'] = read
        return contact_us.objects.create(**validated_data)

    def update(self, instance, validated_data):
        new_messages = validated_data.get('messages', [])
        existing_messages = instance.messages if instance.messages else []
        processed_messages = self.validate_messages(new_messages, existing_messages)
        instance.messages.extend(processed_messages)
        instance.user_data = validated_data.get('user_data', instance.user_data)
        new_read = validated_data.get('read', [])
        instance.read = instance.read or []
        instance.read = list(set(instance.read + new_read))
        instance.save()
        return instance
    def to_representation(self, instance):

        representation = super().to_representation(instance)
        read_ids = instance.read or []  
        for message in representation['messages']:
            message_id = message.get('id')
            message['read'] = message_id in read_ids
       
        representation["user_data"] = user_serializer_show(instance.user_data).data
        return representation    

#====================== Contact Us Code End  ============================


#====================== Plan Code  ============================

class medicine_serializer_show(serializers.ModelSerializer):
    
    class Meta:
        model = medicine
        fields =['id','medicine_name']

class plan_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.CharField(max_length=255, allow_blank=True, required=False)
    price = serializers.IntegerField()
    createdAt = serializers.SerializerMethodField()
    disease_data = serializers.SlugRelatedField(slug_field='id',  queryset=disease.objects.all(),
        required=True )
    product_data = serializers.SlugRelatedField(
        slug_field='id',  
        queryset=medicine.objects.all())
    class Meta:
            model = plan
            fields = "__all__"
            read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  
        local_dt = obj.createdAt.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return plan.objects.create(**validated_data)

    def update(self, instance, validated_data):
       
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.price = validated_data.get('price', instance.price)
        instance.disease_data = validated_data.get('disease_data', instance.disease_data)
        instance.product_data = validated_data.get('product_data', instance.product_data)
        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["disease_data"] = disease_serializer_show(instance.disease_data).data
        representation["product_data"] = medicine_serializer_show(instance.product_data).data
        return representation

#====================== Plan Code End============================


#====================== Membership Code ============================

class plan_serializer_show(serializers.ModelSerializer):
    
    class Meta:
        model = plan
        fields =['id','title']



class membership_serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_data = serializers.SlugRelatedField(slug_field='user_id', queryset=user.objects.all(), required=True)
    plan_data = serializers.SlugRelatedField(slug_field='id', queryset=plan.objects.all(), required=True)
    image = serializers.ImageField(required=False, allow_null=True)
    paymentmethod = serializers.CharField(max_length=255, required=False, allow_blank=True)
    paymentDate = serializers.CharField(max_length=255, required=False, allow_blank=True)
    endDate = serializers.CharField(max_length=255, required=False, allow_blank=True)
    status = serializers.CharField(max_length=255, required=False, allow_blank=True)
    createdAt = serializers.SerializerMethodField()
    class Meta:
        model = user_membership
        fields = "__all__"
        read_only_fields = ['createdAt']

    def get_createdAt(self, obj):
            local_tz = pytz.timezone('Asia/Kolkata')  
            local_dt = obj.createdAt.astimezone(local_tz)
            return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    def create(self, validated_data):
        return user_membership.objects.create(**validated_data)

    def update(self, instance, validated_data):
      
        instance.user_data = validated_data.get('user_data', instance.user_data)
        instance.plan_data = validated_data.get('plan_data', instance.plan_data)
        instance.image = validated_data.get('image', instance.image)
        instance.paymentmethod = validated_data.get('paymentmethod', instance.paymentmethod)
        instance.paymentDate = validated_data.get('paymentDate', instance.paymentDate)
        instance.endDate = validated_data.get('endDate', instance.endDate)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_serializer_show(instance.user_data).data
        representation["plan_data"] = plan_serializer_show(instance.plan_data).data
        return representation

#====================== Membership Code End ============================


#============== Admin Login Code  ==========================


import pytz
class admin_login_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=50,required=True)
    password=serializers.CharField(max_length=50,required=True)
    timestamp = serializers.SerializerMethodField()

    class Meta:
        models=admin_login
        fields ='__all__'
        exclude = ('id',)
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return admin_login.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email=validated_data.get('email',instance.email)
        instance.password=validated_data.get('password',instance.password)

        instance.save()
        return instance

#============== Admin Login Code End  ==========================

