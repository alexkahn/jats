<template>
  <div class="card">
    <div class="card-block">
      <h2 class="card-title">Add a List</h2>
      <div class="form-group">
        <label for="exampleInputEmail1">Name</label>
        <input v-model="name" type="text" class="form-control" placeholder="Give your list a name">
        <small class="form-text text-muted">Try: Groceries, Work or Project Names</small>
      </div>
      <button type="submit" class="btn btn-primary" @click="addList">Add {{ name }}</button>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: ''
      }
    },
    methods: {
      addList() {
        this.$store.commit('createList', this.name);
        this.name = '';
      },
    },
  }  
</script>