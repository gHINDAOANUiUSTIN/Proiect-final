 Feature: We want to check the account deletion functionality on elefant

Background:
 Given A valid account exists

 Scenario: Check that the user can delete their account
  Given Home page: The user is on elefant home page
  When  Home page: The user clicks on account button
  When  Home page: The user clicks on login page button
  When  Login page: The user login with a valid account
  When  Login page: The user clicks on login button
  When  Account page: The user clicks on delete account
  When  Account page: The user clicks on confirm delete account
  Then  Home page: The user should receive a confirmation for deactivating the account


 Scenario: Check that the user's account has been deleted
  Given Home page: The user is on elefant home page
  When  Home page: The user clicks on account button
  When  Home page: The user clicks on login page button
  When  Login page: The user tries to login with the deleted account
  When  Login page: The user clicks on login button
  Then  Login page: The user should receive a message for invalid credentials
