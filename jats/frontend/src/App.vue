<template>
  <div>
    <navigation :currentTab="currentTab" @tabChange="switchTab"></navigation>
    <div class="container">
      <div class="columns">
        <div class="column is-full">
          <ul class="nav nav-pills flex-column"></ul>
        </div>
      </div>
      <hr />
        <div class="columns">
          <div
          class="column" v-show="currentTab === getListId(index)" v-for="(list, index) in this.$store.state.ticket_lists" v-bind:key="index">
            <ticket-list :ticketList="list"></ticket-list>
          </div>
          <div class="column" v-show="currentTab === 'add-item'">
            <add-list></add-list>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
  import store from './store';
  import TicketList from './components/TicketList';
  import AddList from './components/AddList';
  import Navigation from './components/Navigation';

  export default {
    beforeCreate() {
      this.$store.commit('initialize');
    },
    data() {
      return {
        currentTab: 'list-0',
      };
    },
    methods: {
      getListId(id) {
        return 'list-' + id;
      },
      switchTab(newTab) {
        this.currentTab = newTab;
      },
    },
    components: {
      TicketList,
      AddList,
      Navigation,
    },
    store,
  }
</script>
