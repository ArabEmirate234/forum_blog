<template>
    <div>
      <h2>Posts</h2>
      <ul>
        <li v-for="post in posts" :key="post.id">
          {{ post.content }} - <em>by {{ post.user.username }}</em>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import api from '../api';
  
  export default {
    data() {
      return {
        posts: [],
      };
    },
    created() {
      api.get('posts/').then((response) => {
        this.posts = response.data;
      });
    },
  };
  </script>
  