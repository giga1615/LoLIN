/* eslint-disable */
import Vue from 'vue';
import VueRouter from 'vue-router';
import Main from '../views/Main.vue';
import Chat from '../views/chat/Chat.vue';
import Game from '../views/game/Game.vue';
// user
import Login from '../views/user/Login.vue';
import Signup from '../views/user/SignUp.vue';
import Declare from '../views/sub/Declare.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', name: 'Main', component: Main },
  { path: '/login', name: 'Login', component: Login },
  { path: '/signup', name: 'Signup', component: Signup },
  { path: '/chat', name: 'Chat', component: Chat },
  { path: '/declare', name: 'Declare', component: Declare },
  { path: '/game', name: 'Game', component: Game },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
/* eslint-disable */
