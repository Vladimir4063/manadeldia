from database.db import *


def update_parasha_public(nroParasha):

    nroParasha = str(nroParasha)
    query = (
        "UPDATE parasha SET isPublic = CASE WHEN nroParasha = "
        + nroParasha
        + " THEN 1 ELSE 0 END WHERE nroParasha = 1 OR nroParasha NOT IN (SELECT nroParasha FROM parasha WHERE nroParasha = 1);"
    )

    try:
        connection_DB = connection.cursor()
        connection_DB.execute(query)
        connection.commit()
        connection_DB.close()
    except sqlite3.Error as e:
        print("ERROR =>")
        print(f"COMMIT FAIL: {e}")
    else:
        print("SUCCES")
