from status import status
from conn import Connection


connection = Connection(status=status)
connection.connect()