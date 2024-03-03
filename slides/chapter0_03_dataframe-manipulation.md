---
type: slides
---

# Let's start manipulate the Dataframe!

Riprendiamo da dove eravamo rimasti:

```python
print(df)
```

<center><img src="imgs/1.1-print_df.png"></center>

Notes: Ora che hai creato un DataFrame chiamato df, hai la possibilità di richiamarlo quante volte desideri. Tuttavia, quando il DataFrame contiene molte colonne o righe, potrebbe essere complicato esplorarne il contenuto tramite una semplice stampa. Nel nostro caso, con un numero elevato di colonne, vengono mostrate tutt le righe perché il nostro df ha effettivamente solo 6 righe, e solo alcune delle molte colonne del df per rendere più gestibile la visualizzazione.

Nella stampa del DataFrame, puoi notare una barra inversa `\` che indica che le righe stanno continuando a capo nella visualizzazione del print, ma nella realtà dei dati non ci sono interruzioni. Inoltre, puoi vedere dei puntini di sospensione `...`, che indicano che molte colonne sono omesse dalla visualizzazione.

---

# Python comparison operations

| Operation | Meaning |
|:-:|:-:|
| `<` | strictly less than |
| `<=` | less than or equal |
| `>` | strictly greater than |
| `>=` | greater than or equal |
| `==` | equal |
| `!=` | not equal |
| `is` | object identity |
| `is not` | negated object identity |

Notes: Comparison always return a Boolean object which can be either `True` or `False`. You can combine multiple comparisons together using `&` (AND) or `|` (OR) statements. Note, that `True` equals `1` and `False` equals 0.

---

# Boolean operations

| Operation | Note |
|:-:|:-:|
| x \| y | if x is False, then y, else x |
| x & y | if x is False, then x, else y |
| not x | if x is False, then True, else False |

Notes: This might seem confusing at first, but that's important to keep in mind when dealing with multiple comparisons. Imagine you want to select only males who are older than 45 years for your data analysis. Your code would look something like that:

```python
(sex == "Male") & (age > 45)
```

A female who is 50 years old would have `False & True` result of two comparisons, resulting in the final `False` result. And that's exactly what you wanted since you want two conditions to be `True` at the same time.

---

# Examples

```python
# example 1
x = 45
x <= 100
```

```out
True
```

```python
# example 2
y = 20
(x > 10) | (y < 5)
```

```out
True
```

```python
# example 3
result = (x > 10) & (y < 5)
print(result)
print(type(result))
```

```out
False
bool
```

Notes: Example #1 is pretty straightforward. `x` is indeed smaller than 100, so the result is `True`.

In the second example, the left condition was `True` (`x` is greater than 10) and the right condition was `False` (`y` is not less than 5), which resulting in the final `True` result (in other words, at least one condition was `True`).

In the third example, we want to check if **both** conditions are `True`, which is not the case, that's why the final result is `False`. You can also save the result of a condition operation to a new object (like `result` in this example) for later use.

---

# Let's code!
