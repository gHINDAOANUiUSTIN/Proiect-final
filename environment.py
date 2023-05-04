from browser import Browser
from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.filters_page import FiltersPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from pages.base_page import BasePage


def before_all(context):
	context.browser = Browser()
	context.base_page = BasePage()
	context.home_page = HomePage()
	context.login_page = LoginPage()
	context.account_page = AccountPage()
	context.filters_page = FiltersPage()
	context.search_page = SearchPage()
	context.product_page = ProductPage()
	context.cart_page = CartPage()


def after_all(context):
	context.browser.close()
