<template>
  <div>
    <div class="class11">
      <p> qwwff </p>
    </div>
    <!--<b-modal
      id="deleteModal"
      ref="deleteModal"
      @ok="removeViolation"
      size="md"
      title="Видалення запису"
      header-bg-variant="dark"
      header-text-variant="light"
      body-bg-variant="light"
      body-text-variant="dark"
      footer-bg-variant="dark"
      footer-text-variant="light">
      <b-container>
        <b-row class="mb-4 text-center">
          <h2>Ви дійсно бажаєте видалити запис № {{ row.value}}</h2>
        </b-row>
      </b-container>
    </b-modal>-->
  </div>
</template>
import axios from 'axios';

<script>
import { AxiosInstance as axios } from 'axios';

export default {
  name: 'Statistics',
  data() {
    return {
      violations: [],
    };
  },
  methods: {
    getViolations() {
      const path = 'http://192.168.0.104:5000/violations';
      axios.get(path)
        .then((response) => {
          this.violations = response.data.data;
        });
    },
  },
};
</script>

<style scoped>

</style>
