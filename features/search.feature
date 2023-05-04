Feature: We want to check the search functionality on elefant

Scenario: Check if user can explore the products using the filters from elefant homepage
  Given Home page: The user is on elefant home page
  When  Home page: The user select books from category menu
  When  Home page: The user select fiction from genres
  When  Filters page: The user select 15% - 30% from discount
  Then  Filters page: The user should receive a list with at least 1000 products

Scenario Outline: Check if user can make a simple search from the elefant home page
  Given Home page: The user is on elefant home page
  When  Home page: The user types in the search bar "<product_name>"
  When  Home page: The user clicks the search button
  Then  Search page: The user should receive as the first result the searched product
  Examples:
        |  product_name   |
        |  Cartea Rosie   |
        |   Alchimistul   |
        |Crima si pedeapsa|
        | Moara cu noroc  |


