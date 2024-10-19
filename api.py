from psqlpy import Connection, ConnectionPool, QueryResult
from robyn import Robyn

app = Robyn(__file__)

db_pool = ConnectionPool(
    username="user",
    password="password",
    host="localhost",
    port=5432,
    db_name="test_db",
    max_db_pool_size=10,
)

# @app.before_request("/")
# async def before_request(request: Request):
#     print("before_request")
#     return request

# @app.after_request("/")
# async def after_request(response: Response):
#     print("after_request")
#     return response


@app.get("/")
async def h(request):
    conn: Connection = await db_pool.connection()
    res: QueryResult = await conn.execute(
        "SELECT 1 + 3 as calc",
    )

    print(res.result())

    return "Hello, world!"


try:
    app.start(port=8000)
finally:
    db_pool.close()

    print("closed")
