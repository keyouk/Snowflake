#!/usr/bin/env python3
from timeit import default_timer
import snowflake.connector
import sys
from multiprocessing.dummy import Pool as ThreadPool


CONNECTION_POOL_SIZE = 5
NUMBER_OF_TEST_RUNS = 500


def connect(index):
    start = default_timer()
    ctx = snowflake.connector.connect(
        user='',
        password='',
        account=''
        )

    end = default_timer()
    ctx.close()
    return [index, end - start]

 
pool = ThreadPool(CONNECTION_POOL_SIZE)
results = pool.map(connect, range(NUMBER_OF_TEST_RUNS))

for result in results:
    print(result[0], result[1])
