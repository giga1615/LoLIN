<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : 아이디 기억하기 구현
    * 생성일자 : 2021-03-19
    * 최종수정일자 : 2021-04-01
  -->

  <div>
    <section class="ftco-section">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-14 col-lg-11">
            <div class="wrap d-md-flex">
              <!-- 왼쪽 영역 -->
              <div class="text-wrap p-4  d-flex col-md-4">
                <div class="text w-100">
                  <img src="@/assets/img/user/lock.png" class="login_lock" />
                  <img src="@/assets/img/user/login_title.png" class="sub_title" />
                </div>
              </div>
              <!-- 오른쪽 영역 -->
              <div class="login-wrap p-4 p-lg-6-login col-md-8">
                <!-- 아이디 기억하기 -->
                <div class="d-flex">
                  <div class="w-100">
                    <p class="social-media d-flex justify-content-end">
                      <label class="rememberID">
                        <input type="checkbox" class="option-input radio" id="idSaveCheck" />
                        아이디 기억하기
                      </label>
                    </p>
                  </div>
                </div>
                <!-- 로그인 form -->
                <div class="signin-form">
                  <!-- 아이디 input -->
                  <div class="form-group">
                    <label class="label" for="name">Userid</label>
                    <input
                      type="text"
                      id="userid"
                      ref="userid"
                      v-model="user.userid"
                      class="form-control"
                      placeholder="아이디를 입력하세요."
                      required
                      @keypress.enter="login"
                    />
                  </div>
                  <!-- 비밀번호 input -->
                  <div class="form-group mb-5">
                    <label class="label" for="password">Password</label>
                    <input
                      type="password"
                      id="userpwd"
                      ref="userpwd"
                      v-model="user.userpwd"
                      class="form-control"
                      placeholder="비밀번호를 입력하세요."
                      required
                      @keypress.enter="login"
                    />
                  </div>
                  <!-- 로그인 버튼 -->
                  <!-- 빈칸 유무 유효성검사 후, login메소드에서 로그인 처리 시도 -->
                  <div class="form-group m-t-65">
                    <button class="form-control btn btn-primary submit px-3" @click="login">
                      <b>로그인</b>
                    </button>
                  </div>
                  <!-- 회원가입, 비밀번호찾기 text -->
                  <div class="form-group d-md-flex">
                    <div class="w-100 text-center">
                      <router-link to="signup" class="login_move"
                        >아직 회원이 아니신가요?</router-link
                      >
                    </div>
                  </div>
                </div>
              </div>
              <!-- 팬더 티모 -->
              <div order-md-last col-md-1>
                <img src="@/assets/img/user/login_character.png" class="login_character" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters(['getRememberId']),
  },

  data: function() {
    return {
      // user : id와 pass의 input에 입력된 값을 바인딩
      user: {
        userid: '',
        userpwd: '',
      },
      message: '', // 오류 받아 올 변수
    };
  },
  mounted() {
    // 아이디 기억하기 반영하기
    var isRemember = document.getElementById('idSaveCheck');
    if (this.getRememberId !== 'null') {
      isRemember.checked = true;
      this.user.userid = this.getRememberId;
    } else isRemember.checked = false;
  },
  methods: {
    // LOGIN 액션 실행
    login() {
      // 아이디 기억하기
      var inputID = document.getElementById('userid');
      var isRemember = document.getElementById('idSaveCheck');
      if (isRemember.checked == true && inputID.value != null) {
        this.$store.dispatch('setRememberId', this.user.userid);
      } else {
        this.$store.dispatch('setRememberId', 'null');
      }

      // 서버와 통신(axios)을 해 토큰값을 얻어야 하므로 Actions를 호출.
      let form = new FormData(); // form : axios통신 할 값을 넣어 전달
      form.append('id', this.user.userid);
      form.append('pw', this.user.userpwd);

      this.$store
        .dispatch('LOGIN', form)
        .then(() => {
          this.message = this.$store.getters.getMessage;

          // 로그인 성공
          if (this.message === 'SUCCESS') {
            this.$swal
              .fire({
                title: '로그인 성공',
                text: '메인 화면으로 이동합니다.',
                icon: 'success',
                confirmButtonText: 'Yes',
              })
              .then((result) => {
                if (result.value) {
                  this.$router.push(`/`); // main페이지로 이동
                  window.location.reload();
                  window.close();
                }
              });
          } else {
            // 로그인 실패 : 다이얼로그 띄우기
            this.$swal('로그인 실패', '아이디와 비밀번호를 다시 확인해주세요.', 'error');
          }
        })
        .catch(({ message }) => (this.msg = message));
    },
  },
};
</script>

<style scoped>
@import '../../assets/css/user.css';
</style>
