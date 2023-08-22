
# Rust PostgreSQL Driver with JSON Query Results

This project demonstrates how to modify the PostgreSQL driver source code to implement a `query_json` method, which returns query results in JSON format. The modifications are made to the PostgreSQL driver's existing methods.


The PostgreSQL driver typically provides methods like `query` and `execute` for interacting with the database. However, we wanted to add a new method `query_json` that returns query results in JSON format, as specified by the user.

We've added a new method `query_json` to the PostgreSQL driver, which takes a query and parameters, similar to other query methods. It then processes the query results, extracts column values, and constructs JSON objects for each row. Finally, the JSON objects are serialized into a JSON array and returned as a string.

## Usage

To use the modified driver with the new `query_json` method:

In your Rust code 
```rust
use postgres::{Client, NoTls};

# fn main() -> Result<(), postgres::Error> {
let mut client = Client::connect("host=localhost user=postgres", NoTls)?;

let baz = true;
for json_row in client.query_json("SELECT foo FROM bar WHERE baz = $1", &[&baz])? {
    // Access specific fields within the JSON row
    if let Some(foo_value) = json_row.get("foo") {
        let foo: i32 = serde_json::from_value(foo_value.clone())?;
        println!("foo: {}", foo);
    }
}
# Ok(())
# }
```
