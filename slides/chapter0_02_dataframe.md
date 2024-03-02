---
type: slides
---

# I nostri metadati come DataFrame

<center><img src="imgs/1.1-df.png"></center>

Credits: https://www.geeksforgeeks.org/python-pandas-dataframe/

Notes: Un DataFrame rappresenta una tabella bidimensionale costituita da righe e colonne, simile a un foglio di calcolo Excel. Il DataFrame è uno dei vari tipi di variabile che potrai trovare in Python! In questo workshop, il DataFrame costituisce la variabile principale: infatti nei progetti che affronteremo, i metadati da curare saranno trattati come DataFrame. Quindi, gran parte del nostro lavoro consisterà nella manipolazione e nell'analisi dei metadati strutturati in DataFrame.

---

# Importare il file di metadati come DataFrame

Per prima cosa dobbiamo leggere il file di metadati come un DataFrame:

```python
import pandas as pd

df = pd.read_csv("ERP020892.tsv", sep="\t")
print(df)
```

<center><img src="imgs/1.1-print_df.png"></center>

Notes: Ecco, abbiamo iniziato importando la libreria Pandas per poter sfruttare le sue funzioni. La prima funzione che abbiamo esplorato è `read_csv`, essenziale per leggere un file tabulare (csv, tsv, ecc.) e convertirlo in un DataFrame. In questa funzione, abbiamo indicato il nome del file tra virgolette (perché è una stringa, un altro tipo di variabile in Python!) e il separatore del file. Nel nostro caso, i metadati sono in formato TSV (Tab-Separated Values), dove i dati sono separati da un tab. Per questo motivo, nella funzione dobbiamo aggiungere dopo il nome del file, l'opzione `sep="\t"` per indicare alla funzione che i dati sono separati da tabulazione.

Ah, nota che abbiamo usato una funzione predefinita di Python: `print()`. Questa funzione è utilizzata per visualizzare ciò che viene inserito tra le sue parentesi. In questa caso gli abbiamo chiesto di mostrarci il DataFrame df.

---

# Saving your objects

Save the result of a calculation:
```python
x = 2 + 2*2
print(x)
print(type(x))
```

```out
6
int
```

Use it later:

```python
y = x - 10
print(y)
```

```out
-4
```

Notes: Most of the times you will perform more complex tasks in Python than just `2*2` and you will want to save your resulting objects for the later usage. For example, imagine calculating the average values of some parameter among control and treatment groups and using these values to perform statistical test.

In the same way you do this in math, you do it in Python. `x = 5` means that you create a new variable called `x` that will hold an object `5`. Names of the variables are arbitrary, but should be meaningful for the code readability. We will get to the part of code style guidelines a bit later.

You can go bigger, and assign not just one object to a new variable `x`, but the result of an operation. `x` variable will stay in the memory (Python memory, not talking about the hippocampus here) as long as you don't delete it, so you can use it later.

---

# Built-in types

You have seen `int` type already. Here are some more:

```python
var = 5.5 # floating point number
print(type(var))
```

```out
float
```

```python
var = "Hello, Neuroscience" # string
print(type(var))
```

```out
str
```

```python
var = True # boolean
print(type(var))
```

```out
bool
```

Notes: Python has some built-in types, which you can see on this slide, but there are lots and lots more. As told before, each type has its own specific functions that can be applied to it and will go through them as we learn.

---

# Some of the cool stuff you can do with numbers

| Operation | Note |
|:-:|:-:|
| `x + y` | sum of `x` and `y` |
| `x - y` | difference of `x` and `y` |
| `x * y` | product of `x` and `y` |
| `x / y` | quotient of `x` and `y` |
| `x // y` | floored quotient of `x` and `y` |
| `x % y` | remainder of `x` / `y` |
| `-x` | `x` negated |
| `+x` | `x` unchanged |
| `abs(x)` | absolute value or magnitude of `x` |
| `pow(x, y)` | `x` to the power `y` |
| `x ** y` | `x` to the power `y` |

Notes: Most of the numeric operations are pretty straight-forward. However there are some surprises like `2^2`, which **is not** 2 to the power of 2.

---

# Let's code!
