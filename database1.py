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
	query_label.grid(row=12, column=0, columnspan=2)


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

delete_box_label = Label(root, text="ID # to delete:")
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








conn.commit() #commit changes to db

conn.close() # close connection to db

root.mainloop()