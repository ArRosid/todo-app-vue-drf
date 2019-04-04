<template>
    <div>
        <div v-bind:key="todo.id" v-for="todo in todos">
            <TodoItem v-bind:todo="todo" v-on:del-todo="$emit('del-todo', todo.id)" v-on:mark-complete="$emit('mark-complete', todo)"/>
        </div>
    </div>
</template>

<script>
import TodoItem from './TodoItem.vue';
export default {
    name: "Todos",
    components: {
        TodoItem
    },
    props: ["todos"]
}
</script>

<style scoped>

</style>
