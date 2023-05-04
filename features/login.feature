Feature: We want to check the login-logout functionality on elefant

Scenario: Check if user can access login page
  Given Home page: The user is on elefant home page
  When  Home page: The user clicks on account button
  When  Home page: The user clicks on login page button
  Then  Login page: The user should be redirected to login page

Scenario: Check if user can login into the application with valid credentials
  Given Login page: The user is on elefant login page
  When  Login page: The user enters "cont.elefant.test@gmail.com" on the username field
  When  Login page: The user enters "123qwe!@#QWE" on the password field
  When  Login page: The user clicks on login button
  Then  Account page: The user should be logged in and redirected to account page

Scenario: Check that the user can logout
  Given Account page: The user is on elefant account page
  When  Account page: The user clicks on account button
  When  Account page: The user clicks on logout button
  Then  Home page: The user should be logged out and redirected to home page

Scenario Outline: Check if user cannot login into the application with invalid credentials
  Given Home page: The user is on elefant home page
  When  Home page: The user clicks on account button
  When  Home page: The user clicks on login page button
  When  Login page: The user enters "<username>" on the username field
  When  Login page: The user enters "<password>" on the password field
  When  Login page: The user clicks on login button
  Then  Login page: The user should receive a message for invalid credentials
  Examples:
    |            username             |  password   |
    |   cont.elefant.test@gmail.com   |WrongPassword|
    |    WrongUsername@example.com    |123qwe!@#QWE |
    |    WrongUsername@example.com    |WrongPassword|

