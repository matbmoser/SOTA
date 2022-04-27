<template>
  <div id="nav">
    <router-link :to="{ name: 'Home' }">Home</router-link> |
    <router-link :to="{ name: 'About' }">About</router-link> |
    <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>|
    <router-link :to="{ name: 'Login' }">Login</router-link>
    <router-link :to="{ name: 'Register' }">Register</router-link>
  </div>
  <router-view />
</template>