import Vue from 'vue';
import Vuex from 'vuex';
import axios from '../lib/axios';

Vue.use(Vuex);

const state = {
  tickets: [],
}

const mutations = {
  addTicket(state, title) {
    let newTicket = {
        title: title,
        completed: false,
        assigned_to: null,
        creator: 1,
        due_date: null,
        id: null,
        notes: "",
        ticket_list: 1
    }
    axios.post('/api/tickets/', newTicket)
    .then((response) => {
        state.tickets.push(response.data);
    })
    .catch((error) => {
        console.log(error);
    });
  },
  updateTicket() {},
  deleteTicket() {},
  getTicket() {},
  getTicketList(state, tickets) {
    state.tickets = tickets;
  },
}

export default new Vuex.Store({
  state,
  mutations,
});