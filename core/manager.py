from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from constants import USER_BD,PASS_BD,SERVER_BD,BD

async def connect():
    engine = create_async_engine(
        f"mssql+aioodbc://{USER_BD}:{PASS_BD}@{SERVER_BD}/{BD}?driver=ODBC+Driver+17+for+SQL+Server",
            #data['engine'],
            #f"mssql+aioodbc://{data['user']}:{data['password']}@{data['server']}/{data['database']}?driver=ODBC+Driver+17+for+SQL+Server",
            #f"mssql+aioodbc://NISIRA-T14S1\\NISIRA/APOLO?driver=ODBC+Driver+17+for+SQL+Server",
        fast_executemany=True,
        echo=True
        )
    return engine