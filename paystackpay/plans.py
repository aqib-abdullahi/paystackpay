from .base import Base
from .utils import validate_amount


class Plan(Base):


    def create_plan(self,plan_name:str,interval:str,amount:float):
        endpoint = "/plan"

        validated_amount = validate_amount(amount)*100

        data = {
            "name":plan_name,
            "interval":interval,
            "amount":str(validated_amount)
        }

        return self.make_request("POST",endpoint=endpoint,data=data)
    

    def list_plans(self):
        endpoint = "/plan"
        return self.make_request("GET",endpoint=endpoint)
    

    def fetch_plan(self,id_or_code:str):
        endpoint = f"/plan/{id_or_code}"
        return self.make_request("GET",endpoint=endpoint)
    
    def update_plan(self,plan_name:None,interval:None,amount:None,id_or_code:str):
        endpoint = f"/plan/{id_or_code}"

        data = {}

        if plan_name is not None:
            data['name'] = plan_name
        if interval is not None:
            data['interval'] = interval
        if amount is not None:
            data["amount"] = amount

        return self.make_request("PUT",endpoint=endpoint,data=data)