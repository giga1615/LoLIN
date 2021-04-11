<template>
  <div>
    <div class="container">
      <!-- 회원가입 title -->
      <div class="signup_title" style="height: 50px">
        <div class="m-t-100 m-b-50" style="justify-content: center; display: flex">
          <img src="@/assets/img/user/game_title.png" class="sub_title" />
        </div>
      </div>
      <div>
        <header>
          <h1 style="color: #1f8ecd; font-family: 'Do Hyeon', sans-serif;">블루팀</h1>
          <hr />
          <h1 style="color: #ee5a52; font-family: 'Do Hyeon', sans-serif;">레드팀</h1>
        </header>
      </div>

      <!-- 승률 예측 그래프 -->
      <div class="progress" style="height: 35px; margin-bottom: 50px;">
        <!-- 블루팀 -->
        <div
          class="progress-bar  progress-bar-animated"
          style="background-color: #1f8ecd;"
          role="progressbar"
          :style="`width: ${(B_point / (B_point + R_point)) * 100}%`"
          aria-valuenow="35"
          aria-valuemin="0"
          :aria-valuemax="`${B_point + R_point}`"
        >
          <div class="progress-inner">
            <span
              >{{
                (
                  (inGameDataBlue['블루팀'][5]['Bt_point'] /
                    (inGameDataBlue['블루팀'][5]['Bt_point'] +
                      inGameDataRed['레드팀'][5]['Rt_point'])) *
                  100
                ).toFixed(0)
              }}%</span
            >
          </div>
        </div>
        <!-- 레드팀 -->
        <div
          class="progress-bar progress-bar-animated bg-danger"
          role="progressbar"
          :style="`width: ${(R_point / (B_point + R_point)) * 100}%`"
          aria-valuenow="30"
          aria-valuemin="0"
          :aria-valuemax="`${B_point + R_point}`"
        >
          <div class="progress-inner">
            <span
              >{{
                (
                  (inGameDataRed['레드팀'][5]['Rt_point'] /
                    (inGameDataBlue['블루팀'][5]['Bt_point'] +
                      inGameDataRed['레드팀'][5]['Rt_point'])) *
                  100
                ).toFixed(0)
              }}%</span
            >
          </div>
        </div>
      </div>

      <!-- 플레이어 정보 박스 -->
      <div class="playBox">
        <div class="SpectateSummoner">
          <div class="Box">
            <div class="Content">
              <!-- 블루팀 -->
              <table class="Table Team-100">
                <colgroup>
                  <col width="10" />
                  <col width="130" />
                </colgroup>
                <!-- 블루팀 상세 정보 제목 -->
                <thead class="Header">
                  <tr class="Row">
                    <th class="HeaderCell Bar"></th>
                    <th class="HeaderCell TeamName">블루팀</th>
                    <th class="HeaderCell" colspan="2">S2021</th>
                    <th class="HeaderCell">랭크 승률</th>
                    <th class="HeaderCell">챔피언 명</th>
                    <th class="HeaderCell">S2021 챔피언 승률</th>
                    <th class="HeaderCell">S2021 챔피언 KDA</th>
                  </tr>
                </thead>
                <!-- 블루팀 상세 정보 내용 -->
                <tbody class="Body" v-for="item in list" :key="item">
                  <tr class="Row first">
                    <!-- 닉네임 셀 -->
                    <td class="nickName Cell" colspan="2">
                      <span style="font-weight: bold;">{{
                        inGameDataBlue['블루팀'][item]['nickName']
                      }}</span>
                    </td>

                    <!-- 현재 티어 셀 (이미지)-->
                    <td class="CurrentSeasonTier Cell">
                      <img :src="inGameDataBlue['블루팀'][item]['tierImg']" alt="" />
                    </td>

                    <!-- 현재 티어 셀 -->
                    <td class="CurrentSeasonTierRank Cell">
                      <div class="TierRank">
                        <span style="font-weight: bold;">{{
                          inGameDataBlue['블루팀'][item]['tier']
                        }}</span>
                      </div>
                    </td>

                    <!-- 랭크 승률 셀 -->
                    <td class="RankedWinRatio Cell">
                      <!-- 승률이 50% 미만이면(회색) -->
                      <div v-if="parseFloat(inGameDataBlue['블루팀'][item]['rankWinRate']) < 50">
                        <span class="Ratio" style="color: #879292;"
                          >{{ inGameDataBlue['블루팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill bg-secondary"
                            role="progressbar"
                            :style="`width: ${inGameDataBlue['블루팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                      <!-- 랭크 기록이 없으면 -->
                      <div v-else-if="inGameDataBlue['블루팀'][item]['rankWinRate'] == '-'">
                        <span class="Ratio" style="color: #879292;">{{
                          inGameDataBlue['블루팀'][item]['rankWinRate']
                        }}</span>
                      </div>
                      <!-- 승률 50% ~ 59% 일 때(녹색) -->
                      <div
                        v-else-if="
                          50 <= parseFloat(inGameDataBlue['블루팀'][item]['rankWinRate']) &&
                            parseFloat(inGameDataBlue['블루팀'][item]['rankWinRate']) < 60
                        "
                      >
                        <span class="Ratio" style="color: #36a4a4;"
                          >{{ inGameDataBlue['블루팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill bg-success"
                            role="progressbar"
                            :style="`width: ${inGameDataBlue['블루팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                      <!-- 승률 60% ~ 69%(파란색)  -->
                      <div
                        v-else-if="
                          60 <= parseFloat(inGameDataBlue['블루팀'][item]['rankWinRate']) &&
                            parseFloat(inGameDataBlue['블루팀'][item]['rankWinRate']) < 70
                        "
                      >
                        <span class="Ratio" style="color: #3d95e5;"
                          >{{ inGameDataBlue['블루팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill"
                            role="progressbar"
                            :style="`width: ${inGameDataBlue['블루팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                      <!-- 승률 70% 이상(주황색) -->
                      <div v-else style="color: #e37727;">
                        <span class="Ratio"
                          >{{ inGameDataBlue['블루팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill bg-warning"
                            role="progressbar"
                            :style="`width: ${inGameDataBlue['블루팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                    </td>

                    <!-- 챔피언 이름 셀 -->
                    <td class="ChampionName Cell">
                      <span class="Ratio">{{ inGameDataBlue['블루팀'][item]['champName'] }}</span>
                    </td>

                    <!-- 챔피언 승률 셀 -->
                    <td class="ChampionInfo Cell">
                      <div
                        class="WinRatio"
                        v-if="inGameDataBlue['블루팀'][item]['champWinRate'] != '-'"
                      >
                        <span class="Ratio"
                          >{{ inGameDataBlue['블루팀'][item]['champWinRate'].split('%')[0] }}%</span
                        >
                        <span class="Ratio">{{
                          inGameDataBlue['블루팀'][item]['champWinRate'].split('%')[1]
                        }}</span>
                      </div>
                      <div v-else>
                        <span class="Ratio">{{
                          inGameDataBlue['블루팀'][item]['champWinRate'].split('%')[0]
                        }}</span>
                      </div>
                    </td>

                    <!-- 챔피언 KDA 셀 -->
                    <td class="ChampionInfo Cell">
                      <!-- KDA가 3 미만일 때 -->
                      <div
                        v-if="parseFloat(inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]) < 3"
                      >
                        <span class="Ratio" style="color: #879292;">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- KDA가 3 이상 4 미만일 때 -->
                      <div
                        v-else-if="
                          3 <= parseFloat(inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]) &&
                            parseFloat(inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]) < 4
                        "
                      >
                        <span class="Ratio" style="color: #36a4a4;">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- KDA가 4 이상 5 미만일 때 -->
                      <div
                        v-else-if="
                          4 <= parseFloat(inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]) &&
                            parseFloat(inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]) < 5
                        "
                      >
                        <span class="Ratio" style="color: #3d95e5;">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- KDA가 5 이상이거나 perfect 일 때 -->
                      <div
                        v-else-if="
                          5 <= parseFloat(inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]) ||
                            inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0] == 'Perfect'
                        "
                      >
                        <span class="Ratio" style="color: #e37727;">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataBlue['블루팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- kda가 없을 때 -->
                      <div v-else>
                        <span class="Ratio">{{ inGameDataBlue['블루팀'][item]['kda'] }}</span>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>

              <!-- 레드팀 -->
              <table class="Table Team-200">
                <colgroup>
                  <col width="10" />
                  <col width="130" />
                </colgroup>
                <!-- 레드팀 상세 정보 제목 -->
                <thead class="Header">
                  <tr class="Row">
                    <th
                      class="HeaderCell Bar"
                      style="border: 1px solid #c6443e; background-color: #ee5a52;"
                    ></th>
                    <th class="HeaderCell TeamName" style="color: #ee5a52;">레드팀</th>
                    <th class="HeaderCell" colspan="2">S2021</th>
                    <th class="HeaderCell">랭크 승률</th>
                    <th class="HeaderCell">챔피언 명</th>
                    <th class="HeaderCell">S2021 챔피언 승률</th>
                    <th class="HeaderCell">S2021 챔피언 KDA</th>
                  </tr>
                </thead>
                <!-- 레드팀 상세 정보 내용 -->
                <tbody class="Body" v-for="item in list" :key="item">
                  <tr class="Row first">
                    <!-- 닉네임 셀 -->
                    <td class="nickName Cell" colspan="2">
                      <span style="font-weight: bold;">{{
                        inGameDataRed['레드팀'][item]['nickName']
                      }}</span>
                    </td>

                    <!-- 현재 티어 셀 (이미지)-->
                    <td class="CurrentSeasonTier Cell">
                      <img :src="inGameDataRed['레드팀'][item]['tierImg']" alt="" />
                    </td>

                    <!-- 현재 티어 셀 -->
                    <td class="CurrentSeasonTierRank Cell">
                      <div class="TierRank">
                        <span style="font-weight: bold;">{{
                          inGameDataRed['레드팀'][item]['tier']
                        }}</span>
                      </div>
                    </td>

                    <!-- 랭크 승률 셀 -->
                    <td class="RankedWinRatio Cell">
                      <!-- 승률이 50% 미만이면(회색) -->
                      <div v-if="parseFloat(inGameDataRed['레드팀'][item]['rankWinRate']) < 50">
                        <span class="Ratio" style="color: #879292;"
                          >{{ inGameDataRed['레드팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill bg-secondary"
                            role="progressbar"
                            :style="`width: ${inGameDataRed['레드팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                      <!-- 랭크 기록이 없으면 -->
                      <div v-else-if="inGameDataRed['레드팀'][item]['rankWinRate'] == '-'">
                        <span class="Ratio" style="color: #879292;">{{
                          inGameDataRed['레드팀'][item]['rankWinRate']
                        }}</span>
                      </div>
                      <!-- 승률 50% ~ 59% 일 때(녹색) -->
                      <div
                        v-else-if="
                          50 <= parseFloat(inGameDataRed['레드팀'][item]['rankWinRate']) &&
                            parseFloat(inGameDataRed['레드팀'][item]['rankWinRate']) < 60
                        "
                      >
                        <span class="Ratio" style="color: #36a4a4;"
                          >{{ inGameDataRed['레드팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill bg-success"
                            role="progressbar"
                            :style="`width: ${inGameDataRed['레드팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                      <!-- 승률 60% ~ 69%(파란색)  -->
                      <div
                        v-else-if="
                          60 <= parseFloat(inGameDataRed['레드팀'][item]['rankWinRate']) &&
                            parseFloat(inGameDataRed['레드팀'][item]['rankWinRate']) < 70
                        "
                      >
                        <span class="Ratio" style="color: #3d95e5;"
                          >{{ inGameDataRed['레드팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill"
                            role="progressbar"
                            :style="`width: ${inGameDataRed['레드팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                      <!-- 승률 70% 이상(주황색) -->
                      <div v-else style="color: #e37727;">
                        <span class="Ratio"
                          >{{ inGameDataRed['레드팀'][item]['rankWinRate'] }}%</span
                        >
                        <div class="Progress">
                          <div
                            class="progress-bar Fill bg-warning"
                            role="progressbar"
                            :style="`width: ${inGameDataRed['레드팀'][item]['rankWinRate']}%`"
                            aria-valuemin="0"
                            aria-valuemax="100"
                          ></div>
                        </div>
                      </div>
                    </td>

                    <!-- 챔피언 이름 셀 -->
                    <td class="ChampionName Cell">
                      <span class="Ratio">{{ inGameDataRed['레드팀'][item]['champName'] }}</span>
                    </td>

                    <!-- 챔피언 승률 셀 -->
                    <td class="ChampionInfo Cell">
                      <div
                        class="WinRatio"
                        v-if="inGameDataRed['레드팀'][item]['champWinRate'] != '-'"
                      >
                        <span class="Ratio"
                          >{{ inGameDataRed['레드팀'][item]['champWinRate'].split('%')[0] }}%</span
                        >
                        <span class="Ratio">{{
                          inGameDataRed['레드팀'][item]['champWinRate'].split('%')[1]
                        }}</span>
                      </div>
                      <div v-else>
                        <span class="Ratio">{{
                          inGameDataRed['레드팀'][item]['champWinRate'].split('%')[0]
                        }}</span>
                      </div>
                    </td>

                    <!-- 챔피언 KDA 셀 -->
                    <td class="ChampionInfo Cell">
                      <!-- KDA가 3 미만일 때 -->
                      <div
                        v-if="parseFloat(inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]) < 3"
                      >
                        <span class="Ratio" style="color: #879292;">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- KDA가 3 이상 4 미만일 때 -->
                      <div
                        v-else-if="
                          3 <= parseFloat(inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]) &&
                            parseFloat(inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]) < 4
                        "
                      >
                        <span class="Ratio" style="color: #36a4a4;">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- KDA가 4 이상 5 미만일 때 -->
                      <div
                        v-else-if="
                          4 <= parseFloat(inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]) &&
                            parseFloat(inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]) < 5
                        "
                      >
                        <span class="Ratio" style="color: #3d95e5;">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- KDA가 5 이상이거나 perfect 일 때 -->
                      <div
                        v-else-if="
                          5 <= parseFloat(inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]) ||
                            inGameDataRed['레드팀'][item]['kda'].split('KDA')[0] == 'Perfect'
                        "
                      >
                        <span class="Ratio" style="color: #e37727;">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[0]
                        }}</span>
                        <span class="Ratio">&nbsp;KDA</span>
                        <br />
                        <span class="Ratio">{{
                          inGameDataRed['레드팀'][item]['kda'].split('KDA')[1]
                        }}</span>
                      </div>
                      <!-- kda가 없을 때 -->
                      <div v-else>
                        <span class="Ratio">{{ inGameDataRed['레드팀'][item]['kda'] }}</span>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Game',
  computed: {
    ...mapGetters(['getInGameDataBlue', 'getInGameDataRed']),
  },
  data() {
    return {
      inGameDataBlue: {},
      inGameDataRed: {},
      list: [0, 1, 2, 3, 4],
      B_point: '',
      R_point: '',
    };
  },
  methods: {
    getIngame: function(nickName) {
      this.$store
        .dispatch('getIngame', nickName)
        .then(() => {
          this.inGameDataBlue = this.$store.getters.getInGameDataBlue;
          this.inGameDataRed = this.$store.getters.getInGameDataRed;

          this.B_point = this.inGameDataBlue['블루팀'][5]['Bt_point'];
          this.R_point = this.inGameDataRed['레드팀'][5]['Rt_point'];
          this.error = this.$store.getters.getMessage;
        })
        .catch(({ message }) => (this.error = message));
      this.$store.commit('setMessage', null);
    },
  },
  created: function() {
    this.getIngame();
  },
};
</script>

<style scoped>
@import '../../assets/css/user.css';
</style>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

header {
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}

header h1 {
  font-size: 40px;
  text-align: center;
}

.progress-inner {
  height: 100%;
  border-radius: 0px 10px 10px 0px;
}

.progress-inner span {
  position: relative;
  top: 20%;
  font-size: 20px;
}

.playBox .playBoxInner {
  position: relative;
  display: inline-block;
  max-height: 100%;
}

.Box {
  border: 1px solid #cdd2d2;
  border-radius: 4px;
  box-shadow: none;
}

.Content {
  background: #ededed;
}

.Table {
  width: 100%;
  table-layout: fixed;
  background-color: #f2f2f2;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
  display: table;
  box-sizing: border-box;
  text-indent: initial;
  border-color: grey;
}

thead {
  display: table-header-group;
  vertical-align: middle;
  border-color: inherit;
}

tr {
  display: table-row;
  vertical-align: inherit;
  border-color: inherit;
}

th {
  display: table-cell;
  vertical-align: inherit;
}

.SpectateSummoner > .Box > .Content > .Table.Team-100 > .Header > .Row > .HeaderCell.Bar {
  border: 1px solid #1a78ae;
  background-color: #1f8ecd;
}

.SpectateSummoner > .Box > .Content > .Table > .Header > .Row > .HeaderCell {
  padding: 9px 0 8px 0;
  font-size: 12px;
  color: #555e5e;
  text-align: center;
  font-weight: normal;
}

.SpectateSummoner > .Box > .Content > .Table.Team-100 > .Header > .Row > .TeamName {
  color: #1f8ecd;
}

.SpectateSummoner > .Box > .Content > .Table > .Header > .Row > .HeaderCell.TeamName {
  padding-left: 15px;
  text-align: left;
  font-size: 12px;
  font-weight: bold;
}

.SpectateSummoner > .Box > .Content > .Table > .Header > .Row > .HeaderCell {
  padding: 9px 0 8px 0;
  border-bottom: 1px solid #cdd2d2;
  font-size: 12px;
  background-color: #ededed;
  color: #555e5e;
  text-align: center;
  font-weight: normal;
}

tbody {
  display: table-row-group;
  vertical-align: middle;
  border-color: inherit;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row {
  height: 37px;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row.first > .Cell {
  padding-top: 3px;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row > .Cell.nickName {
  text-align: right;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row > .Cell.CurrentSeasonTier {
  text-align: center;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row > .Cell.ChampionName {
  text-align: center;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row > .Cell.CurrentSeasonTierRank {
  font-size: 12px;
  color: #879292;
}

div {
  display: block;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row > .Cell.RankedWinRatio {
  text-align: center;
  font-size: 11px;
  color: #879292;
  line-height: 13px;
}

.Ratio {
  font-weight: bold;
}

.Progress {
  height: 6px;
  border: 1px solid #b8bfbf;
  margin: 3px 5px;
}

.Fill {
  height: 100%;
  border: 1px solid #b8bfbf;
}

.SpectateSummoner > .Box > .Content > .Table > .Body > .Row > .Cell.ChampionInfo {
  text-align: center;
  font-size: 11px;
  color: #879292;
  line-height: 16px;
}

.SpectateSummoner
  > .Box
  > .Content
  > .Table
  > .Body
  > .Row
  > .Cell.ChampionInfo
  > .WinRatio
  > .Ratio {
  display: block;
  font-weight: bold;
}

colgroup {
  display: table-column-group;
}
</style>

<style scoped>
@import '../../assets/css/user.css';
</style>
