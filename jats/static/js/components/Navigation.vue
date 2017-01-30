<template>
  <nav class="navbar navbar-toggleable-md navbar-inverse bg-inverse mb-4">
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <a class="navbar-brand" href="/">Jats</a>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item" v-for="(list, index) in this.$store.state.ticket_lists">
          <a class="nav-link" :class="currentTab === getListId(index) ? 'active': ''" :id="getListId(index)" href="#" @click.stop="switchNav">{{ list.name }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
      </ul>
      <div class="nav-item">
        <a href="/accounts/logout/" class="btn btn-primary">Logout</a>
      </div>
    </div>
  </nav>
</template>

<script>
  const LIST_ID = 'list-';
  const DEFAULT_LIST = LIST_ID + '0';

  export default {
    data() {
      return {
        listId: LIST_ID
      };
    },
    methods: {
      getListId(id) {
        return this.listId + id;
      },
      switchNav(event) {
        this.$emit('tabChange', event.target.id);
      },
    },
    props: ['currentTab'],
  }
</script>