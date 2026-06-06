from typing import OrderedDict

from playwright.sync_api import Playwright

OrderPayLoad = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}


class APIUtils:

    def getToken(self,playwright:Playwright,user_credentails):
        api_request_context= playwright.request.new_context(base_url ="https://rahulshettyacademy.com")
        response =api_request_context.post(url="api/ecom/auth/login",
                                 data ={"userEmail":user_credentails['user_email'],"userPassword":user_credentails['user_password']})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self,playwright:Playwright,user_credentails):
        token = self.getToken(playwright,user_credentails)
        api_request_context = playwright.request.new_context(base_url ="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/order/create-order",
                                 data=OrderPayLoad ,
                                 headers={"Authorization": token})
                                          #"Content-Type": "application/jason"})

        print(response.json())
        response_body =response.json()
        orderID= response_body["orders"][0]
        return orderID











