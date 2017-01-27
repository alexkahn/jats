<template>
  <li class="list-group-item" v-on:click="toggleForm">
    <p v-show="!showForm">Add a new item</p>
    <input v-show="showForm" :value="value" type="text" @keyup.enter="onInput" autofocus>
  </li>
</template>

<script>
export default {
  methods: {
    onInput(event) {
      this.$emit('input', event.target.value);
      this.value = '';
      this.showForm = false;
    },
    toggleForm() {
      if (this.showForm) {
        return;
      }
      this.showForm = true;
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