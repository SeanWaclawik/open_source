#WORD LADDER V 1.30

import networkx as nx
import re
import collections


USE_OTHER=False


def generate_graph(words):
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    lookup = dict((c,lowercase.index(c)) for c in lowercase)
    def edit_distance_one(word):
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i+1:]
            j = lookup[c] # lowercase.index(c)
            for cc in lowercase[j+1:]:
                yield left + cc + right
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G

def words_graph():
    import gzip
    fh=gzip.open('words_dat.txt.gz','r')
    words=set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w=str(line[0:5])
        words.add(w)
    
    if USE_OTHER:
	G = generate_graph(words)
	other_dist_def(G)
	return G
    
    return generate_graph(words)


def four_words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    import gzip
    fh=open('words4.dat','r')
    words=set()
    i = 0
    for line in fh.readlines():
        
        w=str(line[0:4])

        #if (i==0):
            #print "################\n\t w == %s \n################" %w
        
        if ( re.search(r"[*]", w) ):
            continue
        
        words.add(w)
        
    #print "################\n\t i == %d \n################" %i
    return generate_graph(words)

def other_dist_def(G):
    words = G.nodes()
    for i in range(0, networkx.number_of_nodes(G)):
	
	    for j in range(i + 1, networkx.number_of_nodes(G)):
		    A = collections.Counter(sorted(words[i]))
		    B = collections.Counter(sorted(words[j]))

		    if sum((A - B).values()) == 1:
			    G.add_edge(words[i], words[j])
	    
    

if __name__ == '__main__':
    from networkx import *
    G=words_graph()
    print("Loaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          %(number_of_nodes(G),number_of_edges(G)))
    print("%d connected components" % number_connected_components(G))

    for (source,target) in [('chaos','order'),
                            ('nodes','graph'),
                            ('moron', 'smart'),
                            ('pound','marks')]:
        print("Shortest path between %s and %s is"%(source,target))
        try:
            sp=shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")



    ####### four letter normal #######
    
    
    G=four_words_graph()
    print("\n\nLoaded words4.dat containing four-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          %(number_of_nodes(G),number_of_edges(G)))
    print("%d connected components" % number_connected_components(G))

    for (source,target) in [('cold','warm'),
                            ('love','hate')]:
        print("Shortest path between %s and %s is"%(source,target))
        try:
            sp=shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")

    ######  other dist / five letter #######
    #turn on other
    USE_OTHER=True
    
    G=words_graph()

    
    print("\n\nLoaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ by one letter anywhere.\n ***USING OTHER***")
    print("Graph has %d nodes with %d edges"
    
          %(number_of_nodes(G),number_of_edges(G)))
    print("%d connected components" % number_connected_components(G))

    for (source,target) in [('chaos','order'),
                            ('nodes','graph'),
                            ('moron', 'smart'),
                            ('pound','marks')]:
	print("Shortest path between %s and %s is"%(source,target))
	try:
	    sp=shortest_path(G, source, target)
	    for n in sp:
		print(n)
	except nx.NetworkXNoPath:
	    print("None")	


'''
    References
            ----------
            .. [1] Donald E. Knuth,
               "The Stanford GraphBase: A Platform for Combinatorial Computing",
               ACM Press, New York, 1993.
            .. [2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html
            """
            # Authors: Aric Hagberg (hagberg@lanl.gov),
            #          Brendt Wohlberg,
            #          hughdbrown@yahoo.com
            
            #    Copyright (C) 2004-2016 by
            #    Aric Hagberg <hagberg@lanl.gov>
            #    Dan Schult <dschult@colgate.edu>
            #    Pieter Swart <swart@lanl.gov>
            #    All rights reserved.
            #    BSD license.
	    
'''
