from django.contrib.auth.models import User

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.http import Http404
from rest_framework import generics, permissions  # , mixins, status

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


# @csrf_exempt  #! You shouldn't normally do this...
# @api_view(["GET", "POST"])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         # data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetList(APIView):
#     """
#     List all code snippets, or create a new snippet.
#     """

#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetList(
    # mixins.ListModelMixin,  # gives us .list()
    # mixins.CreateModelMixin,  # gives us .create()
    # generics.GenericAPIView,  # Base class for this view
    generics.ListCreateAPIView
):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


# @csrf_exempt  #! You shouldn't normally do this...
# @api_view(["GET", "PUT", "DELETE"])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         # data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a code snippet.
#     """

#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetDetail(
    # mixins.RetrieveModelMixin,  # gives us .retrieve
    # mixins.UpdateModelMixin,  # gives us .update
    # mixins.DestroyModelMixin,  # gives us .delete
    # generics.GenericAPIView,  # Base class for this view
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
