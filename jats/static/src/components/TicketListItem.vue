<template>
    <li :class="{'removed': ticket.complete}" class="list-group-item justify-content-between">
        <div class="form-check">
            <label class="form-check-label" :for="ticketId">
                <input :id="ticketId" class="form-check-input" type="checkbox" v-model="ticket.complete">
                <span>{{ ticket.title }}</span>
            </label>
        </div>
        <!-- use the modal component, pass in the prop -->
        <a href="#" @click="showModal = true"><span class="badge badge-default"><i class="fa fa-chevron-right" aria-hidden="true"></i></span></a>
        <div class="modal">
          <div class="modal-background"></div>
          <div class="modal-content">
            <!-- Any other Bulma elements you want -->
          </div>
          <button class="modal-close is-large" aria-label="close"></button>
        </div>
        <!-- <modal v-if="showModal" @close="showModal = false">
            <h3 slot="header">{{ ticket.title }}</h3>
            <ticket slot="body" :ticket="ticket"></ticket>
        </modal> -->
    </li>
</template>

<script>
  import Ticket from './Ticket';

  export default {
    components: {
      Ticket,
    },
    props: ['ticket'],
    watch: {
      'ticket.complete': function () {
          this.$store.commit('updateTicket', this.ticket);
      },
    },
    computed: {
      ticketId() {
          return "#id_" + this.ticket.id;
      }
    },
    data() {
      return {
          showModal: false,
      }
    }
  }
</script>

<style scoped>
    .removed {
        color: grey;
    }
    .removed span {
        text-decoration: line-through;
    }
</style>
