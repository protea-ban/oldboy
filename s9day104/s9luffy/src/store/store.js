import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: Cookie.get('username'),
    token: Cookie.get('token'),

  },
  mutations: {
    saveToken:function (state, userToken) {
      state.username = userToken.username;
      state.token = userToken.token;
      Cookie.set('username', userToken.username, '20min');
      Cookie.set('token', userToken.token, '20min');
    },
    clearToken:function (state) {
      state.username = null;
      state.token = null;
      Cookie.remove('username');
      Cookie.remove('token');
    }
  }
})
