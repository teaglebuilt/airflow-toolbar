from airflow import settings
from airflow.models import Connection, Variable
from typing import Optional, Union


class AirflowDB:
    sql_alchemy_conn: str = None

    def __init__(self, sql_alchemy_conn: str):
        self.sql_alchemy_conn = sql_alchemy_conn

    def set_connection(
            self,
            conn_id: str,
            conn_type: str,
            host: Optional[str] = None,
            schema: Optional[str] = None,
            login: Optional[str] = None,
            password: Optional[str] = None,
            port: Optional[int] = None,
            extra: Optional[Union[str, dict]] = None,
    ):
        assert repr(settings.engine.url) == self.sql_alchemy_conn
        session = settings.Session()
        new_conn = Connection(conn_id=conn_id, conn_type=conn_type, host=host,
                              login=login, password=password, schema=schema, port=port)
        if extra is not None:
            new_conn.set_extra(extra if isinstance(extra, str) else json.dumps(extra))

        session.add(new_conn)
        session.commit()
        session.close()

    def set_variable(
            self,
            var_id: str,
            value: str,
            is_encrypted: Optional[bool] = None
    ):
        assert repr(settings.engine.url) == self.sql_alchemy_conn
        session = settings.Session()
        new_var = Variable(key=var_id, _val=value, is_encrypted=is_encrypted)
        session.add(new_var)
        session.commit()
        session.close()
