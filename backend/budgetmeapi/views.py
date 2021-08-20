from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from budgetmeapi.models import User
from budgetmeapi.serializers import UserSerializer
from rest_framework.decorators import api_view

# # Create your views here.
def vue_test(request):
    return render(request, 'budgetmeapi/test.html')

# @api_view(['GET', 'POST', 'DELETE'])
# def user_list(request):
#     pass

# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):
#     # find User by pk
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return JsonResponse({'message': 'This User doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)

# @api_view()
