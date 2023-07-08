from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
import io
from app.models import Catalyst
# from django.core import serializers
from app.serializers import FileDataSerializer


# Create your views here.

class FileDataApiView(APIView):
    def post(self, request):
        file = request.FILES['file']
        decode_file = file.read().decode('utf-8')

        io_string = io.StringIO(decode_file)
        next(io_string)

        flag = False
        str1 = ''

        for row in csv.reader(io_string, delimiter=',', quotechar='|'):
            list2 = []
            for i in row:
                if i.startswith('""') and i.endswith('"'):
                    list2.append(i.replace('"', ''))
                    
                elif i.startswith('"'):
                    str1 += i.replace('"', '')
                    flag = True
                    
                elif flag == True:
                    str1 += i.replace('"', '')
                    if i.endswith('"'):
                        flag = False
                        list2.append(str1)
                        str1 = ''
                        
                else:
                    list2.append(i)
            
            print(list2)
            catalyst = Catalyst.objects.create(
                company_number = list2[0],
                name = list2[1],
                domain = list2[2],
                year_founded = list2[3],
                industry = list2[4],
                range = list2[5],
                locality = list2[6],
                country = list2[7],
                linked_in_url = list2[8],
                current_employee_estimate = list2[9],
                total_employee_estimate = list2[10],
                
            )

            # catalyst.save()
        return Response({'message': 'Data Successfully Inserted'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        data = Catalyst.objects.all()
        serializer = FileDataSerializer(data, many=True)
        return Response(serializer.data)
    
class SearchDataApiView(APIView):
    def get(self, request, data):
        print('hello:', data)
        return Response({'msg': 'hello'}, status=status.HTTP_200_OK)



        # json_data = serializers.serialize('json', data)
        # return Response(json_data, content_type="application/json")