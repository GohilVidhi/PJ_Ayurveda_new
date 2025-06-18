
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
print("helloo")

# =============== pagination code ==========================

from rest_framework.pagination import PageNumberPagination
class CustomPagination(PageNumberPagination):
    page_size = 1  # You can change this number
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response({
           
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })
def get_paginated_result(queryset, request, serializer_class, paginator_class):
    paginator = paginator_class()
    page = paginator.paginate_queryset(queryset, request)
    serializer = serializer_class(page, many=True)
    return paginator.get_paginated_response(serializer.data) 

# ===============pagination code end==========================


#======================Disease Code ============================= 
   
class disease_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = disease.objects.get(id=id)
                serializer = disease_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except disease.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = disease.objects.all().order_by("-id")
            serializer = disease_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, disease_serializer, CustomPagination)

    def post(self, request):
        serializer = disease_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = disease.objects.get(id=id)
            except disease.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = disease_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = disease.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except disease.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})
        
#====================== Disease Code End ============================= 


#====================== Medicine Code ============================= 

   
class medicine_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = medicine.objects.get(id=id)
                serializer = medicine_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except medicine.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = medicine.objects.all().order_by("-id")
            serializer = medicine_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, medicine_serializer, CustomPagination)

    def post(self, request):
        serializer = medicine_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = medicine.objects.get(id=id)
            except medicine.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = medicine_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = medicine.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except medicine.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})

#====================== Medicine Code End ============================= 


#====================== Health Parameters Code ============================= 

   
class health_parameters_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = health_parameters.objects.get(id=id)
                serializer = health_parameters_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except health_parameters.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = health_parameters.objects.all().order_by("-id")
            serializer = health_parameters_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, health_parameters_serializer, CustomPagination)

    def post(self, request):
        serializer = health_parameters_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = health_parameters.objects.get(id=id)
            except health_parameters.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = health_parameters_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = health_parameters.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except health_parameters.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})

#====================== Health Parameters Code End ============================= 
        


#====================== Sub Health Parameters Code ============================= 

   
class sub_health_parameters_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = sub_health_parameters.objects.get(id=id)
                serializer = sub_health_parameters_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except sub_health_parameters.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = sub_health_parameters.objects.all().order_by("-id")
            serializer = sub_health_parameters_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, sub_health_parameters_serializer, CustomPagination)

    def post(self, request):
        serializer = sub_health_parameters_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = sub_health_parameters.objects.get(id=id)
            except sub_health_parameters.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = sub_health_parameters_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = sub_health_parameters.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except sub_health_parameters.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})

#====================== Health Parameters Code End ============================= 




#====================== Ask To Expert Code ============================= 

   
class ask_to_expert_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = ask_to_expert.objects.get(id=id)
                serializer = ask_to_expert_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except ask_to_expert.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = ask_to_expert.objects.all().order_by("-id")
            serializer = ask_to_expert_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, ask_to_expert_serializer, CustomPagination)

    def post(self, request):
        serializer = ask_to_expert_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = ask_to_expert.objects.get(id=id)
            except ask_to_expert.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = ask_to_expert_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = ask_to_expert.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except ask_to_expert.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})

#====================== Ask To Expert Code End ============================= 



#====================== Order Code ============================= 

   
class order_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = order.objects.get(id=id)
                serializer = order_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except order.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = order.objects.all().order_by("-id")
            serializer = order_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, order_serializer, CustomPagination)

    def post(self, request):
        serializer = order_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = order.objects.get(id=id)
            except order.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = order_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = order.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except order.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})

#====================== Ask To Expert Code End ============================= 


#==================== User Code =============================
class user_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = user.objects.get(user_id=id)
                serializer = user_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except user.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = user.objects.all().order_by("-id")
            serializer = user_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, user_serializer, CustomPagination)

    def post(self, request):
        serializer = user_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = user.objects.get(user_id=id)
            except user.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = user_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = user.objects.get(user_id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except user.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})
        
