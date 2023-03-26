# declarative
# one story per scenario

Feature: Admin can manage user accounts

    Scenario: 7 - Admin can list all the customers
        Given Admin is logged in on dashboard
        And There is one customer account in the system
        When Admin goes to customers page
        Then Admin can see one customer account in the system 
    
    Scenario: 8 - Admin can edit customer's profile
        Given Admin is logged in on customers page
        When Admin changes name of the first customer account
        Then Customer's name is changed
