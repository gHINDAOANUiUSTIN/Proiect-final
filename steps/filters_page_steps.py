from behave import *


@when("Filters page: The user select 15% - 30% from discount")
def step_impl(context):
    context.filters_page.select_discount()


@then("Filters page: The user should receive a list with at least 1000 products")
def step_impl(context):
    context.filters_page.filter_search_results()
