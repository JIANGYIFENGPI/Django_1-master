from django.contrib.auth.models import User, Group
from models import Movie
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
