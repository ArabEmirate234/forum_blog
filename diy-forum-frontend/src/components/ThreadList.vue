<template>
    <div>
      <h2>Threads</h2>
      <ul>
        <li v-for="thread in threads" :key="thread.id">{{ thread.title }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import api from '../api';
  
  export default {
    data() {
      return {
        threads: [],
      };
    },
    created() {
      api.get('threads/').then((response) => {
        this.threads = response.data;
      });
    },
  };
  </script>
  