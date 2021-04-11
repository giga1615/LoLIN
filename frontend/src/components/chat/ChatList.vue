<template>
  <div>
    <div id="chat">
      <ul class="dmlist">
        <li class="my_nickname"><img class="my_icon" v-bind:src="iconUrl" /> {{ myNick }}</li>
        <!-- 대화중인 사람 닉네임 목록-->
        <li
          id="nickname"
          class="nickname_list"
          v-for="(user, index) in memberList"
          :key="index"
          @click="getYourNickName(user)"
        >
          <!-- 프로필 랜덤으로 돌려줄 필요 -->
          <img class="icon" src="@/assets/img/chat/profile1.png" /> {{ user }}
        </li>
        <!-- 내가 참여중인 채팅방 목록 -->
        <ul class="roomlist">
          <li
            class="myroom"
            v-for="(room, index) in roomList"
            :key="index"
            @click="getRoomNumber(room.roomNumber, room.roomName)"
          >
            <img class="icon" src="@/assets/img/chat/group.png" />
            {{ room.roomName }} ({{ countList[index] }})
          </li>
        </ul>
      </ul>
    </div>
    <img class="makeRoom" src="@/assets/img/chat/plus.png" @click="makeRoomModal" />
  </div>
</template>

<script>
import { EventBus } from '@/EventBus.js';

export default {
  name: 'ChatList',
  data: function() {
    return {
      jwt: localStorage.getItem('jwt'),
      myNick: '',
      iconNo: '',
      iconUrl: '',
      users: {
        nickname: '',
        icon: '',
        url: '',
      },
      memberList: {},
      roomList: {},
      countList: {},
      mesasge: '',
    };
  },
  methods: {
    makeRoomModal: function() {
      this.$swal
        .fire({
          title: '채팅방 만들기',
          text: '채팅방 이름을 입력해주세요',
          input: 'text',
          showCloseButton: true,
          confirmButtonText: '만들기',
          allowOutsideClick: () => !this.$swal.isLoading(),
        })
        .then((result) => {
          if (result.isConfirmed) {
            this.makeChatRoom(result.value);
            this.$swal.fire('채팅방을 만들었습니다!', '', 'success');
          }
        });
    },
    getDmList() {
      this.$store
        .dispatch('getDmList')
        .then(() => {
          this.memberList = this.$store.getters.getDmList;
          this.message = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.msg = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    getMyRoomList() {
      this.$store
        .dispatch('getRoomList')
        .then(() => {
          this.roomList = this.$store.getters.getRoomList;
          this.countList = this.$store.getters.getCountList;
          this.message = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.msg = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    getIcon: function(nickName) {
      this.$store
        .dispatch('getIconUrl', nickName)
        .then(() => {
          this.iconNo = this.$store.getters.getChatIcon;
          this.iconUrl =
            'http://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/' +
            this.iconNo +
            '.png';
          this.message = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.msg = message));
      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    makeChatRoom: function(roomName) {
      let params = new URLSearchParams();
      params.append('jwt', localStorage.getItem('jwt'));
      params.append('roomName', roomName);

      this.$store
        .dispatch('makeChatRoom', params)
        .then(() => {
          this.message = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.msg = message));

      // 초기화(메세지 재사용 위해)
      this.$store.commit('setMessage', null);
    },
    getYourNickName: function(nickname) {
      // Chat.vue로 현재 선택된 닉네임 넘겨줌
      EventBus.$emit('nickname', nickname);
    },
    getRoomNumber: function(roomNumber, roomName) {
      // 현재 선택된 방 번호, 이름 넘겨줌
      EventBus.$emit('roomNumber', roomNumber);
      EventBus.$emit('roomName', roomName);
    },
  },
  created: function() {
    this.myNick = this.$store.state.nickName;
    this.getIcon(this.myNick);
    this.getDmList();
    this.getMyRoomList();
    //setInterval(()=>this.getMyRoomList(),1000);
  },
};
</script>

<style>
#chat {
  background-color: white;
  height: 700px;
  margin-top: 50px;
  border-radius: 10px;
  padding: 2px;
  border: 1px solid #efefef;
}
.my_nickname {
  text-align: center;
  border-bottom: 1px solid #d1d1d1;
}
.my_icon {
  width: 40px;
  height: 40px;
  margin: 10px;
  border-radius: 50%;
}
.icon {
  width: 35px;
  height: 35px;
  margin: 10px;
  border-radius: 50%;
}
.dmlist {
  list-style: none;
}

.nickname_list {
  border-bottom: 1px solid #efefef;
  margin: 10px;
  text-align: left;
}
.roomlist {
  float: left;
}
.myroom {
  border-bottom: 1px solid #efefef;
  margin: 10px;
  text-align: left;
}
.count {
}
.nickname {
  margin: 20px;
}
.makeRoom {
  display: inline-block;
  width: 40px;
  height: 40px;
  float: left;
  margin-top: -50px;
  margin-left: 10px;
}
</style>
