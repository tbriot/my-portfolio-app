<template>
  <div class="container">
    <div class="row">
      <div class="col" align="center">

        <div v-if="refreshing" class="progress" style="width:300px">
          <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 100%">
            <span>Loading...</span>
          </div>
        </div>
        <table v-else-if="positions.length" class="table table-striped table-hover table-sm">
          <thead class="table-primary">
            <tr>
              <th>ticker</th>
              <th>quantity</th>
              <th>cost/share</th>
              <th>position cost</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="p in positions">
              <td>{{ p.ticker }}</td>
              <td>{{ p.qty }}</td>
              <td>{{ p.cost_share }}</td>
              <td>{{ p.pos_cost }}</td>            
            </tr>
          </tbody>
          </table>

          <div v-else-if="!portfolioId" class="alert alert-info" role="alert">Please select a portfolio</div>
          <div v-else class="alert alert-warning" role="alert">No position in that portfolio</div>

        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import $ from 'jquery'

export default {
  name: "Positions",
  components: {},
  props: {
    portfolioId: String
  },
  watch: {
    portfolioId: function(newVal, oldVal) {
      // watch it
      console.log("Prop changed: ", newVal, " | was: ", oldVal);
      this.refreshPositions();
    }
  },
  data: function() {
    return {
      positions: [],
      refreshing: false
    };
  },
  created: function() {
      if (this.portfolioId) this.refreshPositions()
  },
  methods: {
    refreshPositions: function() {
      var self = this;
      self.refreshing = true
      axios
        .get(
          `https://527ne5nrec.execute-api.ca-central-1.amazonaws.com/prod/portfolio/${this.portfolioId}/position`,
          {
            dataType: "json",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json"
            },
            mode: "no-cors"
          }
        )
        .then(function(response) {
          console.log("API call response: " + JSON.stringify(response.data))
          self.positions = response.data
          self.refreshing = false
        })
        .catch(function(error) {
          console.log(error)
          self.refreshing = false
        });
    }
  }
};
</script>

<style>
</style>

