from ofeel.health_calc.models import Dish, Type, Category
from rest_framework import serializers

#from ofeel.users.models import User
#from django.contrib.auth.models import Group

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('name',) 

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    type = TypeSerializer(required=False)

    class Meta:
        model = Category
        fields = ('name', 'type')

#class DishSerializer(serializers.HyperlinkedModelSerializer):
#    url = serializers.HyperlinkedIdentityField(view_name="health:dish-detail")

#    class Meta:
#        model = Dish
#        fields = '__all__' 

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

#    class Meta:
#        model = User
#        fields = ('url', 'username', 'email', 'groups')


#class GroupSerializer(serializers.HyperlinkedModelSerializer):
#    url = serializers.HyperlinkedIdentityField(view_name="group-detail")

#    class Meta:
#        model = Group
#        fields = ('url', 'name')