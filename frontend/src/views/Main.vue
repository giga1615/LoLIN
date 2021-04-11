<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : 프로필 ui 상단
    * 생성일자 : 2021-03-22
    * 최종수정일자 : 2021-04-03
  -->

  <div class="home">
    <div id="main">
      <section id="testimonials" class="testimonials">
        <div class="container">
          <!-- 검색 input -->
          <div v-if="nickName !== null" class="section-title" vue-aos="fade-up">
            <form onsubmit="return false;">
              <input
                id="searchInput"
                type="text"
                name="text"
                v-model="yourNick"
                placeholder="소환사명 검색"
              />
              <div class="testimonials_submit">
                <i class="fa fa-search testimonials_btn" @click="getInfoYou" aria-hidden="true"></i>
              </div>
            </form>
          </div>

          <!-- 메인 content -->
          <div v-if="nickName !== null" class="main-body">
            <div class="row gutters-sm">
              <!-- 왼쪽 -->
              <div class="col-md-9">
                <!-- 추천 content -->
                <div class="card mb-3">
                  <!-- 선택 option -->
                  <div class="card-body recommend-wrap">
                    <div class="p-3 d-flex ">
                      <div class="text w-100">
                        <!-- 추천 title -->
                        <div>
                          <img
                            src="@/assets/img/main/recommend_title.png"
                            class="sub_title mb3rem "
                          />
                        </div>
                        <!-- 티어 select -->
                        <div class="f-left clear m-b-50">
                          <div class="f-left m-r-20">
                            <p class="f-left m-r-40 select-text"><b>티어</b></p>
                            <div class="clear sameLine ">
                              <div class="p-l-10">
                                <vue-slider
                                  class="clear"
                                  :process="false"
                                  :data="sliderData"
                                  :marks="true"
                                  v-model="sliderValue"
                                  @change="dataMake"
                                ></vue-slider>
                              </div>
                            </div>
                          </div>
                        </div>
                        <!-- 포지션, 게임유형, 상태 select -->
                        <div class="f-left clear">
                          <div class="f-left m-r-20">
                            <p class="f-left m-r-10 select-text"><b>포지션</b></p>
                            <div class="clear sameLine ">
                              <b-form-select
                                v-model="selectedPosition"
                                :options="positions"
                                class="main-select"
                                value-field="item"
                                text-field="name"
                                disabled-field="notEnabled"
                              ></b-form-select>
                              <!-- <div class="mt-3">
                                <strong>{{ selected }}</strong>
                              </div> -->
                            </div>
                          </div>
                          <div class="f-left m-l-20 m-r-20">
                            <p class="f-left m-r-10 select-text"><b>게임유형</b></p>
                            <div class="clear sameLine ">
                              <b-form-select
                                v-model="selectedType"
                                :options="types"
                                class="main-select"
                                value-field="item"
                                text-field="name"
                                disabled-field="notEnabled"
                              ></b-form-select>
                            </div>
                          </div>
                          <div class="f-left m-l-20">
                            <p class="f-left m-r-10 select-text"><b>상태</b></p>
                            <div class="clear sameLine ">
                              <b-form-select
                                v-model="selectedStatus"
                                :options="status"
                                class="main-select"
                                value-field="item"
                                text-field="name"
                                disabled-field="notEnabled"
                              ></b-form-select>
                            </div>
                          </div>
                          <b-button class="search_btn m-l-150" @click="RecommendUser"
                            >조회</b-button
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- 추천 영역 -->
                  <div class="card-body" style="height: 871px" v-if="isSelected === false">
                    <div class="row recommend_box">
                      <!-- 추천된 유저 -->
                      <div class="w-100" style="height: 751px">
                        <div v-if="newRow !== 0">
                          <div
                            v-for="(member, index) in newdataAll"
                            :key="index"
                            id="recommend-table"
                            class="col-sm-4 "
                          >
                            <div
                              v-if="(currentPage - 1) * 6 <= index && index < currentPage * 6"
                              class="gray-block p-t-2 member-block m-b-25 people-body "
                            >
                              <!-- 멤버 Component-->
                              <member
                                :index="index"
                                :member="member"
                                :value="value"
                                :online="online[0]"
                                :where="where"
                              ></member>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <!-- pagination -->
                    <div class="pagination">
                      <b-pagination
                        v-model="currentPage"
                        :total-rows="newRow"
                        :per-page="perPage"
                        size="lg"
                        class="pagination_height"
                        aria-controls="recommend-table"
                      ></b-pagination>
                    </div>
                  </div>
                  <div class="card-body" style="height: 871px" v-else>
                    <div class="row recommend_box">
                      <!-- 추천된 유저 -->
                      <div class="w-100" style="height: 751px">
                        <div
                          v-for="(member, index) in recommendedUser"
                          :key="index"
                          id="recommend-table"
                          class="col-sm-4 "
                        >
                          <div>
                            <div
                              v-if="(currentPage2 - 1) * 6 <= index && index < currentPage2 * 6"
                              class="gray-block p-t-2 member-block m-b-25 people-body "
                            >
                              <!-- 멤버 Component-->
                              <member
                                :member="member"
                                :value="value"
                                :online="online[0]"
                                :where="where"
                              ></member>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <!-- pagination -->
                    <div class="pagination">
                      <b-pagination
                        v-model="currentPage2"
                        :total-rows="newRow2"
                        :per-page="perPage2"
                        size="lg"
                        class="pagination_height"
                        aria-controls="recommend-table"
                      ></b-pagination>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 오른쪽 -->
              <div class="col-md-3 mb-3">
                <!-- 프로필 -->
                <div class="card">
                  <div class="card-body">
                    <div class="d-flex flex-column text-center p-3">
                      <!-- 토글 버튼 -->
                      <div>
                        <toggle-button
                          class=" toggle"
                          id="toggleBtn"
                          :value="toggleVaule"
                          :labels="{ checked: 'ON', unchecked: 'OFF' }"
                          @change="onChangeEventHandler"
                        />
                        <span class="align-right">접속</span>
                      </div>
                      <!-- 프로필 사진 & 닉네임 -->
                      <div>
                        <img
                          :src="
                            `http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/${myIcon}.png`
                          "
                          alt="Admin"
                          class="rounded-circle profile_icon"
                          width="70"
                        />
                        <div class="nextLine">
                          <h2 class="main_profile_id">{{ nickName }}</h2>
                          <p class="main_profile_text p-l-11">Level</p>
                          <p class="main_profile_text text-purple">{{ myInfo['user_level'] }}</p>
                          <p class="main_profile_text">Like</p>
                          <p class="main_profile_text text-purple">{{ myInfo['liked'] }}</p>
                        </div>
                      </div>
                      <!-- 티어, 포지션, 게임유형 -->
                      <hr class="widthFull" />
                      <div class="mt-3">
                        <div class="main_game_info">
                          <div class="col-md-4 padding_none">
                            <div class="gray-block m-r-4 p-t-2" style="height: 109px">
                              티어
                              <img rounded class="main_profile_picture" :src="myTierImg" />
                              <p class="text13">{{ myInfo.tier }}</p>
                            </div>
                          </div>
                          <div class="col-md-4 padding_none">
                            <div class="gray-block m-l-4 m-r-4 p-t-2" style="height: 109px">
                              포지션
                              <img
                                v-if="myInfo.liked_position !== '선호하는 포지션이 없습니다.'"
                                rounded
                                class="main_profile_picture"
                                :src="myPositionImg"
                              />
                              <p
                                v-if="myInfo.liked_position !== '선호하는 포지션이 없습니다.'"
                                class="text13"
                              >
                                {{ myInfo['liked_position'] }}
                              </p>
                              <p v-else class="text13">---</p>
                            </div>
                          </div>
                          <div class="col-md-4 padding_none">
                            <div class="gray-block m-l-4 p-t-2" style="height: 109px">
                              게임유형
                              <img rounded class="main_profile_picture" :src="myGameImg" />
                              <p class="text13">{{ myInfo['game_style'] }}</p>
                            </div>
                          </div>
                        </div>
                        <div class="gray-block m-t-10 profile_b_block p-t-4 p-b-4">
                          <p class="sameLine m-r-10 m-b-1">{{ myInfo['wins'] }}승</p>
                          <p class="sameLine m-r-10 m-l-5 m-b-1">{{ myInfo['losses'] }}패</p>
                          <p class="sameLine m-l-5 m-b-1">승률 {{ winRate }}%</p>
                        </div>
                        <div class="gray-block m-t-10 profile_b_block p-t-4 p-b-4">
                          <!-- 플레이 타임은 데이터에 없음 -->
                          <p class="sameLine m-r-10 m-b-1">주로 플레이하는 TIME</p>
                          <p class="sameLine m-b-1 text-purple">{{ myInfo.time_predict }}</p>
                          <p class="sameLine m-l-3 m-b-1">시</p>
                        </div>

                        <!-- 유저가 게임중일 때만 경기 분석 창이 뜸 -->
                        <!-- 경기 중이 아닐 때는 Game.vue에서 에러 있음 -->
                        <button @click="goIngame" class="btn btn-primary m-t-15">
                          실시간 경기분석
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 멤버 목록 -->
                <div class="card mt-3" style="height: 604px">
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li
                        class="d-flex justify-content-between align-items-center flex-wrap p-t-10 p-l-5 m-b-15"
                      >
                        <img src="@/assets/img/main/member_title.png" class="sub_title_chat" />
                        <i
                          class="fa fa-refresh people_like_icon m-l-5"
                          aria-hidden="true"
                          @click="refreshMember"
                        ></i>
                      </li>
                      <div class="card-body" style="height: 460px">
                        <div v-for="(member, index) in memberList" :key="index">
                          <div
                            v-if="
                              (currentPageMember - 1) * 8 <= index && index < currentPageMember * 8
                            "
                          >
                            <li
                              class="list-group-item d-flex justify-content-between align-items-center flex-wrap "
                            >
                              <p class="text-secondary marginMember" @click="moveToChat(member.your_nickname)">{{ member.your_nickname }}</p>
                              <div class="isOnline" v-if="member.connection_check === 1">
                                <i class="fa fa-circle online_icon" aria-hidden="true"></i>
                                {{ online[0] }}
                              </div>
                              <div class="isOnline" v-else>
                                <i class="fa fa-circle offline_icon" aria-hidden="true"></i>
                                {{ online[1] }}
                              </div>
                            </li>
                            <hr class="m-t-8 widthFull" />
                          </div>
                        </div>
                      </div>
                    </ul>
                    <!-- pagination -->
                    <div class="pagination">
                      <b-pagination
                        v-model="currentPageMember"
                        :total-rows="rowsMember"
                        :per-page="perPageMember"
                        size="lg"
                        class="pagination_height"
                        aria-controls="recommend-table"
                      ></b-pagination>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="main-body">
            <img src="@/assets/img/main/not_login.png" class="not_login" />
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Member from '../components/member.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'Main',
  components: {
    Member,
  },
  data() {
    return {
      newRow: 1,
      // 내 정보
      myInfo: {},
      // 검색 정보
      yourInfo: {},
      // 검색 닉네임
      yourNick: '',
      // 승률
      winRate: '',
      // 추천 유저
      recommendedUser: {},
      // 추천 유저 모든 정보
      recommendedAll: {},
      newdataAll: {},
      // 포지션 select
      selectedPosition: '전체',
      positions: [
        { item: '전체', name: '전체' },
        { item: '탑', name: '탑' },
        { item: '정글', name: '정글' },
        // { item: 'jug', name: '정글' },
        { item: '미드', name: '미드' },
        { item: '원딜', name: '원딜' },
        { item: '서포터', name: '서포터' },
        // { item: 'sup', name: '서포터' },
      ],
      // 게임 유형 select
      selectedType: '전체',
      types: [
        { item: '전체', name: '전체' },
        { item: '솔랭', name: '솔랭' },
        // { item: 'solo', name: '솔로랭크' },
        { item: '자랭', name: '자랭' },
        // { item: 'free', name: '자유랭크' },
        { item: '칼바람나락', name: '칼바람나락' },
      ],
      // 접속 상태 select
      selectedStatus: 'all',
      status: [
        { item: 'all', name: '전체' },
        { item: 'on', name: '접속자만' },
      ],
      // 티어 Slider
      sliderValue: 'all',
      sliderData: [
        'all',
        'Iron',
        'Bronze',
        'Silver',
        'Gold',
        'Platinum',
        'Diamond',
        'Master',
        'Grandmaster',
        'Challenger',
      ],
      // 추천 멤버리스트
      memberList: '',
      // 추천 pagination
      perPage: 6,
      currentPage: 1,
      perPage2: 6,
      currentPage2: 1,
      // 멤버 pagination
      perPageMember: 8,
      currentPageMember: 1,
      value: 75, // 승률 progress
      online: ['online', 'offline'], // 접속 여부
      where: 'main',
      myIcon: 1,
      myWinRate: '',
      toggleVaule: '',
      msg: '',
      // 게임 유형 이미지
      gameTypeImgs: [
        // 솔랭, 자랭, 전체
        '/img/gametype/솔랭.png',
        // 칼바람나락
        '/img/gametype/칼바람.png',
      ],
      // 나의 게임 유형 이미지
      myGameImg: '',
      // 포지션 별 이미지
      positionTypeImgs: [
        '/img/position/탑.png',
        '/img/position/미드.png',
        '/img/position/정글.png',
        '/img/position/원딜.png',
        '/img/position/서포터.png',
      ],
      // 나의 포지션 이미지
      myPositionImg: '',
      // 티어 별 이미지
      tierTypeImgs: [
        '/img/tier/Unranked.png',
        '/img/tier/Iron.png',
        '/img/tier/Bronze.png',
        '/img/tier/Silver.png',
        '/img/tier/Gold.png',
        '/img/tier/Platinum.png',
        '/img/tier/Diamind.png',
        '/img/tier/Master.png',
        '/img/tier/Grandmaster.png',
        '/img/tier/Challenger.png',
      ],
      // 내 티어 이미지
      myTierImg: '',
      isSelected: false,
      newRow2: 1,
    };
  },
  computed: {
    ...mapGetters([
      'getMyInfo',
      'nickName',
      'getRecommendedUser',
      'getAllRecommendedUser',
      'getLikeList',
    ]),
    rows() {
      return this.newdataAll.length;
    },
    rows2() {
      return this.recommendedUser.length;
    },
    rowsMember() {
      return this.memberList.length;
    },
  },
  created() {
    if (this.nickName !== null) {
      this.getIcon();
      this.getInfo();
      this.AllRecommendUser();
      this.likeList();

      if (this.getMyInfo.connection_check == 1) this.toggleVaule = true;
      else this.toggleVaule = false;
    }
  },
  methods: {
    // 토글 메소드
    onChangeEventHandler() {
      if (this.myInfo.connection_check === 1) {
        this.$store
          .dispatch('toggleOff')
          .then(() => {
            this.getInfo();
            this.msg = this.$store.getters.getMessage;
          })
          .catch(({ message }) => (this.error = message));
      } else {
        this.$store
          .dispatch('toggleOn')
          .then(() => {
            this.getInfo();
            this.msg = this.$store.getters.getMessage;
          })
          .catch(({ message }) => (this.error = message));
      }
    },

    // 내 아이콘 받아오기
    getIcon() {
      this.$store
        .dispatch('getIconUrl', this.nickName)
        .then(() => {
          this.myIcon = this.$store.getters.getChatIcon;
        })
        .catch(({ message }) => (this.error = message));
    },
    // 사용자 정보 가져오기
    getInfo() {
      this.$store
        .dispatch('getInfo')
        .then(() => {
          this.myInfo = this.$store.getters.getMyInfo;
          if (Number(this.myInfo.wins) == 0) this.winRate = 0;
          else {
            var num =
              (Number(this.myInfo.wins) / (Number(this.myInfo.wins) + Number(this.myInfo.losses))) *
              100;
            this.winRate = Math.ceil(num);
          }
          this.error = this.$store.getters.getMessage;

          // 만약 게임스타일이 all로 나온다면 전체로 바꿔준다.(UI 통일)
          if (this.myInfo['game_style'] === 'all') this.myInfo['game_style'] = '전체';
          // 만약 선호하는 포지션이 없다고 나오면 탑으로 바꿔준다. (UI 개선)
          if (this.myInfo['liked_position'] === '선호하는 포지션이 없습니다.')
            this.myInfo['liked_position'] = '탑';

          // 티어 이미지 넣기
          if (this.myInfo['tier'] === 'Unranked') {
            this.myTierImg = this.tierTypeImgs[0];
          } else if (this.myInfo['tier'] === 'Iron') {
            this.myTierImg = this.tierTypeImgs[1];
          } else if (this.myInfo['tier'] === 'Bronze') {
            this.myTierImg = this.tierTypeImgs[2];
          } else if (this.myInfo['tier'] === 'Silver') {
            this.myTierImg = this.tierTypeImgs[3];
          } else if (this.myInfo['tier'] === 'Gold') {
            this.myTierImg = this.tierTypeImgs[4];
          } else if (this.myInfo['tier'] === 'Platinum') {
            this.myTierImg = this.tierTypeImgs[5];
          } else if (this.myInfo['tier'] === 'Diamind') {
            this.myTierImg = this.tierTypeImgs[6];
          } else if (this.myInfo['tier'] === 'Master') {
            this.myTierImg = this.tierTypeImgs[7];
          } else if (this.myInfo['tier'] === 'Grandmaster') {
            this.myTierImg = this.tierTypeImgs[8];
          } else {
            this.myTierImg = this.tierTypeImgs[9];
          }

          // 포지션 이미지 넣기
          if (this.myInfo['liked_position'] === '탑') {
            this.myPositionImg = this.positionTypeImgs[0];
          } else if (this.myInfo['liked_position'] === '미드') {
            this.myPositionImg = this.positionTypeImgs[1];
          } else if (this.myInfo['liked_position'] === '정글') {
            this.myPositionImg = this.positionTypeImgs[2];
          } else if (this.myInfo['liked_position'] === '원딜') {
            this.myPositionImg = this.positionTypeImgs[3];
          } else {
            this.myPositionImg = this.positionTypeImgs[4];
          }

          // 게임유형 이미지 넣기
          if (
            this.myInfo['game_style'] === '솔랭' ||
            this.myInfo['game_style'] === '자랭' ||
            this.myInfo['game_style'] === '전체'
          ) {
            this.myGameImg = this.gameTypeImgs[0];
          } else {
            this.myGameImg = this.gameTypeImgs[1];
          }

          var check_btn = document.getElementById('toggleBtn');
          if (this.myInfo.connection_check === 1) {
            check_btn.setAttribute(':value', true);
            this.toggleVaule = true;
          } else {
            this.toggleVaule = false;
            check_btn.setAttribute(':value', false);
          }
        })
        .catch(({ message }) => (this.error = message));
      this.$store.commit('setMessage', null);
    },
    // 경기 분석 보러가기
    goIngame() {
      this.$swal
        .fire({
          title: '현재 플레이하고 있습니까?',
          text:
            '현재 플레이 중인 게임에 한해서만 승률분석이 가능합니다! 분석에는 30초정도 소요됩니다.',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: '보러가기',
        })
        .then((result) => {
          if (result.isConfirmed) {
            this.$router.push(`/game`);
          }
        });
    },
    // 추천 유저
    RecommendUser() {
      this.recommendedUser = {};
      let index = 0;
      for (let i = 0; i < this.recommendedAll.length; i++) {
        if (
          this.recommendedAll[i].liked_position == this.selectedPosition &&
          this.recommendedAll[i].game_style == this.selectedType &&
          (this.recommendedAll[i].connection_check == 0 ||
            this.recommendedAll[i].connection_check == 1) &&
          this.selectedStatus == 'all'
        ) {
          this.recommendedUser[index] = this.recommendedAll[i];
          index++;
        } else if (
          this.recommendedAll[i].liked_position == this.selectedPosition &&
          this.recommendedAll[i].game_style == this.selectedType &&
          this.recommendedAll[i].connection_check == 1 &&
          this.selectedStatus == 'on'
        ) {
          this.recommendedUser[index] = this.recommendedAll[i];
          index++;
        }
        this.newRow2 = index;
      }
      this.isSelected = true;
    },
    // 추천 유저 모든 정보
    AllRecommendUser() {
      this.$store
        .dispatch('AllRecommendUser')
        .then(() => {
          this.recommendedAll = this.$store.getters.getAllRecommendedUser;
          this.error = this.$store.getters.getMessage;

          var numIndex = 0;
          for (var item = 0; item < this.recommendedAll.length; item++) {
            this.newdataAll[numIndex] = this.recommendedAll[item];
            numIndex++;
          }
          this.newRow = numIndex;
        })
        .catch(({ message }) => (this.error = message));
    },
    // 좋아요 누른 멤버 목록 새로고침
    refreshMember() {
      this.likeList();
    },
    // 좋아요 누른 멤버 목록
    likeList() {
      this.$store.dispatch('likeList').then(() => {
        this.memberList = this.$store.getters.getLikeList;
        this.error = this.$store.getters.getMessage;
      });
    },
    // 검색 시 모달창
    showModal: function() {
      this.$swal
        .fire({
          title: '<h1>' + this.yourInfo['nickname'] + '</h1>',
          html:
            '<table style="width : 100%; height: 280px;" border="1"><tr><td><b>티어</b></td><td style="width: 50%;">' +
            this.yourInfo['tier'] +
            '</td></tr>' +
            '<tr><td><b>레벨</b></td><td>' +
            this.yourInfo['user_level'] +
            '</td></tr>' +
            '<tr><td><b>선호하는 포지션</b></td><td>' +
            this.yourInfo['liked_position'] +
            '</td></tr>' +
            '<tr><td><b>게임 유형</b></td><td>' +
            this.yourInfo['game_style'] +
            '</td></tr>' +
            '<tr><td><b>Like</b></td><td>' +
            this.yourInfo['liked'] +
            '</td></tr>' +
            '<tr><td><b>승</b></td><td>' +
            this.yourInfo['wins'] +
            '승</td></tr>' +
            '<tr><td><b>패</b></td><td>' +
            this.yourInfo['losses'] +
            '패</td></tr>' +
            '<tr><td><b>승률</b></td><td>' +
            this.win_value +
            '%</td></tr></table>',
          showCloseButton: true,
          showDenyButton: true,
          denyButtonText: '신고',
          focusConfirm: false,
          confirmButtonText:'친구등록', 
        })
        .then((result) => {
          if(result.isConfirmed){
            this.likePlus( this.yourInfo['nickname'])
          }
          if (result.isDenied) {
            this.$store.commit('setMessage', 'declare');
            this.$router.push(`/declare`);
          }
        });

      // 초기화
      var searchInput = document.getElementById('searchInput');
      searchInput.value = '';
    },
    // 유저 검색
    getInfoYou: function() {
      this.$store
        .dispatch('getInfoYou', this.yourNick)
        .then(() => {
          this.yourInfo = this.$store.getters.getYourInfo;

          // 승률 계산
          if (Number(this.yourInfo.wins) == 0) this.win_value = 0;
          else {
            var num =
              (Number(this.yourInfo.wins) /
                (Number(this.yourInfo.wins) + Number(this.yourInfo.losses))) *
              100;
            this.win_value = Math.ceil(num);
          }

          this.showModal();
        })
        .catch(({ message }) => (this.error = message));
    },
    // 검색창에서 실행하는 함수
    searchUser: function(event) {
      this.yourNick = event.target.value;
      this.getInfoYou(this.yourNick);
    },
    dataMake() {
      this.isSelected = false;
      var numIndex = 0;
      for (var item = 0; item < this.recommendedAll.length; item++) {
        if (this.sliderValue == 'all') {
          this.newdataAll[numIndex] = this.recommendedAll[item];
          numIndex++;
        } else if (this.recommendedAll[item].tier == this.sliderValue) {
          this.newdataAll[numIndex] = this.recommendedAll[item];
          numIndex++;
        }
      }
      this.newRow = numIndex;
    },
    moveToChat(nickName) {
      let params = new FormData();
      params.append('jwt', localStorage.getItem('jwt'));
      params.append('yourNickName', nickName);
      params.append('messageData', '새채팅');

      this.$store.dispatch('sendDm', params).then(() => {
        this.$router.replace('/chat');
      });
  },
    likePlus(nickName){
      const form = new FormData();
      form.append('jwt', this.$store.getters.getJWT);
      form.append('yourNickname', nickName);
      this.$store
          .dispatch('like', form)
          .then(() => {
            this.message = this.$store.getters.message;
          })
          .catch(({ message }) => (this.error = message));
    },
  },
};
</script>
<style scoped>
@import '../assets/css/main.css';
@import '../assets/css/user.css';
</style>
