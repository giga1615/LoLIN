import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'; // 서버 통신
import jwt_decode from 'jwt-decode'; // jwt 디코드
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

//const SERVER_URL = 'http://localhost:8000';
const SERVER_URL = 'http://j4a104.p.ssafy.io:8080/api';
export default new Vuex.Store({
  // 여러 컴포넌트에 공유되는 데이터
  state: {
    jwt: null, // acess-token 로그인 세션
    message: null, // action응답을 vue로 건내줄때 사용
    iconNumber: null, // 롤 아이콘 번호
    userId: '', // 유저 아이디
    nickName: '', // 유저 닉네임
    dmList: {}, // 현재 대화중인 상대 닉네임
    urlList: {}, // 현재 대화중인 상대 아이콘 url 리스트
    roomList: {}, // 현재 참여중인 대화방 리스트
    countList: {}, // 현재 참여중인 대화방의 인원 수
    chatIcon: '', // 채팅프로필 아이콘번호
    roomMember: {}, // 채팅방에 참여중인 멤버
    dmData: {}, // dm 메세지
    chatRoomData: {}, // 단체채팅방 베세지
    allMember: {}, // 모든 회원
    recommendList: {}, // 추천된 유저 리스트
    inGameDataBlue: null, // 인게임 블루 승률예측
    inGameDataRed: null, // 인게임 레드 승률예측
    myInfo: null, // 내 정보(프로필)
    recommendedUser: null, // 추천된 사람 정보
    allRecommendedUser: null, // 추천된 사람 모든 정보
    likeList: null, // 내가 좋아요 누른 사람 목록
    yourInfo: null, // 상대 정보(검색)
  },

  // 연산된 state값을 접근
  getters: {
    // localStorage에 있는 jwt 리턴
    getJWT(state) {
      state.jwt = localStorage.getItem('jwt');
      axios.defaults.headers.common['jwt'] = state.jwt;
      return state.jwt;
    },
    // action에서 서버와 통신하고 받은 message 리턴
    getMessage(state) {
      return state.message;
    },
    // 롤 계정 아이콘 리턴
    iconNumber(state) {
      return state.iconNumber;
    },
    // 접속중인 email 리턴
    userId() {
      return localStorage.getItem('userId');
    },
    // 접속중인 nickname 리턴
    nickName() {
      return localStorage.getItem('nickName');
    },
    // 기억해 둔 idRemember 리턴
    getRememberId() {
      return localStorage.getItem('idRemember');
    },
    getDmList(state) {
      return state.dmList;
    },
    getRoomList(state) {
      return state.roomList;
    },
    getCountList(state) {
      return state.countList;
    },
    getChatIcon(state) {
      return state.chatIcon;
    },
    getRoomMember(state) {
      return state.roomMember;
    },
    getDmData(state) {
      return state.dmData;
    },
    getChatRoomData(state) {
      return state.chatRoomData;
    },
    getAllMember(state) {
      return state.allMember;
    },
    getChatRoomIcons(state) {
      return state.chatRoomIcons;
    },
    // 블루팀 예측
    getInGameDataBlue(state) {
      return state.inGameDataBlue;
    },
    // 레드팀 예측
    getInGameDataRed(state) {
      return state.inGameDataRed;
    },
    getMyInfo(state) {
      return state.myInfo;
    },
    // 추천 유저
    getRecommendedUser(state) {
      return state.recommendedUser;
    },
    // 추천 유저 모든 정보
    getAllRecommendedUser(state) {
      return state.allRecommendedUser;
    },
    // 좋아요 누른 멤버 리스트
    getLikeList(state) {
      return state.likeList;
    },
    // 상대 정보(검색)
    getYourInfo(state) {
      return state.yourInfo;
    },
  },

  plugins: [createPersistedState()],

  // state값을 변경하는 이벤트 로직/메서드
  mutations: {
    // message값을 value값으로 변경
    setMessage(state, value) {
      state.message = value;
    },
    // iconNumber 값을 저장
    setIcon(state, value) {
      state.iconNumber = value;
    },
    // 로그인 후 받은 jwt로 state, localStorage에 반영
    setJWT(state, jwt) {
      var decodedJWT = jwt_decode(jwt); // JWT 디코딩
      // store 변수 갱신
      state.jwt = jwt;
      state.userId = decodedJWT['id'];
      state.nickName = decodedJWT['nickName'];
      // localStorage 변수 갱신
      localStorage.setItem('jwt', jwt);
      localStorage.setItem('userId', state.userId);
      localStorage.setItem('nickName', state.nickName);
    },
    setDmList(state, value) {
      state.dmList = value;
    },
    setRoomList(state, value) {
      state.roomList = value;
    },
    setCountList(state, value) {
      state.countList = value;
    },
    setChatIcon(state, value) {
      state.chatIcon = value;
    },
    setRoomMember(state, value) {
      state.roomMember = value;
    },
    setDmData(state, value) {
      state.dmData = value;
    },
    setChatRoomData(state, value) {
      state.chatRoomData = value;
    },
    setAllMember(state, value) {
      state.allMember = value;
    },
    // 로그아웃
    LOGOUT(state) {
      state.jwt = null;
      state.userId = null;
      state.nickName = null;
      state.message = null;
    },
    // 아이디 기억하기
    setRememberId(state, value) {
      localStorage.setItem('idRemember', value);
    },
    // 인게임
    setInGameDataBlue(state, value) {
      state.inGameDataBlue = JSON.stringify({ 블루팀: value });
      state.inGameDataBlue = JSON.parse(state.inGameDataBlue);
    },
    setInGameDataRed(state, value) {
      state.inGameDataRed = JSON.stringify({ 레드팀: value });
      state.inGameDataRed = JSON.parse(state.inGameDataRed);
    },
    setMyInfo(state, value) {
      state.myInfo = value;
    },
    // 추천 유저
    setRecommendedUser(state, value) {
      state.recommendedUser = value;
    },
    // 추천 유저 모든 정보
    setAllRecommendedUser(state, value) {
      state.allRecommendedUser = value;
    },
    setLikeList(state, value) {
      state.likeList = value;
    },
    // 상대 정보(검색)
    setYourInfo(state, value) {
      state.yourInfo = value;
    },
  },

  // 비동기처리 로직을 선언하는 메서드
  // vue에서 actions에 있는 메소드 호출 -> 서버와 통신 -> mutations메소드 호출하여 state값 변경
  actions: {
    // 회원가입1 : 롤 아이콘 조회
    getIcon(context, user) {
      return axios
        .get(`${SERVER_URL}/member/make/auth/makeRandomNumber`, {
          params: { nickName: user },
        })
        .then((response) => {
          context.commit('setMessage', response.data['message']); // message에 저장
          context.commit('setIcon', response.data['iconNumber']); // iconNumber에 저장
        });
    },
    // 회원가입2-1 : 아이콘 변경되었는지 확인
    checkChange(context, user) {
      return axios
        .get(`${SERVER_URL}/member/make/authImgChangeCheck`, {
          params: { nickName: user },
        })
        .then((response) => {
          context.commit('setMessage', response.data['message']); // message에 저장
        });
    },
    // 회원가입2-2 : 존재하는 아이디인지 확인
    isExist(context, user) {
      return axios
        .get(`${SERVER_URL}/member/membershipCheck`, {
          params: { id: user },
        })
        .then((response) => {
          context.commit('setMessage', response.data['message']); // message에 저장
        });
    },
    // 회원가입3 : 회원가입 실행
    signUp(context, user) {
      return axios.post(`${SERVER_URL}/member/make`, user).then((response) => {
        context.commit('setMessage', response.data['message']); // 응답을 message에 저장
        // 회원가입 성공 -> 로그인 요청하여 jwt받아오기
        if (response.data['message'] === 'SUCCESS') {
          let form = new FormData();
          form.append('id', user.get('id'));
          form.append('pw', user.get('pw'));
          return axios.post(`${SERVER_URL}/member/login`, form).then((response2) => {
            // 받아온 jwt로 predictTime호출
            if (response2.data['message'] === 'SUCCESS') {
              return axios
                .get(`${SERVER_URL}/member/executeInitPredictTime`, {
                  params: { jwt: response2.data['jwt'] },
                })
                .then((response3) => {
                  if (response3.data['message'] === 'SUCCESS') {
                    context.commit('setMessage', response.data['message']); // 응답을 message에 저장
                  }
                })
                .catch((error) => {
                  error.response;
                  context.commit('setMessage', response.data['message']); // 응답을 message에 저장
                });
            }
          });
        }
      });
    },
    // 로그인 실행
    LOGIN(context, user) {
      return axios.post(`${SERVER_URL}/member/login`, user).then((response) => {
        context.commit('setMessage', response.data['message']); // 응답을 message에 저장
        if (response.data['message'] === 'SUCCESS') context.commit('setJWT', response.data['jwt']); // 응답을 mutations으로 전달
      });
    },
    getDmList(context) {
      return axios
        .get(`${SERVER_URL}/chat/readDmList`, {
          params: {
            jwt: localStorage.getItem('jwt'),
          },
        })
        .then((response) => {
          context.commit('setDmList', response.data['dmList']);
          context.commit('setMessage', response.data['message']);
        });
    },
    getRoomList(context) {
      return axios
        .get(`${SERVER_URL}/chat/showMyRoomList`, {
          params: {
            jwt: localStorage.getItem('jwt'),
          },
        })
        .then((response) => {
          context.commit('setRoomList', response.data['myRoomList']);
          context.commit('setCountList', response.data['countList']);
          context.commit('setMessage', response.data['message']);
        });
    },
    getIconUrl(context, nickName) {
      return axios
        .get(`${SERVER_URL}/member/getIconNo`, {
          params: {
            jwt: localStorage.getItem('jwt'),
            nickName: nickName,
          },
        })
        .then((response) => {
          context.commit('setChatIcon', response.data['iconNo']);
          context.commit('setMessage', response.data['message']);
        });
    },
    makeChatRoom(context, room) {
      return axios.post(`${SERVER_URL}/chat/makeChatRoom`, room).then((response) => {
        context.commit('setMessage', response.data['message']);
      });
    },
    getRoomMemberList(context, roomNo) {
      return axios
        .get(`${SERVER_URL}/chat/roomMemberList`, {
          params: {
            jwt: localStorage.getItem('jwt'),
            roomNumber: roomNo,
          },
        })
        .then((response) => {
          context.commit('setRoomMember', response.data['memberList']);
          context.commit('setMessage', response.data['message']);
        });
    },
    getAllDms(context, nickName) {
      return axios
        .get(`${SERVER_URL}/chat/readDm`, {
          params: {
            jwt: localStorage.getItem('jwt'),
            yourNickName: nickName,
          },
        })
        .then((response) => {
          context.commit('setDmData', response.data['dmData']);
          context.commit('setMessage', response.data['message']);
        });
    },
    getAllChatRooms(context, roomNo) {
      return axios
        .get(`${SERVER_URL}/chat/detail/ReadAll/chattingRoom`, {
          params: {
            jwt: localStorage.getItem('jwt'),
            roomNumber: roomNo,
          },
        })
        .then((response) => {
          context.commit('setChatRoomData', response.data['allMessage']);
          context.commit('setMessage', response.data['message']);
        });
    },
    sendDm(context, data) {
      return axios.post(`${SERVER_URL}/chat/sendDm`, data).then((response) => {
        context.commit('setMessage', response.data['message']);
      });
    },
    sendRoom(context, data) {
      return axios
        .post(`${SERVER_URL}/chat/detail/sendMessage/chattingRoom`, data)
        .then((response) => {
          context.commit('setMessage', response.data['message']);
        });
    },
    inviteMember(context, data) {
      return axios.post(`${SERVER_URL}/chat/inviteMember`, data).then((response) => {
        context.commit('setMessage', response.data['message']);
      });
    },
    getAllMember(context) {
      return axios
        .get(`${SERVER_URL}/member/getAllNickName`, {
          params: {
            jwt: localStorage.getItem('jwt'),
          },
        })
        .then((response) => {
          context.commit('setAllMember', response.data['memberList']);
          context.commit('setMessage', response.data['message']);
        });
    },
    // 로그아웃
    LOGOUT(context) {
      axios.defaults.headers.common['jwt'] = undefined;
      const form = new FormData();
      form.append('jwt', localStorage.getItem('jwt'));
      return axios.post(`${SERVER_URL}/member/logout`, form).then((response) => {
        context.commit('setMessage', response.data['message']);
        // localStorage에 저장된 값 지우기
        localStorage.removeItem('jwt');
        localStorage.removeItem('userId');
        localStorage.removeItem('nickName');
        // muatation에 있는 state값 날리기
        context.commit('LOGOUT');
      });
    },
    // 아이디 기억하기
    setRememberId(context, value) {
      context.commit('setRememberId', value);
    },
    // 승부 예측
    getIngame(context) {
      return axios
        .get(`http://j4a104.p.ssafy.io:8080/api/bigdata/inGame`, {
          params: {
            jwt: localStorage.getItem('jwt'),
            nickName: localStorage.getItem('nickName'),
          },
        })
        .then((response) => {
          context.commit('setInGameDataBlue', response.data['블루팀']);
          context.commit('setInGameDataRed', response.data['레드팀']);
        });
    },
    // 신고하기
    declare(context, form) {
      return axios.post(`${SERVER_URL}/file/upload`, form).then((response) => {
        context.commit('setMessage', response.data['message']);
      });
    },
    // 내 정보
    getInfo(context) {
      return axios
        .get(`${SERVER_URL}/recommend/getMyInfo`, {
          params: {
            jwt: localStorage.getItem('jwt'),
          },
        })
        .then((response) => {
          context.commit('setMyInfo', response.data);
        });
    },
    // 추천 유저
    RecommendUser(context, user) {
      return axios
        .get(`${SERVER_URL}/recommend/getRecommendedUser`, {
          params: {
            jwt: localStorage.getItem('jwt'),
            selectedGameStyle: user.get('selectedGameStyle'),
            selectedPosition: user.get('selectedPosition'),
          },
        })
        .then((response) => {
          context.commit('setRecommendedUser', response.data);
        });
    },
    // 추천 유저 전체 조회
    AllRecommendUser(context) {
      return axios
        .get(`${SERVER_URL}/recommend/getRecommendedUserAll`, {
          params: {
            jwt: localStorage.getItem('jwt'),
          },
        })
        .then((response) => {
          context.commit('setAllRecommendedUser', response.data);
        });
    },
    // 접속 off : 로그아웃할 때 부르는 애랑 똑같음
    toggleOff(context) {
      const form = new FormData();
      form.append('jwt', localStorage.getItem('jwt'));
      return axios.post(`${SERVER_URL}/member/logout`, form).then((response) => {
        context.commit('setMessage', response.data['message']);
      });
    },
    // 접속 on
    toggleOn(context) {
      const form = new FormData();
      form.append('jwt', localStorage.getItem('jwt'));
      return axios.put(`${SERVER_URL}/member/connectionOn`, form).then((response) => {
        context.commit('setMessage', response.data['message']);
      });
    },
    // 좋아요 멤버리스트
    likeList(context) {
      return axios
        .get(`${SERVER_URL}/like/ilikeU/readMyList`, {
          params: {
            jwt: localStorage.getItem('jwt'),
          },
        })
        .then((response) => {
          context.commit('setLikeList', response.data);
        });
    },
    // 상대 정보(검색)
    getInfoYou(context, nickName) {
      return axios
        .get(`${SERVER_URL}/recommend/getYourInfo`, {
          params: {
            jwt: localStorage.getItem('jwt'),
            yourNickname: nickName,
          },
        })
        .then((response) => {
          context.commit('setYourInfo', response.data);
        });
    },
    like(context, form) {
      return axios.post(`${SERVER_URL}/like/ilikeU/plus`, form).then((response) => {
        context.commit('setMessage', response.data['message']);
      });
    },
    dislike(context, form) {
      return axios
        .delete(`${SERVER_URL}/like/ilikeU/minus`, {
          params: {
            jwt: form.get('jwt'),
            yourNickname: form.get('yourNickname'),
          },
        })
        .then((response) => {
          context.commit('setMessage', response.data);
        });
    },
  },
});
