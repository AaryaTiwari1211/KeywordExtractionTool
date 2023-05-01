import matplotlib.pyplot as plt2

def graph_generator(key,freq):
    
    fig , ax = plt2.subplots(1,2 , figsize = (30,10))
    ax1 = ax[0]
    ax2 = ax[1]
    main_key = key[:30] + key[-30:]
    main_freq = freq[:30] + freq[-30:]
    ax1.plot(main_key,main_freq)

    ax1.title.set_text("Line Visualization")
    for tick in ax1.get_xticklabels():
        tick.set_rotation(90)
    
    ax2.bar(main_key,main_freq, color='blue', width=0.4)
    ax2.title.set_text("Bar Visualization")
    
    for tick2 in ax2.get_xticklabels():
        tick2.set_rotation(90)
    fig.savefig("media/images/graph.png")
