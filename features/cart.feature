Feature: We want to check the cart functionality on elefant

Scenario: Check that the user can add a product to the cart
  Given Home page: The user is on elefant home page
  When  Home page: The user types in the search bar "Moara cu noroc"
  When  Home page: The user clicks the search button
  When  Search page: The user navigate to first returned product page/clicks on first product returned
  When  Product page: The user clicks on add to cart button
  Then  Product page: The user should receive a confirmation that the product has been added to cart

Scenario: Check that the user can modify the quantity of a product
  Given Product page: The user is on Moara cu noroc product page
  When  Product page: The user clicks on view cart page button
  When  Cart page: The user clicks on + button to add one more product of Moara cu noroc
  Then  Cart page: The cart should contain two products of Moara cu noroc

Scenario: Check that the user can remove products from the cart
  Given Cart page: The user is on elefant cart page
  When  Cart page: The user clicks on remove product from the cart button
  Then  Cart page: The product is removed and the cart is empty