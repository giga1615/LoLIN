<template>
  <div>
    <div class="container">
      <div class="chatlist">
        <ChatList> </ChatList>
      </div>
      <div class="message-container">
        <!-- 채팅창 상단 ( 닉네임 or 단톡 이름 ) -->
        <div class="yournick" v-if="nickNameClicked == true">
          <img class="icon" v-bind:src="yourIcon" /> {{ yourNick }}
        </div>
        <div class="yournick" v-if="roomnickNameClicked == true">
          <img class="icon" src="@/assets/img/chat/group.png" />
          {{ chatRoomName }}
        </div>
        <!-- 아무것도 클릭 되지 않았을 때 -->
        <div class="character" v-if="nickNameClicked == false && roomnickNameClicked == false">
          <img class="teemo" src="@/assets/img/user/login_character.png" />
          <div class="start">채팅을 시작해보세요 !</div>
        </div>
        <div v-else class="messages">
          <ul class="only-msg" v-if="nickNameClicked == true && roomnickNameClicked == false">
            <div
              class=""
              :class="{ you: item.yourNickName === myNick }"
              v-for="item in messages"
              :key="item.dmNo"
            >
              <!-- 받는사람이 나이고 보내는 사람이 채팅 방 이름 -->
              <div
                class="your-msg-box you"
                v-if="item.yourNickName === myNick && yourNick === item.myNickName"
              >
                <div class="chat-icon">
                  <img class="icon" v-bind:src="yourIcon" />
                </div>
                <div class="nick-msg">
                  <div class="chat-nick">{{ item.myNickName }}</div>
                  <div class="chat-msg">{{ item.messageData }}</div>
                  <br />
                </div>
              </div>
              <!-- 내가 보냈고, 채팅방이름이 받는사람인거 -->
              <div
                v-else-if="item.myNickName === myNick && yourNick === item.yourNickName"
                class="my"
              >
                <div class="my-msg-box">
                  <div class="my-chat-msg">{{ item.messageData }}</div>
                  <br />
                </div>
              </div>
            </div>
          </ul>
          <ul v-if="(roomnickNameClicked == true) & (nickNameClicked == false)">
            <li
              class="msg-box"
              :class="{ you: item.yourNickName != myNick }"
              v-for="(item, index) in roomMessages"
              :key="index"
            >
              <div class="your-msg-box" v-if="item.nickName != myNick">
                <div class="chat-icon">
                  <img v-bind:src="map[item.nickName]" class="icon" />
                </div>
                <div class="nick-msg">
                  <div class="chat-nick">{{ item.nickName }}</div>
                  <div class="chat-msg">{{ item.messageData }}</div>
                  <br />
                </div>
              </div>
              <div class="my-msg-box" v-else>
                <div class="my-chat-msg">{{ item.messageData }}</div>
                <br />
              </div>
            </li>
          </ul>
        </div>
        <div class="sendform" v-if="(nickNameClicked == true) | (roomnickNameClicked == true)">
          <input
            class="input"
            type="text"
            v-model="inputMessage"
            placeholder="메세지를 입력해주세요"
            @keypress.enter="onSubmit"
          />
          <div class="submit-btn" @click="onSubmit">보내기</div>
        </div>
      </div>
      <div class="friend" v-if="roomnickNameClicked == true">
        <div class="chat_buttons">
          <img class="invite" src="@/assets/img/chat/copy.png" @click="copyAll" />
          <img class="invite" src="@/assets/img/chat/plus2.png" @click="showModal" />
        </div>
        <!-- 대화 참여중인 멤버 리스트 -->
        <div>
          <ul>
            <li class="nickname" v-for="member in memberList" :key="member" @click="copy(member)">
              {{ member }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ChatList from '../../components/chat/ChatList.vue';
import { EventBus } from '@/EventBus.js';

export default {
  components: {
    ChatList,
  },
  data: function() {
    return {
      myNick: this.$store.state.nickName,
      iconNo: this.$store.state.iconNumber,
      yourNick: '',
      yourIcon: '',
      membersIcon: {},
      roomNumber: '',
      chatRoomName: '',
      inputRoomName: '',
      nickname: '',
      memberList: {},
      recommendUsers: ['굿또', '숏다리의꿈', '꼬마자동차붕봉'],
      allMembers: {},
      messages: {
        dmNO: '',
        createTime: '',
        myNickName: '',
        yourNickName: '',
        messageData: '',
      },
      roomMessages: {
        roomNo: '',
        roomName: '',
        id: '',
        createTime: '',
        nickName: '',
        messageData: '',
      },
      nickNameClicked: false,
      roomnickNameClicked: false,
      inputMessage: '',
      error: '',
      profiles: [
        '/img/profile1.png',
        '/img/profile2.png',
        '/img/profile3.png',
        '/img/profile4.png',
        '/img/profile5.png',
      ],
      map: [],
    };
  },
  methods: {
    copyAll: function() {
      this.$copyText(this.memberList).then(
        function(e) {
          alert('Copied');
          console.log(e);
        },
        function(e) {
          alert('Can not copy');
          console.log(e);
        }
      );
    },
    copy: function(member) {
      this.$copyText(member).then(
        function(e) {
          alert('Copied');
          console.log(e);
        },
        function(e) {
          alert('Can not copy');
          console.log(e);
        }
      );
    },
    showModal: function() {
      this.$swal.fire({
        title: '유저 초대',
        text: '닉네임을 입력해주세요',
        input: 'text',
        showCloseButton: true,
        confirmButtonText: '초대',
        allowOutsideClick: () => !this.$swal.isLoading(),
        preConfirm: (nickname) => {
          try {
            const response = this.searchNickName(nickname);
            if (response === 'FAIL') {
              throw new Error(response.statusText);
            } else {
              this.inviteUser(nickname);
              return nickname;
            }
          } catch (error) {
            this.$swal.showValidationMessage(`닉네임이 존재하지 않습니다 : ${error}`);
          }
        },
      });
    },
    getAllDms: function(yourNick) {
      this.$store
        .dispatch('getAllDms', yourNick)
        .then(() => {
          this.messages = this.$store.getters.getDmData;
          this.error = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.error = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    getMessages: function() {
      this.$store
        .dispatch('getAllChatRooms', this.roomNumber)
        .then(() => {
          this.roomMessages = this.$store.getters.getChatRoomData;
          this.error = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.error = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    // 채팅방에 참여중인 멤버 목록
    getMemberInRoom: function(roomNo) {
      this.$store
        .dispatch('getRoomMemberList', roomNo)
        .then(() => {
          this.memberList = this.$store.getters.getRoomMember;
          this.error = this.$store.getters.getMessage;
          for (let i = 0; i < this.memberList.length; i++) {
            this.map[this.memberList[i]] = this.profiles[i];
          }
        })
        .catch(({ message }) => (this.error = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    onSubmit: function() {
      if (this.nickNameClicked == true) {
        const params = new URLSearchParams();
        params.append('jwt', localStorage.getItem('jwt'));
        params.append('yourNickName', this.yourNick);
        params.append('messageData', this.inputMessage);

        this.$store
          .dispatch('sendDm', params)
          .then(() => {
            this.error = this.$store.getters.getMessage;
          })
          .catch(({ message }) => (this.error = message));
        // 초기화(메세지 재사용 위해)
        this.$store.commit('setMessage', null);
      } else if (this.roomnickNameClicked == true) {
        const params = new URLSearchParams();
        params.append('jwt', localStorage.getItem('jwt'));
        params.append('roomNumber', this.roomNumber);
        params.append('messageData', this.inputMessage);

        this.$store
          .dispatch('sendRoom', params)
          .then(() => {
            this.error = this.$store.getters.getMessage;
          })
          .catch(({ message }) => (this.error = message));
        // 초기화(메세지 재사용 위해)
        this.$store.commit('setMessage', null);
      }
      this.inputMessage = '';
    },
    inviteUser: function(nickname) {
      const params = new URLSearchParams();
      params.append('jwt', localStorage.getItem('jwt'));
      params.append('roomName', this.chatRoomName);
      params.append('memberNickName', nickname);
      this.$store
        .dispatch('inviteMember', params)
        .then(() => {
          this.error = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.error = message));
      this.$store.commit('setMessage', null);
    },
    getAllMember: function() {
      this.$store
        .dispatch('getAllMember')
        .then(() => {
          this.allMembers = this.$store.getters.getAllMember;
          this.error = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.error = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    searchNickName: function(nickname) {
      if (this.allMembers.includes(nickname)) {
        return 'SUCCESS';
      } else return 'FAIL';
    },
    getYourIcon: function(yourNick) {
      this.$store
        .dispatch('getIconUrl', yourNick)
        .then(() => {
          let iconNo = this.$store.getters.getChatIcon;
          this.yourIcon =
            'http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/' + iconNo + '.png';
          this.message = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.msg = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
  },
  created: function() {
    EventBus.$on('nickname', (data) => {
      this.yourNick = data;
      this.getYourIcon(this.yourNick);
      this.nickNameClicked = true;
      this.roomnickNameClicked = false;
      setInterval(() => this.getAllDms(this.yourNick), 2000);
    });
    EventBus.$on('roomName', (data) => {
      this.chatRoomName = data;
    });
    EventBus.$on('roomNumber', (data) => {
      this.roomNumber = data;
      this.roomnickNameClicked = true;
      this.nickNameClicked = false;
      setInterval(() => this.getMessages(), 2000);
      setInterval(() => this.getMemberInRoom(this.roomNumber), 2000);
    });

    this.getAllMember();
  },
  computed: {},
};
</script>

<style scoped>
.container {
  float: center;
}
.chatlist {
  display: inline-block;
  width: 300px;
  float: left;
  overflow-y: auto;
  /* 디브 정렬 해주는거 */
}
.message-container {
  background-color: white;
  display: inline-block;
  padding: 10px;
  width: 600px;
  height: 700px;
  border: 1px solid #efefef;
  border-radius: 10px;
  float: left;
  margin-top: 50px;
}
.messages {
  background-color: white;
  display: inline-block;
  padding: 10px;
  width: 580px;
  height: 560px;
  float: left;
  overflow-y: auto;
}
.friend {
  background-color: white;
  display: inline-block;
  width: 200px;
  height: 700px;
  border: 1px solid #efefef;
  border-radius: 10px;
  float: left;
  margin-top: 50px;
  overflow-y: auto;
}

.yournick {
  border-bottom: 1px solid #d1d1d1;
  margin-bottom: 10px;
}
.chat-icon {
  float: left;
}
.nick-msg {
  margin: 10px;
  margin-left: 50px;
}
.chat-nick {
  margin-left: 12px;
  font-size: 8pt;
}
.chat-msg {
  margin-left: 5px;
  padding: 10px;
  height: 40px;
  border: 1px solid #c4c4c4;
  background-color: #fcfcfc;
  border-radius: 20px;
}
.my-chat-msg {
  color: black;
}
.msg-box {
  height: 50px;
  display: block;
  position: relative;
}
.my {
  height: 80px;
}
.you {
  height: 80px;
}
.your-msg-box {
  display: inline-block;
}
.my-msg-box {
  float: right;
  display: inline-block;
  margin-left: 5px;
  padding: 10px;
  height: 40px;
  background-color: #bf98ff9f;
  background-image: linear-gradient(to left, #cf87f8c5, #81d7ff);
  border-radius: 20px;
  clear: both;
  margin-bottom: 20px;
}
.nickname {
  border-bottom: 1px solid #efefef;
  margin: 20px;
  text-align: center;
}
.input {
  display: inline-block;
  border-radius: 20px;
  width: 500px;
  height: 50px;
  border: 1px solid #c4c4c4;
}
.submit-btn {
  display: inline-block;
  text-align: center;
  margin-left: 15px;
}
.invite {
  display: inline-block;
  width: 30px;
  height: 30px;
  float: right;
  margin-right: 10px;
  margin-top: 10px;
}
.chat_buttons {
  height: 40px;
}
.start_dm {
  display: inline-block;
  text-align: center;
  width: 200px;
  height: 50px;
  border: 1px solid #c4c4c4;
  border-radius: 20px;
}
.recommend {
  float: center;
}
.recommend-list {
  border-bottom: 1px solid #efefef;
  margin: 10px;
  text-align: left;
}
.character {
  text-align: center;
}
.teemo {
  margin-top: 50px;
  height: 400px;
}
.start {
  font-size: 16pt;
  font-weight: bold;
  font: #000000;
}
</style>
