<template>
  <div class="container">
    <add-trade-modal id="addTradeModal" v-bind:portfolioId="portfolioId" v-on:tradeAdded="refreshTrades"></add-trade-modal>
    <delete-trade-modal id="deleteTradeModal" v-bind:trade="tradeToDelete" v-on:tradeDeleted="onTradeDeleted($event)"></delete-trade-modal>

    <div class="row">
      <div class="col" align="center">

        <div v-if="refreshing" class="progress" style="width:300px">
          <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 100%">
            <span>Loading...</span>
          </div>
        </div>

        <table v-else-if="trades.length" class="table table-striped table-hover table-sm">
          <thead class="table-primary">
            <tr>
              <th>ID</th>
              <th>ticker</th>
              <th>quantity</th>
              <th>price</th>
              <th>tradedOn</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="trade in trades" v-bind:key="trade.tradeId">
              <td>{{ trade.tradeId }}</td>
              <td>{{ trade.ticker }}</td>
              <td>{{ trade.quantity }}</td>
              <td>{{ trade.price }}</td>
              <td>{{ trade.tradedOn }}</td>
              <td>
                  <font-awesome-icon icon="trash" v-on:click="showDeleteModal(trade)"/>
              </td>              
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="6" align="left">
                <button class="btn btn-primary"  data-toggle="modal" data-target="#addTradeModal">
                  <font-awesome-icon icon="plus"/> Add trade
                </button>
              </td>
            </tr>
          </tfoot>
          </table>
          <div v-else-if="!portfolioId" class="alert alert-info" role="alert">Please select a portfolio</div>
          <div v-else class="alert alert-warning" role="alert">No trade in that portfolio</div>
        </div>
      </div>

    <div v-if="tradeDeleted" class="row">
      <div class="col">
         <div class="alert alert-success" role="alert">
         Trade has been successfully deleted !
         </div>
      </div>
    </div>

  </div>

</template>

<script>
import AddTradeModal from './AddTradeModal.vue'
import DeleteTradeModal from './DeleteTradeModal.vue'
import axios from 'axios'
import $ from 'jquery'

export default {
  name: "Trades",
  components: {
    AddTradeModal,
    DeleteTradeModal
  },
  props: {
    portfolioId: String
  },
  watch: {
    portfolioId: function(newVal, oldVal) {
      // watch it
      console.log("Prop changed: ", newVal, " | was: ", oldVal);
      this.refreshTrades();
    }
  },
  data: function() {
    return {
      trades: [],
      refreshing: false,
      tradeToDelete: null,
      tradeDeleted: null
    };
  },
  created: function() {
      if (this.portfolioId) this.refreshTrades()
  },
  methods: {
    refreshTrades: function() {
      var self = this
      self.refreshing = true
      axios
        .get(
          `https://527ne5nrec.execute-api.ca-central-1.amazonaws.com/prod/portfolio/${
            this.portfolioId
          }/trade`,
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
          self.trades = response.data
          self.refreshing = false
        })
        .catch(function(error) {
          console.log(error)
          self.refreshing = false
        });
    },
    showDeleteModal: function(trade) {
      console.log("Toggle deleteModal for trade id: " + trade.tradeId);
      this.tradeToDelete = trade
      $('#deleteTradeModal').modal('show')
    },
    onTradeDeleted: function(trade) {
      console.log("onTradeDelete: " + trade.tradeId)
      this.tradeDeleted = trade   
      this.refreshTrades()
      var self = this
      setTimeout(function() {
        self.tradeDeleted= null
        console.log("end of timeout")
      }, 5000);
    }
  }
};
</script>

<style>
</style>

