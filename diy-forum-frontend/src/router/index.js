import Vue from 'vue';
import Router from 'vue-router';
import CategoryList from '../components/CategoryList.vue';
import ThreadList from '../components/ThreadList.vue';
import PostList from '../components/PostList.vue';

Vue.use(Router);

export default new Router({
  routes: [
    { path: '/categories', name: 'CategoryList', component: CategoryList },
    { path: '/threads', name: 'ThreadList', component: ThreadList },
    { path: '/posts', name: 'PostList', component: PostList },
  ],
});
