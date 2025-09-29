from tkinter import *
import tkintermapview
import psycopg2

# create tkinter window
root_tk = Tk()
root_tk.title("Najbliža benzinska postaja")
root_tk.geometry(f"{1500}x{1500}")

def submit():
    
    conn = psycopg2.connect(database = "sampledb",
                        host = "localhost",
                        user = "postgres",
                        password = "123456",
                        port = "5432")

    c = conn.cursor()

    t1 = enter.get().split(" ")

    c.execute('INSERT INTO tocka VALUES (1, ST_Point(%s, %s))', t1)
    
    
                
    # Commit Changes  
    conn.commit()
    # Close Connection
    conn.close()

    enter.delete(0, END)

# Insert function
def query():
    conn = psycopg2.connect(database = "sampledb",
                        host = "localhost",
                        user = "postgres",
                        password = "123456",
                        port = "5432")

    c = conn.cursor()
    
    c.execute("""SELECT naziv, adresa
                FROM test as one
                WHERE ST_DWITHIN(points, (SELECT points FROM tocka WHERE id = '1'), 5000)""")

    records = c.fetchall()
    #print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " , " + str(record[1]) + "\n"

    query_label = Label(root_tk, text=print_records)
    query_label.grid(row=200, column=10, columnspan=2, padx=80, pady=150)

    conn.commit()
    conn.close()

# Create Function To Delete A Record
def delete():
    conn = psycopg2.connect(database = "sampledb",
                    host = "localhost",
                    user = "postgres",
                    password = "123456",
                    port = "5432")

    c = conn.cursor()

    c.execute("DELETE FROM tocka")

    # Commit Changes  
    conn.commit()
    # Close Connection
    conn.close()


# Create Button For Coorinates
btn = Button(root_tk, text ="Dodaj koordinate u bazu", command=submit)
btn.grid(row=0, column=150, padx=10, pady=10, ipadx=5)
enter = Entry(root_tk, width=50, borderwidth=5, justify=LEFT)
enter.grid(row=1, column=150, padx=10, pady=10,ipadx=10 )
coordinates = Label(root_tk, text="X i Y koordinate", justify=LEFT)
coordinates.grid(row=1, column=51, pady=10, padx=50, ipadx=50)

# Create Button For Delete Coorinates
btn = Button(root_tk, text ="Izbriši koordinate iz baze", command=delete)
btn.grid(row=0, column=51, padx=8, pady=10)

# Create Button For Comparison
btn = Button(root_tk, text ="Najbliža benzinska postaja", command=query)
btn.grid(row=2, column=150, padx=10, pady=10, ipadx=10)


# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=780, height=600, corner_radius=0)
map_widget.place(relx=0.47, rely=0.54, anchor=W)

# set current widget position and zoom
marker_1 = map_widget.set_position(43.52589, 16.47534, text="Split")  # Split, Croatia

def add_marker_event(coords):
    print(coords)

    new_marker = map_widget.set_marker(coords[0], coords[1])

    

map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)

def left_click_event(coordinates_tuple):
        print("Left click event with coordinates:", coordinates_tuple)

map_widget.add_left_click_map_command(left_click_event)

map_widget.set_zoom(12)

root_tk.mainloop()
