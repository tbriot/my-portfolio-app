<template>
  <div class="modal fade" id="addTradeModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add a trade</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-row">
            <div class="col">
              <label>Ticker</label>
              <input v-model="trade.ticker" type="text" class="form-control" placeholder="AAPL">
            </div>
            <div class="col">
              <label>Quantity</label>
              <input v-model.number="trade.quantity" type="text" class="form-control" placeholder="10">
            </div>
          </div>
          <div class="form-row">
            <div class="col">
              <label>Price</label>
              <input v-model.number="trade.price" type="text" class="form-control" placeholder="185.27">
            </div>
            <div class="col">
              <label>TradedOn</label>
              <input v-model="trade.tradedOn" type="text" class="form-control" placeholder="2018-07-15">
            </div>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" v-on:click="addTrade">Save</button>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import axios from 'axios'
import $ from 'jquery'

export default {
  name: "AddTradeModal",
  props: {
    portfolioId: String
  },
  data: function() {
    return {
      trade: {
          ticker: 'AAPL',
          quantity: 10,
          price: 185.27,
          tradedOn: '2018-07-02'
      }
    };
  },
  methods: {
    addTrade: function() {
      console.log("Adding trade for stock : " + this.trade.ticker);
      var self = this;
      
      axios
        .post(
          `https://527ne5nrec.execute-api.ca-central-1.amazonaws.com/prod/portfolio/${this.portfolioId}/trade`,
          this.trade,
          {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
           }
        )
        .then(function(response) {
          console.log("API call in succes. trade id is " + response.data.tradeId);
          $('#addTradeModal').modal('toggle');
          self.$emit('tradeAdded');
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style>
</style>