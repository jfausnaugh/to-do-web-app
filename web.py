import streamlit as st
import functions


def add_todo():
    todo_item = st.session_state["new_todo"] + "\n"
    todos.append(todo_item)
    functions.write_todos(todos)
    # When user hits enter, it calls the function and executes it


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a basic todo list web app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label_visibility="collapsed", label="Add new todo",
              placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')