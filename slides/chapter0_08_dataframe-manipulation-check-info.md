---
type: slides
---

# Let's manipulate the Dataframe: column extraction & check info

OK, passiamo al cuore dell'attività del workshop: avete trovato le informazioni nel paper e ora volete curare i metadati di quel progetto. Le colonne che dovrete curare per ogni progetto sono 9:

* "library_strategy": la strategia di sequenziamento (AMPLICON, WGS)
* "instrument_platform": la piattaforma di sequenziamento (ILLUMINA, ION TORRENT, ...)
* "instrument_model": modello di sequenziatore (ILLUMINA MiSeq, ILLUMINA NovaSeq, ...)
* "SKIOME_amplicon_target": amplicone targettato (16S, ITS, ...)
* "SKIOME_target_region": regione ipervariabile dell amplicone (V1, V3-V4, ...)
* "SKIOME_primer": primer (GTGCCAGCMGCCGCGGTAA, GGACTACNVGGGTWTCTAAT, ...)
* "SKIOME_individuals_nationality": nazionalità degli individui campionati (Italy, Spain, ...)
* "SKIOME_body_site": sito del corpo campionato (hands, forehead, ...)
* "SKIOME_status": condizione o stato che si attribuisce ai soggetti campionati in base alle diverse ipotesi considerate (healthy vs disease, rural vs urban, ...)

Notes: Le prime 3 colonne ("library_strategy", "instrument_platform", "instrument_model") sono **sempre** presenti nei metadati che andrete a curare, mentre le altre 7 potrebbero essere presenti o meno. Di conseguenza, ci sono due strade che dovrete percorrere:

* Per le **COLONNE SEMPRE PRESENTI** ("library_strategy", "instrument_platform", "instrument_model") dovrete verificare che i valori contenuti in queste colonne coincidano con quelli trovati nel paper. Se corrispono, ottimo! non dovete fare nulla e potete passare alla prossima colonna. Se, invece, i valori nelle colonne sono diversi da quelli che avete trovato nel paper allora dovete modificarli.

* Per le **COLONNE POTENZIALMENTE ASSENTI** dovete innanzitutto verificare se la colonna esiste:
    * Se **ESISTE**, comportatevi come nel caso delle colonne sempre presenti: controllate che il valore contenuto sia lo stesso di quello nel paper. Se i valori coincidono, non è necessario apportare modifiche e potete passare alla prossima colonna. Se i valori sono diversi, dovrete procedere con la correzione.
    * Se **NON ESISTE** allora è necessario crearne una nuova e assegnarle il valore trovato nel paper.
              
---

# Let's manipulate the Dataframe: COLONNE SEMPRE PRESENTI

Verifichiamo che il valore delle tre colonne sempre presenti sia quello che hai trovato nel paper! Partiamo dalla colonna `library_strategy` e poi ripetiamo gli stessi comandi per tutte e 3 le colonne sempre presenti.

```python
strategia = df["library_strategy"].unique()
print(strategia)
```

```out
['AMPLICON']
```

Notes: Per verificare che il valore presente nella colonna da curare sempre presente sia lo stesso trovato nel paper, basta sfruttare quello che hai imparato finora! Quindi abbiamo estratto il valore unico dalla colonna `library_strategy` e l'abbiamo stampato. TA-DAAN: `AMPLICON`. Il valore trovato è corrisponde con quello che abbiamo letto nel paper e quindi possiamo procedere con un'altra colonna.

---

# Let's manipulate the Dataframe: COLONNE SEMPRE PRESENTI

Verifichiamo ora il valore contenuto dalla colonna `instrument_platform`!

```python
piattaforma = df["instrument_platform"].unique()
print(piattaforma)
```

```out
["VALORE SBAGLIATO"]
```

```python
df["SKIOME_instrument_platform"] = "AMPLICON"
```

```out
["AMPLICON"]
```

Notes: Supponiamo che, durante la verifica di questa colonna, abbiamo riscontrato un valore diverso da quello dichiarato nel paper. Niente di più semplice: dobbiamo creare una nuova colonna contenente il valore corretto. Per fare ciò, dobbiamo specificare il nome del DataFrame (`df`) seguito dalle parentesi quadre (`[]`), all'interno delle quali indichiamo il nome della nuova colonna. Quando crei una nuova colonna, segui il nome suggerito nella lista iniziale delle colonne da curare. Nota che, se stai curando quella particolare colonna, devi aggiungere come prefisso "SKIOME_". Questo aiuterà chi utilizzerà la raccolta a capire che la colonna è stata curata!


# Let's manipulate the Dataframe: COLONNE SEMPRE PRESENTI

Non c'è regola se non ci sono eccezioni... Può capitare che non esista una delle tre colonne che ti abbiamo detto essere sempre presenti! E allora che fare? Semplice, crea una nuova colonna e assegna il valore che hai trivato nel paper:

```python
i_am_valid_list = [1, "Hello", [1,2,False], True-0, 42<3.14]
print(i_am_valid_list)
```

```out
[1, 'Hello', [1, 2, False], 1, False]
```

Notes: There are some trivial built-in functions like `sum()`, `max()`, `min()` that could be applied to lists. There is no built-in `avg()` or `mean()` function, but you could easily calculate it yourself.

