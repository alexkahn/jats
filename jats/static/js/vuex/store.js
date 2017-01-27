import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  tickets: [],
}

const mutations = {
  addTicket() {},
  updateTicket() {},
  deleteTicket() {},
  getTicket() {},
  getTicketList() {},
}

export default new Vuex.Store({
  state,
  mutations,
});