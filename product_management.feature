# declarative
# one story per scenario

#TODO

Feature: Product management

    Scenario: 12 - Admin can add new product
        Given Admin is logged in to products
        When Admin fills out necessary information for new product
        Then New product is present in products page
