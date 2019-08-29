import Vue from "vue";
import Vuex from "vuex";

import axios from './lib/axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
      id: null,
    },
    ticket_lists: [
      {name: ''}
    ],
    tickets: [],
    currentList: {},
  },
  mutations: {
    initialize(state) {
      axios.get('/api/users/')
      .then((response) => {
        state.user.id = response.data.id;
        state.ticket_lists = response.data.ticketlist_set;
      })
      .catch((error) => {
          console.log(error);
      });
    },
    addTicket(state, payload) {
      let newTicket = {
          title: payload.newTicket,
          completed: false,
          assigned_to: null,
          creator: state.user.id,
          due_date: null,
          id: null,
          notes: "",
          ticket_list: payload.list.id
      };
      axios.post('/api/tickets/', newTicket)
      .then((response) => {
        let ticket = response.data;
        state.ticket_lists.map((list) => {
          if (list.id === ticket.ticket_list) {
            list.tickets.push(ticket);
          }
        });
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
        state.ticket_lists = state.ticket_lists.map((list) => {
          list.tickets.map((ticket, index) => {
            if (ticket.id === resTicket.id) {
              return resTicket;
            }
            return ticket;
          })
          return list;
        });
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
    createList(state, name) {
      let newList = {
        name: name,
        creator: state.user.id,
      };
      axios.post('/api/lists/', newList)
      .then((response) => {
        state.ticket_lists.push(response.data);
      })
      .catch((error)=>{console.log(error)});
    }
  },
  actions: {}
});