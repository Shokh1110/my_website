<template>
  <div class="menu">
    <h1>{{ restaurantName }}</h1>
    <div v-for="item in menu" :key="item.id" class="menu-item">
      <h3>{{ item.name }}</h3>
      <p>{{ item.price }} so'm</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      restaurantName: "O'zbekiston Oshxonasi",
      menu: []
    }
  },
  async mounted() {
    const response = await fetch('http://localhost:8000/api/menu/')
    this.menu = await response.json()
  }
}
</script>