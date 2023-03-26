# declarative
# one story per scenario

Feature: User can search for product

    Scenario Outline: 4 - User searches for a product 
        Given User is on homepage
        When User enters <item> in the search bar
        Then User should see <item> product in the results

        Examples:
            | item    |
            | Iphone  |
            | Ipod    |

    Scenario Outline: 5 - User can open product detail from search result
        Given User searched for an <item>
        When User opens first search result
        Then User should see product detail of <item>

        Examples:
            | item    |
            | Iphone  |
            | Ipod    |
