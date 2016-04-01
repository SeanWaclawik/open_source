## Lab 7 - Scientific Computation 3/25/2016

- One/Two page slide presentation of your project and post your slide in RCOS class channel #csci2963-01

###[link here](https://docs.google.com/presentation/d/19yFc4ZK7H81wID0rD5aqw-f_UnLK0qGLjN7Kk4QWxYo/edit?usp=sharing)

- Graphs and Networks are ubiquitous in Scientific Computations. Networkx is an open source python package located here https://networkx.github.io/

- A nice tutorial may be found in https://networkx.github.io/documentation/latest/_downloads/networkx_tutorial.pdf

- Your task for this class is to use networkx to do graph theoretic/network computations.

Please do the following problems.

- Download and Install networkx and download install matplotlib http://matplotlib.org/ 

```bash

sudo apt-get install python-networkx python-matplotlib

```

- Investigate networkx using examples in https://networkx.github.io/documentation/latest/_downloads/networkx_tutorial.pdf (use this as a reference as you continue)

- Stanford Graphbase is a book written by Prof. Donald Knuth and contains many interesting examples on graph algorithms and implementations of programs (written in literate programming style). [Here is an abstract of that book](http://tex.loria.fr/sgb/abstract.pdf) - [Dr. Goldschmidt Master's thesis](http://www.cs.rpi.edu/research/groups/pb/jgb/Masters.pdf) is a Java implementation.  These problems are also implemented in networkx.

- Implement the [word ladder game]( https://en.wikipedia.org/wiki/Word_ladder) and its variations. (The algorithmic idea behind this
problem is the shortest path algorithm implemented in networkx) [This link](https://github.com/networkx/networkx/blob/master/examples/graph/words.py) provides  a word ladder implementation - [Another implementation (simpler but slower) is here](http://www.csie.ntu.edu.tw/~azarc/sna/networkx/examples/graph/words.py). You can find 
[input data (for words of length five ) is here]( https://www.csie.ntu.edu.tw/~azarc/sna/networkx/examples/graph/) under words.da.txt.gz or use this [direct link]( http://www.cs.rpi.edu/research/groups/pb/jgb/java/words.dat).
[Words of length four are here](http://www.cs.rpi.edu/research/groups/pb/jgb/java/words4.dat) (Do the problem  "words of length 4 and words of length 5 --  {W_n | len(w) =n} and W_4, W_5 )


- Test your word ladder with the following words
    1.   `chaos` to `order`
    2.   `nodes` to `graph`
    3.   `moron` to `smart`
    4.   `pound` to `marks`


###Result:
>'Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ in one letter.
Graph has 5757 nodes with 14135 edges
853 connected components
>
>
Shortest path between chaos and order is
chaos
chats
coats
colts
colas
codas
codes
coder
cider
eider
elder
older
order

>
>
Shortest path between nodes and graph is
nodes
modes
moles
molds
golds
goads
grads
grade
grape
graph

>
>
Shortest path between moron and smart is
moron
boron
baron
caron
capon
capos
capes
canes
banes
bands
bends
beads
bears
sears
stars
start
smart
>
>
Shortest path between pound and marks is
None'
>


-   [For four letter words try 
cold to warm , love to hate]( http://wordplay.blogs.nytimes.com/2013/06/19/climb-the-ladder/ )

###Result:
>
Loaded words4.dat containing four-letter English words.
Two words are connected if they differ in one letter.
Graph has 2174 nodes with 8040 edges
129 connected components
>
>
Shortest path between cold and warm is
cold
cord
word
worm
warm
>
>
Shortest path between love and hate is
love
hove
have
hate
>

-  Implement a variation where we consider two words (nodes) are adjacent if the number of letters that differ (not necessarily in same position) by 1. (You need to the change the edit_distance function). Repeat with the same data.
(use multiset from collection)

An example:
```
Shortest path between chaos and order is
chaos
echos
chore
coder
order
```

> 
###Result
Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ by one letter anywhere.
 ***USING OTHER***
Graph has 5757 nodes with 112278 edges
16 connected components
>
>
Shortest path between chaos and order is
chaos
echos
chore
decor
order
>
>
Shortest path between nodes and graph is
nodes
snore
snare
apers
grape
graph
>
>
Shortest path between moron and smart is
moron
moors
morts
smart
>
>
Shortest path between pound and marks is
pound
sound
modus
drums
mrads
marks
>




- Create/fork a github repository for your project and work on your first commit

###[link here](https://github.com/SeanWaclawik/courseproject.git)
