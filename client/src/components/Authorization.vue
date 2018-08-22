<template>
  <b-container>
    <b-row>
      <b-col sm="4"></b-col>
      <b-col sm="4" class="text-center">
        <img src="../assets/logo_mt.svg" width="150px" id="img">
          <b-form>
            <b-form-group id="exampleInputGroup1"
                          label="Логін">
              <b-form-input type="text"
                            :state="loginState"
                            required
                            v-model.trim="form.login"
                            placeholder="Введіть логін "
              ></b-form-input>
            </b-form-group>
            <b-form-group id="exampleInputGroup2"
                          label="Пароль">
              <b-form-input type="password"
                            v-model="form.password"
                            :state="passwordState"
                            required
                            aria-describedby="inputLiveFeedback"
                            placeholder="Введіть пароль">
              </b-form-input>
              <b-form-invalid-feedback id="inputLiveFeedback">
                {{ this.msg }}
              </b-form-invalid-feedback>
            </b-form-group>

            <b-form-group id="exampleGroup4">
              <b-form-checkbox-group v-model="form.checked" id="exampleChecks">
                <b-form-checkbox value="Remember me">Запам'ятати</b-form-checkbox>

              </b-form-checkbox-group>
            </b-form-group>
            <b-button type="submit" variant="primary" class="but">Вхід</b-button>
          </b-form>
      </b-col>
      <b-col sm="4"></b-col>
    </b-row>

  </b-container>
</template>

import axios from 'axios';

<script>
export default {
  name: 'Authorization',
  data() {
    return {
      msg: 'Мінімальна кількість символів 6',
      form: {
        login: '',
        password: '',
        checked: [],
        stat: '',
      },
    };
  },
  computed: {
    loginState() {
      if (this.form.login.length < 1) {
        return null;
      }
      if (this.form.login.length >= 3) {
        return true;
      }
      if (this.form.login.length < 3) {
        return false;
      }
    },
    passwordState() {
      if (this.form.password.length < 1) {
        return null;
      }
      if (this.form.password.length > 4) {
        return true;
      }
      if (this.form.password.length < 4) {
        return false;
      }
    },
  },
  methods: {
    auth() {

    },
  },
};
</script>

<style scoped>
#exampleInputGroup1,#exampleInputGroup2, #exampleChecks{
  font-size: 20px;
  color: #2699FB;
  font-weight: bold;
}
  #inputLiveFeedback{
    font-size: 12px;
  }
.but{
  width: 150px;
}
</style>
