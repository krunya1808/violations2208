<template>
  <b-container fluid>
    <b-jumbotron header="База даних порушень безпеки інформації">
      <template slot="lead">
        Сумарна кількість правопорушень: <b-badge variant="primary">{{ violationsCount }}</b-badge>
      </template>
          <b-row class="my-2">
            <b-col md="3" class="my-1">
              <b-form-group horizontal label="Фільтр" class="mb-0 text-center">
                <b-input-group>
                  <b-form-input v-model="filter" placeholder="Введіть для пошуку" />
                  <b-input-group-append>
                    <b-btn variant="primary"
                           :disabled="!filter"
                           @click="filter = ''">Видалити</b-btn>
                  </b-input-group-append>
                </b-input-group>
              </b-form-group>
            </b-col>
            <b-col md="1" class="my-1">
              <b-form-group horizontal label="Ел." class="mb-0 text-center">
                <b-form-select :options="pageOptions" v-model="perPage" />
              </b-form-group>
            </b-col>
            <b-col md="3" class="my-1">
              <b-btn v-b-modal.addViolationModal variant="primary">Новий запис</b-btn>
            </b-col>
            <b-modal
              id="addViolationModal"
              ref="addViolationModal"
              size="lg"
              title="Новий запис"
              header-bg-variant="dark"
              header-text-variant="light"
              body-bg-variant="light"
              body-text-variant="dark"
              footer-bg-variant="dark"
              footer-text-variant="light">
              <b-container fluid>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Хто виявив</b-col>
                  <b-col sm="4"><b-form-select
                    :options="people"
                    v-model="violation.whoFound"
                    required>
                  </b-form-select></b-col>
                  <b-col sm="2">Дата</b-col>
                  <b-col sm="4"><b-form-input
                    type="date"
                    v-model="violation.date"
                    required>
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Мережа</b-col>
                  <b-col sm="4"><b-form-select
                    :options="network"
                    v-model="violation.network"
                    required>
                  </b-form-select></b-col>
                  <b-col sm="2">IP-адреса</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.ipAdress"
                    required>
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Підрозділ</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.department"
                    required>
                  </b-form-input></b-col>
                  <b-col sm="2">Підпорядкування</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.subordinate">
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">В/ч</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.militaryUnit">
                  </b-form-input></b-col>
                  <b-col sm="2">Розташування</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.deslocation"
                    required>
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Норм. док.</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.normDoc">
                  </b-form-input></b-col>
                  <b-col sm="2">Обсяг інф.</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.volumeInf">
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">№ вх.док.</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.incomeDoc">
                  </b-form-input></b-col>
                  <b-col sm="2">№ вих.док.</b-col>
                  <b-col sm="4"><b-form-input
                    ype="text"
                    v-model="violation.sourceDoc">
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Зміст</b-col>
                  <b-col sd="10"><b-form-textarea
                    v-model="violation.violCont"
                    type="text"
                    rows="3"
                    max-rows="6"
                    placeholder="Введіть текст порушення"
                    required>
                  </b-form-textarea></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Вхід. файл</b-col>
                  <b-col class="text-left" sm="6"><b-form-file v-model="inputFile"
                                             accept=".docx, .doc, .pdf"
                                             ref="inpF"
                                             @change="inputFileSelected"></b-form-file>
                  </b-col>
                </b-row>
                <b-row class="mb-4">
                  <b-col>
                    <b-progress :value="inputFUploadProgress"
                                :max="100"
                                show-progress
                                animated></b-progress>
                  </b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Вихід. файл</b-col>
                  <b-col class="text-left" sm="6"><b-form-file v-model="outputFile"
                                             accept=".docx, .doc, .pdf"
                                             ref="outF"
                                             @change="outputFileSelected"></b-form-file>
                  </b-col>
                </b-row>
                <b-row class="mb-4">
                  <b-col>
                    <b-progress :value="outputFUploadProgress"
                                :max="100"
                                show-progress
                                animated></b-progress>
                  </b-col>
                </b-row>
              </b-container>
              <div slot="modal-footer" class="w-100">
                <b-btn class="float-left"
                       variant="danger"
                       @click="clearModal">Clear</b-btn>
                <b-btn class="float-right"
                       variant="primary"
                       @click="createViolation">Ok</b-btn>
                <b-btn class="float-right mx-2"
                       variant="secondary"
                       @click="hideAddModal">Close</b-btn>
              </div>
            </b-modal>
            <b-modal
              id="editViolationModal"
              ref="editViolationModal"
              size="lg"
              title="Редагування запису"
              header-bg-variant="dark"
              header-text-variant="light"
              body-bg-variant="light"
              body-text-variant="dark"
              footer-bg-variant="dark"
              footer-text-variant="light">
              <b-container fluid>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Хто виявив</b-col>
                  <b-col sm="4"><b-form-select
                    :options="people"
                    v-model="violation.whoFound"
                    required>
                  </b-form-select></b-col>
                  <b-col sm="2">Дата</b-col>
                  <b-col sm="4"><b-form-input
                    type="date"
                    v-model="violation.date"
                    required>
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Мережа</b-col>
                  <b-col sm="4"><b-form-select
                    :options="network"
                    v-model="violation.network"
                    required>
                  </b-form-select></b-col>
                  <b-col sm="2">IP-адреса</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.ipAdress"
                    required>
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Підрозділ</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.department"
                    required>
                  </b-form-input></b-col>
                  <b-col sm="2">Підпорядкування</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.subordinate">
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">В/ч</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.militaryUnit">
                  </b-form-input></b-col>
                  <b-col sm="2">Розташування</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.deslocation"
                    required>
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Норм. док.</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.normDoc">
                  </b-form-input></b-col>
                  <b-col sm="2">Обсяг інф.</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.volumeInf">
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">№ вх.док.</b-col>
                  <b-col sm="4"><b-form-input
                    type="text"
                    v-model="violation.incomeDoc">
                  </b-form-input></b-col>
                  <b-col sm="2">№ вих.док.</b-col>
                  <b-col sm="4"><b-form-input
                    ype="text"
                    v-model="violation.sourceDoc">
                  </b-form-input></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Зміст</b-col>
                  <b-col sd="10"><b-form-textarea
                    v-model="violation.violCont"
                    type="text"
                    rows="3"
                    max-rows="6"
                    placeholder="Введіть текст порушення"
                    required>
                  </b-form-textarea></b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Вхід. файл</b-col>
                  <b-col class="text-left" sm="6"><b-form-file v-model="inputFile"
                                                               ref="inpF"
                                                               accept=".docx, .doc, .pdf"
                                                               @change="inputFileSelected">
                  </b-form-file>
                  </b-col>
                </b-row>
                <b-row class="mb-4">
                  <b-col>
                    <b-progress :value="inputFUploadProgress"
                                :max="100"
                                animated></b-progress>
                  </b-col>
                </b-row>
                <b-row class="mb-4 text-center">
                  <b-col sm="2">Вихід. файл</b-col>
                  <b-col class="text-left" sm="6"><b-form-file v-model="outputFile"
                                                               ref="outF"
                                                               accept=".docx, .doc, .pdf"
                                                               @change="outputFileSelected">
                  </b-form-file>
                  </b-col>
                </b-row>
                <b-row class="mb-4">
                  <b-col>
                    <b-progress :value="outputFUploadProgress"
                                :max="100"
                                animated></b-progress>
                  </b-col>
                </b-row>
              </b-container>
              <div slot="modal-footer" class="w-100">
                <b-btn class="float-left"
                       variant="danger"
                       @click="removeViolation(violation.index)">Видалити</b-btn>
                <b-btn class="float-right"
                       variant="primary"
                       @click="editViolation(violation, violation.index)">Ok</b-btn>
                <b-btn class="float-right mx-2"
                       variant="secondary"
                       @click="hideEditModal">Close</b-btn>
              </div>
            </b-modal>
          </b-row>
          <b-table
            bordered
            :items="violations"
            :fields="fields"
            :current-page="currentPage"
            :per-page="perPage"
            :filter="filter"
            @filtered="onFiltered"
            @row-dblclicked="rowdClick">
            <template slot="index" slot-scope="row">
              <b-button size="sm" @click.stop="row.toggleDetails" class="mr-2" variant="primary">
                {{ row.value }}
              </b-button>
            </template>
            <template slot="row-details" slot-scope="row">
              <b-card>
                <b-row class="mb-2">
                  <b-col>
                    <p>Вхідний файл</p>
                    <b-button href="#" variant="success">Download file</b-button>
                  </b-col>
                  <b-col>
                    <p>Вихідний файл</p>
                    <b-button href="#" variant="success">Download file</b-button>
                  </b-col>
                </b-row>
              </b-card>
            </template>
          </b-table>
          <b-row>
            <b-col md="6" class="my-1">
              <b-pagination
                :total-rows="totalRows"
                :per-page="perPage"
                v-model="currentPage"/>
            </b-col>
          </b-row>
    </b-jumbotron>
  </b-container>
