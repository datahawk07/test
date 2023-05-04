import tkinter as tk
import cx_Oracle

# Connect to the Oracle database
conn = cx_Oracle.connect("system/Charan@14@localhost:1521/orcl")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a Tkinter window
window = tk.Tk()
window.title("Courier Management System")

def insert_order():
    # Retrieve the data from the input fields
    order_id = order_id_input.get()
    customer_name = customer_name_input.get()
    customer_address = customer_address_input.get()
    recipient_name = recipient_name_input.get()
    recipient_address = recipient_address_input.get()
    order_date = order_date_input.get()
    expected_delivery_date = expected_delivery_date_input.get()
    # Insert the data into the Orders table
    cursor.execute(f"INSERT INTO Orders (order_id, customer_name, customer_address, recipient_name, recipient_address, order_date, expected_delivery_date) VALUES ({order_id}, '{customer_name}', '{customer_address}', '{recipient_name}', '{recipient_address}', TO_DATE('{order_date}', 'YYYY-MM-DD'), TO_DATE('{expected_delivery_date}', 'YYYY-MM-DD'))")
    conn.commit()
    # Clear the input fields
    order_id_input.delete(0, tk.END)
    customer_name_input.delete(0, tk.END)
    customer_address_input.delete(0, tk.END)
    recipient_name_input.delete(0, tk.END)
    recipient_address_input.delete(0, tk.END)
    order_date_input.delete(0, tk.END)
    expected_delivery_date_input.delete(0, tk.END)

# Define the function to update an existing order
def update_order():
    # Retrieve the data from the input fields
    order_id = order_id_input.get()
    customer_name = customer_name_input.get()
    customer_address = customer_address_input.get()
    recipient_name = recipient_name_input.get()
    recipient_address = recipient_address_input.get()
    order_date = order_date_input.get()
    expected_delivery_date = expected_delivery_date_input.get()
    # Update the data in the Orders table
    cursor.execute(f"UPDATE Orders SET customer_name = '{customer_name}', customer_address = '{customer_address}', recipient_name = '{recipient_name}', recipient_address = '{recipient_address}', order_date = TO_DATE('{order_date}', 'YYYY-MM-DD'), expected_delivery_date = TO_DATE('{expected_delivery_date}', 'YYYY-MM-DD') WHERE order_id = {order_id}")
    conn.commit()
    # Clear the input fields
    order_id_input.delete(0, tk.END)
    customer_name_input.delete(0, tk.END)
    customer_address_input.delete(0, tk.END)
    recipient_name_input.delete(0, tk.END)
    recipient_address_input.delete(0, tk.END)
    order_date_input.delete(0, tk.END)
    expected_delivery_date_input.delete(0, tk.END)

# Define the function to delete an existing order
def delete_order():
    # Retrieve the data from the input field
    order_id = order_id_input.get()
    # Delete the data from the Orders table
    cursor.execute(f"DELETE FROM Orders WHERE order_id = {order_id}")
    conn.commit()
    # Clear the input field
    order_id_input.delete(0, tk.END)

def insert_delivery():
    # Retrieve the data from the input fields
    delivery_id = delivery_id_input.get()
    order_id = order_id_input.get()
    courier_name = courier_name_input.get()
    delivery_date = delivery_date_input.get()
    delivery_status = delivery_status_input.get()
    cursor.execute("INSERT INTO deliveries VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)", (delivery_id, order_id, courier_name, delivery_date, delivery_status))    
    conn.commit()
    # Clear the input fields
    order_id_input.delete(0, tk.END)
    courier_name_input.delete(0, tk.END)
    delivery_date_input.delete(0, tk.END)
    delivery_status_input.delete(0, tk.END)

# Define the function to update an existing delivery
def update_delivery():
    # Retrieve the data from the input fields
    delivery_id = delivery_id_input.get()
    courier_name = courier_name_input.get()
    delivery_date = delivery_date_input.get()
    delivery_status = delivery_status_input.get()
    # Update the data in the Deliveries table
    cursor.execute(f"UPDATE Deliveries SET courier_name = '{courier_name}', delivery_date = TO_DATE('{delivery_date}', 'YYYY-MM-DD'), delivery_status = '{delivery_status}' WHERE delivery_id = {delivery_id}")
    conn.commit()
    # Clear the input fields
    delivery_id_input.delete(0, tk.END)
    courier_name_input.delete(0, tk.END)
    delivery_date_input.delete(0, tk.END)
    delivery_status_input.delete(0, tk.END)

# Define the function to delete an existing delivery
def delete_delivery():
    # Retrieve the data from the input field
    delivery_id = delivery_id_input.get()
    # Delete the data from the Deliveries table
    cursor.execute(f"DELETE FROM Deliveries WHERE delivery_id = {delivery_id}")
    conn.commit()
    # Clear the input field
    delivery_id_input.delete(0, tk.END)

