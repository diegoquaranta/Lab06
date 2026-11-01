import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def get_lista_strumenti_mostra(self):
        return self._model.get_strumenti()
    def mostra_strumenti(self):
        strumenti = self.get_lista_strumenti_mostra()

        self._view.lista_strumenti.controls.clear()

        for strumento in strumenti:
            self._view.lista_strumenti.controls.append(ft.Text(str(strumento)))

        self._view.update()

    def get_tipo(self):
        return self._model.tipo
    def set_tipo(self,  tipo):
        self._model.tipo = tipo
    def cerca_tipo(self, e):
        tipo = self._view.input_tipo_strumento.value

        strumenti_trovati = self._model.cerca_strumenti_per_tipo(tipo)

        self._view.lista_strumenti_ricerca.controls.clear()

        for strumento in strumenti_trovati:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(strumento))) #importante che si deve mettere ft.Text

        self._view.update()
