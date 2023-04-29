import streamlit as st
import Functions

todos = Functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.write_todos(todos)

st.title("List of Animals")
st.subheader("This is a list of animals I want to see.")
st.write("This app allows you to keep track of animals I really like!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="", placeholder="Enter an animal",
              on_change=add_todo, key="new_todo")






