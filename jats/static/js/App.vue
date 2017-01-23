<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>Hello Django and Vue</h1>
                <p>This has been a long time coming...</p>
            </div>
            <div class="col-12">
              <ul v-for="ticket in tickets">
                <li>{{ ticket.title }}</li>
              </ul>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios';

  export default {
    beforeCreate() {
      axios.get('/api/tickets/')
      .then((response) => { this.tickets = response.data; }, () => {});
    },
    data() {
      return {
          tickets: []
      }
    },
  }
</script>