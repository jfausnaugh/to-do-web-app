import streamlit as st
import functions


def add_todo():
    """
    Takes the text input the user typed in and appends it to the list
    :return:
    """
    todo_item = st.session_state["new_todo"] + "\n"
    todos.append(todo_item)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My To-do App")
st.subheader("This is a basic to-do list web app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # if the checkbox is checked it will remove the item from the list
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label_visibility="collapsed", label="Add new todo",
              placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
# When user hits enter in textbox, it calls the add function and executes it
