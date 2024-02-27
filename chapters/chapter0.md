---
title: 'Chapter 0: PYTHON - INTRODUCTION'
description:
  "Partiamo dalle basi"
prev: null
next: /chapter1
type: chapter
id: 0
---

<exercise id="1" title="Introduction">

Ciao Data Hunter!

Qui puoi trovare tutte le informazioni necessarie per affrontare le sfide del workshop, oltre a una vasta gamma di altri dettagli e risorse.

</exercise>

<exercise id="3" title="Data sets used" type="slides">

<slides source="chapter0_02_data">
</slides>

</exercise>

<exercise id="4" title="Python installation">

If you don't have Python installed on your computer, but you want to have it installed, I would suggest to check out Anaconda.

<center><img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png" width="300"></img></center>

**Anaconda** is a distribution of the Python and R programming languages (and julia recently) for scientific computing, that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS.

Simply saying, after installation of Anaconda you will get Python and 95% of the most used libraries ready to use. Installation of Anaconda is a pretty simple process, which is described precisely in the documentation.

[Download](https://www.anaconda.com/products/individual) || [Installation guides (macOS, Windows, Linux)](https://docs.anaconda.com/anaconda/install/)

If you have never worked with Python, I would suggest starting with [JupyterLab](https://jupyter.org/) environment. If you have installed Anaconda, you don't need any additional installations. Here is a nice video tutorial: [Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough](https://www.youtube.com/watch?v=HW29067qVWk)

<center><img src="https://jupyterlab.readthedocs.io/en/stable/_images/jupyterlab.png" width="600"></img></center>

[JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/)

<br>
Do I necessarily have to install Python for this course?

<choice id="1">
<opt text="Yes">
You *don't have to*, but you might benefit more from the course if you go beyond the exercises in the course and apply gained knowledge on your own problems.
</opt>

<opt text="No" correct="true">
You have Python interpreter built on Binder directly on the website, so you can do all the coding here.
</opt>
</choice>

</exercise>

<exercise id="5" title="Where to search for help">

<center><img src="imgs/documentation.jpg" width="500"></img></center>

What could you do if you know the name of the function (for example `print()`) but you don't know how to use it? You can look into the documentation of the function on the [website](https://docs.python.org/3/library/functions.html#print) or use the [`help()`](https://docs.python.org/3/library/functions.html#help) function directly in Python:

```python
help(print)
```
```out
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

However, what should you do if you don't know which function can help if solving an issue (for example, how to calculate average in Python)? In such a case Google search will help. Most of the questions you have were asked online before you. The best way to get the solution to your problem is Stack Overflow. Data Science has a great online community that is happy to help.

<center><img src="imgs/stackoverflow.png" width="500"></img></center>

There are hundreds of packages with hundreds of functions in each, so it's impossible to learn them all by heart. Here is a nice collection of the packages divided by tasks: [Awesome Python](https://awesome-python.com/) or [GitHub link](https://github.com/vinta/awesome-python).

And of course cheat sheets might also become handy: [Data Science Cheat Sheets](https://www.datacamp.com/community/data-science-cheatsheets).

</exercise>

<exercise id="6" title="A little bit of motivation">

In 1963 there was an experiment by Held and Hein where they put neonatal (newborn) kittens in a special device. One kitten was able to move around in a circle, the other one was kept in a basket so he couldn't move around but could observe the world around due to the movements induced by the actively moving kitten. Animals spent around 3 hours a day in that device and the rest of the time they spent in a cage with no light. Each animal was tested in several tests afterward, such as avoidance of a visual cliff or blink to an approaching object. The study showed that passively moved kittens failed to show a response (blink) to an approaching object or discrimination of the cliff.

<center><img src="imgs/cats.png" width="500"></img></center>

Held, R., & Hein, A. (1963). Movement-produced stimulation in the development of visually guided behavior. *Journal of Comparative and Physiological Psychology*, 56(5), 872–876. https://doi.org/10.1037/h0040546

What does that mean? Quote from the paper: "*Self-produced movement with its concurrent visual feedback is necessary for the development of visually-guided behavior*". In other words, actively moving kittens were able to make an association of the world around them by engaging with it, whereas passively moved kittens were not able to do so, although they both were kept in the same environment and saw the same objects. Development of the visually-guided behavior (for example, estimation of the distance to the object or discriminating the shallow objects) cannot be achieved just by observing the world around.

Why do I bring this up here? We can abstractly transfer this to programming learning. There are 1000+ different libraries and functions in Python and there is no course that can introduce them all to you. And more importantly, **no Python course will make you a good programmer by simply watching the videos/slides without the interaction**. Programming is not a type of knowledge that can be learned by observing.

This course will introduce basic concepts of programming with the example of some functions and problems but there are lots more! I highly encourage you to play around with the problem sets apart from the tasks described. You could ask yourself questions like "What will change if I replace value X with value Y?" or "What does this argument do and what happens if I drop it?". Don't be afraid to change different parts of the code and see what happens. I promise you that your computer will not explode because of it (if it does, feel free to complain about it in DM on Twitter). In the worst-case scenario, you will get an error message from Python, which is usually very informative and tell you what exactly you did wrong.

</exercise>

<exercise id="7" title="Acknowledgments">

* Thanks to [Natasha](https://twitter.com/_apfeltasha) for creating an amazing logo for the website.
* Thanks to [Ines Montani](https://twitter.com/_inesmontani) for providing the [website template](https://github.com/ines/course-starter-python) for the course.
* Thanks to researchers who are making their data and articles publicly available.
* Thanks to everyone who is making the knowledge freely accessible.
* And thank you for participating in the course.

</exercise>
