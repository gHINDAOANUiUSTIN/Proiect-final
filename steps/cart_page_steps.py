from behave import *


@given("Cart page: The user is on elefant cart page")
def step_impl(context):
    context.base_page.skip_current_step()


@when("Cart page: The user clicks on + button to add one more product of Moara cu noroc")
def step_impl(context):
    context.cart_page.click_add_product_button()


@when('Cart page: The user clicks on remove product from the cart button')
def step_impl(context):
    context.cart_page.click_remove_product()


@then("Cart page: The cart should contain two products of Moara cu noroc")
def step_impl(context):
    context.cart_page.check_number_of_products()


@then("Cart page: The product is removed and the cart is empty")
def step_impl(context):
    context.cart_page.cart_is_empty()

