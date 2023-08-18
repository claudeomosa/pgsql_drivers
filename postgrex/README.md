# Postgrex

  

PostgreSQL driver for Elixir, with a few tweaks.

#### Prerequisites: 

* Install [Elixir](https://elixir-lang.org/install.html) 
* Install [Postgres](https://www.postgresql.org/download/)

Once you have both installed and having cloned this repository, change into this directory:

```shell
cd postgrex
```

Install the dependencies with this command:

```shell
mix deps.get
```

Once installed open up the elixir interactive shell: 

```shell
iex -S mix
```


To view how [Postgrex](https://github.com/elixir-ecto/postgrex) , PostgreSQL driver for Elixir works you can go to their official github and view the example in their README.md:  

### How this version works:

This version has updates that return data in a json format after a query rather than the %Postgrex.Result{} struct that is returned when you use [Postgrex](https://github.com/elixir-ecto/postgrex). Steps:

1. Make a connection to your database, update your credentials as required:

```elixir

iex> {:ok, pid} = Postgrex.start_link(hostname: "localhost", username: "postgres", password: "postgres", database: "postgres")

{:ok, #PID<0.69.0>}

```

2. Run a query as below:

``` elixir

iex> Postgrex.query(pid, "SELECT user_id, text FROM project_members", [])

{:ok,
 %{
   "data" => [
     %{"project_id": 3, "user_id": 3},
     %{"project_id": 3, "user_id": 3},
     %{"project_id": 4, "user_id": 4},
     %{"project_id": 4, "user_id": 4},
     %{"project_id": 3, "user_id": 3},
     %{"project_id": 6, "user_id": 6},
   ],
   "status_code": 200
 }}

```

  
