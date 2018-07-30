<template>
  <div id="app">
    <div class="container">
      <div class="row">
        <div class="col">
          <NavbarTop v-on:portfolioChange="portfolioId=$event"/>
        </div>
      </div>
      <div class="row">
        <div class="col-1">
          <NavbarLeft v-on:changePage="currentPage=$event"/>
        </div>
        <div class="col">
          <Positions v-if="currentPage === 'positions'" v-bind:portfolioId="portfolioId"/>
          <Trades v-if="currentPage === 'trades'" v-bind:portfolioId="portfolioId"/>
        </div>
      </div>
    </div>  
  </div>
</template>

<script>
import NavbarTop from './components/NavbarTop.vue'
import NavbarLeft from './components/NavbarLeft.vue'
import Positions from './components/Positions.vue'
import Trades from './components/Trades.vue'

export default {
  name: 'app',
  components: {
    NavbarTop,
    NavbarLeft,
    Positions,
    Trades
  },
  data: function () {
    return {
      portfolioId: 77,
      currentPage: 'positions'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
