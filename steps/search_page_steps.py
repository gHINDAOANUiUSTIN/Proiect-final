from behave import *


@then("Search page: The user should receive as the first result the searched product")
def step_impl(context):
    context.search_page.simple_search_results()


@given("Search page: The user is on Moara cu noroc search page")
def step_impl(context):
    context.base_page.skip_current_step()


@when("Search page: The user navigate to first returned product page/clicks on first product returned")
def step_impl(context):
    context.search_page.click_on_product()
