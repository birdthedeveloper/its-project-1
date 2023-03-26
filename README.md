# ITS Projekt 1

- **Autor:** Martin Ptáček (xptace20)
- **Datum:** 2023-03-26

# TODO
## Matice pokrytí artefaktů

Čísla testů jednoznačně identifikují scénář v souborech `.feature`.

| Page                  | 1 | 2 | 3 | 4  | 5  |   6 |   7 |   8 | 9 | 10 | 11 | 12 |
|-----------------------|---|---|---|----|----|-----|-----|-----|---|----|----|----|
| User Homepage         | x |   |   |    |    |     |     |     |   |    |    |    |
| User Product detail   |   | x |   |    |  x |     |     |     |   |    |    |    |
| User Search results   |   |   |   | x  | x  |     |     |     |   |    |    |    |
| User Shopping cart    |   | x | x |    |    |     |     |     |   |    |    |    |
| User Login            | x |   |   |    |    |     |     |     |   |    |    |    |
| User Register         |   |   |   |    |    |     |     |     |   |    |    |    |
| User Checkout         |   |   | x |    |    |     |     |     |   |    |    |    |
| User My account       |   |   |   |    |    |     |     |     |   |    |    |    |
| User Order history    | x |   |   |    |    |     |     |     |   |    |    |    |
| Admin dashboard       |   |   |   |    |    |     |     |     |   |    |    |    |
| Admin customers       |   |   |   |    |    |     |     |     |   |    |    |    |
| Admin customer detail |   |   |   |    |    |     |     |     |   |    |    |    |
| Admin orders          |   |   |   |    |    |     |     |     | x | x  |    |    |
| Admin order detail    |   |   |   |    |    |     |     |     |   |    |  x |    |

# TODO
## Matice pokrytí aktivit

| Activities                            | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---------------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|
| User: Text searching for a product    |   |   |   |   |   |   |   |   |   |    |    |    |
| User: Viewing product detail          |   |   |   |   |   |   |   |   |   |    |    |    |
| User: Adding product to shopping cart |   | x |   |   |   |   |   |   |   |    |    |    |
| User: Checking out an order           |   |   | x |   |   |   |   |   |   |    |    |    |
| User: Canceling an order              |   |   |   |   |   |   |   |   |   |    |    |    |
| User: Registering                     |   |   |   |   |   |   |   |   |   |    |    |    |
| User: Viewing order state             | x |   |   |   |   |   |   |   |   |    |    |    |
| User: Creating an order               |   |   |   |   |   |   |   |   |   |    |    |    |
| User: Viewing cart contents           |   |   |   |   |   |   |   |   |   |    |    |    |
| Admin: Editing quantity of a product  |   |   |   |   |   |   |   |   |   |    |    |    |
| Admin: Listing all products           |   |   |   |   |   |   |   |   |   |    |    |    |
| Admin: Editing customer account       |   |   |   |   |   |   |   |   |   |    |    |    |
| Admin: Listing all customer accounts  |   |   |   |   |   |   |   |   |   |    |    |    |
| Admin: Editing order state            |   |   |   |   |   |   |   |   |   |    |    |    |
| Admin: Listing all orders             |   |   |   |   |   |   |   |   |   |    |    |    |



## Matice Feature-Test

| Feature file                      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|-----------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|
| order_history.feature             | x |   |   |   |   |   |   |   |   |    |    |    |
| order_management.feature          |   |   |   |   |   |   |   |   | x | x  | x  |    |
| product_management.feature        |   |   |   |   |   |   |   |   |   |    |    | x  |
| product_purchase.feature          |   | x | x |   |   |   |   |   |   |    |    |    |
| product_search.feature            |   |   |   | x | x |   |   |   |   |    |    |    |
| registration.feature              |   |   |   |   |   | x |   |   |   |    |    |    |
| user_account_management.feature   |   |   |   |   |   |   | x | x |   |    |    |    |
