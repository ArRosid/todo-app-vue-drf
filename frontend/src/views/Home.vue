<template>
  <div id="app">
    <AddTodo v-on:add-todo="addTodo"/>
    <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo" v-on:mark-complete="markComplete" />
  </div>
</template>

<script>
import axios from 'axios';
import Todos from '../components/Todos';
import AddTodo from '../components/AddTodo';

export default {
  name: 'home',
  components: {
    AddTodo,
    Todos
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    deleteTodo(id) {
      axios.delete(`http://localhost:8000/api/todos/${id}`)
      .then(res => this.todos = this.todos.filter(todo => todo.id !== id))
      .catch(err => console.log(err))
    },
    addTodo(newTodo) {
      const {title, completed} = newTodo;
      axios.post('http://localhost:8000/api/todos/',{
        title:title,
        completed:completed
      })
      .then(res => this.todos = [...this.todos, res.data])
      .catch(err => console.log(err))
    },
    markComplete(todo) {
      console.log(todo)
      axios.patch(`http://localhost:8000/api/todos/${todo.id}/`,{
        completed: !todo.completed
      })
      .then(res => todo.completed = res.data.completed)
      .catch(err => console.log(err))
    }
  },
  created() {
    axios.get('http://localhost:8000/api/todos/')
      .then(res => this.todos = res.data)
      .catch(err => console.log(err));
  }
}
</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
  }

  .btn {
    display: inline-black;
    border: none;
    background: #555;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover {
    background: #666;
  }
</style>
