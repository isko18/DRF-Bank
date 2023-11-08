from rest_framework import mixins 
from rest_framework.viewsets import GenericViewSet
from apps.users.models import BankUser
from apps.users.serializers import UserSerializers, RegisterUserSerializers
# Create your views here.

class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin):
    queryset = BankUser.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.action in ('creat', ):
            return RegisterUserSerializers
        
        return UserSerializers