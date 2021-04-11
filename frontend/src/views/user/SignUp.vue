<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : 회원가입 서버연동
    * 생성일자 : 2021-03-19
    * 최종수정일자 : 2021-03-31
  -->

  <div>
    <section class="ftco-section">
      <div class="container">
        <div class="row justify-content-center">
          <!-- 회원가입 title -->
          <div class="signup_title">
            <img src="@/assets/img/user/signup_title.png" class="sub_title" />
          </div>
          <!-- 회원가입 content -->
          <div class="col-md-14 col-lg-11">
            <div class="wrap d-md-flex">
              <div class="signup-wrap p-4 p-lg-6-signup col-md-12">
                <!-- 회원가입 form -->
                <div class="signin-form">
                  <!-- 아이디 input -->
                  <div class="form-group">
                    <label class="label col-md-3 sign_label" for="name">Userid</label>
                    <input
                      type="text"
                      id="userid"
                      ref="userid"
                      v-model="user.userid"
                      class="form-control col-md-9"
                      placeholder="아이디를 입력하세요."
                      required
                    />
                  </div>

                  <!-- 비밀번호 input -->
                  <div class="form-group ">
                    <label class="label col-md-3 sign_label" for="password">Password</label>
                    <input
                      type="password"
                      id="userpwd"
                      ref="userpwd"
                      v-model="user.userpwd"
                      class="form-control col-md-9"
                      placeholder="비밀번호를 입력하세요."
                      required
                    />
                    <span class="validation" v-if="msg.pass">{{ msg.pass }}</span>
                  </div>

                  <!-- 비밀번호 확인 input -->
                  <div class="form-group">
                    <label class="label col-md-3 sign_label" for="passwordCheck"
                      >Password Check</label
                    >
                    <input
                      type="password"
                      id="userpwd_check"
                      ref="userpwd_check"
                      v-model="user.userpwd_check"
                      class="form-control col-md-9 "
                      placeholder="비밀번호 확인을 입력하세요."
                      required
                    />
                    <span class="validation " v-if="msg.pass_check">{{ msg.pass_check }}</span>
                  </div>

                  <!-- 닉네임 input -->
                  <div class="form-group mb-5">
                    <label class="label col-md-3 sign_label" for="nickName">nickName</label>
                    <input
                      type="text"
                      id="nickname"
                      ref="nickname"
                      v-model="user.nickname"
                      class="col-md-6 nick-input m-b-15"
                      placeholder="리그오브레전드 닉네임을 입력하세요."
                      required
                    />
                    <b-button
                      size="sm"
                      id="check_btn"
                      class="col-md-2 m-l-20 btn-signup-check order-md-last"
                      @click="getIcon"
                      >인증</b-button
                    >
                  </div>

                  <!-- 닉네임 인증 div -->
                  <div class="sign_pic">
                    <div class="col-md-3"></div>
                    <div v-if="iconUrl" class="col-md-9 m-b-75">
                      <b-avatar
                        rounded
                        class="sign_picture"
                        :src="
                          `http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/${iconUrl}.png`
                        "
                      ></b-avatar>
                      <div class="sign_pic_text">
                        롤에 접속 후, 왼쪽 아이콘으로 변경하여 본인을 인증하세요.
                      </div>
                    </div>
                  </div>

                  <!-- 회원가입 버튼 -->
                  <div class="form-group btn-wrap m-t-70">
                    <button
                      id="goSign"
                      class="form-control btn btn-primary submit px-3 sign_btn"
                      @click="checkId"
                    >
                      <b>회원가입</b>
                    </button>
                    <div class="sign_pic_text p-t-20">
                      빅데이터 분석으로 추천받기 위해 회원가입에 최대 1분이 소요될 수 있습니다. 완료
                      창이 나타날때까지 기다려주세요.
                    </div>
                  </div>
                </div>
              </div>
              <!-- 메롱메롱 혓바닥 캐릭터 -->
              <div order-md-last col-md-1>
                <img src="@/assets/img/user/signup_character.png" class="signup_character" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        userid: '', // 아이디
        userpwd: '', // 비밀번호
        userpwd_check: '', // 비밀번호 확인
        nickname: '', // 닉네임
      },
      message: '', // 오류 받아 올 변수
      iconUrl: '', // 아이콘 url
      msg: [], // 유효성검사 후, 출력할 메세지 담을 배열
    };
  },
  watch: {
    // 비밀번호 유효성 검사
    'user.userpwd'(value) {
      this.validatePassword(value, 'userpwd');
    },
    // 비밀번호 확인 유효성 검사
    'user.userpwd_check'(value) {
      this.validatePassword(value, 'userpwd_check');
    },
  },
  methods: {
    // 회원가입은 총 3단계로 진행합니다.
    // 1단계 : 닉네임에 해당하는 아이디가 바꿀 아이콘을 알려준다.
    getIcon() {
      this.$store
        .dispatch('getIcon', this.user.nickname)
        .then(() => {
          this.message = this.$store.getters.getMessage;

          // 닉네임 조회 성공
          if (this.message === 'SUCCESS') {
            // Use sweetalert2
            this.$swal(
              '닉네임 조회 성공',
              '표시된 아이콘으로 변경 후, 회원가입을 진행해주세요.',
              'success'
            );

            var check_btn = document.getElementById('check_btn');
            check_btn.style.backgroundColor = '#8696f7'; // 배경색 바꾸고
            check_btn.value = '조회완료';
            check_btn.disabled = 'disabled'; // 버튼 비활성화

            this.iconUrl = this.$store.getters.iconNumber;
          } else {
            // api키 만료
            this.$swal('닉네임 조회 실패', '계속 반복될 시, 연락바랍니다.', 'error');
          }
        })
        .catch(({ message }) => (this.msg = message));
    },

    // 2단계 : 아이디가 겹치는지 체크
    checkId() {
      this.$store
        .dispatch('isExist', this.user.userid)
        .then(() => {
          this.message = this.$store.getters.getMessage;
          if (this.message === '존재') {
            this.$swal('회원가입 실패', '이미 존재하는 닉네임입니다.', 'error');
          } else {
            this.signUp();
          }
        })
        .catch(({ message }) => (this.msg = message));
    },

    // 3단계 : 모든 인증 성공 회원가입하러가기
    signUp() {
      var goSign = document.getElementById('goSign');
      goSign.style.backgroundColor = '#8696f7'; // 배경색 바꾸고
      goSign.setAttribute('value', '진행중');
      goSign.disabled = 'disabled'; // 버튼 비활성화

      if (this.user.userpwd === this.user.userpwd_check) {
        let form = new FormData();
        form.append('id', this.user.userid);
        form.append('pw', this.user.userpwd);
        form.append('nickName', this.user.nickname);

        this.$store
          .dispatch('signUp', form)
          .then(() => {
            this.message = this.$store.getters.getMessage;

            // 회원가입 성공
            if (this.message === 'SUCCESS') {
              this.$swal
                .fire({
                  title: '회원가입 성공',
                  text: '로그인 화면으로 이동합니다.',
                  icon: 'success',
                  confirmButtonText: 'Yes',
                })
                .then((result) => {
                  if (result.value) {
                    this.$router.push(`/login`); // login페이지로 이동
                  }
                });
            } else if (this.message === 'FAIL') {
              this.$swal('회원가입 실패', '이미 존재하는 아이디입니다.', 'error');
            }
          })
          .catch(({ message }) => (this.msg = message));
      }
    },

    // 비밀번호 유효성 검사 정규식 : 영어,숫자,특수문자 조합, 8글자 이상
    validatePassword(v, title) {
      if (title === 'userpwd')
        if (/^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$/g.test(v)) {
          this.msg['pass'] = '';
        } else this.msg['pass'] = '영어, 숫자, 특수문자를 조합하여 8글자 이상 입력해주세요.';
      else {
        if (this.user.userpwd_check !== this.user.userpwd)
          // 비밀번호 확인과 비밀번호의 입력값이 다른 경우
          this.msg['pass_check'] = '비밀번호가 일치하지 않습니다.';
        else this.msg['pass_check'] = '';
      }
    },
  },
};
</script>

<style scoped>
@import '../../assets/css/user.css';
</style>
