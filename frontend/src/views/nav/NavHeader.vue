<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : 네비게이션 변경
    * 생성일자 : 2021-03-22
    * 최종수정일자 : 2021-04-07
  -->

  <div>
    <!-- Navigation -->
    <nav id="menu" class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <img class="nav_logo" src="@/assets/img/nav/logo.png" />
        </div>

        <!-- 메뉴 탭 -->
        <div class="collapse navbar-collapse">
          <ul class="nav  navbar-nav">
            <li><router-link to="/" class="page-scroll">Home</router-link></li>
            <li><router-link to="/chat" class="page-scroll">채팅</router-link></li>
            <li><router-link to="/declare" class="page-scroll">유저신고</router-link></li>
          </ul>

          <!-- 로그인 & 회원가입 -->
          <ul class="nav navbar-nav-login navbar-right" v-if="getJWT">
            <li>
              <a class="login_nick page-scroll">{{ nickName }}</a>
            </li>
            <li><a class="page-scroll" @click.prevent="logout">로그아웃</a></li>
          </ul>
          <ul class="nav navbar-nav-login navbar-right" v-else>
            <li><router-link to="/login" class="page-scroll">로그인</router-link></li>
            <li><router-link to="/signup" class="page-scroll">회원가입</router-link></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters(['getJWT', 'userId', 'nickName']),
  },
  methods: {
    logout() {
      this.$store.dispatch('LOGOUT').then(() => this.$router.replace('/').catch(() => {}));
    },
  },
};
</script>

<style>
.nav_logo {
  margin: 0 20px;
  height: 50px;
}
</style>
