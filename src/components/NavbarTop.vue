<template>
  <div class="container bg-info">
   <div class="row justify-content-end">
     <div class="col">
       <div class="form-inline float-right">
         <div class="form-group">
           <label for="portfolioSearch">Portfolio ID</label>
           <input v-model="portfolio_id" class="form-control search-input" id="portfolioSearch" type="search" maxlength="3" aria-label="Search">
           <button v-on:click="$emit('portfolioChange', portfolio_id)" class="btn btn-secondary btn-sm">Search</button>
        </div>
      </div>
    </div>
   </div>
  </div>
</template>


<script>
export default {
  name: "NavbarTop",
  data: function() {
    return {
      portfolio_id: null
    };
  }
};
</script>

<style>
.title {
  color: whitesmoke;
}

input.search-input {
  width: 100%;
  max-width: 70px;
  padding: 5px 8px;
}
</style>