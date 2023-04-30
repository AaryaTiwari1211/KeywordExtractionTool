import matplotlib.pyplot as plt2

def graph_generator(key,freq):
    
    fig , ax = plt2.subplots(1,2 , figsize = (10,5))
    ax1 = ax[0]
    ax2 = ax[1]
    ax1.plot(key,freq)
    ax1.title.set_text("Line Visualization")
    for tick in ax1.get_xticklabels():
        tick.set_rotation(63)
    
    ax2.bar(key, freq, color='maroon', width=0.4)
    ax2.title.set_text("Bar Visualization")
    
    for tick2 in ax2.get_xticklabels():
        tick2.set_rotation(63)
        
    fig.savefig("media/images/graph.png")
