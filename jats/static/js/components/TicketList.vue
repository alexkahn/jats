<template>
  <div>
    <ul class="list-group">
      <ticket-list-item v-for="ticket in tickets" :ticket="ticket"></ticket-list-item>
      <add-ticket v-model="newTicket"></add-ticket>
    </ul>
  </div>
</template>

<script>
  import TicketListItem from './TicketListItem';
  import AddTicket from './AddTicket';

  export default {
    components: {
      TicketListItem,
      AddTicket,
    },
    data() {
      return {
        newTicket: ''
      }
    },
    props: ['tickets'],
  }
</script>