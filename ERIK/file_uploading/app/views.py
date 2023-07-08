import pandas as pd
from django.conf import settings
from django.db import IntegrityError
from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os, openpyxl
from app.models import EmployeesDetails
from app.serializers import RetrieveDataSerializer
from rest_framework import status

class FileUploadApiView(APIView):
    def post(self, request):
        
        #accessing excel file from postman
        file_obj = request.FILES['file']
        check_extension = str(file_obj)

        # check file extention
        if check_extension.endswith(".xlsx"):
            file_path = os.path.join(settings.MEDIA_ROOT, file_obj.name)

            #upload file
            with open(file_path, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

            return Response({'msg': 'File uploaded successfully'},status=status.HTTP_200_OK)
        
        else:
            return Response({'msg': 'Please Upload xlsx file only'},status=status.HTTP_404_NOT_FOUND)
        

class DataApiView(APIView):
    def get(self, request,  *args, **options):
            # accessing the uploaded file path
            folder_path = 'media/'
            
            if  os.listdir(folder_path):
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)

                    #use open pyxl to load workbook and active axcel sheet
                    wb = openpyxl.load_workbook(file_path)
                    sheet = wb.active
                    # all column name stored in header_row
                    header_row = sheet[1]
                    sheet_header = []

                    for cell in header_row:
                        sheet_header.append(cell.value)
                    
                    # save fields name in model_header
                    fields = EmployeesDetails._meta.get_fields()
                    model_headers=[field.name for field in fields][1:]

                    # check count of column headers
                    if len(sheet_header) == len(model_headers):
                        for idx in range(0, len(model_headers)):
                            # check the column name from excel with db fields
                            if model_headers[idx] != sheet_header[idx]:
                                return Response({'msg': 'Column name are not same as in Model fields'}, os.remove(file_path))
                        else:
                            try:
                                for row in sheet.iter_rows(min_row=2, values_only=True):
                                    # check is there any numerical value in emp_name
                                    if not str(row[0]).isalpha():
                                        return Response({'msg': 'emp_name should not be numeric or alphanumaric only alphabet'})
                                    else:
                                        # excel data insert in database
                                        employee = EmployeesDetails.objects.create(
                                            emp_name = row[0],
                                            emp_city = row[1],
                                            emp_state = row[2],
                                            emp_designation = row[3],
                                            emp_date_of_joinning = row[4],
                                            emp_status = row[5],
                                            emp_salary = row[6]
                                        )
                                        employee.save()
                                os.remove(file_path)    
                                return Response({'msg': 'Data successfully added'}, status=status.HTTP_201_CREATED)
                            
                            except IntegrityError:
                                return Response({"msg": "This rows are duplicate or None values"})
                            
                            except ValidationError:
                                return Response({'msg': 'Not proper date format'})
                            
                            
                    else:
                        return Response({'msg': 'Column length are not equal'}, os.remove(file_path))
                    
            else:
                return Response({'msg': 'file not found'})
        
        
class RetrieveDataApiView(APIView):

    # retrieve all data
    def get(self, request):

        data = EmployeesDetails.objects.all()
        serializer = RetrieveDataSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK )
    

class DataExportApiView(APIView):
    def get(self, request):
        # query to get data from database table
        queryset = EmployeesDetails.objects.all().annotate().values_list('emp_name','emp_city','emp_state','emp_designation','emp_date_of_joinning','emp_status','emp_salary')
        
        df = pd.DataFrame(list(queryset), columns=['emp_name','emp_city','emp_state','emp_designation','emp_date_of_joinning','emp_status','emp_salary'])
   
        # # Save the DataFrame to an XLSX file
        filepath = 'convert_in_excel.xlsx'
        df.to_excel(filepath, index=False)

        # # Return the file path for download
        return Response({'file': filepath}, status=status.HTTP_200_OK)
    
class Test(APIView):
    def get(self, request):
            folder_path = 'media/'
            for file in os.listdir(folder_path):
                    
                file_path = os.path.join(folder_path, file)
                work_book = openpyxl.load_workbook(file_path)
                sheet = work_book.active
                for row in sheet.iter_rows(min_row=2, values_only=True):

                    print('sheettt:', row)
                
            return Response({'msg': 'success'}, status=status.HTTP_404_NOT_FOUND)