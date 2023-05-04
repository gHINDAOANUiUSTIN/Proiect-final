from behave import *


@then("Account page: The user should be logged in and redirected to account page")
def step_impl(context):
    context.account_page.check_user_is_logged()


@given("Account page: The user is on elefant account page")
def step_impl(context):
    context.base_page.skip_current_step()


@when("Account page: The user clicks on account button")
def step_impl(context):
    context.home_page.click_account_button()


@when("Account page: The user clicks on logout button")
def step_impl(context):
    context.account_page.click_logout_button()


@when("Account page: The user clicks on delete account")
def step_impl(context):
    context.account_page.click_delete_account()


@when("Account page: The user clicks on confirm delete account")
def step_impl(context):
    context.account_page.click_confirm_delete_account()
