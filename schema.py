import graphene
from graphene_django import DjangoObjectType

# from customer.models import Customer
# from drivers.models import Driver, MonthlyDeductionTable, DriverNote, DriverSafety
# from trailers.models import Trailer, TrailerSafetyDetail, TrailerMonthlyDeduction, TrailerRepairService
# from trucks.models import Truck, TruckSafetyDetail, TruckMonthlyDeduction
from vendor.models import Vendor


## QUERIES ##
class VendorType(DjangoObjectType):
    class Meta:
        model = Vendor
        fields = (
            "user",
            "full_name",
            "address_street",
            "address_city",
            "address_state",
            "address_unit",
            "address_ZIP",
            "EIN_number",
            "WCB_number",
            "phone_1",
            "phone_2",
            "fax_number",
            "terms",
            "contact",
            "company",
            "email",
            "website",
            "notes" )

class Query(graphene.ObjectType):

    all_vendors = graphene.List(VendorType)
    def resolve_all_vendors(root, info, f):
        return Vendor.objects.all()






## MUTATIONS ##

# class CategoryMutation(graphene.Mutation):
    
#     vendor = graphene.Field(VendorType)

#     class Arguments:    
    
#         pass


# class Mutation(graphene.ObjectType):

#     add_vendors = CategoryMutation.Field()
#     def resolve_add_vendors(root, info):
#         return Vendor.objects.all()


schema = graphene.Schema(query=Query)#, mutation=Mutation)