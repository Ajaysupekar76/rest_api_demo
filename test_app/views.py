from rest_framework import views, status
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer

class CompanyView(views.APIView):

    def get(self, request, company_id=None):
        # If company_id is provided, fetch a specific company
        if company_id:
            try:
                company = Company.objects.get(company_id=company_id)
                serializer = CompanySerializer(company)
                return Response(serializer.data)
            except Company.DoesNotExist:
                return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

        # If no company_id is provided, return all companies
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
   
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, company_id):
        try:
            company = Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompanySerializer(company, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, company_id):
        try:
            company = Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

        company.delete()
        return Response({"detail": "Company deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
