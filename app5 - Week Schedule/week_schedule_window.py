import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#import pickle

def show_plot(course_list, config):
    '''
    <config> signature: dictionary
    '''
    def show_figure(fig):

        # create a dummy figure and use its
        # manager to display "fig"  
        dummy = plt.figure(figsize=(12,6),constrained_layout=True)
        new_manager = dummy.canvas.manager
        new_manager.canvas.figure = fig
        fig.set_canvas(new_manager.canvas)


    fig = plt.figure(figsize=(12,6),facecolor='white')
    #ax = fig.add_axes([0.08,-0.4,0.9,1.7])
    ax = fig.add_axes([0.08,0,0.9,0.9])
    ax.set_xlim([0,180])
    ax.set_ylim([0,70])

    try:
        mat = np.loadtxt('mat.dat')
    except:
        mat = np.ones((70, 180))
    mat = np.ones((70, 180))    # added this line to stop reloading the <mat> data

    num_slots = [np.unique(mat).size - 1] # this is a single-element list. Because lists are mmutable
        # once we pass them to a fucntion, any change in them remain constant. However, if we use 
        # immutable objects like number, string, and tuples, any change in them leads to a new contaruction 
        # of the object
    print("num of courses %s" % num_slots[0])

    # try:
    #     fp = open('infor.pkl', 'rb')
    #     text_on_plot = pickle.load(fp)
    #     fp.close()
    # except:
    #     text_on_plot = {}
    text_on_plot = {} # added this line to stop reloading the <text_on_plo> data
    '''
    text_on_plot is dict:
    {'name_on_slot': [x_orig, y_orig]}
    '''

    def get_lims(i,j):
        x_lim = [10, 30]
        y_lim = [20, 30]
        start_time = float(course_list[i].slots[j][0])
        if start_time < 9 :
            x_lim[0] = (start_time+12)*20 - 180
        else:
            x_lim[0] = start_time*20 - 180
        end_time = float(course_list[i].slots[j][1])
        if end_time < 9 :
            x_lim[1] = (end_time+12)*20 - 180
        else:
            x_lim[1] = end_time*20 - 180
        dict_of_weekdays = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5,
                            'Saturday' : 6, 'Sunday': 7}
        day_of_week = dict_of_weekdays[course_list[i].slots[j][2]]
        y_lim[1] = day_of_week*10
        y_lim[0] = y_lim[1] - 10

        x_lim = list(map(int, x_lim))
        y_lim = list(map(int, y_lim))
        return x_lim , y_lim

    def add_subslot(mat,slot_text, slot_num, num_slots,i,j):
        x_lim , y_lim = get_lims(i,j)
        print("num of new course %s"%num_slots)
        text_on_plot[slot_text+'(%d)'%slot_num] = [x_lim[0]+4,y_lim[0]+4]
        for x in range(x_lim[0],x_lim[1]):
            for y in range(y_lim[0], y_lim[1]):
                mat[y,x] = (num_slots%7)/8.0 + 0.01

    def add_slot(mat,i, num_slots):
        slot_text = course_list[i].name
        num_sub_slots = len(course_list[i].slots)
        slot_num = 1
        for j in range(num_sub_slots):
            add_subslot(mat,slot_text, slot_num, num_slots[0],i,j)
            slot_num += 1
        num_slots[0] += 1
    def del_slot(i,j):
        nonlocal num_slots  
        x_lim , y_lim = get_lims(i,j)
        for names in text_on_plot.keys():
            if (text_on_plot[names][0]-4 == x_lim[0]) and (text_on_plot[names][1]-4 == y_lim[0]):
                del text_on_plot[names]
                break
        for x in range(x_lim[0],x_lim[1]):
            for y in range(y_lim[0], y_lim[1]):
                mat[y,x] = 1
        num_slots -= 1

    if config['clear_all'] == 1:
        mat = np.ones_like(mat)
        num_slots = 0
        text_on_plot = {}
    else:
        for name in config['del']:
            name
        for i in range(course_list.__len__()):
            add_slot(mat,i, num_slots)
        

    for names in text_on_plot.keys():
        ax.text(text_on_plot[names][0], text_on_plot[names][1], names)

    #print(text_on_plot)


    ax.imshow(mat, cmap='Set2', vmin=0, vmax=1)

    for i in range(1,7):
        ax.plot([0,180],[i*10,i*10], color='black')

    for i in range(1,9):
        ax.plot([i*20,i*20],[0,70],'--', color='#747574')

    ax.xaxis.set_major_locator(ticker.LinearLocator(10))

    ax.set_yticklabels(['','Monday','Tuesday','Wednesday','Thursday','Friday',
                        'Saturday','Sunday'], minor=False, rotation=45)



    ax.set_xticklabels(['9am','10am','11am','12pm','1pm','2pm','3pm','4pm','5pm',
                        '6pm'], minor=False, rotation=0)

    np.savetxt('mat.dat', mat)
    np.savetxt('info', np.array([num_slots]))
    plt.show()

    fig.savefig('fig.jpeg')

    # fp = open('FigureObject.fig.pickle', 'wb')
    # pickle.dump(fig, fp)
    # fp.close()
    # fp = open('infor.pkl', 'wb')
    # pickle.dump(text_on_plot, fp)
    # fp.close()

    return mat

