<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>Hello Django and Vue</h1>
                <p>This has been a long time coming...</p>
            </div>
            <div class="col-12">
              <ticket-list :tickets="this.$store.state.tickets"></ticket-list>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios';
  import store from './vuex/store';
  import TicketList from './components/TicketList';

  export default {
    mounted() {
      axios.get('/api/tickets/')
      .then((response) => {
        this.$store.commit('getTicketList', response.data);
      }, () => {});
    },
    components: {
      TicketList,
    },
    store,
  }
</script>