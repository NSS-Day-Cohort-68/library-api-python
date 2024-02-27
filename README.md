# Library API

## Setup instructions:
1. Create your own repo using this template
1. `git clone` that new repo locally
1. `pipenv shell`
1. `pipenv install`
1. Create a file called `library.sqlite3`
1. Run `library.sql` on that database
1. Start the debugger and test with `http://localhost:8000/genres`. You should get genres back

## Leading the workshop
1. Search for TODO to see the unimplemented code in the repo
1. Complete the views in order. 

## Suggested stretch goals
1. custom endpoint to checkout a material at `/materials/{id}/checkout`
1. custom endpoint to return a material at `/materials/{id}/return`
1. Add logic to add a calculated `due_date` property to the material details based on `checkout_date` and the `material_type.checkout_days`