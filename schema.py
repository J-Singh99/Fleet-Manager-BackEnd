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
        model = Truck
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
        model = TruckSafetyDetail
        fields = (
            "truck",
            "safety_details",
            "renewal_date",
            "description",
            "stop_dispatch_on_expiry")

class TruckMonthlyDeductionType(DjangoObjectType):
    class Meta:
        model = TruckMonthlyDeduction
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

class DriverType(DjangoObjectType):
    class Meta:
        model = Driver
        fields = (
            "full_name",
            "address_street",
            "address_city",
            "address_state",
            "address_unit",
            "address_ZIP",
            "company",
            "phone_int",
            "cellphone_Canada",
            "cellphone_US",
            "WCB",
            "SSN",
            "driver_paid_by_Company_OwnerOperator",
            "appointment_date",
            "loadedMileRange_Alone",
            "loadedMileRange_Team",
            "emptyMileRange_Alone",
            "emptyMileRange_Team",
            "percentage_pay",
            "perectage",
            "notes",
            "bank_details",
            "truck_int",
            "CSA_FAST_Driver",
            "pay_GST",
            "deduct_taxes_on_pay",
            "exempt_EI",
            "exempt_CPP",
            "claim_code",
            "CRA_Tax_pay_periods_year",
            "currently_working")


class Query(graphene.ObjectType):

    all_vendors = graphene.List(VendorType) #DjangoListField
    def resolve_all_vendors(root, info):
        return Vendor.objects.all() #Vendor.objects.filter(id=1)


    vendor_with_id = graphene.Field(VendorType, id=graphene.Int())
    def resolve_vendor_with_id(root, info, id):
        return Vendor.objects.get(pk=id)

    all_trucks = graphene.List(TruckType) #DjangoListField
    def resolve_all_trucks(root, info):
        return Truck.objects.all()

    truck_with_id = graphene.Field(TruckType, id=graphene.Int())
    def resolve_truck_with_id(root, info, id):
        return Truck.objects.get(pk=id)

    all_drivers = graphene.List(DriverType) #DjangoListField
    def resolve_all_drivers(root, info):
        return Driver.objects.all()

    driver_with_id = graphene.Field(DriverType, id=graphene.Int())
    def resolve_driver_with_id(root, info, id):
        return Driver.objects.get(pk=id)

    truck_by_driver_FULL_NAME = graphene.List(TruckType, fname = graphene.String())
    def resolve_truck_by_driver_FULL_NAME(root, info, fname):
        d = Driver.objects.get(full_name = fname)
        return Truck.objects.filter(driver = d.id)



## MUTATIONS ##

class TruckMutation(graphene.Mutation):
    
    class Arguments:    
        make_name = graphene.String(required=True)
        unit_name = graphene.String(required=True)
        plate_num = graphene.String(required=True)

    truck = graphene.Field(TruckType)

    @classmethod
    def mutate(cls, root, info, make_name, unit_name, plate_num):
      truck = Truck(make = make_name, unit = unit_name, plate = plate_num)
      truck.save()
      return TruckMutation( truck = truck )



class Mutation(graphene.ObjectType):

    update_trucks = TruckMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)