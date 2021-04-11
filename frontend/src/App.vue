<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : 푸터 추가
    * 생성일자 : 2021-03-19
    * 최종수정일자 : 2021-03-24
  -->

  <div id="app">
    <!-- 네비게이션 바 -->
    <div id="nav"><nav-header></nav-header></div>

    <!-- 컨텐츠 -->
    <router-view />
  </div>
</template>

<script>
/* eslint-disable */
import NavHeader from '@/views/nav/NavHeader.vue';
import NavFooter from './views/nav/NavFooter.vue';

export default {
  components: {
    NavHeader,
    NavFooter,
  },
};
/* eslint-disable */
</script>

<style>
/* <!-- Bootstrap --> */
@import './assets/css/bootstrap.css';
@import './assets/fonts/font-awesome/css/font-awesome.css';

/* <!-- Stylesheet --> */
@import './assets/css/style.css';
@import './assets/css/util.css';
@import './assets/css/nivo-lightbox/nivo-lightbox.css';
@import './assets/css/nivo-lightbox/default.css';
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700');
@import url('https://fonts.googleapis.com/css?family=Lato:400,700');
@import url('https://fonts.googleapis.com/css?family=Raleway:300,400,500,600,700,800,900');
</style>
