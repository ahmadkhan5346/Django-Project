from django.http import HttpResponse
import pandas as pd
from django.contrib.auth.models import User


def createSuperUser(request):
    data = pd.read_csv("user_create.csv")
    # print(data.loc[0, 'username'])

    # for i in range(data.shape[0]):
    #     print(data.loc[i, 'username'])

    try:
        for i in range(
            data.shape[0]
        ):  # data.shape[0] it will give len of row and shap[1] len of column
            try:
                user = User.objects.create_user(  # password as it save then use create_user password save in hashing forma
                    username=data.loc[i, "username"],
                    first_name=data.loc[i, "first_name"],
                    last_name=data.loc[i, "last_name"],
                    email=data.loc[i, "email"],
                    is_active=data.loc[i, "is_active"],
                    is_staff=data.loc[i, "is_staff"],
                    is_superuser=data.loc[i, "is_superuser"],
                    password=data.loc[i, "password"],
                )  # data.loc[rowindex, column_name] gives all column name correspend row according to ndex
            except:
                print(
                    "Already exist=================", data.loc[i, "username"]
                )  # You can use pass statement
        return HttpResponse("User created successfully")

    except Exception as e:
        return HttpResponse("Some problem for file path")


# def adding_users(request):
#     print("came inside")
#     data = pd.read_csv("/home/bhavana_sawant/dsp/india-gcp-dsp/dsp_app/user_list - Superuser (1).csv")
#     print('Got file')
#     try:
#         for i in range(data.shape[0]):
#             try:
#                 user = User.objects.create_user(username=data.loc[i,'username'],first_name=data.loc[i,'first_name'],last_name=data.loc[i,'last_name'],email=data.loc[i,'email'],is_active=data.loc[i,'is_active'],is_staff=data.loc[i,'is_staff'],is_superuser=data.loc[i,'is_superuser'],password='pcil1234')
#                 print("executed Successfully",data.loc[i,'username'])
#             except:
#                 print('Already exists====================',data.loc[i,'username'])

#         return HttpResponse("==============USERS ADDED SUCCESFULLY======================")
#     except Exception as e:
#         log.exception('export_cse_data:Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e)._name_, e)
#         return render(request,'warning.html',{"msg":"Something went wrong!!!"})
