<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand" href="/">

      <div class="navbar-item">
        <a href="/" class="navbar-item">Jats</a>
      </div>
      <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item">
          Home
        </a>

        <a class="navbar-item">
          Documentation
        </a>
      <ul class="navbar-nav mr-auto">
        <li class="nav-item" v-for="(list, index) in this.$store.state.ticket_lists">
          <a class="nav-link" :class="currentTab === getListId(index) ? 'active': ''" :id="getListId(index)" href="#" @click.stop="switchNav">{{ list.name }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
      </ul>
      </div>
      <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a href="/accounts/logout/" class="button is-light">Logout</a>
        </div>
      </div>
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