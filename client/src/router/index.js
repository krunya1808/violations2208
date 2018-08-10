import Vue from 'vue';
import Router from 'vue-router';
import Violations from '@/components/Violations';
import Statistics from '@/components/Statistics';
import Authorization from '@/components/Authorization';


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/violations',
      name: 'Violations',
      component: Violations,
    },
    {
      path: '/violation_new',
      name: 'NewViolation',
    },
    {
      path: '/violation_edit',
      name: 'EditViolation',
    },
    {
      path: '/statistics',
      name: 'Statistics',
      component: Statistics,
    },
    {
      path: '/',
      name: 'Auth',
      component: Authorization,
    },
  ],
  mode: 'history',
});
