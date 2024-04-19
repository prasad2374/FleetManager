import streamlit as st
import mysql.connector

# Database connection
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Prasad@2374",
    database="fleet_manager_db"
)
cursor = db_connection.cursor()

# Function to add a new vehicle
def add_vehicle(license_plate, make, model, year, mileage, status):
    insert_query = "INSERT INTO Vehicles (LicensePlate, Make, Model, Year, Mileage, Status) VALUES (%s, %s, %s, %s, %s, %s)"
    vehicle_data = (license_plate, make, model, year, mileage, status)
    cursor.execute(insert_query, vehicle_data)
    db_connection.commit()
    st.success('Vehicle added successfully!')

# Function to update a vehicle
def update_vehicle(license_plate, make, model, year, mileage, status):
    update_query = "UPDATE Vehicles SET Make=%s, Model=%s, Year=%s, Mileage=%s, Status=%s WHERE LicensePlate=%s"
    vehicle_data = (make, model, year, mileage, status, license_plate)
    cursor.execute(update_query, vehicle_data)
    db_connection.commit()
    st.success('Vehicle updated successfully!')

# Function to search for vehicles
def search_vehicle(make):
    search_query = "SELECT * FROM Vehicles WHERE Make=%s"
    cursor.execute(search_query, (make,))
    results = cursor.fetchall()
    return results

# Function to delete a vehicle
def delete_vehicle(license_plate):
    delete_query = "DELETE FROM Vehicles WHERE LicensePlate=%s"
    cursor.execute(delete_query, (license_plate,))
    db_connection.commit()
    st.warning('Vehicle deleted!')

# Function to add a new driver
# Function to add a new driver
# Function to add a new driver
# Function to add a new driver
def add_driver(first_name, last_name, license_number, contact_number, email):
    try:
        insert_query = "INSERT INTO Drivers (FirstName, LastName, LicenseNumber, ContactNumber, Email) VALUES (%s, %s, %s, %s, %s)"
        driver_data = (first_name, last_name, license_number, contact_number, email)
        cursor.execute(insert_query, driver_data)
        db_connection.commit()
        st.success('Driver added successfully!')
    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")



# Function to update a driver
def update_driver(driver_id, first_name, last_name, license_number, contact_number, email):
    update_query = "UPDATE Drivers SET FirstName=%s, LastName=%s, LicenseNumber=%s, ContactNumber=%s, Email=%s WHERE DriverID=%s"
    driver_data = (first_name, last_name, license_number, contact_number, email, driver_id)
    cursor.execute(update_query, driver_data)
    db_connection.commit()
    st.success('Driver updated successfully!')

# Function to search for drivers
def search_driver(last_name):
    search_query = "SELECT * FROM Drivers WHERE LastName=%s"
    cursor.execute(search_query, (last_name,))
    results = cursor.fetchall()
    return results

# Function to delete a driver
def delete_driver(driver_id):
    delete_query = "DELETE FROM Drivers WHERE DriverID=%s"
    cursor.execute(delete_query, (driver_id,))
    db_connection.commit()
    st.warning('Driver deleted!')

# Function to add a new trip
def add_trip(vehicle_id, driver_id, start_location, end_location, start_time, end_time, distance, fuel_used, cost):
    insert_query = "INSERT INTO Trips (VehicleID, DriverID, StartLocation, EndLocation, StartTime, EndTime, Distance, FuelUsed, Cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    trip_data = (vehicle_id, driver_id, start_location, end_location, start_time, end_time, distance, fuel_used, cost)
    cursor.execute(insert_query, trip_data)
    db_connection.commit()
    st.success('Trip added successfully!')

# Function to search for trips
def search_trip(location):
    search_query = "SELECT * FROM Trips WHERE StartLocation LIKE %s OR EndLocation LIKE %s"
    location_pattern = f'%{location}%'
    cursor.execute(search_query, (location_pattern, location_pattern))
    results = cursor.fetchall()
    return results

