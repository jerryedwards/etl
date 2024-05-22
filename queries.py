mysqlDropTable = "DROP TABLE db1.applStocks"

mysqlCreateTable =  """
    CREATE TABLE applStocks (
    Date DATE PRIMARY KEY,
    Open DECIMAL(20,6),
    High DECIMAL(20,6),
    Low DECIMAL(20,6),
    Close DECIMAL(20,6),
    AdjClose DECIMAL(20,6),
    Volume int
    )
    """

mysqlExtractTable = "SELECT * FROM db1.applStocks"
