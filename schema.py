import graphene
from graphene_django import DjangoObjectType

# from customer.models import Customer
# from drivers.models import Driver, MonthlyDeductionTable, DriverNote, DriverSafety
# from trailers.models import Trailer, TrailerSafetyDetail, TrailerMonthlyDeduction, TrailerRepairService
# from trucks.models import Truck, TruckSafetyDetail, TruckMonthlyDeduction
from vendor.models import Vendor
from trucks.models import Truck, TruckSafetyDetail, TruckMonthlyDeduction
from drivers.models import Driver, MonthlyDeductionTable, DriverNote, DriverSafety

## QUERIES ##
class VendorType(DjangoObjectType):
    class Meta:
        model = Vendor
        fields = (
            "id",
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


class TruckType(DjangoObjectType):
    class Meta:
        model = Vendor
        fields = (
            "driver",
            "unit",
            "make",
            "plate",
            "type",
            "year",
            "driver_1",
            "driver_2",
            "country",
            "state",
            "VIN_number",
            "terminal",
            "city_truck",
            "tour",
            "still_working",
            "leave_date",
            "truck_ownership",
            "value",
            "weight_pounds",
            "IFTA_group",
            "account",
            "percentage",
            "rate_per_mile_LOAD",
            "rate_per_mile_EMPTY",
            "rate_per_hour")

class TruckSafetyDetailType(DjangoObjectType):
    class Meta:
        model = Vendor
        fields = (
            "truck",
            "safety_details",
            "renewal_date",
            "description",
            "stop_dispatch_on_expiry")

class TruckMonthlyDeductionType(DjangoObjectType):
    class Meta:
        model = Vendor
        fields = (
            "truck",
            "monthly_deductions",
            "day_of_month",
            "currency_CDN",
            "charges",
            "valid_till",
            "belongs_to_company",
            "vendor",
            "HST")


class Query(graphene.ObjectType):

    all_vendors = graphene.List(VendorType) #DjangoListField
    def resolve_all_vendors(root, info):
        return Vendor.objects.all() #Vendor.objects.filter(id=1)


    vendor_with_id = graphene.Field(VendorType, id=graphene.Int())
    def resolve_vendor_with_id(root, info, id):
        return Vendor.objects.get(pk=id)

    # resolve_whateevr:
    #   whtevr.objects.filter(foreginKey = id)



## MUTATIONS ##

class CategoryMutation(graphene.Mutation):
    
    vendor = graphene.Field(VendorType)

    class Arguments:    
    
        pass


class Mutation(graphene.ObjectType):

    add_vendors = CategoryMutation.Field()
    def resolve_add_vendors(root, info):
        return Vendor.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)