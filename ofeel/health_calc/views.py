from django.contrib.auth.models import Group
from ofeel.users.models import User
from rest_framework import viewsets
#from ofeel.health_calc.serializers import UserSerializer, GroupSerializer
from ofeel.health_calc.serializers import TypeSerializer, CategorySerializer
from ofeel.health_calc.models import Dish, Type, Category

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#class DishViewSet(viewsets.ModelViewSet):
#    queryset = Dish.objects.all()
#    serializer_class = DishSerializer

#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer


#class GroupViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer
