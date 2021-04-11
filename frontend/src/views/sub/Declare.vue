<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : 신고페이지 UI
    * 생성일자 : 2021-03-22
    * 최종수정일자 : 2021-04-06
  -->

  <div class="home">
    <div id="main">
      <section id="testimonials" class="testimonials">
        <div class="container">
          <!-- 신고 content -->
          <div v-if="nickName !== null" class="main-body">
            <div class="row gutters-sm">
              <!-- 신고 title -->
              <div class="signup_title">
                <img src="@/assets/img/declare/declare_title.png" class="sub_title" />
              </div>
              <div class="col-md-12">
                <div v-if="this.msg == 'declare'" class="card mb-3 d-w" style="height: 1070px">
                  <!-- 유저 영역 -->
                  <div class="row recommend_box">
                    <!-- 신고누른 유저 -->
                    <div class="w-100 justCenter">
                      <div id="recommend-table" class="col-sm-3 ">
                        <div class="gray-block p-t-2 declare-block m-b-25 people-body ">
                          <!-- 멤버 Component-->
                          <member :member="yourInfo" :value="value" :where="where"></member>
                        </div>
                      </div>
                    </div>
                    <div class="m-t-20"></div>
                  </div>
                  <!--신고 영역 -->
                  <div class="card-body m-t-40 m-b-30" style="height: 430px">
                    <h2 class="sub_text_title m-b-20">신고사유</h2>
                    <div class="declare_wrap">
                      <div class="m-b-30">
                        <b-button
                          id="reason_1"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-b-15"
                          @click="reasonSelect(1)"
                          >고의 트롤</b-button
                        >
                        <b-button
                          id="reason_2"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-l-15 m-b-15"
                          @click="reasonSelect(2)"
                          >욕설 및 혐오발언</b-button
                        >
                        <b-button
                          id="reason_3"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-l-15 m-b-15"
                          @click="reasonSelect(3)"
                          >탈주 / 자리비움</b-button
                        >
                        <br />
                        <b-button
                          id="reason_4"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-b-15"
                          @click="reasonSelect(4)"
                          >부정행위(불법프로그램 사용)</b-button
                        >
                        <b-button
                          id="reason_5"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-l-15 m-b-15"
                          @click="reasonSelect(5)"
                          >타인을 비방하는 닉네임</b-button
                        >
                        <b-button
                          id="reason_6"
                          variant="outline-secondary declare_rea_btn"
                          class="m-l-15 m-b-15"
                          @click="reasonSelect(6)"
                          >기타 사유</b-button
                        >
                      </div>
                      <b-form-textarea
                        id="declare_text"
                        v-model="text"
                        placeholder="신고 내용을 입력해주세요."
                        rows="3"
                        max-rows="6"
                      ></b-form-textarea>
                      <input
                        type="file"
                        class="upload p-b-7 m-t-20 p-l-15"
                        id="input-imgage"
                        @change="processFile($event)"
                        @keypress.enter="checkHandler"
                      />
                      <button class="btn btn-primary dBtn m-t-25" @click="declare">신고하기</button>
                    </div>
                  </div>
                </div>
                <div v-else class="card mb-3 d-w" style="height: 700px">
                  <!--신고 영역 -->
                  <div class="card-body m-t-40 m-b-30" style="height: 430px">
                    <h2 class="sub_text_title m-b-20">신고사유</h2>
                    <div class="declare_wrap">
                      <div class="m-b-30">
                        <b-button
                          id="reason_1"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-b-15"
                          @click="reasonSelect(1)"
                          >고의 트롤</b-button
                        >
                        <b-button
                          id="reason_2"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-l-15 m-b-15"
                          @click="reasonSelect(2)"
                          >욕설 및 혐오발언</b-button
                        >
                        <b-button
                          id="reason_3"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-l-15 m-b-15"
                          @click="reasonSelect(3)"
                          >탈주 / 자리비움</b-button
                        >
                        <br />
                        <b-button
                          id="reason_4"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-b-15"
                          @click="reasonSelect(4)"
                          >부정행위(불법프로그램 사용)</b-button
                        >
                        <b-button
                          id="reason_5"
                          variant="outline-secondary declare_rea_btn"
                          class="m-r-15 m-l-15 m-b-15"
                          @click="reasonSelect(5)"
                          >타인을 비방하는 닉네임</b-button
                        >
                        <b-button
                          id="reason_6"
                          variant="outline-secondary declare_rea_btn"
                          class="m-l-15 m-b-15"
                          @click="reasonSelect(6)"
                          >기타 사유</b-button
                        >
                      </div>
                      <b-form-textarea
                        id="declare_text"
                        v-model="text"
                        placeholder="신고 내용을 입력해주세요."
                        rows="3"
                        max-rows="6"
                      ></b-form-textarea>
                      <input
                        type="file"
                        class="upload p-b-7 m-t-20 p-l-15"
                        id="input-imgage"
                        @change="processFile($event)"
                        @keypress.enter="checkHandler"
                      />
                      <button class="btn btn-primary dBtn m-t-25" @click="declare">신고하기</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Member from '../../components/member.vue';