</template>
<script>

import axios from 'axios';
import Statistics from './Statistics';

const violations = [];

export default {
  name: 'Violations',
  components: { Statistics },
  data() {
    return {
      violationsCount: '0',
      hoverState: false,
      people: [
        'п/п-к Неграш В.М.', 'м-р Вишневський С.М.', 'ст.л-нт Моторний О.В.',
      ],
      network: [
        'ІСД-інтернет', 'АСУ-дніпро',
      ],
      violation: {
        index: '',
        whoFound: '',
        date: '',
        network: '',
        ipAdress: '',
        department: '',
        militaryUnit: '',
        deslocation: '',
        subordinate: '',
        normDoc: '',
        violCont: '',
        volumeInf: '',
        sourceDoc: '',
        incomeDoc: '',
      },
      fields: {
        index: { label: '№', sortable: true },
        date: { label: 'Дата', sortable: true, thStyle: { minWidth: '100px' } },
        whoFound: { label: 'Хто виявив', sortable: true },
        network: { label: 'Мережа', sortable: true },
        ipAdress: { label: 'IP-адреса' },
        department: { label: 'Підрозділ (порушник)', sortable: true },
        militaryUnit: { label: 'в/ч', sortable: true },
        deslocation: { label: 'Розташування', sortable: true },
        subordinate: { label: 'Підпорядкування', sortable: true },
        normDoc: { label: 'Нормативний документ' },
        violCont: { label: 'Зміст порушення' },
        sourceDoc: { label: '№ вих.' },
        incomeDoc: { label: '№ вх.' },
      },
      violations: [],
      currentPage: 1,
      perPage: 10,
      totalRows: violations.length,
      pageOptions: [10, 25, 50, 100],
      filter: null,
      inputFile: null,
      outputFile: null,
      inputFUploadProgress: 0,
      outputFUploadProgress: 0,
    };
  },
  created() {
    this.getViolations();
  },
  methods: {
    getViolations() {
      const path = 'http://192.168.0.104:5000/violations';
      axios.get(path)
        .then((response) => {
          this.violations = response.data.data;
          this.violationsCount = response.data.data.length;
        });
    },
    rowdClick(item) {
      this.violation = item;
      this.$refs.editViolationModal.show();
    },
    clearModal() {
      this.violation.whoFound = '';
      this.violation.date = '';
      this.violation.network = '';
      this.violation.ipAdress = '';
      this.violation.department = '';
      this.violation.militaryUnit = '';
      this.violation.deslocation = '';
      this.violation.subordinate = '';
      this.violation.normDoc = '';
      this.violation.violCont = '';
      this.violation.volumeInf = '';
      this.violation.sourceDoc = '';
      this.violation.incomeDoc = '';
      this.violation.file = '';
      this.$refs.inpF.reset();
      this.$refs.outF.reset();
    },
    hideAddModal() {
      this.$refs.addViolationModal.hide();
    },
    hideEditModal() {
      this.$refs.editViolationModal.hide();
    },
    createViolation() {
      const newViolation = {
        whoFound: this.violation.whoFound,
        date: this.violation.date,
        network: this.violation.network,
        ipAdress: this.violation.ipAdress,
        department: this.violation.department,
        militaryUnit: this.violation.militaryUnit,
        deslocation: this.violation.deslocation,
        subordinate: this.violation.subordinate,
        normDoc: this.violation.normDoc,
        violCont: this.violation.violCont,
        volumeInf: this.violation.volumeInf,
        sourceDoc: this.violation.sourceDoc,
        incomeDoc: this.violation.incomeDoc,
      };
      axios.post('http://192.168.0.104:5000/violation_new', newViolation, {
      });
      this.clearModal();
      this.hideAddModal();
    },
    editViolation(violation, index) {
      const path = 'http://192.168.0.104:5000/violation_edit/' + index;
      axios.put(path, violation);
      this.hideEditModal();
    },
    removeViolation(index) {
      const path = 'http://192.168.0.104:5:5000/violation_delete/' + index;
      axios.delete(path);
      this.hideEditModal();
    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    inputFileSelected(event) {
      this.inputFile = event.target.files[0];
    },
    outputFileSelected(event) {
      this.outputFile = event.target.files[0];
    },
  },
};
</script>
<style type="text/css">
  .table thead th {
    background-color:#343a40;
    color: white;
    vertical-align: middle;
    text-align:center;
    border:none;
  }
  .table tbody td {
    background-color:#f8f9fa;
    color:black;
    vertical-align: middle;
    text-align:center;
  }
  .jumbotron {
    margin-bottom: 0px;
    padding-top:1px;
  }
  .container-fluid {
    margin:0px;
    padding:0px;
  }

</style>
