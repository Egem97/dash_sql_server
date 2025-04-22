import pandas as pd
import asyncio
from sqlalchemy import text
from core.manager import connect
from datetime import datetime

async def getDataTest():
    engine = await connect()
    async with engine.begin() as conn:
        result = await conn.execute(text(f""" SET NOCOUNT ON; SELECT * FROM [Production].[ProductReview] """))
        rows = result.fetchall()
        return pd.DataFrame(rows, columns=result.keys())
def dataOut():
    df = asyncio.run(getDataTest())
    df['time'] = datetime.now()
    return df

async def getYears():
    engine = await connect()
    async with engine.begin() as conn:
        result = await conn.execute(
            text(f""" SET NOCOUNT ON; 
                 SELECT DISTINCT YEAR(OrderDate)AS 'Year' 
                    FROM Sales.SalesOrderHeader
                    ORDER BY 'Year'; """
            )
        )
        rows = result.fetchall()
        return pd.DataFrame(rows, columns=result.keys())

def listYear(): 
    df = asyncio.run(getYears())
    df["Year"] = df["Year"].astype(str)
    return df

async def getTopVentas(year = "2011", top = "10"):
    engine = await connect()
    async with engine.begin() as conn:
        result = await conn.execute(
            text(f""" SET NOCOUNT ON; 
                 EXEC usp_GetTopSellingProductsByYear @Year = {int(year)}, @TopN = {int(top)}; """
            )
        )
        rows = result.fetchall()
        return pd.DataFrame(rows, columns=result.keys())

def spGetTopSellingProductsByYear(year,top): return asyncio.run(getTopVentas(year,top))