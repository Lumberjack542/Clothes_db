from rest_framework.viewsets import ModelViewSet
from .serializers import ShoesSerializer, ShoesCreateSerializer
from .models import Shoes
# Create your views here.


class ShoesApiView(ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

    def get_serializer_class(self):
        if self.action in ['update', 'create']:
            self.serializer_class = ShoesCreateSerializer
        else:
            self.serializer_class = ShoesSerializer

        return self.serializer_class







