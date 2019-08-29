<template>
  <li class="list-group-item">
    <button v-on:click="openForm" v-show="!showForm" class="btn btn-secondary btn-block"><i class="fa fa-plus-square-o" aria-hidden="true"></i>&nbsp;Add a new item</button>
    <div v-show="showForm" class="input-group">
      <input  :value="value" type="text" class="form-control" @keyup.enter.stop="onInput" autofocus>
      <span class="input-group-btn">
        <button class="btn btn-danger" type="button" @click="closeForm"><i class="fa fa-times-circle-o" aria-hidden="true"></i> Cancel</button>
      </span>
    </div>
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
    closeForm() {
      console.log('got close form');
      this.showForm = false;
      console.log(this.showForm);
    },
    openForm() {
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