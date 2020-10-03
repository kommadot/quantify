<template>
  <v-container id="icons" fluid tag="section">
    <base-material-card color="#1F4E70" dark>
      <template v-slot:heading>
        <div class="display-2 font-weight-light">퀀트 투자의 시작 Quantify</div>
      </template>

      <template>
        <v-card>
          <v-tabs background-color="gray" color="#1F4E70" fixed-tabs dark>
            <v-tab>종목정보</v-tab>
            <v-tab>퀀트전략</v-tab>
            <v-tab>모의투자</v-tab>
            <v-tab>백테스트</v-tab>

            <!-- 퀀트전략 -->
            <v-tab-item>
              <v-container fluid style="background-color: gray">
                <v-row>
                  <v-col cols="12" sm="6" lg="3">
                    <base-material-stats-card
                      :value="samsung"
                      color="red"
                      icon="mdi-arrow-up"
                      title="삼성전자"
                      sub-icon="mdi-clock"
                      sub-text="Just Updated"
                    />
                  </v-col>

                  <v-col cols="12" sm="6" lg="3">
                    <base-material-stats-card
                      :value="kakao"
                      color="red"
                      icon="mdi-arrow-up"
                      title="카카오"
                      sub-icon="mdi-clock"
                      sub-text="Just Updated"
                    />
                  </v-col>

                  <v-col cols="12" sm="6" lg="3">
                    <base-material-stats-card
                      :value="hyundaiCar"
                      color="red"
                      icon="mdi-arrow-up"
                      title="현대차"
                      sub-icon="mdi-clock"
                      sub-text="Just Updated"
                    />
                  </v-col>

                  <v-col cols="12" sm="6" lg="3">
                    <base-material-stats-card
                      :value="naver"
                      color="blue"
                      icon="mdi-arrow-down"
                      title="네이버"
                      sub-icon="mdi-clock"
                      sub-text="Just Updated"
                    />
                  </v-col>
                </v-row>
              </v-container>
            </v-tab-item>

            <v-tab-item>
              <v-container fluid style="background-color: gray">
                <v-card>
                  <v-toolbar flat color="#1F4E70" dark>
                    <v-toolbar-title>전략 소개</v-toolbar-title>
                  </v-toolbar>
                  <v-tabs vertical color="#1F4E70">
                    <v-tab>
                      <v-icon left>mdi-account</v-icon>
                      저변동성 전략
                    </v-tab>
                    <v-tab>
                      <v-icon left>mdi-lock</v-icon>
                      모멘텀 전략
                    </v-tab>
                    <v-tab>
                      <v-icon left>mdi-access-point</v-icon>
                      밸류 전략
                    </v-tab>
                    <v-tab>
                      <v-icon left>mdi-access-point</v-icon>
                      퀄리티 전략
                    </v-tab>

                    <v-tab-item>
                      <v-card flat>
                        <v-card-text>
                          <p>
                            변동성이 적은 주식은 장기적으로 시장에 영향을 많이
                            받는 주식들보다 수익률이 좋고 보다 안정적인 수익을
                            기대할 수 있습니다.
                          </p>
                        </v-card-text>
                      </v-card>
                    </v-tab-item>
                    <v-tab-item>
                      <v-card flat>
                        <v-card-text>
                          <p>
                            투자에서 모멘텀이란 주가 혹은 이익의 추세로서, 상승
                            추세의 주식은 지속적으로 상승하는 경향을 보입니다.
                          </p>
                          <p>
                            1년간의 수익률과 변동성을 고려한 위험조정 수익률을
                            제공합니다.
                          </p>
                        </v-card-text>
                      </v-card>
                    </v-tab-item>
                    <v-tab-item>
                      <v-card flat>
                        <v-card-text>
                          <p>
                            가치주 전략은 내재 가치 대비 낮은 가격의 주식(저PER,
                            저PBR 등)이, 내재 가치 대비 비싼 주식보다 수익률이
                            높은 현상을 이용합니다. PER, PBR, PSR에 각 기업의
                            순위를 매겨 종합 순위가 낮은 주식을 추천합니다.
                          </p>
                        </v-card-text>
                      </v-card>
                    </v-tab-item>
                    <v-tab-item>
                      <v-card flat>
                        <v-card-text>
                          <p>
                            퀄리티 전략은 기업의 재무제표 데이터를 활용하여
                            기업의 우량성 정도를 나타내는 F-score를 계산합니다.
                            수익성, 수익의 안정성, 기업 구조, 수익의 성장성,
                            회계적 우량성, 배당, 투자등의 가치를 종합적으로
                            분석합니다.
                          </p>
                        </v-card-text>
                      </v-card>
                    </v-tab-item>
                  </v-tabs>
                </v-card>
              </v-container>
            </v-tab-item>

            <!-- 모의투자 -->
            <v-tab-item>
              <!-- <v-container fluid style="background-color: gray"> -->
              <v-card class="mx-auto" width="100%">
                <v-img
                  class="white--text align-end"
                  height="200px"
                  src="@/assets/invest.png"
                >
                  <v-card-title>모의투자</v-card-title>
                </v-img>

                <v-card-subtitle class="pb-0"> 모의투자란 </v-card-subtitle>

                <v-card-text class="text--primary">
                  <div>
                    모의투자는 가상화폐를 이용하여 투자를 흉내 내어 보는 것으로
                    실제 재산을 잃을 걱정 없이 투자 기술을 익히고 훈련할 수
                    있도록 하는 것으로
                  </div>

                  <div>
                    많은 초보자분들이 모의 투자를 통하여 연습을 하면서 매수
                    타이밍, 매도 타이밍 등등 다양한 기술들을 익히고 공부해 볼 수
                    있습니다.
                  </div>
                </v-card-text>
              </v-card>
              <!-- </v-container> -->
            </v-tab-item>

            <!-- 백테스팅 -->
            <v-tab-item>
              <!-- <v-container fluid style="background-color: gray"> -->
              <v-card class="mx-auto" width="100%">
                <v-img
                  class="black--text align-end"
                  height="200px"
                  src="@/assets/backtest.png"
                >
                  <v-card-title>백테스팅</v-card-title>
                </v-img>

                <v-card-subtitle class="pb-0"> 백테스팅이란 </v-card-subtitle>

                <v-card-text class="text--primary">
                  <div>
                    백테스팅은 계량 투자에 있어서 가장 중요한 요소 중
                    하나입니다. 백테스팅이란 간단히 말해 '내가 이러한 투자
                    전략을 과거에 똑같이 적용했다면 성과가 어땠을까?'라는 질문에
                    대한 답변을 제공해는 역할을 한다고 볼 수 있습니다.
                  </div>

                  <div>
                    백테스팅을 통해 퀀티파이가 제공하는 각 전략들이 얼마나
                    신뢰성을 갖는지 테스트해보고 과거의 성과를 정확히 알고
                    투자하는 것은 굉장한 이점을 줄 수 있습니다.
                  </div>
                </v-card-text>
              </v-card>
              <!-- </v-container> -->
            </v-tab-item>
          </v-tabs>
        </v-card>
      </template>
    </base-material-card>
  </v-container>
</template>

<script>
import axios from "axios";
import http from "@/util/http-common";
import { mapState, mapActions } from "vuex";

export default {
  name: "",
  data() {
    return {
      stocks: [],
      samsung: 58200,
      kakao: 364500,
      hyundaiCar: 178500,
      naver: 296500,
    };
  },
  created() {
    this.getStocks();
  },
  methods: {
    getStocks() {
      http.get("/price/" + "005930").then((res) => {
        this.samsung = res.data.price;
      });
      http.get("/price/" + "035720").then((res) => {
        this.kakao = res.data.price;
      });
      http.get("/price/" + "005380").then((res) => {
        this.hyundaiCar = res.data.price;
      });
      http.get("/price/" + "035420").then((res) => {
        this.naver = res.data.price;
      });
    },
  },
};
</script>
