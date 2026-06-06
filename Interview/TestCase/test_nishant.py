import json
from time import sleep

import pytest
from boto3.dynamodb.conditions import And

from pytest_bdd import then as and_
from playwright.sync_api import Playwright, Page
from pytest_bdd import given, when, then, scenarios

from Interview.POM.Login import LoginPage
from Interview.Utils3.apiBase import APIUtils
from Interview.conftest import credentails_list

scenarios('/Users/akanshasoni/PycharmProjects/PythonProject/PytestPythonProject/Interview/FeatureInterview/interview.feature')

@pytest.fixture()
def shared_values():
    return { }

with open("Interview/Data3/Credentails.json") as f:
    testdata = json.load(f)
    credentails_list = testdata['user_credentails']

@pytest.mark.parametrize('cred',credentails_list)
@given('place the order with username and password')
def place_order(playwright:Playwright,cred,browser):
    apiutils =APIUtils()
    orderID= apiutils.createorder(playwright,cred)

@given('the user is on landing page')
def onlandingpage(browser,shared_values):
    loginpage =LoginPage(browser)
    loginpage.navigate()
    shared_values['login_page'] =loginpage

@when('I login to portal with username and password')
def login_toportal(cred,shared_values):
    loginpage=shared_values['login_page']
    dashboard=loginpage.login(cred)
    shared_values['dashboard_page'] = dashboard

@when('navigate to order page')
def on_order_page(shared_values):
    dashboard =shared_values['dashboard_page']
    check=dashboard.selectorder()
    shared_values['check'] = check

@then('order message is displayed')
def order_message(shared_values):
    orderID= shared_values['order_id']
    check =shared_values['check']
    check.orderhistory(orderID)
    #item =page.locator(".card").filter(has_text="ZARA COAT 3")

   ##item.get_by_role("button",name=  "Add To Cart").click()
    ##page.locator("[routerlink='/dashboard/cart']").click()
    ##page.get_by_role("button" , name ="Checkout").click()
    ##page.get_by_role("textbox", name="Select Country").type("India")
    ##page.get_by_text("India", exact=True).click()
    ##page.get_by_text("Place Order").click()
    ##expect(page.get_by_text(" Thankyou for the order. ")).to_be_visible()






















