"""
Aufgabe Facebook Likebutton (schwer)

THEMA: State-Maschine, Enum
Benötigtes Wissen: Enum-Modul

# Beschreibung:
Das Facebook-Element "Gefällt mir" besteht aus zwei Buttons: Like und Dislike
symbolisiert durch Daumen hoch, und Daumen runter.

Das Element kann in einem von drei Zuständen (State) sein:
- Empty (kein Like oder Dislike)
- Liked (Daumen hoch)
- Disliked (Daumen runter)

nben den drei Zuständen (states) gibt es zwei Events:
- like Button drücken
- dislike Button drücken

Empty:
+-----------------+
| Like [ ]        |
| Dislike [ ]     |
+-----------------+

Liked:
+-----------------+
| Like [X]        |
| Dislike [ ]     |
+-----------------+

Disliked:
+-----------------+
| Like [ ]        |
| Dislike [X]     |
+-----------------+

Klick auf LIKE-BUTTON:
Wenn Zustand ist empty, Zustand wird liked
Wenn Zustand ist liked, Zustand wird empty
Wenn Zustand ist disliked, Zustand wird liked

Klick auf DISLIKE-BUTTON:
Wenn Zustasnd empty, Zustand wird disliked,
Wenn Zustand liked, Zustand  wird disklike
Wenn Zustand gerade disliked, wird Zustand empty

Implementiere die zwei Events (click like und dislike) und drei Zustände
(empty, liked, disliked).

Nutze Enum.

# ----------------------------------------------------------------------
Zusatzaufgabe: Teste das System, indem eine Folge von Klicks auf
den Button simuliert wird.

zb. "lldd" => Drücke like, Drücke like, drücke dislike, drücke dislike
und prüfe das Ergebnis.

def press_many(start_state: LikeState, actions: str) -> LikeState:
    ...

press_many(LikeState.empty, "ddll")

"""

import enum


class LikeState(enum.Enum):
    """
    der Zustand des Likebuttons (es gibt drei Zustände)
    """

    ...


def press_like(s: LikeState) -> LikeState:
    """
    Args:
        s: Likezustand
    Return:
        Likezustand

    """
    ...


def press_dislike(s: LikeState) -> LikeState:
    """
    Args:
        s: Likezustand
    Return:
        Likezustand
    """
    ...


def press_many(start_state: LikeState, actions: str) -> LikeState:
    """Simulation von vielen Klicks auf die Like/Dislike-Button

    Simuliere das System, indem eine Folge von Klicks auf den Button simuliert wird
    zb. "lldd" => Drücke like, Drücke like, drücke dislike, drücke dislike
    Args:
        start_state: LikeState
        actions: str
    Return:
        LikeState
    """


def test_likestate():
    assert press_many(LikeState.empty, "ll") is LikeState.empty  # like, like
    assert press_many(LikeState.empty, "dd") is LikeState.empty  # dislike, dislike
    assert press_many(LikeState.empty, "ld") is LikeState.disliked  # like, dislike
    assert press_many(LikeState.empty, "dl") is LikeState.liked  # dislike, like
    assert (
        press_many(LikeState.empty, "ldd") is LikeState.empty
    )  # like, dislike, dislike
    assert press_many(LikeState.empty, "lldd") is LikeState.empty  #  usf
    assert press_many(LikeState.empty, "ddl") is LikeState.liked


test_likestate()
