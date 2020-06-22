from  .models import Userprofile
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404
from .serializers import UserSerializer
from rest_framework import status, views, generics, viewsets, permissions
from django.db import connection
import collections

from rest_framework import status, views, generics, viewsets, permissions
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
import psycopg2
from rest_framework.permissions import AllowAny

class UserViewSet(ModelViewSet):
    queryset = Userprofile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

# All Users View
class users(object):

    def get_data():
        try:
            cur = connection.cursor()
            cur.callproc('users')
            rows = cur.fetchall()
            print('testing',rows)
            field_names = [i[0] for i in cur.description]
            object_lists = []
            for row in rows:
                d = collections.OrderedDict()
                d[field_names[0]] = row[0]
                d[field_names[1]] = row[1]
                d[field_names[2]] = row[2]
                d[field_names[3]] = row[3]
                object_lists.append(d)

            print('testing',object_lists)
            return object_lists
        except Userprofile.DoesNotExist:
            return None

class UserView(views.APIView):

    def get(self,request):
        total = users.get_data(

        )

        print(total)
        if total is None:
            return Response({
                'status': 'No such Category',
                'message': 'Category not found'
            }, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(total)
