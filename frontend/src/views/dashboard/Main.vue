<template>
  <v-container id="icons" fluid tag="section">
    <base-material-card color="success" dark>
      <template v-slot:heading>
        <div class="display-2 font-weight-light">퀀트 투자의 시작 Quantify</div>
      </template>

      <template>
        <v-card>
          <v-tabs
            background-color="gray"
            color="green accent-4"
            fixed-tabs
            dark
          >
            <v-tab>종목정보</v-tab>
            <v-tab>퀀트전략</v-tab>
            <v-tab>모의투자</v-tab>
            <v-tab>백테스트</v-tab>

            <!-- 종목정보 -->
            <v-tab-item>
              <v-container fluid style="background-color: gray">
                <p>다양한 퀀트 전략</p>
              </v-container>
            </v-tab-item>

            <!-- 퀀트전략 -->
            <v-tab-item>
              <v-container fluid style="background-color: gray">
                <v-card>
                  <v-toolbar flat color="green" dark>
                    <v-toolbar-title>전략 소개</v-toolbar-title>
                  </v-toolbar>
                  <v-tabs vertical>
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
              <v-container fluid style="background-color: gray">
                <p>다양한 퀀트 전략</p>
              </v-container>
            </v-tab-item>

            <!-- 백테스트 -->
            <v-tab-item>
              <v-container fluid style="background-color: gray">
                <p>다양한 퀀트 전략</p>
              </v-container>
            </v-tab-item>
          </v-tabs>
        </v-card>
      </template>
    </base-material-card>
  </v-container>
</template>

<script>
</script>
