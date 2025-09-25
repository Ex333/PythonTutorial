"""
FOR LOOP — JEDNA LEKCJA W JEDNYM PLIKU

Co umie pętla for w Pythonie:
- iteracja po sekwencjach/iterable: listy, krotki, stringi, słowniki, pliki, range, generatory
- narzędzia pomocnicze: range(), enumerate(), zip()
- sterowanie przebiegiem: break, continue, else
- skróty: list/dict/set comprehensions
- iteracja po pliku linia-po-linii (oszczędna pamięciowo)

Użycie:
>>> import for_lesson
>>> for_lesson.demo()

Wszystkie przykłady zwracają dane (nie tylko print), więc można je testować/importować.
"""

from pathlib import Path
from typing import Iterable, List, Tuple, Dict


# --- PODSTAWY ---------------------------------------------------------------

def iterate_list(xs: Iterable[int]) -> List[int]:
    """Zwróć elementy z xs tak jak przechodzi po nich for."""
    out = []
    for x in xs:
        out.append(x)
    return out


def iterate_string(s: str) -> List[str]:
    """Zwróć listę znaków stringa (iteracja po str)."""
    chars = []
    for ch in s:
        chars.append(ch)
    return chars


def numeric_loops(start: int, stop: int, step: int = 1) -> List[int]:
    """Iteracja po liczbach z użyciem range(start, stop, step)."""
    out = []
    for i in range(start, stop, step):
        out.append(i)
    return out


# --- enumerate / zip --------------------------------------------------------

def with_enumerate(items: List[str], start: int = 0) -> List[Tuple[int, str]]:
    """Zwróć (indeks, wartość) z enumerate."""
    out = []
    for idx, val in enumerate(items, start=start):
        out.append((idx, val))
    return out


def with_zip(names: List[str], ages: List[int]) -> List[Tuple[str, int]]:
    """
    Zwróć pary (name, age) łącząc listy równolegle.
    Uwaga: zip kończy na najkrótszej liście.
    """
    pairs = []
    for n, a in zip(names, ages):
        pairs.append((n, a))
    return pairs


# --- dict iteration ---------------------------------------------------------

def dict_iteration(d: Dict[str, int]) -> Tuple[List[str], List[Tuple[str, int]]]:
    """
    Zwróć (lista_kluczy, lista_par_klucz_wartość).
    Pokazuje iterację po dict: po kluczach i po items().
    """
    keys = []
    for k in d:         # to samo co for k in d.keys()
        keys.append(k)

    items = []
    for k, v in d.items():
        items.append((k, v))

    return keys, items


# --- break / continue / else ------------------------------------------------

def find_first_even(nums: List[int]) -> Tuple[int | None, bool]:
    """
    Zwróć (pierwsza_parzysta albo None, czy_else_wykonane).
    'else' wykona się TYLKO jeśli pętla NIE została przerwana breakiem.
    """
    first = None
    else_ran = False

    for n in nums:
        if n % 2 == 0:
            first = n
            break
    else:
        else_ran = True

    return first, else_ran


def odds_only(nums: List[int]) -> List[int]:
    """Użyj continue, by pominąć liczby parzyste."""
    out = []
    for n in nums:
        if n % 2 == 0:
            continue
        out.append(n)
    return out


# --- nested loops -----------------------------------------------------------

def multiplication_table(n: int) -> List[List[int]]:
    """Zwróć tabliczkę mnożenia n×n jako listę list."""
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table


# --- comprehensions ---------------------------------------------------------

def squares_until(n: int) -> List[int]:
    """List comprehension: kwadraty 0..n-1."""
    return [i * i for i in range(n)]


def even_squares_until(n: int) -> List[int]:
    """List comprehension z warunkiem: parzyste kwadraty 0..n-1."""
    return [i * i for i in range(n) if i % 2 == 0]


def dict_comp_word_lengths(words: List[str]) -> Dict[str, int]:
    """Dict comprehension: {słowo: długość}."""
    return {w: len(w) for w in words}


# --- iteracja po pliku ------------------------------------------------------

def ensure_file(path: Path) -> None:
    """Upewnij się, że plik istnieje (bez nadpisywania zawartości)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)


def count_lines(path: Path) -> int:
    """
    Policz linie w pliku iterując po uchwycie pliku (wydajnie pamięciowo).
    Tworzy pusty plik, jeśli nie istnieje.
    """
    ensure_file(path)
    count = 0
    with path.open("r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    return count


def append_lines(path: Path, lines: Iterable[str]) -> None:
    """Dopisanie linii do pliku (pokazanie trybu 'a')."""
    ensure_file(path)
    with path.open("a", encoding="utf-8") as f:
        for line in lines:
            f.write(line.rstrip("\n") + "\n")


# --- DEMO: szybkie uruchomienie wszystkiego --------------------------------

def demo() -> None:
    print("\n== Podstawy ==")
    print("iterate_list:", iterate_list([1, 2, 3]))
    print("iterate_string:", iterate_string("hej"))
    print("numeric_loops 1..5:", numeric_loops(1, 6))

    print("\n== enumerate / zip ==")
    print("with_enumerate:", with_enumerate(["red", "green", "blue"], start=1))
    print("with_zip:", with_zip(["Ala", "Ola", "Ewa"], [25, 30, 22]))

    print("\n== dict iteration ==")
    keys, items = dict_iteration({"a": 1, "b": 2})
    print("keys:", keys)
    print("items:", items)

    print("\n== break / continue / else ==")
    first_even, else_ran = find_first_even([1, 3, 5, 8, 9])
    print("first_even:", first_even, "else_executed:", else_ran)
    print("odds_only:", odds_only([1, 2, 3, 4, 5, 6]))

    print("\n== nested loops ==")
    print("multiplication_table 1..3:", multiplication_table(3))

    print("\n== comprehensions ==")
    print("squares_until(6):", squares_until(6))
    print("even_squares_until(10):", even_squares_until(10))
    print("dict_comp_word_lengths:", dict_comp_word_lengths(["kot", "pies", "anakonda"]))

    print("\n== file iteration ==")
    p = Path("file.txt")
    before = count_lines(p)
    append_lines(p, ["pierwsza", "druga", "trzecia"])
    after = count_lines(p)
    print(f"lines before: {before}, after append: {after} (dodano {after - before})")


# Opcjonalnie: odkomentuj, jeśli chcesz uruchamiać bez importu:
# if __name__ == "__main__":
#     demo()