Keep in mind, that list can hold objects of different types, even another lists. Some functions like `sum()` wouldn't work in that case since you cannot take the sum of string and number for obvious reasons.

---

# method == function?

```python
participants = ['Bob', 'Bill', 'Sarah', 'Max', 'Jill']
# methods that modify the initial list
participants.append('Jack') # append one element to the end
# ['Bob', 'Bill', 'Sarah', 'Max', 'Jill', 'Jack']
participants.extend(['Anna', 'Bill']) # append multiple elements to the end
# ['Bob', 'Bill', 'Sarah', 'Max', 'Jill', 'Jack', 'Anna', 'Bill']
participants.insert(0, 'Louis') # insert the element at index 0 (shifts everything to the right)
# ['Louis', 'Bob', 'Bill', 'Sarah', 'Max', 'Jill', 'Jack', 'Anna', 'Bill']
participants.remove('Jill') # searches for the first instance and removes it
# ['Louis', 'Bob', 'Bill', 'Sarah', 'Max', Jack', 'Anna', 'Bill']
participants.pop(1) # removes the element at index 1 and returns it
# ['Louis', 'Bill', 'Sarah', 'Max', Jack', 'Anna', 'Bill']
```
```python
# methods that don't modify initial list and return a new object
print(participants.count('Bill')) # returns the number of instances
print(participants.index('Max'))  # returns the index of the first instance
```

```out
2
3
```

```python
# not a method, but in this way you can change the value(s) of the list
participants[2] = 'Ben' # replace the element at the index 2
# ['Louis', Bill', 'Ben', 'Max', Jack', 'Anna', 'Bill']
```

Notes: You heard the terms "method" and "function" already and most of the time they could be used interchangeably. But in fact, they are not the same. Think of methods as a function, that could be applied only on a specific data type. Whereas function `len()` for example can be applied on strings, lists and many other objects. We call function by `function(object)` and method by `object.method()`.

On this slide you can see some of the methods, that are unique for the lists.  It's important to note that all of these methods change the initial string. You can see how the string changes in comment lines.

If you run a code like this one, you will end up with `NoneType` object:

```python
l = [1,2,3]
l = l.append(4)
```

Keep in mind that this is not always the case. Some methods don't change the method (or have an argument that allows to specify it). The best way to know whether the method changes the object or returns new objects is the documentation.

---

# Tuples

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

```python
brain_lobes = ('frontal', 'parietal', 'temporal', 'occipital')
# or:
# brain_lobes_list = ['frontal', 'parietal', 'temporal', 'occipital']
# brain_lobes = tuple(brain_lobes_list)
print(type(brain_lobes))
```

```out
tuple
```

```python
brain_lobes[0] = 'anterior'
```

```out
TypeError: 'tuple' object does not support item assignment
```


Notes: Another collection type in Python is tuple. We defined lists using the square brackets (`[1,2,3]`), but for tuples we use parentheses (`(1,2,3)`).

Tuples are quite "boring" since they don't have so many methods that can be applied to them. But there is a reason for that. Tuples are **unchangeable**. This means that no function or method can change objects in the tuple.

---

# Sets

Set is a collection which is unsorted and un-indexed. No duplicate members.
```python
languages = {'python', 'r', 'java'} # create a set directly
snakes = set(['cobra', 'viper', 'python']) # create a set from a list
```

**Set operations**:
```python
languages & snakes # intersection, AND
```

```out
{'python'}
```

```python
languages | snakes # union, OR
```

```out
{'cobra', 'java', 'python', 'r', 'viper'}
```

```python
languages - snakes # set difference
```

```out
{'java', 'r'}
```

Notes: Figure brackets are the indicator for sets, another collection type. You cannot access items in a set by referring to an index since sets are unordered and have **no index**. But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

You can apply basic sets commands (like union or intersection). Note that we didn't get `'python'` twice for the union since sets consist only of unique values. This fact can become handy used when looking for the unique values in a list.

---

# Dictionaries

Dictionaries are: unordered, iterable, mutable.

```python
participant = {'name': 'Jon Doe', 'group': 'Control', 'age': 42}
print(participant['name'])
```

```out
Jon Doe
```

```python
# add new key-value pair to the dictionary
participant['ID'] = 'CJD'
print(participant)
```
```out
{'name': 'Jon Doe', 'group': 'Control', 'age': 42, 'ID': 'CJD'}
```

```python
participant.keys()
```
```out
['name', 'group', 'age', 'ID']
```

```python
my_dict.values()
```
```out
['Jon Doe', 'Control', 42, 'CJD']
```

Notes: Dictionaries are structures which can contain multiple data types, and is ordered with key-value pairs: for each unique key, the dictionary has one value. Keys can be strings, numbers, or tuples, while the corresponding values can be any Python object.

```python
dict_obj = {
    'key1': value1,
    'key2': value2,
    ...}
```
As you can see from the first example, you cannot access values of the dictionary by the indexes (like you did in lists). But you can access them by the key. Due to this feature dictionaries don't allow duplicated keys.

You can also access just the keys or just the indexes by `.keys()` and `.values()` methods.
---

# Let's code!
