import pytest
from pytest_bdd import given, when, then, parsers
from pytest_bdd import scenarios
import os


from PageObjects.login import LoginPage
from Utils.apiBaseframework import APIUtils

scenarios('/Users/akanshasoni/PycharmProjects/PythonProject/PytestPythonProject/testplaywright_practice/Features/orderTransaction.feature')

@pytest.fixture
def shared_date():
    return{}

@given(parsers.parse('place the order with {username} and {password}'))
def place_order(playwright,username,password,shared_date):
    user_credentails ={}
    user_credentails["user_email"] = username
    user_credentails["user_password"] = password
    api_utils= APIUtils()
    orderID = api_utils.createOrder(playwright,user_credentails)
    shared_date['order_id']=orderID

@given('user is on landing page')
def user_is_on_landing_page(browserInstance,shared_date):
    loginpage= LoginPage(browserInstance)
    loginpage.navigate()
    shared_date['login_page']=loginpage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_page_login(username,password,shared_date):
    loginpage=shared_date['login_page']
    dashboard = loginpage.login(username, password)
    shared_date['dashboard']=dashboard

@when('navigate to order page')
def navigate_to_order_page(shared_date):
    dashboard = shared_date['dashboard']
    orderHistoryPage = dashboard.navigation()
    shared_date['orderHistoryPage'] = orderHistoryPage


@when('select the order')
def select_order(shared_date):
    orderHistoryPage = shared_date['orderHistoryPage']
    orderID = shared_date['order_id']
    OrderDetailspage = orderHistoryPage.view(orderID)
    shared_date['OrderDetailspage']=OrderDetailspage

@then('order message is successfully displayed')
def order_displayed(shared_date):
    OrderDetailspage = shared_date['OrderDetailspage']
    OrderDetailspage.verify()
