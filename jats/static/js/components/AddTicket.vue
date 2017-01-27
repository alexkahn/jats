<template>
  <li class="list-group-item" v-on:click.once="toggleForm">
    <p v-show="!showForm">Add a new item</p>
    <input v-show="showForm" :value="value" type="text" @input="onInput" autofocus>
  </li>
</template>

<script>
export default {
  methods: {
    onInput(event) {
      this.$emit('input', event.target.value);
    },
    toggleForm() {
      this.showForm = !this.showForm;
    }
  },
  data() {
    return {
      showForm: false,
    }
  },
  props: ['value'],
}
</script>

<style scoped>
  
</style>