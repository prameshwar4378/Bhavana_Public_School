from import_export import resources
from .models import DB_Enqueries

class Enquiry_Resource(resources.ModelResource):
    class Meta:
        model = DB_Enqueries
        fields=['id','full_name','email','mobile','subject','message','enquiry_date']

        