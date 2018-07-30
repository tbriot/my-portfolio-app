<template>
  <ul class="nav nav-pills nav-fill" role="tablist" aria-orientation="vertical">
     <li class="nav-item">
      <a class="nav-link active" v-on:click="$emit('changePage', 'positions')" 
        role="tab" href="#" data-toggle="tab" aria-controls="nav-home" aria-selected="true">Positions</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" v-on:click="$emit('changePage', 'trades')"
        role="tab" href="#" data-toggle="tab" aria-controls="nav-profile" aria-selected="false">Trades</a>
    </li>
  </ul>
</template>


<script>
export default {
  name: "NavbarLeft",
  data: function() {
    return {      
    };
  }
};
</script>

<style>
</style>