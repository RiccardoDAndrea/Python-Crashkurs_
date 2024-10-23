from typing import TypeVar
import dataclasses
import streamlit as st

StateT = TypeVar('StateT')

# Funktion, um den Spielzustand persistent zu speichern
def persistent_game_state(initial_state: StateT) -> StateT:
    if 'gamestate' not in st.session_state:
        # Wenn der Zustand nicht existiert, initialisiere ihn
        st.session_state['gamestate'] = initial_state
    return st.session_state['gamestate']

# Beispiel für die Verwendung der Funktion
@dataclasses.dataclass
class GameState:
    number: int

# Initialisiere den Zustand mit einer Zufallszahl, wenn nicht vorhanden
import random
state = persistent_game_state(GameState(random.randint(1, 1000)))

# Ausgabe des Spielzustands
st.write(f"Der aktuelle Spielzustand hat die Nummer: {state.number}")
