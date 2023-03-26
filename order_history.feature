# declarative
# one story per scenario

#TODO

Feature: Order history

    Scenario: 1 - User can view order history
        Given User is authenticated on homepage and made an order before
        When User navigates to his order history
        Then User should see that order in order history
