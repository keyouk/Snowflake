from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from timeit import default_timer



engine = create_engine(
    'snowflake://{user}:{password}@{account}/'.format(
        user='',
        password='',
        account='',
    )
)


try:
    connection = engine.connect()
    results = connection.execute('select current_version()').fetchone()
    print(results[0])



finally:
    connection.close()
    engine.dispose()