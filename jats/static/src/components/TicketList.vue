<template>
  <div class="card">
    <ul class="list-group list-group-flush">
      <ticket-list-item v-for="ticket in tickets" :ticket="ticket"></ticket-list-item>
      <add-ticket v-model="newTicket" @input="addTicket"></add-ticket>
    </ul>
    <div class="card-block text-center">
      <button class="btn btn-default" @click="setFilter(filters.all)">All</button>
      <button class="btn btn-default" @click="setFilter(filters.completed)">Completed</button>
      <button class="btn btn-default" @click="setFilter(filters.inProgress)">In Progress</button>
    </div>
  </div>
</template>

<script>
  import TicketListItem from './TicketListItem';
  import AddTicket from './AddTicket';

  const filters = {
    all: 'all',
    completed: 'completed',
    inProgress: 'in progress'
  };

  export default {
    components: {
      TicketListItem,
      AddTicket,
    },
    computed: {
      tickets() {
        if (!this.ticketList.tickets) {
          return [];
        }
        return this.ticketList.tickets.filter((ticket) => {
          switch(this.filter) {
            case this.filters.all:
              return true;
            case this.filters.completed:
              return ticket.complete;
            case this.filters.inProgress:
              return !ticket.complete;
          }
        });
      }
    },
    data() {
      return {
        newTicket: '',
        filter: 'in progress',
        filters: {
          all: 'all',
          completed: 'completed',
          inProgress: 'in progress'
        },
      }
    },
    methods: {
      addTicket() {
        let payload = { newTicket: this.newTicket, list: this.ticketList };
        this.$store.commit('addTicket', payload);
        this.newTicket = '';
      },
      setFilter(value) {
        this.filter = value;
      }
    },
    props: ['ticketList'],
  }
</script>

<style scoped>
  .filter-footer {
    background-color: white;
    height: 4rem;
    /*box-shadow: 0px -1px 2px 1px rgba(0, 0, 0, 0.2);*/
  }
</style>