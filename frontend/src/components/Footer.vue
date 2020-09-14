<template>
  <v-footer dark padless>
    <v-card width="100%" flat tile>
      <v-card-text class="text-center">퀀티파이</v-card-text>
      <v-divider class="mx-4" inset></v-divider>
      <v-card-text>
        <v-row>
          <v-col cols="12" sm="4" md="3" offset-sm="2" offset-md="3">
            <p class="ma-0">
              <span class="font-weight-bold">공동대표</span>
              &nbsp; 김주형, 박세종, 심효빈, 김보성
            </p>
            <p class="ma-0">
              <span class="font-weight-bold">주소</span>
              &nbsp; 역삼역 멀티캠퍼스
            </p>
          </v-col>
          <v-col cols="12" sm="4" md="3">
            <p class="ma-0">
              <span class="font-weight-bold">전화</span>
              &nbsp; 010-8388-1652
            </p>
            <p class="ma-0">
              <span class="font-weight-bold">이메일</span>
              &nbsp; bwjubrother@gmail.com
            </p>
          </v-col>
          <v-col class="text-center" cols="12">
            © 2020 —
            <strong>퀀티파이</strong>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      //
    };
  },
};
</script>