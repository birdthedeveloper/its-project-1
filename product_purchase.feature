# declarative
# one story per scenario

Feature: Purchase a product

    Scenario: 2 - User can add product to his cart
        Given User is on a product detail of a product that is in stock
        When User adds product to his shopping cart
        Then Product is in user's shopping cart
    
    Scenario: 3 - User can place an order
        Given User's shopping cart is not empty
        And User is on checkout page
        When User fills in all necessary data
        Then User can place the order
