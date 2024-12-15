import streamlit as st
import Functions

todos = Functions.read_todos()

def add_new_todo():
    todo_local = st.session_state["new_todo"]+"\n"
    todos.append(todo_local)
    Functions.write_todos(todos)
    st.session_state["new_todo"]=""


st.title("To-Do App")
st.subheader("This is your To-Do app.")
st.text("Become productive today.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add a todo...", on_change=add_new_todo, key="new_todo")
