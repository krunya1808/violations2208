<template>
  <div>
    <b-modal
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
    </b-modal>
  </div>
</template>

<script>
export default {
  name: 'Statistics',
};
</script>

<style scoped>

</style>
