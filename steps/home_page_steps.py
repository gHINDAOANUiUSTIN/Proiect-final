from behave import *


@given("Home page: The user is on elefant home page")
def step_impl(context):
    context.home_page.home_page()
    context.base_page.accept_cookies()


@when("Home page: The user clicks on account button")
def step_impl(context):
    context.home_page.click_account_button()


@when("Home page: The user clicks on login page button")
def step_impl(context):
    context.home_page.click_login_page_button()


@then("Home page: The user should be logged out and redirected to home page")
def step_impl(context):
    context.home_page.check_logout_page_redirection()


@when("Home page: The user select books from category menu")
def step_impl(context):
    context.home_page.select_category()


@when("Home page: The user select fiction from genres")
def step_impl(context):
    context.home_page.select_genre()


@when('Home page: The user types in the search bar "{product_name}"')
def step_impl(context, product_name):
    context.home_page.type_search_product(product_name)


@When("Home page: The user clicks the search button")
def step_impl(context):
    context.home_page.click_search_button()


@then("Home page: The user should receive a confirmation for deactivating the account")
def step_impl(context):
    context.home_page.delete_confirmation()



