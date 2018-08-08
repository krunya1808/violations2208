<template>
  <div id="z">
    <div>
      <b-navbar type="dark" variant="primary" toggleable>
        <b-navbar-toggle target="nav_dropdown_collapse"></b-navbar-toggle>
        <b-collapse is-nav id="nav_dropdown_collapse">
          <b-navbar-nav>
            <b-nav-item href="/violations">База даних</b-nav-item>
            <b-nav-item href="/statistics">Статистика</b-nav-item>
            <b-nav-item-dropdown text="Користувач" right>
              <b-dropdown-item href="#">Налаштування</b-dropdown-item>
              <b-dropdown-item href="#">Вийти</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
  #app {
    background-color:#f8f9fa;
    margin-top: 60px;
  }
  body {
    background-color:#f8f9fa;
  }
  .navbar {
    padding: 0px;
  }
  .nav-item {
    line-height:35px;
  }
  .nav-item :hover {
    background-color:#f8f9fa;
  }

</style>
