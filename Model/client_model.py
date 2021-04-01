from os.path import exists

from sqlalchemy import text

from Domain.client import Client
from utils import engine


class ClientFileModel:
    def __init__(self, filename):
        self.__filename = filename
        self.__all_clients = []
        self.read_clients()

    def get_all_clients(self):
        return self.__all_clients

    def create_client(self, cnp, last_name, first_name, email):
        client = Client(
            cnp=cnp,
            last_name=last_name,
            first_name=first_name,
            email=email
        )

        self.__all_clients.append(client)
        self.__save_to_file()

    def read_clients(self):
        """

        :return: 
        """
        if not exists(self.__filename):
            return

        with open(self.__filename, 'r') as my_file:
            for line in my_file:
                line = line.strip().split('|')
                client = Client(
                    cnp=line[0],
                    last_name=line[1],
                    first_name=line[2],
                    email=line[3]
                )

                self.__all_clients.append(client)

    def __save_to_file(self):
        """

        """
        with open(self.__filename, 'w') as my_file:
            for client in self.__all_clients:
                line = ''
                line += str(client.get_cnp()) + '|' + client.last_name + '|' + client.first_name + '|' + \
                        client.email + '\n'
                my_file.write(line)

    def update_client(self, cnp, last_name, first_name, email):
        """

        """
        for index, client in enumerate(self.__all_clients):
            if client.get_cnp() == cnp:
                if last_name:
                    self.__all_clients[index].last_name = last_name
                if first_name:
                    self.__all_clients[index].first_name = first_name
                if email:
                    self.__all_clients[index].email = email
                break
        self.__save_to_file()

    def delete_client(self, cnp):
        for index, client in enumerate(self.__all_clients):
            if client.get_cnp() == cnp:
                del self.__all_clients[index]

        self.__save_to_file()

    def find_by_id(self, cnp):
        for client in self.__all_clients:
            if client.get_cnp() == cnp:
                return client
        return None

    def id_exists(self, cnp):
        for client in self.__all_clients:
            if client.get_cnp() == cnp:
                return True
        return False

class ClientSQLModel:
    def __init__(self):
        self.__engine = engine

    def get_all_clients(self):
        return self.read_clients()

    def create_client(self, cnp, last_name, first_name, email):

        age_group = Client.get_age_group(cnp)

        with self.__engine.connect() as conn:
            conn.execute(text(f"INSERT INTO clients (cnp, first_name, last_name, age_group, email) "
                              f"VALUES ('{cnp}', '{first_name}', '{last_name}', '{age_group}', '{email}')"))

    def read_clients(self):
        all_clients = []
        with self.__engine.connect() as conn:
            query = conn.execute(text('SELECT * FROM clients'))
            for item in query:
                client = Client(
                    cnp=item[0],
                    first_name=item[1],
                    last_name=item[2],
                    email=item[4],
                )
                all_clients.append(client)
        return all_clients

    def update_client(self, cnp, last_name, first_name, email):
        with self.__engine.connect() as conn:
            query = conn.execute(text(f'SELECT * FROM clients WHERE cnp = {cnp}'))
            values = query.first()
            if values:
                _, current_first_name, current_last_name, _, current_email, _ = values
                conn.execute(text(f'UPDATE clients '
                                  f'SET last_name = "{last_name or current_last_name}", '
                                  f'first_name = "{first_name or current_first_name}", '
                                  f'email = "{email or current_email}" '
                                  f'WHERE cnp = "{cnp}"'
                                  ))

    def delete_client(self, cnp):
        with self.__engine.connect() as conn:
            result = conn.execute(text(f'DELETE FROM clients WHERE cnp = {cnp}'))

    def find_by_id(self, cnp):
        with self.__engine.connect() as conn:
            query = conn.execute(text(f'SELECT * FROM clients WHERE cnp = {cnp}'))
            client_data = query.first()
            if client_data:
                cnp, last_name, first_name, _, email, _ = client_data
                client = Client(
                    cnp=cnp,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                return client
        return None

    def id_exists(self, cnp):
        with self.__engine.connect() as conn:
            query = conn.execute(text(f'SELECT * FROM clients WHERE cnp = {cnp}'))
            client_data = query.first()
            if client_data:
                return True
        return False
