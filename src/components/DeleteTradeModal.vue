<template>
  <div class="modal fade" id="deleteTradeModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Delete a trade</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div v-if="trade">Delete trade ticker={{ trade.ticker }}, id={{ trade.tradeId }} ?</div>
        <div v-else>No trade selected</div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" v-on:click="deleteTrade(trade.tradeId)">Delete</button>
        <button type="button" class="btn btn-light" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import $ from 'jquery'

export default {
  name: "DeleteTradeModal",
  props: {
    trade: Object
  },
  methods: {
    deleteTrade: function(trade_id) {
      console.log("Deleting trade id: " + trade_id);
      var self = this;
      axios
        .delete(
          `https://527ne5nrec.execute-api.ca-central-1.amazonaws.com/prod/trade/${trade_id}`,
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
          console.log("API call response: " + JSON.stringify(response.data));
          self.$emit('tradeDeleted', self.trade)
          $('#deleteTradeModal').modal('hide')
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