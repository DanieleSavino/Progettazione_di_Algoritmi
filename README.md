# 📚 Esercizi di Progettazione di Algoritmi (Monti)

Questa repository raccoglie una serie di esercizi tratti dal corso di **Progettazione di Algoritmi (Algoritmi II)**
del corso triennale di Informatica presso l'Università di Roma "La Sapienza".
Ogni lezione contiene problemi algoritmici corredati da soluzioni ottimizzate e un'analisi della complessità computazionale.

🔍 **Obiettivo**: Fornire un supporto per lo studio e l'approfondimento degli argomenti trattati nel corso.

⚠️ **Nota**: Questa repository è destinata esclusivamente all'esercitazione personale e non intende sostituire le fonti ufficiali.

---

## 📌 Lezione 1: Richiami ad `Introduzione agli Algoritmi`

🔹 **Algoritmi trattati**:
- ✅ [Conta Triple](src/lezione_1/conta_triple.md)
- ✅ [Maggioranza Assoluta](src/lezione_1/maggioranza_assoluta.md)
- ✅ [Trova Somma](src/lezione_1/trova_somma.md)
- ✅ [Unione Sottoinsiemi](src/lezione_1/unione_sottoinsiemi.md)

📂 **Percorso file:** `src/lezione_1`

---

## 📌 Lezione 2: Introduzione ai Grafi

🔹 **Algoritmi trattati**:
- ✅ [Pozzo Universale](src/lezione_2/pozzo_universale.md)

📂 **Percorso file:** `src/lezione_2`

---

## 📌 Lezione 3: `DFS`, Depth First Search

🔹 **Algoritmi trattati**:
- ✅ [Depth First Search](src/lezione_3/depth_first_search.md)

📂 **Percorso file:** `src/lezione_3`

---

## 📌 Lezione 4: Algoritmo `path finding` su grafi tramite DFS 

🔹 **Algoritmi trattati**:
- ✅ [Dfs Padri](src/lezione_4/dfs_padri.md)
- ✅ [Trova Path](src/lezione_4/trova_path.md)

📂 **Percorso file:** `src/lezione_4`

---

## 📌 Lezione 5: Componenti Connesse in un Grafo

🔹 **Algoritmi trattati**:
- ✅ [Componenti Connesse](src/lezione_5/componenti_connesse.md)
- ✅ [Componenti Fortemente Connesse](src/lezione_5/componenti_fortemente_connesse.md)

📂 **Percorso file:** `src/lezione_5`

---

## 📌 Lezione 6: Sort Topologico e Grafi Ciclici

🔹 **Algoritmi trattati**:
- ✅ [Grafi Ciclici](src/lezione_6/grafi_ciclici.md)
- ✅ [Sort Topologico](src/lezione_6/sort_topologico.md)

📂 **Percorso file:** `src/lezione_6`

---

## 📌 Lezione 7: 

🔹 **Algoritmi trattati**:
- ✅ [Archi Ponte](src/lezione_7/archi_ponte.md)

📂 **Percorso file:** `src/lezione_7`

---


## 📢 Esecuzione dei Test

Questa repository include test automatici per verificare la correttezza delle soluzioni implementate.
I test sono eseguiti mediante il framework **pytest**, lo stesso utilizzato dai test per gli homework di **Fondamenti di programmazione**.

### 🔍 Prerequisiti

Per eseguire i test è necessario avere installato **Python** ed il package **pytest**. Se non è già installato, eseguire il seguente comando:

```bash
pip install pytest
```

### ✅ Esecuzione dei test

1. **Accedere alla cartella del progetto:**
   ```bash
   cd /percorso/della/repository
   ```
2. **Eseguire tutti i test:**
   ```bash
   pytest
   ```
   Questo comando eseguirà tutti i test presenti nella directory `test/` e produrrà un report dettagliato.

3. **Eseguire un file specifico di test:**
   ```bash
   pytest test/lezione_1/maggioranza_assoluta_test.py
   ```

4. **Eseguire un test specifico all'interno di un file:**
   ```bash
   pytest test/lezione_1/maggioranza_assoluta_test.py::test_maggioranza_assoluta_count
   ```

### ⚙ Interpretazione dei risultati

Al termine dell'esecuzione di `pytest`, il terminale restituirà un output simile al seguente:

```bash
test/lezione_1/maggioranza_assoluta_test.py::test_maggioranza_assoluta_count PASSED
```

- **`PASSED`** → Il test è stato superato con successo.
- **`FAILED`** → Il test non è stato superato. Verrà fornito un messaggio di errore per il debug.
- **`SKIPPED`** → Il test è stato ignorato (ad esempio, a causa di una configurazione specifica).

### 📄 Esempio di file di test

Di seguito è riportato un esempio di file di test per l'algoritmo **Trova Somma**:

```python
import pytest

from src.lezione_1.trova_somma import (
    trova_somma_bruteforce,
    trova_somma_set
)
        
test_cases = [
    ([1, 2, 3, 4, 5], 5, True),
    ([10, 20, 30, 40], 50, True),
    ([5, 7, 1, 2, 8, 4, 3], 10, True),
    ([], 5, False),
]

@pytest.mark.parametrize("arr, k, exist", test_cases)
def test_trova_somma_bruteforce(arr, k, exist):
    res = trova_somma_bruteforce(arr, k)
    assert (res is not None) == exist
```

Questi test verificano che le funzioni restituiscano risultati corretti, validando il comportamento dell'algoritmo in diversi scenari.

---

## 📌 Caratteristiche della Repository:
- Ogni esercizio include un'analisi della complessità computazionale.
- Sono presenti più implementazioni per confrontare differenti approcci risolutivi.
- Sono forniti test automatici per garantire la correttezza del codice.
- Il file readme è generato automaticamente, può dunque contenere errori.
