import pymssql

from datetime import date
from logger import logs
from pymssql._pymssql import Connection, Cursor

CONNECTION_STRING = 'yand.dyndns.org;MyDb;northwind;northwind'


class ValidatorBase:

    def __init__(self, date_of_interest: date):
        self.date_of_interest = date_of_interest

    def query(self) -> str:
        raise NotImplementedError


class Qty(ValidatorBase):

    def __init__(self, check_date):
        super().__init__(date_of_interest=check_date)

    def query(self) -> str:
        return """
            SELECT * FROM
                (SELECT COUNT(1) as cnt FROM sales WHERE Date = %(date)s) as x,
                (SELECT COUNT(1) as cnt FROM sales WHERE Date = %(date)s AND Qty=0) as y;
            """

    def checker(self):
        con = SqlConnection(connection_string=CONNECTION_STRING)
        res = con.get_connection(sql_query=self.query(), param={'date': self.date_of_interest})
        full_qty, zero_qty = res[0]
        result = None
        if full_qty:
            result = round(100 - 100 * (zero_qty/full_qty))
            logs.debug(result)
            log_text = f'Проверка заполнения Qty:\t\t{result}%'
            if result >= 98:
                logs.info(log_text)
            else:
                logs.warning(log_text)
        else:
            logs.warning('Проверка заполнения Qty:\t\tWe haven`t any products on this day.')
        return result



class Category(ValidatorBase):

    def __init__(self, check_date):
        super().__init__(date_of_interest=check_date)

    def query(self) -> str:
        return """
        SELECT * FROM
            (SELECT COUNT(1) as cnt FROM Sales WHERE Date = %(date)s) as x,
            (SELECT COUNT(1) as cnt FROM Sales WHERE Date = %(date)s AND Category is null) as y;
        """

    def checker(self):
        con = SqlConnection(connection_string=CONNECTION_STRING)
        res = con.get_connection(sql_query=self.query(), param={'date': self.date_of_interest})
        full_cnt, null_cnt = res[0]
        result = None
        if full_cnt:
            result = round(100 - 100 * (null_cnt / full_cnt))
            logs.debug(result)
            log_text = f'Проверка заполнения категории:\t\t{result}%'
            if result >= 95:
                logs.info(log_text)
            else:
                logs.warning(log_text)
        else:
            logs.warning('Проверка заполнения категории:\t\tWe haven`t any products on this day.')
        return result


class ClientIsPremium(ValidatorBase):

    def __init__(self, check_date):
        super().__init__(date_of_interest=check_date)

    def query(self) -> str:
        return """
            SELECT COUNT(1) FROM Sales 
            WHERE Date=%(date)s AND Category='Ювелирные изделия' AND ClientPremium = 'true';
        """

    def checker(self):
        con = SqlConnection(connection_string=CONNECTION_STRING)
        res = con.get_connection(sql_query=self.query(), param={'date': self.date_of_interest})
        count = res[0][0]
        logs.debug(count)
        is_premium = False
        if count:
            is_premium = True
            logs.info(f'Проверка покупок премиум клиентами:\tесть')
        else:
            logs.warning(f'Проверка покупок премиум клиентами:\tнет')
        return is_premium


class FoodPurchases(ValidatorBase):

    def __init__(self, check_date):
        super().__init__(date_of_interest=check_date)

    def query(self) -> str:
        return """
            SELECT COUNT(1) FROM Sales WHERE Date=%(date)s AND Category='Еда';
        """

    def checker(self):
        con = SqlConnection(connection_string=CONNECTION_STRING)
        res = con.get_connection(sql_query=self.query(), param={'date': self.date_of_interest})
        count = res[0][0]
        purchase_food = False
        logs.debug(count)
        if count:
            purchase_food = True
            logs.info(f'Проверка покупок еды:\t\t\tесть')
        else:
            logs.warning(f'Проверка покупок еды:\t\t\tнет')
        return purchase_food


class SqlConnection:

    def __init__(self, connection_string: str):
        params = connection_string.split(';')
        self.server = params[0]
        self.database = params[1]
        self.user = params[2]
        self.password = params[3]

    def get_connection(self, sql_query, param):
        conn: Connection
        with pymssql.connect(server=self.server, database=self.database,
                             user=self.user, password=self.password) as conn:
            curr: Cursor
            with conn.cursor() as curr:
                curr.execute(sql_query, param)
                result = curr.fetchall()
        return result
