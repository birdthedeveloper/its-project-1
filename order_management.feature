# declarative
# one story per scenario

Feature: Admin order management

    Scenario: 9 - Admin can list the orders
        Given Admin is logged in to dashboard
        When Admin navigates to orders
        Then Admin can list all orders in the system

    Scenario: 10 - Admin can add new order
        Given Admin is logged in to orders
        When Admin fills out necessary data for new order and saves it
        Then New order is present in the system

    Scenario: 11 - Admin can change state of one order
        Given Admin is logged in to orders
        And One order exists in the system
        When Admin changes state of the order to complete
        Then Order history log records this change 
