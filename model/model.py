from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self._tipo = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        self.lista_strumenti_mostra = [] #ogni volta che si preme mostra la lista viene svuotata

        conn = get_connection()

        cursore = conn.cursor()

        query = "SELECT * FROM STRUMENTO "
        cursore.execute(query) #eseguo la query

        for riga in cursore:
            self.lista_strumenti_mostra.append(Strumento(*riga))  #importatne mettere l'* perche permette di separare gli elementi della riga nell'ogg Strumento

        cursore.close()
        conn.close()
        return self.lista_strumenti_mostra

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        self._lista_strumenti_tipo= []
        conn = get_connection()

        cursore2 = conn.cursor()

        query = """SELECT *
                FROM STRUMENTO
                WHERE TIPO = %s"""

        cursore2.execute(query, (tipo, ))

        for riga in cursore2:
            self._lista_strumenti_tipo.append(Strumento(*riga))

        cursore2.close()
        conn.close()
        return self._lista_strumenti_tipo

