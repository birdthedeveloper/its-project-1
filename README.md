# ITS Projekt 1

- **Autor:** Martin Ptáček (xptace20)
- **Datum:** 2023-03-26

## Matice pokrytí artefaktů

Čísla testů jednoznačně identifikují scénář v souborech `.feature`.

| Page                  | 1 | 2 | 3 | 4  | 5  |   6 |   7 |   8 | 9 | 10 | 11 | 12 |
|-----------------------|---|---|---|----|----|-----|-----|-----|---|----|----|----|
| User Homepage         | x |   |   |    |    |     |     |     |   |    |    |    |
| User Product detail   |   | x |   |    |  x |     |     |     |   |    |    |    |
| User Search results   |   |   |   | x  | x  |     |     |     |   |    |    |    |
| User Shopping cart    |   | x | x |    |    |     |     |     |   |    |    |    |
| User Login            | x |   |   |    |    |     |     |     |   |    |    |    |
| User Register         |   |   |   |    |    |  x  |     |     |   |    |    |    |
| User Checkout         |   |   | x |    |    |     |     |     |   |    |    |    |
| User Order history    | x |   |   |    |    |     |     |     |   |    |    |    |
| Admin dashboard       |   |   |   |    |    |     |   x |     | x |    |    |    |
| Admin customers       |   |   |   |    |    |     |   x |     |   |    |    |    |
| Admin customer detail |   |   |   |    |    |     |     |  x  |   |    |    |    |
| Admin orders          |   |   |   |    |    |     |     |     | x | x  |    |    |
| Admin order detail    |   |   |   |    |    |     |     |     |   |    |  x |    |
| Admin products        |   |   |   |    |    |     |     |     |   |    |    |  x |


## Matice pokrytí aktivit

| Activities                            | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---------------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|
| User: Text searching for a product    |   |   |   | x | x |   |   |   |   |    |    |    |
| User: Viewing product detail          |   |   |   |   | x |   |   |   |   |    |    |    |
| User: Adding product to shopping cart |   | x |   |   |   |   |   |   |   |    |    |    |
| User: Checking out                    |   |   | x |   |   |   |   |   |   |    |    |    |
| User: Sign in                         |   |   |   |   |   | x |   |   |   |    |    |    |
| User: Viewing order state             | x |   |   |   |   |   |   |   |   |    |    |    |
| User: Creating an order               |   |   | x |   |   |   |   |   |   |    |    |    |
| User: Viewing cart contents           |   | x |   |   |   |   |   |   |   |    |    |    |
| Admin: Add new product                |   |   |   |   |   |   |   |   |   |    |    | x  |
| Admin: Editing customer account       |   |   |   |   |   |   |   | x |   |    |    |    |
| Admin: Listing all customer accounts  |   |   |   |   |   |   | x |   |   |    |    |    |
| Admin: Editing order state            |   |   |   |   |   |   |   |   |   |    |  x |    |
| Admin: Listing all orders             |   |   |   |   |   |   |   |   | x |    |    |    |
| Admin: Add new order                  |   |   |   |   |   |   |   |   |   | x  |    |    |



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