import '@/assets/css/declare.css';
import { mapGetters } from 'vuex';

export default {
  name: 'Main',
  components: {
    Member,
  },
  created() {
    this.msg = this.$store.getters.getMessage;

    this.yourInfo = this.$store.getters.getYourInfo;
    this.$store.commit('setMessage', '');
  },
  data() {
    return {
      // 플레이 멤버리스트(임시임시임시임시)
      memberList: ['고삐풀린나', '붕어싸만코', '배고파디짐', '낙곱새킬러'],
      member: '',
      value: 75, // 승률 progress
      where: 'declare',
      clickedBtn: '', // 클릭된 버튼
      clickedReason: '', // 클릭된 신고사유
      text: '', // 신고 내용
      files: null, // 증거 사진
      msg: '',
      yourInfo: '',
    };
  },
  computed: {
    ...mapGetters(['nickName']),
    rows() {
      return this.memberList.length;
    },
  },
  methods: {
    // 신고할 유저 선택
    declareSelect(id) {
      var btnName = 'btn_' + id;
      if (btnName !== this.clickedBtn) {
        // 클릭됐던 버튼 해제
        if (this.clickedBtn !== '')
          document.getElementById(this.clickedBtn).style.backgroundColor = '#fff';

        // 닉네임 클릭 처리
        this.clickedBtn = btnName;
        var clickBtn = document.getElementById(btnName);
        clickBtn.style.backgroundColor = '#6372ff44';
      }
    },
    // 신고 사유 1가지만 선택
    reasonSelect(id) {
      var btnName = 'reason_' + id;
      if (btnName !== this.clickedReason) {
        // 클릭됐던 버튼 해제
        if (this.clickedReason !== '')
          document.getElementById(this.clickedReason).style.backgroundColor = '#cdcdcd5d';

        // 닉네임 클릭 처리
        this.clickedReason = btnName;
        var clickBtn = document.getElementById(this.clickedReason);
        clickBtn.style.backgroundColor = '#6372ff44';
      }
    },
    // 신고 증거 이미지 제출
    processFile(event) {
      this.files = event.target.files[0];
    },
    declare() {
      let form = new FormData();
      form.append('jwt', this.$store.getters.getJWT);
      if (this.files != null) {
        form.append('files', this.files);
      }

      this.$store.dispatch('declare', form).then(() => {
        // 응답 결과
        this.message = this.$store.getters.message;
        if (this.message === 'FAIL')
          this.$swal('로그인 세션 만료', '다시 로그인 해주세요.', 'error');
        else {
          this.$swal('신고 완료', '기분 풀고 다시 재밌게 게임을 즐겨주세요.', 'success');
        }
      });
    },
  },
};
</script>
<style scoped>
@import '../../assets/css/main.css';
@import '../../assets/css/user.css';
</style>