# Streamlit app
def main():
    st.title('Fleet Manager App')

    # Sidebar
    st.sidebar.title('Menu')
    menu_option = st.sidebar.selectbox('Select Option', ('Add Vehicle', 'Update Vehicle', 'Delete Vehicle', 'Search Vehicle', 'Add Driver', 'Update Driver', 'Delete Driver', 'Search Driver', 'Add Trip', 'Search Trip'))

    if menu_option == 'Add Vehicle':
        st.subheader('Add New Vehicle')
        license_plate = st.text_input('License Plate')
        make = st.text_input('Make')
        model = st.text_input('Model')
        year = st.number_input('Year', min_value=1900, max_value=2050)
        mileage = st.number_input('Mileage')
        status = st.text_input('Status')
        if st.button('Add'):
            add_vehicle(license_plate, make, model, year, mileage, status)

    elif menu_option == 'Update Vehicle':
        st.subheader('Update Vehicle Details')
        license_plate = st.text_input('Enter License Plate')
        make = st.text_input('Make')
        model = st.text_input('Model')
        year = st.number_input('Year', min_value=1900, max_value=2050)
        mileage = st.number_input('Mileage')
        status = st.text_input('Status')
        if st.button('Update'):
            update_vehicle(license_plate, make, model, year, mileage, status)

    elif menu_option == 'Delete Vehicle':
        st.subheader('Delete Vehicle')
        license_plate = st.text_input('Enter License Plate to delete')
        if st.button('Delete'):
            delete_vehicle(license_plate)

    elif menu_option == 'Search Vehicle':
        st.subheader('Search Vehicle')
        make = st.text_input('Enter Make to search')
        if st.button('Search'):
            results = search_vehicle(make)
            if results:
                st.write('Search Results:')
                for result in results:
                    st.write(f"License Plate: {result[1]}, Make: {result[2]}, Model: {result[3]}, Year: {result[4]}, Mileage: {result[5]}, Status: {result[6]}")
            else:
                st.warning('No vehicles found.')

    elif menu_option == 'Add Driver':
        st.subheader('Add New Driver')
        first_name = st.text_input('First Name')
        last_name = st.text_input('Last Name')
        license_number = st.text_input('License Number')
        contact_number = st.text_input('Contact Number')
        email = st.text_input('Email')
        if st.button('Add'):
            add_driver(first_name, last_name, license_number, contact_number, email)

    elif menu_option == 'Update Driver':
        st.subheader('Update Driver Details')
        driver_id = st.number_input('Enter Driver ID')
        first_name = st.text_input('First Name')
        last_name = st.text_input('Last Name')
        license_number = st.text_input('License Number')
        contact_number = st.text_input('Contact Number')
        email = st.text_input('Email')
        if st.button('Update'):
            update_driver(driver_id, first_name, last_name, license_number, contact_number, email)

    elif menu_option == 'Delete Driver':
        st.subheader('Delete Driver')
        driver_id = st.number_input('Enter Driver ID to delete')
        if st.button('Delete'):
            delete_driver(driver_id)

    elif menu_option == 'Search Driver':
        st.subheader('Search Driver')
        last_name = st.text_input('Enter Last Name to search')
        if st.button('Search'):
            results = search_driver(last_name)
            if results:
                st.write('Search Results:')
                for result in results:
                    st.write(f"Driver ID: {result[0]}, First Name: {result[1]}, Last Name: {result[2]}, License Number: {result[3]}, Contact Number: {result[4]}, Email: {result[5]}")
            else:
                st.warning('No drivers found.')

    elif menu_option == 'Add Trip':
        st.subheader('Add New Trip')
        vehicle_id = st.number_input('Vehicle ID')
        driver_id = st.number_input('Driver ID')
        start_location = st.text_input('Start Location')
        end_location = st.text_input('End Location')
        start_time = st.text_input('Start Time')
        end_time = st.text_input('End Time')
        distance = st.number_input('Distance')
        fuel_used = st.number_input('Fuel Used')
        cost = st.number_input('Cost')
        if st.button('Add'):
            add_trip(vehicle_id, driver_id, start_location, end_location, start_time, end_time, distance, fuel_used, cost)

    elif menu_option == 'Search Trip':
        st.subheader('Search Trip')
        location = st.text_input('Enter Location to search')
        if st.button('Search'):
            results = search_trip(location)
            if results:
                st.write('Search Results:')
                for result in results:
                    st.write(f"Trip ID: {result[0]}, Vehicle ID: {result[1]}, Driver ID: {result[2]}, Start Location: {result[3]}, End Location: {result[4]}, Start Time: {result[5]}, End Time: {result[6]}, Distance: {result[7]}, Fuel Used: {result[8]}, Cost: {result[9]}")
            else:
                st.warning('No trips found.')

if __name__ == '__main__':
    main()
