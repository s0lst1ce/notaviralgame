The goal of the game is to create the biggest possible botnet.

The game surface is made up of multiple nodes (circles). Some are connected (lines) while some aren’t. *if we have time we could handle connect/disconnect mechanisms*

You infect a node by LMB (=Left Mouse Button) on it. The first you infect always works (it’s your computer). 

You can only infect a node that has a direct connection to an infected node.

When you infect a node you are not guaranteed to succeed. Your chances grow with the number of infected node connected to your target.

Upon failure you:

- do not get to infect your target
- have a chance for the nodes which tried to infect the target to be blacklisted (=unable to pass proxies)





Some are protected by a proxy that protects against known infected.





            index = rects.index(elem)
            rects.pop(index)
            nodes.pop(index)