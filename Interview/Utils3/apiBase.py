from playwright.sync_api import Playwright

from Akansha.executionfiles.apiBase2 import orderPayLoad

orderPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
class APIUtils:

    def gettoken(self,playwright:Playwright,cred):
        api_request_context= playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response =api_request_context.post(url="api/ecom/auth/login",
                                 data={"userEmail": cred['email'], "userPassword": cred['password']}
                                 )
        assert response.ok
        print(response.json())
        token =response.json()["token"]
        return token



    def createorder(self,playwright:Playwright,cred):
        token =self.gettoken(playwright,cred)
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response =api_request_context.post("api/ecom/order/create-order",
                                 data =orderPayLoad,
                                 headers = {"authorization" :token,
                                            "Content-Type" :"application/json"
                                            })
        print(response.json())
        response_body = response.json()
        orderID = response_body["orders"][0]
        return orderID




