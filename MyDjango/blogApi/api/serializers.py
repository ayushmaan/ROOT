from .models import Books
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = [

            'id','BookName','Author',"Pages"
        ]



class BookCreateSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = [

            'BookName','Author',"Pages","NoOfReader"
        ]