#==================== User Code End =============================
#====================== User Login View =============================
from rest_framework import status
class user_login_view(APIView):
    def post(self, request):
        serializer = user_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            try:
                user_obj = user.objects.get(email=email)
                if user_obj.password == password:
                    return Response({
                        "success": True,
                        "data": {
                            "id": str(user_obj.id),  # assuming this is a MongoDB-style ObjectId
                            "userId": user_obj.user_id,
                            "name": user_obj.name,
                            "email": user_obj.email
                        }
                    }, status=status.HTTP_200_OK)
            except user.DoesNotExist:
                pass

            return Response({
                "success": False,
                "message": "Unregistered Email & Password"
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            "success": False,
            "message": "Invalid input",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
#====================== User Login View End =============================

#==================== Advertisement Code =============================
 
class advertisement_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = advertisement.objects.get(id=id)
                serializer = advertisement_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except advertisement.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = advertisement.objects.all().order_by("-id")
            serializer = advertisement_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, advertisement_serializer, CustomPagination)

    def post(self, request):
        serializer = advertisement_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = advertisement.objects.get(id=id)
            except advertisement.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = advertisement_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = advertisement.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except advertisement.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})


#==================== Advertisement Code End =============================


#====================== Contact Us Code ============================
class contact_us_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = contact_us.objects.get(id=id)
                serializer = contact_us_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except contact_us.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = contact_us.objects.all().order_by("-id")
            serializer = contact_us_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, contact_us_serializer, CustomPagination)

    def post(self, request):
        serializer = contact_us_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = contact_us.objects.get(id=id)
            except contact_us.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = contact_us_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = contact_us.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except contact_us.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})
        
#====================== Contact Us Code End ============================


#====================== Plan Code ============================

class plan_View(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = plan.objects.get(id=id)
                serializer = plan_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except plan.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = plan.objects.all().order_by("-id")
            serializer = plan_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, plan_serializer, CustomPagination)

    def post(self, request):
        serializer = plan_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = plan.objects.get(id=id)
            except plan.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = plan_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = plan.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except plan.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})
        
#====================== Plan Code End ============================


#====================== Membership Code ============================
        
class membership_View(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = user_membership.objects.get(id=id)
                serializer = membership_serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except user_membership.DoesNotExist:
                return Response({'status': "Invalid Id"})
            
        else:
            uid = user_membership.objects.all().order_by("-id")
            serializer = membership_serializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
            # return get_paginated_result(uid, request, membership_serializer, CustomPagination)

    def post(self, request):
        serializer = membership_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        if id:
            try:
                uid = user_membership.objects.get(id=id)
            except user_membership.DoesNotExist:
                return Response({'status': "invalid Id"})
            
            serializer = membership_serializer(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        else:
                return Response({'status': "invalid data"})
        

    def delete(self, request, id=None):
        if id:
            try:
                uid = user_membership.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except user_membership.DoesNotExist:
                return Response({'status': "invalid Id"})
        else:
            return Response({'status': "invalid data"})
        
#====================== Membership Code End ============================


#============== Admin Login Code  ==========================


class admin_login_view(APIView):
    def get(self, request):
        uid = admin_login.objects.all().order_by("-id")
        serializer = admin_login_serializers(uid, many=True)
        return Response({'status': 'success', 'data': serializer.data})
    
    def post(self,request):
            serializer=admin_login_serializers(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                uid=admin_login.objects.filter(email=email).exists()
                if uid:
                    uid=admin_login.objects.get(email=email)
                    if uid.password == password:
                        serializer=admin_login_serializers(uid)

                        return Response({'status':'success','data':serializer.data})
                    else:
                        return Response({'status':'invalid password'})
                else:
                    return Response({'status':'invalid email'})

            else:
                return Response({'status':"invalid data"})

#============== Admin Login Code End  ==========================


