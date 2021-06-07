from tkinter import *
from PIL import ImageTk, Image
import sqlite3



root = Tk()
root.title("Tkinter databases1")
root.geometry("400x400")

#create or connect to database
conn = sqlite3.connect('address_book.db') 

c = conn.cursor() #cursor instance created

'''
#create a table
c.execute("""CREATE TABLE addresses (
		first_name text, 
		last_name text,
		address text,
		city text,
		county text,
		postcode text
		)""")

''' #don't create it each time you run!

#submit function submit text boxes to a table in db
def submit():
	conn = sqlite3.connect('address_book.db') #connect to db
	c = conn.cursor() #create cursor
	#insert into table of db, see dummy variable :f_name etc
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :county, :postcode)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'county': county.get(),
				'postcode': postcode.get()

			})


	conn.commit()
	conn.close() #commit and close db
	#clear boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	county.delete(0, END)
	postcode.delete(0, END)

#query function
def query():
	conn = sqlite3.connect('address_book.db') #connect to db
	c = conn.cursor() #create cursor
	#query the database, oid for primary sqlite id
	c.execute("SELECT *, oid FROM addresses")
	#c.fetchone()
	#c.fetchmany()
	#c.fetchall()
	records = c.fetchall()
	#print(records) #came back as list with tuples inside, tuples being each record in the table
	
	#loop thru results
	print_records = ''
	for record in records:
		#print_records += str(record) + "\n" #so if we want just first name could go with str(record[0])
		print_records += str(record[0]) + " " + str(record[1]) + "\t " + str(record[6]) + "\n" # or mix them like this to show just two of the fields from record

	#make a tkinter label to display
	query_label = Label(root, text=print_records)
	query_label.grid(row=14, column=0, columnspan=2)


	conn.commit()
	conn.close() #commit and close db
	
#delete function by searching via oid (sqlite id which is record[6])
def delete():
	conn = sqlite3.connect('address_book.db') #connect to db
	c = conn.cursor() #create cursor

	#delete record
	c.execute("DELETE from addresses WHERE oid=" +delete_box.get()) #according to oid, could have done f_name etc. instead but unwise
	# want a box and a button to get id and then execute command but not in this function

	conn.commit()
	conn.close() #commit and close db


#do update for edit record i.e. write the new record to database
def doupdate():
	conn = sqlite3.connect('address_book.db') #connect to db
	c = conn.cursor() #create cursor

	#get the record_id from the select ID box in root window

	record_id = delete_box.get()

	c.execute(""" UPDATE addresses SET 
		first_name =:first,
		last_name =:last,
		address =:address,
		city =:city,
		county =:county,
		postcode =:postcode

		WHERE oid = :oid""",
		#dictionary
		{
		'first': f_name_editor.get(),
		'last': l_name_editor.get(),
		'address': address_editor.get(),
		'city': city_editor.get(),
		'county': county_editor.get(),
		'postcode': postcode_editor.get(),
		'oid': record_id



		})

	

	conn.commit()
	conn.close() #commit and close db
	#destroy window
	editor.destroy()




	
#edit a record function

def update():
	conn = sqlite3.connect('address_book.db') #connect to db
	c = conn.cursor() #create cursor

	#create global variables so can use in doupdate function
	global editor #so we can destroy window in doupdate
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global county_editor
	global postcode_editor


	#new window here
	editor = Tk()
	editor.title("Update records")
	editor.geometry("500x500")

	#so we need all the text boxes and their labels again!
	#create the text boxes
	#note they are not in root window, but the new editor window created just above
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0)) 

	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=1, column=1, padx=20)

	address_editor = Entry(editor, width=30)
	address_editor.grid(row=2, column=1, padx=20)

	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1, padx=20)

	county_editor = Entry(editor, width=30)
	county_editor.grid(row=4, column=1, padx=20)

	postcode_editor = Entry(editor, width=30)
	postcode_editor.grid(row=5, column=1, padx=20)

	f_name_label = Label(editor, text="First Name:")
	f_name_label.grid(row=0, column=0, pady=(10,0))

	l_name_label = Label(editor, text="Last Name:")
	l_name_label.grid(row=1, column=0)

	address_label = Label(editor, text="Address:")
	address_label.grid(row=2, column=0)

	city_label = Label(editor, text="City:")
	city_label.grid(row=3, column=0)

	county_label = Label(editor, text="County:")
	county_label.grid(row=4, column=0)

	postcode_label = Label(editor, text="Post code:")
	postcode_label.grid(row=5, column=0)

	#need a save button now

	save_btn = Button(editor, text="Save updated record to the database", command=doupdate) #use the doupdate function
	save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

	# want to propogate the text boxes with data from the record we selected to edit!


	record_id = delete_box.get() #get the record idea from the box in the root window

	c.execute("SELECT *, oid FROM addresses WHERE oid = " +record_id) #select the record
	#c.fetchone()
	#c.fetchmany()
	#c.fetchall()

	records = c.fetchall()
	#print(records) #came back as list with tuples inside, tuples being each record in the table
	
	#loop thru results and insert to the boxes
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		county_editor.insert(0, record[4])
		postcode_editor.insert(0, record[5])


	conn.commit()
	conn.close() #commit and close db




############

#create the text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0)) 

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

county = Entry(root, width=30)
county.grid(row=4, column=1, padx=20)

postcode = Entry(root, width=30)
postcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1)

#make some text box labels

f_name_label = Label(root, text="First Name:")
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root, text="Last Name:")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address:")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City:")
city_label.grid(row=3, column=0)

county_label = Label(root, text="County:")
county_label.grid(row=4, column=0)

postcode_label = Label(root, text="Post code:")
postcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="ID # to select:")
delete_box_label.grid(row=10, column=0)


#button to add text from the boxes to the database

submit_btn = Button(root, text="Add record to the database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#button to query the db

query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


#button to delete a record from db

delete_btn = Button(root, text="Delete a record", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

#button to update records

update_btn = Button(root, text="Update a record", command=update)
update_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)







conn.commit() #commit changes to db

conn.close() # close connection to db

root.mainloop()