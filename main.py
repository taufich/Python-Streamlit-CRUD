import psycopg2
import streamlit as st


# Connecting to database

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="admin",
    database="python_crud"
)

myCursor = mydb.cursor()
print("Connection Good!")




# Streamlit App Creation


def main():
    st.title("CRUD Operation with POSTGRES")
    
    #sidebar option selector
    option = st.sidebar.selectbox("Select an Option",("Create","Read","Update","Delete"))

    #Perform selected operation

    if option == "Create":
        st.subheader("Create a record")

        name = st.text_input("Name")
        email = st.text_input("Email")

        if st.button("Create"):
            query = "INSERT INTO app_users (name,email) VALUES (%s,%s)"
            val = (name, email)
            myCursor.execute(query,val)
            mydb.commit()

            st.success("Record Created")
            option == "Read"






    elif option == "Read":
        st.subheader("Read a record")
        myCursor.execute("SELECT * FROM app_users")
        result = myCursor.fetchall()
        st.dataframe(result)
        





    elif option == "Update":
        st.subheader("Update a record")
        id = st.number_input("Enter Record Id", min_value=1)

        name = st.text_input("Enter New Name")
        email = st.text_input("Enter New Email")

        if st.button("Update"):
            query = "UPDATE app_users SET name = %s, email = %s WHERE id = %s"
            val = (name, email, id)
            myCursor.execute(query,val)
            mydb.commit()

            st.success("Record Updated")





    elif option == "Delete":
        st.subheader("Delete a record")
        id = st.number_input("Enter Record Id", min_value=1)
        
        if st.button("Delete"):
           query = "DELETE FROM app_users WHERE id = %s"
           val = (id,)
           myCursor.execute(query,val)
           mydb.commit()

           st.success("Record Deleted")










if __name__ == "__main__":
    main()
