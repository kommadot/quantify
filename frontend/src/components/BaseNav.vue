<template>
  <div>
    <nav
      class="navbar"
      :class="[
            {'navbar-expand-md': expand},
            {'navbar-transparent': transparent},
            {[`bg-${type}`]: type}
         ]"
    >
      <div :class="containerClasses">
        <slot name="brand">
          <router-link
            :to="$route.path"
            class="h4 mb-0 text-white text-uppercase d-none d-lg-inline-block"
          >{{$route.name}}</router-link>
        </slot>
        <navbar-toggle-button
          v-if="showToggleButton"
          :toggled="toggled"
          :target="contentId"
          @click.native.stop="toggled = !toggled"
        >
          <span class="navbar-toggler-icon"></span>
        </navbar-toggle-button>

        <div
          class="collapse navbar-collapse"
          :class="{show: toggled}"
          :id="contentId"
          v-click-outside="closeMenu"
        >
          <slot :close-menu="closeMenu"></slot>
        </div>
      </div>
    </nav>
    <!-- <div v-if="$route.name=='LowVariability'">
      <div class="px-5">
        <h6 class="text-white">변동성이 적은 주식은 장기적으로 시장에 영향을 많이 받는 주식들보다 수익률이 좋고 보다 안정적인 수익을 기대할 수 있습니다.</h6>
      </div>
    </div>
    <div v-else-if="$route.name=='Momentum'">
      <div class="px-5">
        <h4 class="text-white">
          투자에서 모멘텀이란 주가 혹은 이익의 추세로서, 상승 추세의 주식은 지속적으로 상승하는 경향을 보입니다.
          <br />1년간의 수익률과 변동성을 고려한 위험조정 수익률을 제공합니다.
        </h4>
      </div>
    </div>
    <div v-else-if="$route.name=='ValueStrategy'">
      <div class="px-5">
        <h4 class="text-white">
          가치주 전략은 내재 가치 대비 낮은 가격의 주식(저PER, 저PBR 등)이, 내재 가치 대비 비싼 주식보다 수익률이 높은 현상을 이용합니다.
          <br />PER, PBR, PSR에 각 기업의 순위를 매겨 종합 순위가 낮은 주식을 추천합니다.
        </h4>
      </div>
    </div>
    <div v-else-if="$route.name=='QualityStrategy'">
      <div class="px-5">
        <h4 class="text-white">
          퀄리티 전략은 기업의 재무제표 데이터를 활용하여 기업의 우량성 정도를 나타내는 F-score를 계산합니다.
          <br />수익성, 수익의 안정성, 기업 구조, 수익의 성장성, 회계적 우량성, 배당, 투자등의 가치를 종합적으로 분석합니다.
        </h4>
      </div>
    </div>-->
  </div>
</template>
<script>
import NavbarToggleButton from "./NavbarToggleButton";

export default {
  name: "base-nav",
  components: {
    NavbarToggleButton,
  },
  props: {
    type: {
      type: String,
      default: "",
      description: "Navbar type (e.g default, primary etc)",
    },
    title: {
      type: String,
      default: "",
      description: "Title of navbar",
    },
    contentId: {
      type: [String, Number],
      default: Math.random().toString(),
      description:
        "Explicit id for the menu. By default it's a generated random number",
    },
    containerClasses: {
      type: [String, Object, Array],
      default: "container-fluid",
    },
    transparent: {
      type: Boolean,
      default: false,
      description: "Whether navbar is transparent",
    },
    expand: {
      type: Boolean,
      default: false,
      description: "Whether navbar should contain `navbar-expand-lg` class",
    },
    showToggleButton: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      toggled: false,
    };
  },
  methods: {
    closeMenu() {
      this.toggled = false;
    },
  },
};
</script>
<style>
</style>
