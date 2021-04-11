<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : 멤버 컴포넌트 불필요한 주석 삭제
    * 생성일자 : 2021-04-05
    * 최종수정일자 : 2021-04-06
  -->

  <div>
    <div class="isOnline m-b-10" v-if="where === 'main' && member.connection_check === 1">
      <i class="fa fa-circle online_icon" aria-hidden="true"></i>
      online
    </div>
    <div class="isOnline m-b-10" v-else-if="where === 'main'">
      <i class="fa fa-circle offline_icon" aria-hidden="true"></i>
      offline
    </div>

    <!-- 유저정보 -->
    <div class="m-b-20 recommend-title">
      <img
        :src="`http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/${myIcon}.png`"
        alt="Admin"
        class="rounded-circle profile_icon"
        style="width: 50px"
      />
      <div class="nextLine">
        <div class="w-100 padding0">
          <h3 id="memberNick" class="recommend_profile_id body-rule">{{ member.nickname }}</h3>
          <i
            v-if="where === 'main' && isLike === 'off'"
            :id="`likeBtn_${index}`"
            class="fa fa-heart people_like_icon m-l-5"
            aria-hidden="true"
            @click="changeLike"
          ></i>
          <i
            v-else-if="where === 'main'"
            :id="`likeBtn_${index}`"
            class="fa fa-heart people_like_icon m-l-5 heartBtn"
            aria-hidden="true"
            @click="changeLike"
          ></i>
        </div>
        <div class="nextLine">
          <p class="main_profile_text p-l-11">Level</p>
          <p class="main_profile_text text-purple">{{ member.user_level }}</p>
          <p class="main_profile_text">Like</p>
          <p class="main_profile_text text-purple">{{ member.liked }}</p>
        </div>
      </div>
    </div>

    <div class="win-padding">
      <hr class="widthFull " />
    </div>

    <!-- 티어, 랭킹, 타입 -->
    <div class="user_game_info ">
      <div class="block3">
        <div class="gray-block2 p-t-2 ">
          <img rounded class="recommend_profile_picture" :src="myTierImg" />
          {{ member.tier }}
        </div>
      </div>
      <div class="block3">
        <div class="gray-block2  p-t-2 ">
          <img rounded class="recommend_profile_picture" :src="myPositionImg" />
          <div v-if="member.liked_position !== '선호하는 포지션이 없습니다.'">
            {{ member.liked_position }}
          </div>
          <div v-else>
            ---
          </div>
        </div>
      </div>
      <div class="block3">
        <div class="gray-block2  p-t-2">
          <img rounded class="recommend_profile_picture" :src="myGameImg" />
          {{ member.game_style }}
        </div>
      </div>
    </div>

    <!-- 승률 -->
    <div class="win-padding">
      <p class="sameLine m-r-10 m-b-1">{{ member.wins }}승</p>
      <p class="sameLine m-r-10 m-l-5 m-b-1">{{ member.losses }}패</p>
      <p class="sameLine m-l-5 m-b-1">승률 {{ this.win_value }}%</p>
      <b-progress height="15px" :value="win_value" show-progress class="mb-3 m-t-5"></b-progress>
    </div>

    <!-- 채팅버튼 -->
    <div class="m-t-30 make_chat_btn">
      <b-button v-if="where === 'main'" variant="outline-secondary main_rec_btn" @click="moveToChat"
        ><i class="fa fa-paper-plane-o people_like_icon m-r-8" aria-hidden="true"></i
        >채팅하기</b-button
      >
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  props: ['index', 'member', 'value', 'online', 'where'],
  computed: {
    ...mapGetters(['getLikeList']),
  },
  data() {
    return {
      isLike: 'off',
      myIcon: '',
      win_value: '',
      winRate: '',
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
      map: [],
      likeList: '',
    };
  },
  created() {
    // 유저 아이콘
    this.getIcon();

    // 승률 계산
    if (Number(this.member.wins) == 0) this.win_value = 0;
    else {
      var num =
        (Number(this.member.wins) / (Number(this.member.wins) + Number(this.member.losses))) * 100;
      this.win_value = Math.ceil(num);
    }

    // 티어, 포지션, 게임유형 아이콘 적용
    // 만약 게임스타일이 all로 나온다면 전체로 바꿔준다.(UI 통일)
    if (this.member['game_style'] === 'all') this.member['game_style'] = '전체';
    // 만약 선호하는 포지션이 없다고 나오면 탑으로 바꿔준다. (UI 개선)
    if (this.member['liked_position'] === '선호하는 포지션이 없습니다.')
      this.member['liked_position'] = '탑';

    // 티어 이미지 넣기
    if (this.member['tier'] === 'Unranked') {
      this.myTierImg = this.tierTypeImgs[0];
    } else if (this.member['tier'] === 'Iron') {
      this.myTierImg = this.tierTypeImgs[1];
    } else if (this.member['tier'] === 'Bronze') {
      this.myTierImg = this.tierTypeImgs[2];
    } else if (this.member['tier'] === 'Silver') {
      this.myTierImg = this.tierTypeImgs[3];
    } else if (this.member['tier'] === 'Gold') {
      this.myTierImg = this.tierTypeImgs[4];
    } else if (this.member['tier'] === 'Platinum') {
      this.myTierImg = this.tierTypeImgs[5];
    } else if (this.member['tier'] === 'Diamind') {
      this.myTierImg = this.tierTypeImgs[6];
    } else if (this.member['tier'] === 'Master') {
      this.myTierImg = this.tierTypeImgs[7];
    } else if (this.member['tier'] === 'Grandmaster') {
      this.myTierImg = this.tierTypeImgs[8];
    } else {
      this.myTierImg = this.tierTypeImgs[9];
    }

    // 포지션 이미지 넣기
    if (this.member['liked_position'] === '탑') {
      this.myPositionImg = this.positionTypeImgs[0];
    } else if (this.member['liked_position'] === '미드') {
      this.myPositionImg = this.positionTypeImgs[1];
    } else if (this.member['liked_position'] === '정글') {
      this.myPositionImg = this.positionTypeImgs[2];
    } else if (this.member['liked_position'] === '원딜') {
      this.myPositionImg = this.positionTypeImgs[3];
    } else {
      this.myPositionImg = this.positionTypeImgs[4];
    }

    // 게임유형 이미지 넣기
    if (
      this.member['game_style'] === '솔랭' ||
      this.member['game_style'] === '자랭' ||
      this.member['game_style'] === '전체'
    ) {
      this.myGameImg = this.gameTypeImgs[0];
    } else {
      this.myGameImg = this.gameTypeImgs[1];
    }

    // 좋아요 여부 반영
    this.likeList = this.$store.getters.getLikeList;
    this.setLike();
  },
  methods: {
    // 좋아요 여부 반영
    setLike() {
      for (var i = 0; i < this.likeList.length; i++) {
        if (this.likeList[i].your_nickname === this.member.nickname) {
          this.isLike = 'on';
        }
      }
    },
    // 내 아이콘 받아오기
    getIcon() {
      this.$store
        .dispatch('getIconUrl', this.member.nickname)
        .then(() => {
          this.myIcon = this.$store.getters.getChatIcon;
        })
        .catch(({ message }) => (this.error = message));
    },
    // 채팅으로 이동하기
    moveToChat() {
      let params = new FormData();
      params.append('jwt', localStorage.getItem('jwt'));
      params.append('yourNickName', this.member.nickname);
      params.append('messageData', '새채팅');

      this.$store.dispatch('sendDm', params).then(() => {
        this.$router.replace('/chat');
      });
    },
    // 좋아요
    changeLike() {
      const form = new FormData();
      form.append('jwt', this.$store.getters.getJWT);
      form.append('yourNickname', this.member.nickname);

      if (this.isLike === 'off') {
        this.isLike = 'on';
        this.$store
          .dispatch('like', form)
          .then(() => {
            this.message = this.$store.getters.message;
          })
          .catch(({ message }) => (this.error = message));
      } else {
        this.isLike = 'off';
        this.$store
          .dispatch('dislike', form)
          .then(() => {
            this.message = this.$store.getters.message;
          })
          .catch(({ message }) => (this.error = message));
      }
    },
  },
};
</script>

<style scoped>
@import '../assets/css/main.css';
@import '../assets/css/user.css';
</style>
