from behave import *
from valid_accounts import valid_accounts
from utils import remove_account, update_valid_accounts_file


@then("Login page: The user should be redirected to login page")
def step_impl(context):
    context.login_page.check_login_page_redirection()


@given("Login page: The user is on elefant login page")
def step_impl(context):
    context.base_page.skip_current_step()


@when('Login page: The user enters "{username}" on the username field')
def step_impl(context, username):
    context.login_page.insert_username(username)


@when('Login page: The user enters "{password}" on the password field')
def step_impl(context, password):
    context.login_page.insert_password(password)


@when("Login page: The user clicks on login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("Login page: The user should receive a message for invalid credentials")
def step_impl(context):
    context.login_page.check_error_message()


@given("A valid account exists")
def step_impl(context):
    if not valid_accounts:
        context.scenario.skip(reason="No valid accounts available")
    else:
        context.valid_account = valid_accounts[0]


@when("Login page: The user login with a valid account")
def step_impl(context):
    context.login_page.insert_username(context.valid_account["email"])
    context.login_page.insert_password(context.valid_account["password"])


@when("Login page: The user tries to login with the deleted account")
def step_impl(context):
    context.login_page.insert_username(context.valid_account["email"])
    context.login_page.insert_password(context.valid_account["password"])
    remove_account(valid_accounts[0])
    update_valid_accounts_file(valid_accounts)


