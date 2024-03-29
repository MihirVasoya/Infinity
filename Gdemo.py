import streamlit as st
import psycopg2
import pandas as pd
import google.generativeai as genai
import openai
# from openai import OpenAI



data=pd.read_csv("org.csv")

# st.write(data)

# conn = psycopg2.connect(
#             dbname="Infinity",
#             user="postgres",
#             password="Mihir@9199",
#             host="localhost",
#             port="5432"
#         )

# Function to check if student ID exists in the database
# def check_student_id(student_id):
#     try:
#         # Connect to the PostgreSQL database
        
        
#         # Create a cursor object
#         cursor = conn.cursor()

        

#         # Execute SQL query to check if student ID exists
#         cursor.execute("SELECT * FROM student WHERE sid = %s", (student_id,))
#         row = cursor.fetchone()


#         # Close cursor and connection
#         cursor.close()
#         conn.close()

#         # Return True if student ID exists, False otherwise
#         if row:
#             df = pd.DataFrame([row], columns=["S_id", "Probability", "Linear Algebra", "Chemistry","Physics","Biology","Social Science","mid"])  # Adjust column names as per your database schema
            
#             return True , df
           
#         else:
#             return False
#     except psycopg2.Error as e:
#         st.error(f"Database error: {e}")
#         return False
    

openai.api_key = "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"

def get_completion(prompt, model="gpt-3.5-turbo-16k"):
            messages = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                 
            model=model,
            messages=messages,
            max_tokens=2000,
            temperature=0.8
            )
            

           
            return response.choices[0].message["content"]
 



 

if "authenticated" not in st.session_state:
    st.session_state.authenticated = "Home"



if st.session_state.authenticated=="Home":
    st.title("Login...")
    col1,col2 = st.columns(2)   
    with col1:
        if st.button("Student Login"):
            st.session_state.authenticated ="student_page" 
            st.experimental_rerun()

    with col2:

        if st.button("Mentor Login"):
            st.session_state.authenticated ="mentor_page" 
            st.experimental_rerun()

if "messages1" not in st.session_state:
                st.session_state.messages1 =None

if st.session_state.authenticated=="student_page":
        
        st.title(" Student Login...")
        
        student_id = st.text_input("Enter your Student ID:")
        st.write(student_id)
        # student = int(student_id)
        

        # st.write(student_id)
        # st.write(data["StudentID"])
        
        st.session_state.messages1 = student_id

        if  st.button("login"):
            # is_valid,data = check_student_id(student_id)
            data1=data[data["StudentID"] == int(student_id,base=0)]
           
            if not data.empty:
                st.success("Login successful! Redirecting to dashboard...")
                st.session_state.authenticated ="main_page1" 
                st.experimental_rerun()
            else:
                st.error("Invalid student ID. Please enter a valid ID.")



if st.session_state.authenticated=="mentor_page":
        

        st.title("Mentor Assist Bot")
        

        # Return True if student ID exists, False otherwise
        # if row:
        #     df1 = pd.DataFrame([row], columns=["" ,"S_id", "Probability", "Linear Algebra", "Chemistry","Physics","Biology","Social Science","mid","1"])  # Adjust column names as per your database schema
        #     st.write(df1)   
                
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-3.5-turbo"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask Question?"):
            prompt1 =f""" this is the student test wise subject marks and quartile so your task is givedetail answer based on question and data

                    data:{data}
                    question:{prompt}

        """

            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # with st.chat_message("assistant"):
                # stream = openai.ChatCompletion.create(
                #     model=st.session_state["openai_model"],
                #     messages=[
                #         {"role": m["role"], "content":prompt1 }
                #         for m in st.session_state.messages
                #     ],
                #     stream=True,
                # )


            response =st.write(get_completion(prompt1))
            st.session_state.messages.append({"role": "assistant", "content": response})
        
            







if st.session_state.authenticated=="main_page1": 
            
            st.title("Student Assist Bot")

            student_id= st.session_state.messages1
            

            
            # Chat interface

            data1=data[data["StudentID"]==int(student_id,base=0)]
            st.write(data1)

            # client = openai(api_key=st.secrets["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"])

            if "openai_model" not in st.session_state:
                st.session_state["openai_model"] = "gpt-3.5-turbo"

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("Ask Question?"):
                prompt1 =f""" this is student data ```{data1}``` answer the question ```{prompt}``` of student
            """

                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    # stream = openai.ChatCompletion.create(
                    #     model=st.session_state["openai_model"],
                    #     messages=[
                    #         {"role": m["role"], "content":prompt1 }
                    #         for m in st.session_state.messages
                    #     ],
                    #     stream=True,
                    # )


                    response =st.write(get_completion(prompt1))
                st.session_state.messages.append({"role": "assistant", "content": response})



















            
            
            
                
                

        
        










        


    # Streamlit app


    # Login button


            





            
            # Add code to redirect to another page or display dashboard
        