# Define the function to display the orders
def display_orders():
    # Retrieve the data from the Orders table
    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()
    # Display the data in the output field
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, "Orders:\n")
    for order in orders:
        output_field.insert(tk.END, f"Order ID: {order[0]}\nCustomer Name: {order[1]}\nCustomer Address: {order[2]}\nRecipient Name: {order[3]}\nRecipient Address: {order[4]}\nOrder Date: {order[5]}\nExpected Delivery Date: {order[6]}\n\n")

# Define the function to display the deliveries
def display_deliveries():
    # Retrieve the data from the Deliveries table
    cursor.execute("SELECT * FROM Deliveries")
    deliveries = cursor.fetchall()
    # Display the data in the output field
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, "Deliveries:\n")
    for delivery in deliveries:
        output_field.insert(tk.END, f"Delivery ID: {delivery[0]}\nOrder ID: {delivery[1]}\nCourier Name: {delivery[2]}\nDelivery Date: {delivery[3]}\nDelivery Status: {delivery[4]}\n\n")

# Define the input fields for orders
order_id_label = tk.Label(window, text="Order ID:")
order_id_input = tk.Entry(window)
customer_name_label = tk.Label(window, text="Customer Name:")
customer_name_input = tk.Entry(window)
customer_address_label = tk.Label(window, text="Customer Address:")
customer_address_input = tk.Entry(window)
recipient_name_label = tk.Label(window, text="Recipient Name:")
recipient_name_input = tk.Entry(window)
recipient_address_label = tk.Label(window, text="Recipient Address:")
recipient_address_input = tk.Entry(window)
order_date_label = tk.Label(window, text="Order Date (YYYY-MM-DD):")
order_date_input = tk.Entry(window)
expected_delivery_date_label = tk.Label(window, text="Expected Delivery Date (YYYY-MM-DD):")
expected_delivery_date_input = tk.Entry(window)

# Define the input fields for deliveries
delivery_id_label = tk.Label(window, text="Delivery ID:")
delivery_id_input = tk.Entry(window)
order_id_label2 = tk.Label(window, text="Order ID:")
order_id_input2 = tk.Entry(window)
courier_name_label = tk.Label(window, text="Courier Name:")
courier_name_input = tk.Entry(window)
delivery_date_label = tk.Label(window, text="Delivery Date (YYYY-MM-DD):")
delivery_date_input = tk.Entry(window)
delivery_status_label = tk.Label(window, text="Delivery Status:")
delivery_status_input = tk.Entry(window)


add_order_button = tk.Button(window, text="Add Order", command=insert_order)
update_order_button = tk.Button(window, text="Update Order", command=update_order)
delete_order_button = tk.Button(window, text="Delete Order", command=delete_order)
display_orders_button = tk.Button(window, text="Display Orders", command=display_orders)
add_delivery_button = tk.Button(window, text="Add Delivery", command=insert_delivery)
update_delivery_button = tk.Button(window, text="Update Delivery", command=update_delivery)
delete_delivery_button = tk.Button(window, text="Delete Delivery", command=delete_delivery)
display_deliveries_button = tk.Button(window, text="Display Deliveries", command=display_deliveries)

# Add the widgets to the window
order_id_label.grid(row=0, column=0)
order_id_input.grid(row=0, column=1)
customer_name_label.grid(row=1, column=0)
customer_name_input.grid(row=1, column=1)
customer_address_label.grid(row=2, column=0)
customer_address_input.grid(row=2, column=1)
recipient_name_label.grid(row=3, column=0)
recipient_name_input.grid(row=3, column=1)
recipient_address_label.grid(row=4, column=0)
recipient_address_input.grid(row=4, column=1)
order_date_label.grid(row=5, column=0)
order_date_input.grid(row=5, column=1)
expected_delivery_date_label.grid(row=6, column=0)
expected_delivery_date_input.grid(row=6, column=1)

delivery_id_label.grid(row=0, column=2)
delivery_id_input.grid(row=0, column=3)
order_id_label2.grid(row=1, column=2)
order_id_input2.grid(row=1, column=3)
courier_name_label.grid(row=2, column=2)
courier_name_input.grid(row=2, column=3)
delivery_date_label.grid(row=3, column=2)
delivery_date_input.grid(row=3, column=3)
delivery_status_label.grid(row=4, column=2)
delivery_status_input.grid(row=4, column=3)


add_order_button.grid(row=8, column=0)
update_order_button.grid(row=8, column=1)
delete_order_button.grid(row=8, column=2)
display_orders_button.grid(row=8, column=3)
add_delivery_button.grid(row=9, column=0)
update_delivery_button.grid(row=9, column=1)
delete_delivery_button.grid(row=9, column=2)
display_deliveries_button.grid(row=9, column=3)

output_field = tk.Text(window, height=10, width=50)
output_field.grid(row=12, column=0, columnspan=8)

window.mainloop()


    