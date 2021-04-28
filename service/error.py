from rest_framework.response import Response
from rest_framework import status


class Error:

    @staticmethod
    def error_fields(field):
        err = f"{str(field)} fields have been transferred"
        return Response({'message': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def error_incorrect_code():
        err = "incorrect_code"
        return Response({"error": err}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def error_obj_does_not_exist(model_name):
        err = f"{model_name} does not exist"
        return Response({"error": err}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def error_obj_already_exist(err):
        return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def error_value_error(err):
        return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)