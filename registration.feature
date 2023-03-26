# declarative
# one story per scenario

#TODO

Feature: Registration

    Scenario: 6 - User can sign in after registration
        Given User has an account 
        When User enters right credentials into log in page 
        Then User should be signed in
    
    Scenario: 
