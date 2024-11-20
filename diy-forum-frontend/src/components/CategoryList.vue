<template>
    <div>
      <h2>Categories</h2>
      <ul>
        <li v-for="category in categories" :key="category.id">{{ category.name }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import api from '../api';
  
  export default {
    data() {
      return {
        categories: [],
      };
    },
    created() {
      api.get('categories/').then((response) => {
        this.categories = response.data;
      });
    },
  };
  </script>
  