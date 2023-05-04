from behave import *


@when("Product page: The user clicks on add to cart button")
def step_impl(context):
    context.product_page.add_to_cart()


@then("Product page: The user should receive a confirmation that the product has been added to cart")
def step_impl(context):
    context.product_page.add_to_cart_confirmation()


@given("Product page: The user is on Moara cu noroc product page")
def step_impl(context):
    context.base_page.skip_current_step()


@when("Product page: The user clicks on view cart page button")
def step_impl(context):
    context.product_page.click_view_cart_button()
