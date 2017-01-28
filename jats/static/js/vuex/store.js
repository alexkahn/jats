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
    };
    axios.post('/api/tickets/', newTicket)
    .then((response) => {
        state.tickets.push(response.data);
    })
    .catch((error) => {
        console.log(error);
    });
  },
  updateTicket(state, ticket) {
    let url = '/api/tickets/' + ticket.id + '/';
    axios.put(url, ticket)
    .then((response) => {
      let resTicket = response.data;
      state.tickets = state.tickets.map((ticket, index) => {
        if (ticket.id === resTicket.id) {
          return resTicket;
        }
        return ticket;
      })
    })
    .catch((error) => {})
  },
  deleteTicket() {},
  getTicket() {},
  getTicketList(state, tickets) {
    axios.get('/api/tickets/')
    .then((response) => {
      state.tickets = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
  },
}

export default new Vuex.Store({
  state,
  mutations,
});