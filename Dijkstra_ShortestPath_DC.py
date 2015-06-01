# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:33:36 2015

@author: Josh New
"""

import networkx as nx
import time

def dijkstra_short_path(graph, start, target):
 
    time_start = time.time()

    start = start
    target = target
    
    unsolved = list(g.nodes())
    unsolved.remove(start)
    solved = []
    path = {}
    distance = {}
    start_nodes = g[start].keys()
        
    for i in start_nodes:
            path[i] = {}    
            weight = g[start][i]["weight"]
            distance[i] = weight
            path[i].update({start:weight})
            solved.append(i)
            unsolved.remove(i)
        
    
    count = 0
    while count < 35:
    
        for i in unsolved:
                path[i] = {}   
                foo = set(g.neighbors(i))
                for j in foo:
                        try:
                            dist = g[i][j]["weight"] + distance[j]
                            path[i].update({j:dist})
                        except KeyError:
                               continue
                try:
                    distance[i] = min(path[i].values())
                except ValueError:
                    continue
         
        count = count + 1 
        
    short_path_length = min(path[target].values(), key = path[target].get)
        
    print "The shortest path from your start position to the target is", short_path_length
        
    short_path = [target]
    path_target = target
        
    finished = False
    while not finished:
            ping = path_target
            pong = min(path[ping], key = path[ping].get)
            path_target = pong
            short_path.append(pong)
            finished = start in short_path
        
    print "The shortest path from the target to your start node is", short_path
    
    end = time.time() - time_start
    
    print "This algortihm took", end, "seconds"
        

##########Sample implemenations of function

g = nx.read_weighted_edgelist(path = "DC.txt", nodetype = int)



dijkstra_short_path(g,0,8000)
nx.dijkstra_path_length(g,0,8000)


dijkstra_short_path(g,12,9000)
nx.dijkstra_path_length(g,12,9000)

dijkstra_short_path(g,100,8500)
nx.dijkstra_path_length(g,100,8500)

dijkstra_short_path(g,153,2345)
dijkstra_short_path(g,224,1000)
dijkstra_short_path(g,314,567)
dijkstra_short_path(g,1000,7546)
dijkstra_short_path(g,0,256)
dijkstra_short_path(g,10,1257)
dijkstra_short_path(g,5,6432)
dijkstra_short_path(g,24,976)
dijkstra_short_path(g,168,8577)